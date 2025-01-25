import requests
import time
import threading
import nltk
from textblob import TextBlob
import pandas as pd
import numpy as np

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
                
                # Store and print results
                self.sentiment_results = sentiment_results
                self._print_sentiment_report()
            
            # Wait for 15 minutes before next update
            time.sleep(900)

    def _print_sentiment_report(self):
        """
        Print detailed sentiment report.
        """
        print("\n--- Market Sentiment Report ---")
        print(f"Overall Market Sentiment: {self.market_sentiment}")
        print("\nDetailed Sentiment Breakdown:")
        for result in self.sentiment_results[:10]:  # Limit to top 10 for readability
            print(f"Title: {result['title']}")
            print(f"Source: {result['source']}")
            print(f"Sentiment: {result['sentiment']} (Score: {result['sentiment_score']:.2f})\n")

    def start(self):
        """
        Start the market sentiment analysis in a background thread.
        """
        sentiment_thread = threading.Thread(target=self.update_market_sentiment, daemon=True)
        sentiment_thread.start()

# Usage example
def main():
    # Replace with your actual API key
    API_KEY = '6794fc627deb45.88144783'
    
    # Initialize and start the market sentiment analyzer
    analyzer = MarketSentimentAnalyzer(API_KEY, tickers=['UNIT', 'ETF', 'FUND'])
    analyzer.start()

    # Keep main thread running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping market sentiment analysis...")

if __name__ == '__main__':
    main()