monthly_income = input("Enter your monthly income:")
total_monthly_income = input("Enter your total monthly expenses:")
monthly_savings = monthly_income - total_monthly_income
Projected_Savings = monthly_savings * 12 + ( monthly_savings * 12 * 0.05 )
print("Enter your monthly income:", monthly_income)
print("Enter your total monthly expenses:", total_monthly_income)
print("Your monthly savings are", monthly_savings)
print("Projected savings after one year, with interest, is:",Projected_Savings)