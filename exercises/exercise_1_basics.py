"""
Exercise 1: Python Basics for Business
=======================================

Practice the fundamental concepts you learned in Module 1.
Complete each section by writing the requested code.

Instructions:
- Read each question carefully
- Write your code below each comment
- Run the script to check your answers
- Compare with the solution file when you're done
"""

print("=== EXERCISE 1: PYTHON BASICS ===")
print()

# PART 1: Variables and Basic Calculations
print("PART 1: Business Calculations")
print("-" * 30)

# TODO: Create variables for a hotel business scenario
# hotel_name = your hotel name as a string
# nightly_rate = price per night as a number
# tax_rate = 0.12 (12% tax)
# service_fee = 25 (flat service fee)

# Write your code here:



# TODO: Calculate the total cost for a 3-night stay
# Include the nightly rate, tax, and service fee
# Formula: (nightly_rate * nights * (1 + tax_rate)) + service_fee

# Write your code here:



# TODO: Print a formatted message showing:
# "For a 3-night stay at [hotel_name], the total cost is $[total_cost]"

# Write your code here:



print("\n" + "="*40 + "\n")

# PART 2: Working with Text Data
print("PART 2: Text Processing")
print("-" * 25)

# Given data
customer_name = "  JOHN SMITH  "
email = "john.smith@EMAIL.COM"

# TODO: Clean the customer name (remove spaces, proper capitalization)
# Hint: Use .strip() and .title() methods

# Write your code here:



# TODO: Clean the email (remove spaces, make lowercase)
# Hint: Use .strip() and .lower() methods

# Write your code here:



# TODO: Create a welcome message
# Format: "Welcome [clean_name]! We'll send confirmations to [clean_email]"

# Write your code here:



print("\n" + "="*40 + "\n")

# PART 3: Decision Making
print("PART 3: Business Logic")
print("-" * 20)

# Given data
customer_age = 65
is_member = True
booking_amount = 150

# TODO: Implement discount logic:
# - Senior discount (age >= 65): 10% off
# - Member discount: 5% off  
# - Both discounts can apply
# Calculate the final amount after discounts

# Write your code here:
final_amount = booking_amount  # Start with original amount

# Apply senior discount if applicable


# Apply member discount if applicable


# TODO: Print the final amount and what discounts were applied

# Write your code here:



print("\n" + "="*40)
print("Exercise 1 Complete!")
print("Check your answers against solutions/solution_1_basics.py")
print("="*40)