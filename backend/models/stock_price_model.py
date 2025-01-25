

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import joblib
import os

# Load the dataset
df = pd.read_csv('C:\\Users\\aryan\\Desktop\\Tensor\\Tensor-Titans\\backend\\models\\ITC.csv') # Replace with your stock price dataset

# Feature engineering
df['Daily_Return'] = (df['Close'] - df['Open']) / df['Open'] * 100
df['MA_5'] = df['Close'].rolling(window=5).mean()
df['MA_10'] = df['Close'].rolling(window=10).mean()
df['Price_Up'] = (df['Close'].shift(-1) > df['Close']).astype(int)

# Drop NaN values
df = df.dropna()

# Define features and target
features = df[['Open', 'High', 'Low', 'Close', 'Volume', 'Daily_Return', 'MA_5', 'MA_10']]
X = features
y = df['Price_Up']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Scaling the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train KNN model
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Save the model and scaler
model_dir = 'models'
os.makedirs(model_dir, exist_ok=True)

joblib.dump(knn, os.path.join(model_dir, 'stock_price_knn_model.pkl'))
joblib.dump(scaler, os.path.join(model_dir, 'scaler.pkl'))

print("Stock price model and scaler saved successfully.")