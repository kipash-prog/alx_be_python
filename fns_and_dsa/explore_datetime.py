from datetime import *

def display_current_datetime():
    current_date=datetime.datetime.now("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")
def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))   
    current_date=datetime.datetime.now()
    future_date = current_date + datetime.timedelta(days=number_of_days)
    future_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Future date: {future_date}")
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()   
 
