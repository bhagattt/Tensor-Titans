import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Load the dataset
df = pd.read_csv('financial_goals_dataset.csv')

# Preprocessing
# Encode categorical variables
categorical_columns = ['Age_Group', 'Income_Level', 'Primary_Financial_Goal', 'Risk_Tolerance']
investment_columns = ['Stocks', 'Bonds', 'Real Estate', 'Mutual Funds', 'ETFs', 'Cryptocurrency']

# Label Encoding for categorical variables
label_encoders = {}
for col in categorical_columns:
    le = LabelEncoder()
    df[f'{col}_Encoded'] = le.fit_transform(df[col])
    label_encoders[col] = le

# Prepare features and target
X = df[[f'{col}_Encoded' for col in categorical_columns] + investment_columns]
y = df['Recommended_Strategy']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest Classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)

# Evaluate the model
y_pred = rf_classifier.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Feature Importance
feature_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': rf_classifier.feature_importances_
}).sort_values('importance', ascending=False)
print("\nFeature Importance:")
print(feature_importance)

# Save model and encoders
joblib.dump(rf_classifier, 'investment_strategy_model.pkl')
joblib.dump(label_encoders, 'label_encoders.pkl')

# Personalized Investment Strategy Recommender Function
def recommend_investment_strategy(age_group, income_level, financial_goal, risk_tolerance, current_portfolio):
    # Load saved model and encoders
    model = joblib.load('investment_strategy_model.pkl')
    encoders = joblib.load('label_encoders.pkl')

    # Encode categorical inputs
    encoded_inputs = [
        encoders['Age_Group'].transform([age_group])[0],
        encoders['Income_Level'].transform([income_level])[0],
        encoders['Primary_Financial_Goal'].transform([financial_goal])[0],
        encoders['Risk_Tolerance'].transform([risk_tolerance])[0]
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

# Example usage
sample_portfolio = {
    'Stocks': 50,
    'Bonds': 20,
    'Real Estate': 10,
    'Mutual Funds': 10,
    'ETFs': 5,
    'Cryptocurrency': 5
}

recommendation = recommend_investment_strategy(
    age_group='36-45', 
    income_level='Medium-High', 
    financial_goal='Retirement', 
    risk_tolerance='Balanced', 
    current_portfolio=sample_portfolio
)

print("\nPersonalized Investment Recommendation:")
print(f"Strategy: {recommendation['strategy']}")
print(f"Description: {recommendation['details']['description']}")
print("Recommended Allocation:")
for asset, allocation in recommendation['details']['allocation'].items():
    print(f"{asset}: {allocation}%")