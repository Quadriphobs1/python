annual_return = 0.04
semi_annual_raise = 0.07
total_cost = 1000000
portion_down_payment = total_cost * 0.25

number_of_months = 36

starting_salary = int(input("Enter your annual salary: "))


low = 0
high = 10000
guess = int((low + high)/2)
number_of_guess = 0

is_found = False
total_savings = 0.0

while abs(low - high) > 1:
    number_of_guess += 1
    annual_salary = starting_salary
    final_guess = guess / 10000
    monthly_saved = (annual_salary / 12.0) * final_guess
    current_savings = 0.0
    for i in range(1, number_of_months + 1):
        monthly_return = current_savings * (annual_return / 12)
        current_savings += monthly_return + monthly_saved

        if abs(current_savings - portion_down_payment) < 100:
            low = high
            is_found = True
            break
        elif current_savings > portion_down_payment + 100:
            break

        if i % 6 == 0:
            annual_salary += annual_salary + semi_annual_raise
            monthly_saved = (annual_salary / 12.0) * final_guess
    if current_savings < portion_down_payment - 100:
        low = guess
    elif current_savings > portion_down_payment + 100:
        high = guess
    guess = int((low + high)/2)
    total_savings = int(current_savings)
if is_found:
    print("Best savings rate:", guess / 10000)
    print("Total savings:", total_savings)
    print("Steps in bisection search path:", number_of_guess)
else:
    print("It is not possible to pay the down payment in 3 years")
    print("Steps in bisection search path:", number_of_guess)
