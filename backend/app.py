# backend/app.py
from flask import Flask, request, jsonify
from models.finance_goal import recommend_investment_strategy  # Import from finance_goal.py
from models.stock_price_model import predict_stock_movement  # Import from stock_price_model.py
import pandas as pd
import traceback
import threading
import time
import nltk
from textblob import TextBlob
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Download necessary NLTK resources
nltk.download('punkt', quiet=True)

class MarketSentimentAnalyzer:
    def __init__(self, api_key, tickers=['UNIT']):
        self.EOD_API_KEY = api_key
        self.tickers = tickers
        self.sentiment_results = []
        self.market_sentiment = "Neutral"

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
            except Exception as e:
                print(f"Error fetching news for {ticker}: {e}")
        return all_headlines

    def analyze_sentiment(self, headlines):
        """
        Advanced sentiment analysis using TextBlob.
        """
        sentiment_data = []
        for article in headlines:
            # Combine title and description for comprehensive analysis
            text = f"{article['title']} {article['description']}".lower()
            
            # Use TextBlob for sentiment analysis
            blob = TextBlob(text)
            sentiment_score = blob.sentiment.polarity
            
            # Categorize sentiment
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
        Continuously update market sentiment.
        """
        while True:
            # Fetch news
            headlines = self.fetch_news()
            
            if headlines:
                # Analyze sentiment
                sentiment_results = self.analyze_sentiment(headlines)
                
                # Calculate overall market sentiment
                sentiment_scores = [result['sentiment_score'] for result in sentiment_results]
                avg_sentiment = np.mean(sentiment_scores)
                
                # Determine market sentiment
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
                
                # Store results
                self.sentiment_results = sentiment_results
            
            # Wait for 15 minutes before next update
            time.sleep(900)

    def get_sentiment_report(self):
        """
        Return the current sentiment report.
        """
        return {
            "market_sentiment": self.market_sentiment,
            "sentiment_results": self.sentiment_results
        }

# Initialize the MarketSentimentAnalyzer
API_KEY = '6794fc627deb45.88144783'  # Replace with your actual API key
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
        return jsonify({"error": str(e), "traceback": traceback.format_exc()}), 500

# Endpoint for stock price movement prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        # Convert input data to a DataFrame for the predict_stock_movement function
        input_data = pd.DataFrame([data])  # Wrap the dictionary in a list to create a single-row DataFrame
        prediction = predict_stock_movement(input_data)
        return jsonify({"prediction": prediction})
    except Exception as e:
        return jsonify({"error": str(e), "traceback": traceback.format_exc()}), 500

# Endpoint for market sentiment analysis
@app.route('/sentiment', methods=['GET'])
def sentiment():
    try:
        # Get the current sentiment report
        report = analyzer.get_sentiment_report()
        
        # Add timestamp to track when data was generated
        report['timestamp'] = time.time()
        
        # Optionally limit sentiment results to most recent
        report['sentiment_results'] = report['sentiment_results'][:10]
        
        return jsonify(report)
    except Exception as e:
        logging.error(f"Sentiment endpoint error: {e}")
        return jsonify({
            "error": "Unable to retrieve sentiment",
            "details": str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)