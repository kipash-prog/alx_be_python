# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  # Factor for converting Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5    # Factor for converting Celsius to Fahrenheit

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# User interaction
try:
    temperature = float(input("Enter the temperature to convert: "))
    choose = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

    if choose == "C":
        fahrenheit = convert_to_fahrenheit(temperature)
        print(f"{temperature:.1f}°C is {fahrenheit:.1f}°F")
    elif choose == "F":
        celsius = convert_to_celsius(temperature)
        print(f"{temperature:.1f}°F is {celsius:.1f}°C")
    else:
        print("Invalid choice. Please enter 'C' or 'F'.")
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
