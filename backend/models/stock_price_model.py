# backend/models/stock_price_model.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib

# Load the dataset
data = pd.read_csv('ITC.csv')

# Add derived columns
data['Daily_Return'] = (data['Close'] - data['Open']) / data['Open'] * 100
data['MA_5'] = data['Close'].rolling(window=5).mean()
data['MA_10'] = data['Close'].rolling(window=10).mean()
data['Price_Up'] = (data['Close'].shift(-1) > data['Close']).astype(int)

# Drop NaN values after rolling calculations
data = data.dropna()

# Define features and target
features = data[['Open', 'High', 'Low', 'Close', 'Volume', 'Daily_Return', 'MA_5', 'MA_10']]
X = features
target = data['Price_Up']
y = target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Scaling the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Initialize and train KNN model
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Save the model and scaler
joblib.dump(knn, 'stock_price_knn_model.pkl')
joblib.dump(scaler, 'scaler.pkl')

# Function to predict stock price movement
def predict_stock_movement(input_data):
    # Load the saved model and scaler
    model = joblib.load('stock_price_knn_model.pkl')
    scaler = joblib.load('scaler.pkl')

    # Feature engineering for the new input
    input_data['Daily_Return'] = (input_data['Close'] - input_data['Open']) / input_data['Open'] * 100
    input_data['MA_5'] = data['Close'].rolling(window=5).mean().iloc[-1]  # Example for missing MA_5
    input_data['MA_10'] = data['Close'].rolling(window=10).mean().iloc[-1]  # Example for missing MA_10

    # Prepare features
    new_features = input_data[['Open', 'High', 'Low', 'Close', 'Volume', 'Daily_Return', 'MA_5', 'MA_10']]
    new_features_scaled = scaler.transform(new_features)  # Apply the same scaling used during training

    # Make the prediction
    prediction = model.predict(new_features_scaled)

    return "increase" if prediction[0] == 1 else "decrease"