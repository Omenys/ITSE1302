#Chapter 2 Week 4 Assignment

# Get user input on purchase amount
user_input = float(input("Please enter the amount of your purchase in numeric format: $"))

# Calculate taxes
state_tax = user_input * 0.05
county_tax = user_input * 0.025
total_tax = state_tax + county_tax

# Calcuate sale total
sale_total = total_tax + user_input

# Display total cost to user
print(f"\nThe sale total is ${sale_total:0.2f}.\n")

# Display breakdown of cost to user
print(f"Purchase Amount: ${user_input:0.2f}")
print(f"Total taxes: ${total_tax:0.2f}")
print(f"  State tax: ${state_tax:0.2f}")
print(f"  County tax: ${county_tax:0.2f}")
