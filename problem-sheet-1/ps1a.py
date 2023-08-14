# problem set 1: part a house hunting

##############
annual_salary = float(input("What is your annual salary? "))
portion_saved = float(input("What percentage, as a decimal, of your salary do you wish to save? "))
total_cost = float(input("What is the total cost of your dream home? "))

current_savings = 0
portion_down_payment = 0.25*total_cost
salary_savings = portion_saved*(annual_salary/12)

# annual rate of returns on investments
r = 0.04

number_of_months = 0
# loop until enough money is available
while current_savings < portion_down_payment:
    # monthly increase of savings from investments
    current_savings += ((current_savings*r)/12)
    # net monthly increase of savings with salary savings
    current_savings += salary_savings
    # increase monthly counter
    number_of_months += 1

print("total number of months needed to save up:", number_of_months)


