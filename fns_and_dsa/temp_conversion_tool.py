# Temperature conversion constants (as functions)
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9  # Correctly convert Fahrenheit to Celsius

def convert_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32  # Correctly convert Celsius to Fahrenheit

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
