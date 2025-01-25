import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Load the dataset
data = pd.read_csv('ITC.csv')

# Preview the data
print(data.head())

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

# Make predictions
y_pred = knn.predict(X_test)

# Evaluate the model

#Pnt("Confusion Matrix:")
#print(confusion_matrix(y_test, y_pred))

# print("\nClassification Report:")


new_input = pd.DataFrame({
    'Open': [439],
    'High': [445],
    'Low': [479.85],
    'Close': [481.60],
    'Volume': [37072992]
})

# Feature engineering for the new input
new_input['Daily_Return'] = (new_input['Close'] - new_input['Open']) / new_input['Open'] * 100
new_input['MA_5'] = data['Close'].rolling(window=5).mean().iloc[-1]  # Example for missing MA_5
new_input['MA_10'] = data['Close'].rolling(window=10).mean().iloc[-1]  # Example for missing MA_10

new_features = new_input[['Open', 'High', 'Low', 'Close', 'Volume', 'Daily_Return', 'MA_5', 'MA_10']]
new_features_scaled = scaler.transform(new_features)  # Apply the same scaling used during training

# Make the prediction
prediction = knn.predict(new_features_scaled)

if prediction[0] == 1:
    print("Prediction: The stock price will increase.")
else:
    print("Prediction: The stock price will decrease.")