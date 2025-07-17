# --- Project Carbontra: Final Code ---

# --- 1. EMISSION FACTORS (Constants) ---
CO2_PER_KM = 0.17
CO2_PER_KWH = 0.82
CO2_PER_KG_WASTE = 0.57

# --- 2. HELPER FUNCTION FOR ROBUST INPUT ---
def get_valid_float_input(prompt):
    """Keeps asking the user for input until a valid number is entered."""
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
    return (kwh_monthly / 4.33) * CO2_PER_KWH

def calculate_waste_footprint(kg_waste):
    """Calculates CO2 from weekly waste."""
    return kg_waste * CO2_PER_KG_WASTE

# --- 4. MAIN FUNCTION ---
def calculate_carbon_footprint():
    """Main function to run the calculator."""
    print("\n--- Carbon Footprint Calculator ---")
    
    # Use our new helper function to get crash-proof input
    km_driven = get_valid_float_input("How many kilometers do you drive per week? ")
    kwh_used = get_valid_float_input("How many kWh of electricity do you use per month? ")
    waste_generated = get_valid_float_input("How many kg of waste do you generate per week? ")

    # Calculations remain the same
    co2_from_driving = calculate_travel_footprint(km_driven)
    co2_from_electricity = calculate_electricity_footprint(kwh_used)
    co2_from_waste = calculate_waste_footprint(waste_generated)
    
    total_weekly_co2 = co2_from_driving + co2_from_electricity + co2_from_waste

    # Output remains the same
    print("\n--- Your Weekly Carbon Footprint Breakdown ---")
    print(f"🚗 Travel: {co2_from_driving:.2f} kg of CO2")
    print(f"💡 Electricity: {co2_from_electricity:.2f} kg of CO2")
    print(f"🗑️ Waste: {co2_from_waste:.2f} kg of CO2")
    print("-------------------------------------------")
    print(f"🌍 Your estimated total is {total_weekly_co2:.2f} kg of CO2 per week.")

    print("\n--- Feedback ---")
    if total_weekly_co2 < 20:
        print("👍 Your carbon footprint is relatively low. Great job!")
    elif total_weekly_co2 < 50:
        print("😐 Your carbon footprint is average. There are opportunities to reduce it.")
    else:
        print("❗ Your carbon footprint is high. Consider looking for ways to reduce your impact.")

# --- 5. RUN THE PROGRAM WITH A LOOP ---
while True:
    calculate_carbon_footprint()
    
    another_calculation = input("\nDo you want to perform another calculation? (yes/no): ")
    if another_calculation.lower() != 'yes':
        print("\nThank you for using the calculator!")
        break
