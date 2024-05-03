"""
Tax Calculator - 
    Asks the user to enter a cost and either a country or state tax. 
    It then returns the tax plus the total cost with tax.
"""
import tkinter as tk
from tkinter import messagebox
import pandas as pd

# Load tax data from a CSV file
tax_data = pd.read_csv("tax.csv")

def calculate_tax():
    given_country = country_var.get()
    income = float(income_entry.get().replace(',', ''))

    try:
        # Filter tax data for the given country
        country_tax_data = tax_data[tax_data["Country"] == given_country]
        
        if not country_tax_data.empty:
            # Retrieve the tax rate for the given income range
            tax_rate = country_tax_data["Tax Rate"].iloc[0]
            
            # Calculate tax amount
            tax_amount = income * (tax_rate / 100)
            
            # Display the result
            messagebox.showinfo("Tax Calculation", f"The tax amount for {given_country} is: {tax_amount:.2f}")
        else:
            messagebox.showerror("Error", f"No tax rate found for {given_country}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create main window
window = tk.Tk()
window.title("Tax Calculator")

# Country selection
tk.Label(window, text="Select Country:").grid(row=0, column=0, padx=5, pady=5)
country_var = tk.StringVar(window)
country_var.set("Select")
country_dropdown = tk.OptionMenu(window, country_var, *tax_data["Country"].unique())
country_dropdown.grid(row=0, column=1, padx=5, pady=5)

# Income input
tk.Label(window, text="Enter Income:").grid(row=1, column=0, padx=5, pady=5)
income_entry = tk.Entry(window)
income_entry.grid(row=1, column=1, padx=5, pady=5)

# Calculate button
calculate_button = tk.Button(window, text="Calculate Tax", command=calculate_tax)
calculate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Start the main loop
window.mainloop()
