import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    try:
        # Convert the arguments to float or int
        numerator = float(sys.argv[1])
        denominator = float(sys.argv[2])

        # Call the safe_divide function and print the result
        result = safe_divide(numerator, denominator)
        print(result)

    except ValueError:
        print("Invalid input! Both numerator and denominator must be numbers.")
        sys.exit(1)

if __name__ == "__main__":
    main()
