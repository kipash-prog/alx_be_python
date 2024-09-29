task = input("Enter your task: ")
Priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Match the priority and time-bound status
match Priority:
    case "high" if time_bound == "yes":
        print(f"Reminder: '{task}' is a {Priority} priority task that requires immediate attention today!")
    case "low" if time_bound == "no":
        print(f"Note: '{task}' is a {Priority} priority task. Consider completing it when you have free time.")
    case _:
        print(f"Task '{task}' with priority '{Priority}' and time-bound status '{time_bound}' does not match specific criteria.")
