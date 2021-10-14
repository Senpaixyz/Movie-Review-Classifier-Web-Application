# Movie Review Classifier (RNN/LSTM)
##### _The model build from RNN and LSTM networks layers_

The goal of this web application was to predict the negativity and positivity of the phrase using sentiment analysis. Each character convert to each respective unique token that later on vectorize and input to model then the model will gives some prediction accuracy both Positive and Negative percentage rate.

[![N|Solid](https://github.com/Senpaixyz/Movie-Review-Classifier-Web-Application/blob/master/images/landingPage.PNG?raw=true)](https://github.com/Senpaixyz/Movie-Review-Classifier-Web-Application/blob/master/images/landingPage.PNG)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/Senpaixyz/faceEmotion-classifierr)
## Features

- The model can predict multiple phrases and convert the percentage of negativity rate and positivity rate.
- It  the model has  84.04% accuracy 
- It can be deployed in realtime or be use as API.

## Instruction

- The input box only accept English phrases. It may result to wrong prediction if the user input different types of language.
- There are some sample phrase in the web application that can be guide the user.
- The level of positivity or negativity rate was depends on the results of the model. This may be gives some false prediction for some phrase since the sentiment analysis was not accurate 100%.

### Datasets

You can download [datasets](https://mega.nz/file/OkUk2bDY#7B4n7j49ko159Mp3H5xM6HDaH6Wh40DvGdS9VDVykns) that Ive uploaded from the Mega. The sample table below was compoased of input text (Text_Final) and converted it into each respective token each words and inserted it in array. Each phrases was sentiment was labelled and put in the different column. Feel free to use it anytime.

[![N|Solid](https://github.com/Senpaixyz/Movie-Review-Classifier-Web-Application/blob/master/images/datasetsTB.PNG?raw=true)](https://github.com/Senpaixyz/Movie-Review-Classifier-Web-Application/blob/master/images/datasetsTB.PNG)

### Model Prediction
##### Positive Prediction
The sample figure below has a phrase that 76.7% predicted as negative and 22.0% positive. The model figure out that the phrases was composed of much more positive token compare to negative.

[![N|Solid](https://github.com/Senpaixyz/Movie-Review-Classifier-Web-Application/blob/master/images/positive.PNG?raw=true)](https://github.com/Senpaixyz/Movie-Review-Classifier-Web-Application/blob/master/images/positive.PNG)

##### Negative Prediction
The sample figure below has a phrase that 96.6% predicted as negative and 3.4% positive. We all know that it is negative comment, the sentiment analysis this time predicted phrase more accurate.

[![N|Solid](https://github.com/Senpaixyz/Movie-Review-Classifier-Web-Application/blob/master/images/negative.PNG?raw=true)](https://github.com/Senpaixyz/Movie-Review-Classifier-Web-Application/blob/master/images/negative.PNG)

The predictor model will tell you how accurate that the prediction was. Since it is not perfect there are some instances that the predictor model will predict incorrect emotion.
## Packages
Additional Packages
| Package | URL |
| ------ | ------ |
| GoogleNewsVector | [GoogleNews](https://s3.amazonaws.com/dl4j-distribution/GoogleNews-vectors-negative300.bin.gz)|
| NLTK | [NLTK](https://www.nltk.org/data.html) |
| Trained Tokenizer | [Tokenizer](https://mega.nz/file/65kx1Y4a#uB__IGaQZ80XQUbpOoCHboKlo8r1d7y1indDJS4C64k) |
| Model File | [RNN_LSTM.h5](https://mega.nz/file/X51zRYJQ#NIsEJzHp86aiuzKh29ZVTlVlZCowvFbHBXAkkcSiCfs) |

## Installation

For first time use please download all the packages needed in this web application, please create virtual environment from the Pycharm IDE. Then open the terminal and run:

```sh
pip install -r requirements.txt
```
After use install all the dependency that needed in this web application. just simply type in the terminal:

```sh
python app.py
```
Verify the deployment by navigating to your server address in
your preferred browser.

```sh
http://127.0.0.1:5000/
```
This web application was supported by ngrok api. Uncomment this in the app.py to use it and shared this web application from another devices and via internet.

`//run_with_ngrok(app)`

## License

MIT

**Free Web Application Developed by Jheno Cerbito**