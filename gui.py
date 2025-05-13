import tkinter as tk
from tkinter import messagebox
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("date_to_price_model.pkl")


# Function to predict the stock price
def predict_price():
    try:
        # Get the date from input
        input_date = pd.to_datetime(entry.get())

        # Extract date features
        features = pd.DataFrame({
            'Day': [input_date.day],
            'Month': [input_date.month],
            'Year': [input_date.year],
            'DayOfWeek': [input_date.dayofweek]
        })

        # Predict using the model
        predicted_price = model.predict(features)[0]
        result_var.set(f"Predicted Price: ₹{predicted_price:.2f}")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid date format or prediction error.\n{e}")


# Function to clear input and result
def clear_fields():
    entry.delete(0, tk.END)
    result_var.set("")


# Create the main window
root = tk.Tk()
root.title("Stock Price Predictor")


# Entry for date input
tk.Label(root, text="Enter Date (YYYY-MM-DD):").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(root, width=20)
entry.grid(row=0, column=1, padx=10, pady=10)

# Result label
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=('Arial', 12, 'bold'))
result_label.grid(row=1, column=0, columnspan=2, pady=10)

# Buttons
tk.Button(root, text="Predict", width=10, command=predict_price).grid(row=2, column=0, pady=10)
tk.Button(root, text="Clear", width=10, command=clear_fields).grid(row=2, column=1, pady=10)
tk.Button(root, text="Close", width=10, command=root.destroy).grid(row=3, column=0, columnspan=2, pady=10)


# Run the GUI
root.mainloop()
