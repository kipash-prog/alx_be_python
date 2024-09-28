monthly_income = int(input("Enter your monthly income: "))
total_monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - total_monthly_expenses  # Ensure this line is present
Projected_Savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print("Your monthly income is: $", monthly_income)
print("Your total monthly expenses are: $", total_monthly_expenses)
print("Your monthly savings are: $", monthly_savings)
print("Projected savings after one year, with interest, is: $", Projected_Savings)
