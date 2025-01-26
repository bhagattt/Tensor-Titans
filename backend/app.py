from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import traceback
import logging
import os
import joblib

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load the finance goal model, allocation model, and encoders for v2
finance_model_path = os.path.join('models', 'strategy_model_v2.pkl')
allocation_model_path = os.path.join('models', 'allocation_model_v2.pkl')
finance_encoders_path = os.path.join('models', 'label_encoders_v2.pkl')

if not os.path.exists(finance_model_path) or not os.path.exists(allocation_model_path) or not os.path.exists(finance_encoders_path):
    raise FileNotFoundError("Finance goal model, allocation model, or encoders not found. Please train the models first.")

finance_model = joblib.load(finance_model_path)
allocation_model = joblib.load(allocation_model_path)
finance_encoders = joblib.load(finance_encoders_path)

# Load the stock price model and scaler
stock_model_path = os.path.join('models', 'stock_price_knn_model.pkl')
stock_scaler_path = os.path.join('models', 'scaler.pkl')

if not os.path.exists(stock_model_path) or not os.path.exists(stock_scaler_path):
    raise FileNotFoundError("Stock price model or scaler not found. Please train the model first.")

stock_model = joblib.load(stock_model_path)
stock_scaler = joblib.load(stock_scaler_path)

# Endpoint for AI asset allocation
def get_recommendation(age_group, income_level, financial_goal, risk_tolerance):
    # Define rules for asset allocation
    if age_group == "18-25" and risk_tolerance == "High":
        return {
            "strategy": "Aggressive Growth",
            "allocation": {
                "Stocks": 70,
                "Bonds": 10,
                "Real Estate": 10,
                "Mutual Funds": 5,
                "ETFs": 5,
                "Cryptocurrency": 0
            }
        }
    elif age_group == "46-55" and risk_tolerance == "Moderate-Conservative":
        return {
            "strategy": "Balanced Growth",
            "allocation": {
                "Stocks": 50,
                "Bonds": 30,
                "Real Estate": 10,
                "Mutual Funds": 5,
                "ETFs": 5,
                "Cryptocurrency": 0
            }
        }
    elif age_group == "65+" and risk_tolerance == "Conservative":
        return {
            "strategy": "Conservative Growth",
            "allocation": {
                "Stocks": 30,
                "Bonds": 50,
                "Real Estate": 10,
                "Mutual Funds": 5,
                "ETFs": 5,
                "Cryptocurrency": 0
            }
        }
    else:
        # Default recommendation
        return {
            "strategy": "Balanced Growth",
            "allocation": {
                "Stocks": 40,
                "Bonds": 40,
                "Real Estate": 10,
                "Mutual Funds": 5,
                "ETFs": 5,
                "Cryptocurrency": 0
            }
        }

# Endpoint for AI asset allocation
@app.route('/asset', methods=['POST'])
def asset_allocation():
    try:
        # Get the JSON data from the request
        data = request.json

        # Validate the input data
        required_fields = ['age_group', 'income_level', 'financial_goal', 'risk_tolerance']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({
                "error": "Missing required fields in JSON body",
                "missing_fields": missing_fields
            }), 400

        # Get the recommendation based on hardcoded rules
        recommendation = get_recommendation(
            data['age_group'],
            data['income_level'],
            data['financial_goal'],
            data['risk_tolerance']
        )

        # Return the recommendation as JSON
        return jsonify(recommendation)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
# Endpoint for stock price movement prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the JSON data from the request
        data = request.json
        logging.info(f"Received data: {data}")

        # Validate the input data
        required_fields = ['Open', 'High', 'Low', 'Close', 'Volume']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({
                "error": "Missing required fields in JSON body",
                "missing_fields": missing_fields
            }), 400

        # Create a DataFrame for the input data
        input_data = pd.DataFrame([{
            'Open': data['Open'],
            'High': data['High'],
            'Low': data['Low'],
            'Close': data['Close'],
            'Volume': data['Volume'],
            'MA_5': data.get('MA_5', None),  # Optional field
            'MA_10': data.get('MA_10', None)  # Optional field
        }])

        # Calculate Daily_Return
        input_data['Daily_Return'] = (input_data['Close'] - input_data['Open']) / input_data['Open'] * 100

        # Calculate MA_5 and MA_10 if not provided
        if input_data['MA_5'].isnull().any():
            input_data['MA_5'] = input_data['Close'].rolling(window=5, min_periods=1).mean().iloc[-1]

        if input_data['MA_10'].isnull().any():
            input_data['MA_10'] = input_data['Close'].rolling(window=10, min_periods=1).mean().iloc[-1]

        # Ensure the input data has all the features used during training
        required_features = ['Open', 'High', 'Low', 'Close', 'Volume', 'Daily_Return', 'MA_5', 'MA_10']
        input_data = input_data[required_features]

        # Scale the input features
        input_features_scaled = stock_scaler.transform(input_data)

        # Predict stock movement
        prediction = stock_model.predict(input_features_scaled)[0]

        # Return the prediction
        return jsonify({"prediction": "increase" if prediction == 1 else "decrease"})
    except Exception as e:
        logging.error(f"Prediction error: {e}")
        return jsonify({"error": str(e), "traceback": traceback.format_exc()}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)