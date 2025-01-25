
from flask import Flask, request, jsonify
from flask_cors import CORS  # Enable CORS
import requests  # Added missing import
import pandas as pd
import traceback
import threading
import time
import nltk
from textblob import TextBlob
import numpy as np
import logging  # Added missing import
import os  # For environment variables

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Download necessary NLTK resources
nltk.download('punkt', quiet=True)

class MarketSentimentAnalyzer:
    def __init__(self, api_key, tickers=['UNIT']):
        self.EOD_API_KEY = api_key
        self.tickers = tickers
        self.sentiment_results = []
        self.market_sentiment = "Neutral"
        self.lock = threading.Lock()  # Thread safety

    def fetch_news(self, limit=20):
        """
        Fetch news for multiple tickers with comprehensive error handling.
        """
        all_headlines = []
        for ticker in self.tickers:
            url = f"https://eodhd.com/api/news?s={ticker}&api_token={self.EOD_API_KEY}&fmt=json&limit={limit}"
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                articles = response.json()
                headlines = [
                    {
                        'title': article.get('title', ''),
                        'description': article.get('description', ''),
                        'source': article.get('source', '')
                    } 
                    for article in articles if article.get('title')
                ]
                all_headlines.extend(headlines)
            except requests.exceptions.RequestException as e:
                logging.error(f"Error fetching news for {ticker}: {e}")
        return all_headlines

    def analyze_sentiment(self, headlines):
        """
        Perform sentiment analysis using TextBlob.
        """
        sentiment_data = []
        for article in headlines:
            text = f"{article['title']} {article['description']}".lower()
            blob = TextBlob(text)
            sentiment_score = blob.sentiment.polarity
            if sentiment_score > 0.2:
                sentiment = "Strongly Positive"
            elif sentiment_score > 0:
                sentiment = "Positive"
            elif sentiment_score == 0:
                sentiment = "Neutral"
            elif sentiment_score > -0.2:
                sentiment = "Negative"
            else:
                sentiment = "Strongly Negative"
            sentiment_data.append({
                'title': article['title'],
                'source': article['source'],
                'sentiment_score': sentiment_score,
                'sentiment': sentiment
            })
        return sentiment_data

    def update_market_sentiment(self):
        """
        Continuously update market sentiment in the background.
        """
        while True:
            headlines = self.fetch_news()
            if headlines:
                sentiment_results = self.analyze_sentiment(headlines)
                sentiment_scores = [result['sentiment_score'] for result in sentiment_results]
                avg_sentiment = np.mean(sentiment_scores)
                with self.lock:  # Thread-safe access
                    if avg_sentiment > 0.2:
                        self.market_sentiment = "Bullish"
                    elif avg_sentiment > 0:
                        self.market_sentiment = "Slightly Bullish"
                    elif avg_sentiment == 0:
                        self.market_sentiment = "Neutral"
                    elif avg_sentiment > -0.2:
                        self.market_sentiment = "Bearish"
                    else:
                        self.market_sentiment = "Strongly Bearish"
                    self.sentiment_results = sentiment_results
            time.sleep(900)  # Wait for 15 minutes before next update

    def get_sentiment_report(self):
        """
        Return the current sentiment report.
        """
        with self.lock:  # Thread-safe access
            return {
                "market_sentiment": self.market_sentiment,
                "sentiment_results": self.sentiment_results
            }

# Initialize the MarketSentimentAnalyzer
API_KEY = os.getenv('EOD_API_KEY', '6794fc627deb45.88144783')  # Use environment variable for API key
analyzer = MarketSentimentAnalyzer(API_KEY, tickers=['UNIT', 'ETF', 'FUND'])

# Start the sentiment analyzer in a background thread
sentiment_thread = threading.Thread(target=analyzer.update_market_sentiment, daemon=True)
sentiment_thread.start()

# Endpoint for investment strategy recommendation
@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        data = request.json
        recommendation = recommend_investment_strategy(
            age_group=data['age_group'],
            income_level=data['income_level'],
            financial_goal=data['financial_goal'],
            risk_tolerance=data['risk_tolerance'],
            current_portfolio=data['current_portfolio']
        )
        return jsonify(recommendation)
    except Exception as e:
        logging.error(f"Recommendation error: {e}")
        return jsonify({"error": str(e), "traceback": traceback.format_exc()}), 500

# Endpoint for stock price movement prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        input_data = pd.DataFrame([data])
        prediction = predict_stock_movement(input_data)
        return jsonify({"prediction": prediction})
    except Exception as e:
        logging.error(f"Prediction error: {e}")
        return jsonify({"error": str(e), "traceback": traceback.format_exc()}), 500

# Endpoint for market sentiment analysis
@app.route('/sentiment', methods=['GET'])
def sentiment():
    try:
        report = analyzer.get_sentiment_report()
        report['timestamp'] = time.time()
        report['sentiment_results'] = report['sentiment_results'][:10]  # Limit to top 10 results
        return jsonify(report)
    except Exception as e:
        logging.error(f"Sentiment endpoint error: {e}")
        return jsonify({
            "error": "Unable to retrieve sentiment",
            "details": str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)