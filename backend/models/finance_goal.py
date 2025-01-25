import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Load the dataset
df = pd.read_csv('C:/Users/aryan/Desktop/Tensor/Tensor-Titans/backend/models/financial_goals_dataset.csv')
# Preprocessing
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

# Save the model and encoders
model_dir = 'models'
os.makedirs(model_dir, exist_ok=True)

joblib.dump(rf_classifier, os.path.join(model_dir, 'investment_strategy_model.pkl'))
joblib.dump(label_encoders, os.path.join(model_dir, 'label_encoders.pkl'))

print("Finance goal model and encoders saved successfully.")