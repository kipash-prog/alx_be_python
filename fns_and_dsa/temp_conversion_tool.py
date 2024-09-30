# Define conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Temperature conversion functions
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR  # Convert Fahrenheit to Celsius

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32  # Convert Celsius to Fahrenheit

# Get user input
temperature = input("Enter the temperature to convert: ")
choose = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

# Check if the input is a valid float
try:
    temperature = float(temperature)
    
    if choose == "C":
        fahrenheit = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {fahrenheit:.2f}°F")
    elif choose == "F":
        celsius = convert_to_celsius(temperature)
        print(f"{temperature}°F is {celsius:.2f}°C")
    else:
        print("Invalid choice. Please enter 'C' or 'F'.")
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
