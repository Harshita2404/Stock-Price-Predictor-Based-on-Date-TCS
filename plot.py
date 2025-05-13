import pandas as pd
import matplotlib.pyplot as plt
import joblib

# Load the trained model
model = joblib.load("date_to_price_model.pkl")

# Load the stock price dataset
df = pd.read_csv("TCS_stock_price.csv")
df['Date'] = pd.to_datetime(df['Date'])

# Create features for each date
df['Day'] = df['Date'].dt.day
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year
df['DayOfWeek'] = df['Date'].dt.dayofweek

# Predict using the model
features = df[['Day', 'Month', 'Year', 'DayOfWeek']]
df['Predicted_Price'] = model.predict(features)

# Plot actual vs predicted
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Close'], label='Actual Price', color='blue')
plt.plot(df['Date'], df['Predicted_Price'], label='Predicted Price (Model)', color='red', linestyle='--')

plt.title("TCS Stock Price vs Predicted Price using Linear Regression Model")
plt.xlabel("Date")
plt.ylabel("Stock Price (₹)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
