task = input("Enter your task: ")
Priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match Priority:
    case "high" if time_bound == "yes" and Priority=="high":
        print(f"Reminder: ' {task} ' is a {Priority} priority task that requires immediate attention today!")
    case "low" if time_bound == "no" and Priority=="low":
        print(f"Note:' {task} ' is a {Priority} priority task. Consider completing it when you have free time.")
