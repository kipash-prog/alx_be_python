FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
def convert_to_fahrenheit(celsius):
    return (celsius - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
temperature=input("Enter the temperature to convert: ")
choose =input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
temperature = float(temperature)
def main():
        if choose == "C":
            print(f"{temperature}°C is {convert_to_celsius(temperature)}°F")
        elif choose == "F":
            print(f"{temperature}°F is {convert_to_fahrenheit(temperature)}°C")
        elif choose !="C" or  choose !="F":
            print("enter approriate conversion unit")
        else:
           print("Invalid temperature. Please enter a numeric value.")
if __name__ =="__main__":
      main()
