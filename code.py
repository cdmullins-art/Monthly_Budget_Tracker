print("===== MONTHLY BUDGET TRACKER =====")

monthly_income = float(input("Enter your monthly income: $"))

rent = float(input("Enter your rent: $"))
food = float(input("Enter your food expenses: $"))
transportation = float(input("Enter your transportation expenses: $"))
phone = float(input("Enter your phone bill: $"))
utilities = float(input("Enter your utilities: $"))
entertainment = float(input("Enter your entertainment expenses: $"))
other = float(input("Enter your other expenses: $"))

total_expenses = rent + food + transportation + phone + utilities + entertainment + other

money_left = monthly_income - total_expenses

rent_percent = (rent / monthly_income) * 100
food_percent = (food / monthly_income) * 100
transportation_percent = (transportation / monthly_income) * 100
phone_percent = (phone / monthly_income) * 100
utilities_percent = (utilities / monthly_income) * 100
entertainment_percent = (entertainment / monthly_income) * 100
other_percent = (other / monthly_income) * 100

total_percent = (total_expenses / monthly_income) * 100

print()
print("===== MONTHLY BUDGET SUMMARY =====")
print("Monthly Income: $", monthly_income)
print()
print("Rent: $", rent)
print("Rent percentage:", rent_percent, "%")
print()
print("Food: $", food)
print("Food percentage:", food_percent, "%")
print()
print("Transportation: $", transportation)
print("Transportation percentage:", transportation_percent, "%")
print()
print("Phone: $", phone)
print("Phone percentage:", phone_percent, "%")
print()
print("Utilities: $", utilities)
print("Utilities percentage:", utilities_percent, "%")
print()
print("Entertainment: $", entertainment)
print("Entertainment percentage:", entertainment_percent, "%")
print()
print("Other expenses: $", other)
print("Other percentage:", other_percent, "%")
print()
print("Total Expenses: $", total_expenses)
print("Percentage of Income Spent:", total_percent, "%")
print("Money Left: $", money_left)
