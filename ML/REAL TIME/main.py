import requests
import pandas as pd

# Alpha Vantage API Key
API_KEY = '34JHGJPNINHZK8SH'  # Replace with your Alpha Vantage API key

# List of 10 Nifty 50 stocks (replace with actual symbols)
NIFTY_50_STOCKS = ['RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS', 'INFY.NS', 'HINDUNILVR.NS', 
                   'ICICIBANK.NS', 'KOTAKBANK.NS', 'AXISBANK.NS', 'LT.NS', 'ITC.NS']

# Categorize stocks into Low, Moderate, and High Risk
STOCK_CATEGORIES = {
    'Low Risk': ['HDFCBANK.NS', 'INFY.NS', 'TCS.NS'],  # Example: Stable, large-cap stocks
    'Moderate Risk': ['RELIANCE.NS', 'HINDUNILVR.NS', 'ITC.NS'],  # Example: Blue-chip stocks
    'High Risk': ['ICICIBANK.NS', 'KOTAKBANK.NS', 'AXISBANK.NS', 'LT.NS']  # Example: Volatile stocks
}

# Function to fetch real-time stock data
def get_realtime_data(symbol):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={API_KEY}'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        
        # Check if the API returned an error message
        if 'Error Message' in data:
            print(f"Error fetching data for {symbol}: {data['Error Message']}")
            return None
        return data
    except requests.exceptions.RequestException as e:
        print(f"Request failed for {symbol}: {e}")
        return None

# Function to analyze trends
def analyze_trends(data):
    if not data or 'Time Series (5min)' not in data:
        print("No data available for analysis.")
        return None
    
    df = pd.DataFrame(data['Time Series (5min)']).T
    df['4. close'] = df['4. close'].astype(float)
    
    # Calculate Moving Averages
    df['MA_5'] = df['4. close'].rolling(window=5).mean()  # 5-minute moving average
    df['MA_20'] = df['4. close'].rolling(window=20).mean()  # 20-minute moving average
    
    # Calculate RSI (Relative Strength Index)
    delta = df['4. close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    
    return df

# Function to generate recommendations
def generate_recommendation(df):
    if df is None or df.empty:
        return "No data for recommendation"
    
    latest_close = df['4. close'].iloc[-1]
    ma_5 = df['MA_5'].iloc[-1]
    ma_20 = df['MA_20'].iloc[-1]
    rsi = df['RSI'].iloc[-1]
    
    recommendation = "Hold"
    if latest_close > ma_5 > ma_20 and rsi < 70:
        recommendation = "Buy"
    elif latest_close < ma_5 < ma_20 and rsi > 30:
        recommendation = "Sell"
    
    return recommendation

# Function to analyze stocks in a specific category
def analyze_category(category):
    results = {}
    
    for symbol in STOCK_CATEGORIES[category]:
        try:
            print(f"Fetching data for {symbol}...")
            data = get_realtime_data(symbol)
            if data:
                df = analyze_trends(data)
                if df is not None:
                    recommendation = generate_recommendation(df)
                    results[symbol] = {
                        'Latest Close': df['4. close'].iloc[-1],
                        'MA_5': df['MA_5'].iloc[-1],
                        'MA_20': df['MA_20'].iloc[-1],
                        'RSI': df['RSI'].iloc[-1],
                        'Recommendation': recommendation
                    }
                else:
                    results[symbol] = "No data for analysis"
            else:
                results[symbol] = "Failed to fetch data"
        except Exception as e:
            print(f"Error analyzing {symbol}: {e}")
            results[symbol] = "Error"
    
    return results

# Main function to run the analysis
def main():
    # Input the category to analyze
    category = input("Enter the category to analyze (Low Risk, Moderate Risk, High Risk): ").strip()
    
    if category not in STOCK_CATEGORIES:
        print("Invalid category. Choose from 'Low Risk', 'Moderate Risk', or 'High Risk'.")
        return
    
    # Analyze the category
    results = analyze_category(category)
    
    # Display the results
    print(f"\n{category} Stocks Analysis:")
    for symbol, data in results.items():
        if data == "Error" or data == "No data for analysis" or data == "Failed to fetch data":
            print(f"{symbol}: {data}")
        else:
            print(f"{symbol}:")
            print(f"  Latest Close: {data['Latest Close']}")
            print(f"  MA_5: {data['MA_5']}")
            print(f"  MA_20: {data['MA_20']}")
            print(f"  RSI: {data['RSI']}")
            print(f"  Recommendation: {data['Recommendation']}")
            print()

# Run the program
if __name__ == "__main__":
    main()