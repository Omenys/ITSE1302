# Name: Raven Daigle
# Course: ITSE 1302
# Date: March 11, 2023
# Description: Calculate accumulated salary and display total amount in a table 


# Instructions to user for input
print("Your salary is $0.01 on your first day of work.")
print("Your salary will double each day.")

# Loop until valid input
valid_response = False

while True:
    try:
        # Get total days worked
        days_worked = int(input("Enter the number of days worked to calculate your total pay: "))
        if days_worked < 0:
            print("! Error !: Invalid response. Input must be zero or more.")
            continue
        valid_response = True
        break
    # Exception if invalid input
    except BaseException:
        print("! Error !: Invalid input.")
        continue

# Calculate total pay from input
if valid_response and days_worked == 0:
    print("You did not earn a salary.")
elif valid_response:
    # Accumulator variable
    total_pay = 0.00
    # Starting pay rate variable 
    current_pay = 0.01

    for day in range(1, days_worked+1):
        print(f"Day Worked: {day}, Salary: {current_pay}")
        total_pay += current_pay
        current_pay *= 2
    print(f"Your total salary is ${total_pay:,.2f}.")