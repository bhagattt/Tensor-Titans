import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.multioutput import MultiOutputRegressor
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Load the new dataset
df = pd.read_csv('C:/Users/aryan/Desktop/Tensor/Tensor-Titans/backend/models/financial_goals_dataset.csv')


# Define categorical and investment columns
categorical_columns = ['Age_Group', 'Income_Level', 'Primary_Financial_Goal', 'Risk_Tolerance']
investment_columns = ['Stocks', 'Bonds', 'Real Estate', 'Mutual Funds', 'ETFs', 'Cryptocurrency']

# Label Encoding for categorical variables
label_encoders = {}
for col in categorical_columns:
    le = LabelEncoder()
    df[f'{col}_Encoded'] = le.fit_transform(df[col])
    label_encoders[col] = le

# Prepare features and targets
X = df[[f'{col}_Encoded' for col in categorical_columns] + investment_columns]
y_strategy = df['Recommended_Strategy']  # Target for strategy
y_allocation = df[investment_columns]   # Target for asset allocation

# Split the data
X_train, X_test, y_strategy_train, y_strategy_test, y_allocation_train, y_allocation_test = train_test_split(
    X, y_strategy, y_allocation, test_size=0.2, random_state=42
)

# Train Random Forest Classifier for Recommended Strategy
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_strategy_train)

# Train Multi-Output Random Forest Regressor for Asset Allocation
rf_regressor = MultiOutputRegressor(RandomForestRegressor(n_estimators=100, random_state=42))
rf_regressor.fit(X_train, y_allocation_train)

# Save the models and encoders
model_dir = 'models'
os.makedirs(model_dir, exist_ok=True)

joblib.dump(rf_classifier, os.path.join(model_dir, 'strategy_model_v2.pkl'))
joblib.dump(rf_regressor, os.path.join(model_dir, 'allocation_model_v2.pkl'))
joblib.dump(label_encoders, os.path.join(model_dir, 'label_encoders_v2.pkl'))

print("Models and encoders saved successfully.")