from flask import Flask, jsonify, request, render_template
from datetime import datetime
from nltk.sentiment import SentimentAnalyzer, SentimentIntensityAnalyzer
import pandas as pd
import numpy as np
import nltk

nltk.download('vader_lexicon')

def get_sentiment_and_scores(text:str) ->dict:
    # get sentiments from ntlk
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(text)
    # dict now maintains order from python 3.6 
    # onwards so using next line
    neg,neu,pos,_=scores.values()
    senti = {neg:"Negative",pos:"Positive",neu:"Neutral"}
    # get sentiments 
    senti = senti[max(senti.keys())]
    return {"scores":scores,"sentiment":senti}

## test
# get_sentiment_and_scores("Wow, NLTK is really powerful!")

## flask app
app = Flask(__name__)

# route home 
@app.route("/")
def home():
    return render_template('index.html')

# route test to check if active
@app.route("/test")
def test_api():
    return jsonify({"status":"OK","time":datetime.now()})

# route to predict the sentiment and give scores
@app.route("/predict", methods=['POST'])
def predict_sentiment():
    text = request.json.get("text")
    return jsonify(get_sentiment_and_scores(text))

if __name__=="__main__":
    app.run(debug=True,port=5000)
