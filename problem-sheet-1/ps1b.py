# problem set 1: part b saving with a raise

##############
annual_salary = float(input("What is your annual salary? "))
portion_saved = float(input("What percentage, as a decimal, of your salary do you wish to save? "))
total_cost = float(input("What is the total cost of your dream home? "))
semi_annual_raise = float(input("What is your semi annual raise as a decimal percentage? "))

current_savings = 0
portion_down_payment = 0.25*total_cost
# salary_savings = portion_saved*(annual_salary/12)

# annual rate of returns on investments
r = 0.04

number_of_months = 0
# loop until enough money is available
while current_savings < portion_down_payment:
    # monthly increase of savings from investments
    current_savings += ((current_savings*r)/12)
    # calculate salary savings
    salary_savings = portion_saved*(annual_salary/12)
    # net monthly increase of savings with salary savings
    current_savings += salary_savings
    # increase monthly counter
    number_of_months += 1
    # increase annual salary every 6 months
    if number_of_months % 6 == 0:
        annual_salary = annual_salary*(1+semi_annual_raise)

print("total number of months needed to save up:", number_of_months)

