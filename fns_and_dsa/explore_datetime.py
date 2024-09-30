import datetime  # Ensure this line is present

def display_current_datetime():
    current_date = datetime.datetime.now()
    print(f"Current date and time: {current_date}")

def calculate_future_date():
    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.datetime.now().date()  # Get only the date part
        future_date = current_date + datetime.timedelta(days=number_of_days)  # Correct timedelta usage
        print(f"Future date: {future_date}")
    except ValueError:
        print("Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
