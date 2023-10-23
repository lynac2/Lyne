#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 18:06:22 2023

@author: Lynenaccache
"""



#EXO1

# Create a dictionary to store element information with melting and boiling points in Kelvin
element_info = {
    'H': {'name': 'Hydrogen', 'melting_point_K': 14, 'boiling_point_K': 20},
    'He': {'name': 'Helium', 'melting_point_K': 1, 'boiling_point_K': 4},
    'Li': {'name': 'Lithium', 'melting_point_K': 453, 'boiling_point_K': 1603},
    'Be': {'name': 'Beryllium', 'melting_point_K': 1560, 'boiling_point_K': 2742},
    'B': {'name': 'Boron', 'melting_point_K': 2349, 'boiling_point_K': 4200},
    'C': {'name': 'Carbon', 'melting_point_K': 3915, 'boiling_point_K': 3915},
    'N': {'name': 'Nitrogen', 'melting_point_K': 63, 'boiling_point_K': 77},
    'O': {'name': 'Oxygen', 'melting_point_K': 54, 'boiling_point_K': 90},
    'F': {'name': 'Fluorine', 'melting_point_K': 53, 'boiling_point_K': 85},
    'Ne': {'name': 'Neon', 'melting_point_K': 25, 'boiling_point_K': 27},
}

# Function to check the state of an element at a given temperature in Kelvin
def check_element_state(symbol, temperature_K):
    symbol = symbol.capitalize()  # Ensure the symbol is in uppercase
    element = element_info.get(symbol)
    
    if element:
        melting_point = element['melting_point_K']
        boiling_point = element['boiling_point_K']
        
        if temperature_K < melting_point:
            return f"{element['name']} is a solid at {temperature_K} K."
        elif melting_point <= temperature_K < boiling_point:
            return f"{element['name']} is a liquid at {temperature_K} K."
        else:
            return f"{element['name']} is a gas at {temperature_K} K."
    else:
        return "Element not found in the dictionary."

# Example usage:
element_symbol = input("Enter the symbol of the element: ")
temperature_K = float(input("Enter the temperature (in K): "))

result = check_element_state(element_symbol, temperature_K)
print(result)



#EXO2

# Define a dictionary to store mortgage rates for different banks
mortgage_rates = {
    'ANZ': {'name': 'ANZ', 'Years 1&2': 0.023 , 'Years 3 onwards': 0.041},
    'Bank of Australia': {'name': 'Bank of Australia', 'Years 1&2': 0.001 , 'Years 3 onwards': 0.05},
    'Commonwealth Bank': {'name': 'Commonwealth Bank', 'Years 1&2': 0.035 , 'Years 3 onwards': 0.038},
    'Westpac': {'name': 'Westpac', 'Years 1&2': 0.037 , 'Years 3 onwards': 0.037},
}
 
# Function to calculate the monthly mortgage payment
def calculate_monthly_payment(amount, years, bank_name):
    # Check if the bank_name exists in the dictionary
    if bank_name in mortgage_rates:
        bank_info = mortgage_rates[bank_name]
        annual_rate = bank_info['Years 1&2'] if years <= 2 else bank_info['Years 3 onwards']
        monthly_rate = annual_rate / 12
        num_payments = years * 12
        # Calculate the monthly payment using the formula
        monthly_payment = amount * (monthly_rate * (1 + monthly_rate)**num_payments) / ((1 + monthly_rate)**num_payments - 1)
        return monthly_payment
    else:
        return "Bank not found in the dictionary."
 
# Example usage
amount = int(input("Enter the value of the principal amount: "))# Principal amount
years = int(input("Enter the number of year: "))          # Mortgage term in years
bank_name =input("Enter the name of the bank: ")  # Specify the bank providing the mortgage
 
monthly_payment = calculate_monthly_payment(amount, years, bank_name)
if isinstance(monthly_payment, str):
    print(monthly_payment)
else:
    print(f"Your monthly mortgage payment with {bank_name} is ${monthly_payment:.2f}")
















