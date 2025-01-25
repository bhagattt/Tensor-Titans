import joblib

def recommend_investment_strategy(age_group, income_level, financial_goal, risk_tolerance, current_portfolio):
    # Load the model and encoders
    model = joblib.load('investment_strategy_model.pkl')
    label_encoders = joblib.load('label_encoders.pkl')

    # Encode categorical inputs
    encoded_inputs = [
        label_encoders['Age_Group'].transform([age_group])[0],
        label_encoders['Income_Level'].transform([income_level])[0],
        label_encoders['Primary_Financial_Goal'].transform([financial_goal])[0],
        label_encoders['Risk_Tolerance'].transform([risk_tolerance])[0]
    ]

    # Prepare input features
    input_features = encoded_inputs + list(current_portfolio.values())

    # Predict strategy
    strategy = model.predict([input_features])[0]
    
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

    return {
        'strategy': strategy,
        'details': recommendations[strategy]
    }
