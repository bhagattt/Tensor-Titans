from flask import Flask, request, jsonify
from flask_cors import CORS  # Enable CORS
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

# Load the finance goal model and encoders
finance_model_path = os.path.join('models', 'investment_strategy_model.pkl')
finance_encoders_path = os.path.join('models', 'label_encoders.pkl')

if not os.path.exists(finance_model_path) or not os.path.exists(finance_encoders_path):
    raise FileNotFoundError("Finance goal model or encoders not found. Please train the model first.")

finance_model = joblib.load(finance_model_path)
finance_encoders = joblib.load(finance_encoders_path)

# Load the stock price model and scaler
stock_model_path = os.path.join('models', 'stock_price_knn_model.pkl')
stock_scaler_path = os.path.join('models', 'scaler.pkl')

if not os.path.exists(stock_model_path) or not os.path.exists(stock_scaler_path):
    raise FileNotFoundError("Stock price model or scaler not found. Please train the model first.")

stock_model = joblib.load(stock_model_path)
stock_scaler = joblib.load(stock_scaler_path)

# Endpoint for investment strategy recommendation
@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        # Get the JSON data from the request
        data = request.json
        logging.info(f"Received data: {data}")

        # Validate the input data
        required_fields = ['age_group', 'income_level', 'financial_goal', 'risk_tolerance', 'current_portfolio']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({
                "error": "Missing required fields in JSON body",
                "missing_fields": missing_fields
            }), 400

        # Check if the age_group is valid
        valid_age_groups = finance_encoders['Age_Group'].classes_
        if data['age_group'] not in valid_age_groups:
            return jsonify({
                "error": f"Invalid age group: {data['age_group']}. Valid age groups are: {list(valid_age_groups)}"
            }), 400

        # Check if the risk_tolerance is valid
        valid_risk_tolerances = finance_encoders['Risk_Tolerance'].classes_
        if data['risk_tolerance'] not in valid_risk_tolerances:
            return jsonify({
                "error": f"Invalid risk tolerance: {data['risk_tolerance']}. Valid risk tolerances are: {list(valid_risk_tolerances)}"
            }), 400

        # Encode categorical inputs
        encoded_inputs = [
            finance_encoders['Age_Group'].transform([data['age_group']])[0],
            finance_encoders['Income_Level'].transform([data['income_level']])[0],
            finance_encoders['Primary_Financial_Goal'].transform([data['financial_goal']])[0],
            finance_encoders['Risk_Tolerance'].transform([data['risk_tolerance']])[0]
        ]

        # Prepare input features
        input_features = encoded_inputs + list(data['current_portfolio'].values())

        # Predict strategy
        strategy = finance_model.predict([input_features])[0]

        # Provide detailed recommendation
        recommendations = {
            'Low-Risk Preservation': {
                'description': 'Focus on capital preservation with minimal risk.',
                'allocation': {'Bonds': 60, 'Real Estate': 20, 'ETFs': 10, 'Stocks': 10}
            },
            'Conservative Growth': {
                'description': 'Prioritize stability with modest growth potential.',
                'allocation': {'Bonds': 50, 'Real Estate': 15, 'Stocks': 25, 'Mutual Funds': 10}
            },
            'Balanced Growth': {
                'description': 'Balanced approach between growth and stability.',
                'allocation': {'Stocks': 40, 'Bonds': 30, 'Mutual Funds': 15, 'Real Estate': 15}
            },
            'Aggressive Growth': {
                'description': 'Higher risk tolerance with focus on growth.',
                'allocation': {'Stocks': 60, 'Mutual Funds': 20, 'ETFs': 10, 'Cryptocurrency': 10}
            },
            'High-Risk Aggressive': {
                'description': 'Maximum growth potential with highest risk.',
                'allocation': {'Stocks': 70, 'Cryptocurrency': 15, 'ETFs': 10, 'Mutual Funds': 5}
            }
        }

        return jsonify({
            'strategy': strategy,
            'details': recommendations[strategy]
        })
    except Exception as e:
        logging.error(f"Recommendation error: {e}")
        return jsonify({"error": str(e), "traceback": traceback.format_exc()}), 500

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