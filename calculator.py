# --- Project Carbontra: Final Code ---

# --- 1. EMISSION FACTORS (Constants) ---
# These values represent the average kg of CO2 produced per unit.
CO2_PER_KM = 0.17
CO2_PER_KWH = 0.82
CO2_PER_KG_WASTE = 0.57

# --- 2. HELPER FUNCTION FOR ROBUST INPUT ---
def get_valid_float_input(prompt):
    """
    Keeps asking the user for input until a valid number is entered.
    Handles errors if the user types text instead of a number.
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

# --- 3. SPECIALIZED CALCULATION FUNCTIONS ---

def calculate_travel_footprint(kilometers):
    """Calculates CO2 from kilometers driven."""
    return kilometers * CO2_PER_KM

def calculate_electricity_footprint(kwh_monthly):
    """Calculates weekly CO2 from monthly kWh."""
    # We divide by 4.33 to approximate weeks in a month.
    return (kwh_monthly / 4.33) * CO2_PER_KWH

def calculate_waste_footprint(kg_waste):
    """Calculates CO2 from weekly waste."""
    return kg_waste * CO2_PER_KG_WASTE

# --- 4. MAIN FUNCTION ---
def calculate_carbon_footprint():
    """Main function to run the calculator and display results."""
    print("\n--- Carbon Footprint Calculator ---")
    
    # Use our helper function to get crash-proof input from the user.
    km_driven = get_valid_float_input("How many kilometers do you drive per week? ")
    kwh_used = get_valid_float_input("How many kWh of electricity do you use per month? ")
    waste_generated = get_valid_float_input("How many kg of waste do you generate per week? ")

    # Call the specialized functions to perform the calculations.
    co2_from_driving = calculate_travel_footprint(km_driven)
    co2_from_electricity = calculate_electricity_footprint(kwh_used)
    co2_from_waste = calculate_waste_footprint(waste_generated)
    
    # Calculate the total.
    total_weekly_co2 = co2_from_driving + co2_from_electricity + co2_from_waste

    # Display the final report. The :.2f formats the number to two decimal places.
