import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
data=pd.read_csv('House Price India.csv')


X = data['Area of the house(excluding basement)'].values.reshape(-1, 1) 
y = data['Price']  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model=LinearRegression()
model.fit(X_train,y_train)

y_pred=model.predict(X_test)

plt.scatter(X, y, color='blue')

# Plot the regression line
plt.plot(X,  model.predict(X), color='red')

# Add labels and title
plt.xlabel('Area of the house(excluding basement)')
plt.ylabel('Price (INR)')
plt.title('Linear Regression - Area vs Price')
plt.legend()
plt.show()