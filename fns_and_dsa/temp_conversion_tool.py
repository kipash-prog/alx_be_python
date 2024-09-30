# temp_conversion_tool.py

# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_OFFSET = 32

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    return (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET

def main():
    """Main function to handle user interaction and temperature conversion."""
    while True:
        user_input = input("Enter the temperature (e.g., 25C or 77F) or type 'exit' to quit: ")
        
        if user_input.lower() == 'exit':
            print("Exiting the temperature conversion tool.")
            break
        
        try:
            # Check if input ends with 'C' or 'F'
            if user_input[-1].upper() == 'C':
                celsius = float(user_input[:-1])
                fahrenheit = convert_to_fahrenheit(celsius)
                print(f"{celsius}°C is {fahrenheit:.2f}°F")
            elif user_input[-1].upper() == 'F':
                fahrenheit = float(user_input[:-1])
                celsius = convert_to_celsius(fahrenheit)
                print(f"{fahrenheit}°F is {celsius:.2f}°C")
            else:
                raise ValueError("Invalid temperature unit. Please specify 'C' for Celsius or 'F' for Fahrenheit.")
        
        except ValueError as e:
            print(f"Invalid temperature. Please enter a numeric value. Error: {e}")

if __name__ == "__main__":
    main()
