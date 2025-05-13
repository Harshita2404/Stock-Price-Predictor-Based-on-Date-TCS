import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import joblib

# Load the stock price dataset (Date + Close)
df = pd.read_csv("TCS_stock_price.csv")

# Convert the Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Create date-related features
df['Day'] = df['Date'].dt.day
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year
df['DayOfWeek'] = df['Date'].dt.dayofweek

# Features and target
X = df[['Day', 'Month', 'Year', 'DayOfWeek']]
y = df['Close']

# Create a pipeline (scaler + model)
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LinearRegression()),
    # ('model', RandomForestRegressor(n_estimators=100, random_state=42)),
])

# Train the model
pipeline.fit(X, y)

# Save the model
joblib.dump(pipeline, "date_to_price_model.pkl")
print("Model saved as 'date_to_price_model.pkl'")
