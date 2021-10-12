import nltk
try:
    nltk.data.find('punkt')
    nltk.data.find('stopwords')

except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
from nltk import word_tokenize
from nltk.corpus import stopwords
import re
import string
import pickle
import numpy as np


class SentimentAnalysis(object):
    def __init__(self):
        self.stoplist = stopwords.words('english')
        self.model_file = self.load_model_file()
        self.MAX_SEQUENCE_LENGTH = 50

    def predict_phrase(self, phrase):
        pos, neg = 0, 0
        self.tokenizer_file = self.load_tokenize_pickle()
        data = self.clean_phrase(phrase)
        tokenize_data = self.tokenize_phrase(data)
        data_sorted = sorted(list(set(tokenize_data)))
        self.tokenizer_file.fit_on_texts(data_sorted)
        training_sequences = self.tokenizer_file.texts_to_sequences(data_sorted)

        final_data = pad_sequences(training_sequences, maxlen=self.MAX_SEQUENCE_LENGTH)

        prediction = self.model_file.predict(final_data)
        analysis_ave, pos_ave, neg_ave = self.analysis_by_average(prediction)
        analysis_max = self.analysis_by_max(prediction)
        if analysis_max == 1:
            pos += 1
        else:
            neg += 1
        if analysis_ave == 1:
            pos += 1
        else:
            neg += 1
        print("POS: ", pos, " NEG: ", neg, " MAX: ", analysis_max, " AVE: ", analysis_ave)
        print("POS_AVE: ", pos_ave)
        print("NEG_AVE: ", neg_ave)
        if pos > neg:
            return "Positive", pos_ave, neg_ave
        else:
            return "Negative", pos_ave, neg_ave

    def analysis_by_max(self, prediction):
        max_score_idx = np.argmax(prediction)
        a = prediction.reshape(-1, len(prediction) * 2)[0]
        print("SHAPE: ", a)
        print("MAX: ", max_score_idx)
        tmp = {}
        i = 0
        for c in a:
            if i % 2 == 0:
                tmp[i] = 0
            else:
                tmp[i] = 1
            i += 1
        print("TMP : ", tmp)
        return tmp[max_score_idx]

    def analysis_by_average(self, prediction):
        pos_sum = 0
        neg_sum = 0
        for col in prediction:
            neg_sum += col[0]
            pos_sum += col[1]
        ave_pos = (pos_sum / len(prediction))
        ave_neg = (neg_sum / len(prediction))
        if ave_pos > ave_neg:
            return 1, ave_pos, ave_neg
        else:
            return 0, ave_pos, ave_neg

    def clean_phrase(self, phrase):
        cleaned_html = self.remove_html(phrase)
        remove_punc = self.remove_punct(cleaned_html)
        cleaned_final = self.clean_final(remove_punc)
        return cleaned_final

    def tokenize_phrase(self, phrase):
        words_tokenize = word_tokenize(phrase)
        filtered_words = [self.remove_stop_words(sen) for sen in words_tokenize]
        filtered_words = filter(None, filtered_words)
        result = [' '.join(sen) for sen in filtered_words]
        return result

    def load_tokenize_pickle(self):
        tokenizer_loaded = None
        try:
            with open('model/tokenizer.pickle', 'rb') as handle:
                tokenizer_loaded = pickle.load(handle)
                return tokenizer_loaded
        except FileNotFoundError:
            print("Missing tokenizer pickle file!")

    def load_model_file(self):
        try:
            model = load_model('model/rcnn-lstm-model.h5')
            return model
        except FileNotFoundError:
            print("File model not found!")

    def remove_stop_words(self, tokens):
        if tokens not in self.stoplist:
            return tokens

    def remove_html(self, text):
        # clean=re.compile('<.*?>')
        cleantext = re.sub('<[^<]+?>', '', text)
        return cleantext

    def remove_punct(self, text):
        text = text.lower()
        text = re.sub('\[.*?\]', '', text)
        text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
        text = re.sub('\w*\d\w*', '', text)
        return text

    def clean_final(self, text):
        text = re.sub('[''"",,,]', '', text)
        text = re.sub('\n', '', text)
        return text