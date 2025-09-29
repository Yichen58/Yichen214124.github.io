"""
Solution 1: Python Basics for Business
=======================================

Here are the solutions to Exercise 1. Compare your answers with these.
"""

print("=== SOLUTION 1: PYTHON BASICS ===")
print()

# PART 1: Variables and Basic Calculations
print("PART 1: Business Calculations")
print("-" * 30)

# Solution: Create variables for a hotel business scenario
hotel_name = "Grand Business Hotel"
nightly_rate = 120
tax_rate = 0.12
service_fee = 25

print(f"Hotel: {hotel_name}")
print(f"Nightly rate: ${nightly_rate}")
print(f"Tax rate: {tax_rate*100}%")
print(f"Service fee: ${service_fee}")
print()

# Solution: Calculate the total cost for a 3-night stay
nights = 3
subtotal = nightly_rate * nights
tax_amount = subtotal * tax_rate
total_cost = subtotal + tax_amount + service_fee

print(f"Subtotal ({nights} nights): ${subtotal}")
print(f"Tax amount: ${tax_amount:.2f}")
print(f"Service fee: ${service_fee}")
print(f"Total cost: ${total_cost:.2f}")
print()

# Solution: Print formatted message
print(f"For a {nights}-night stay at {hotel_name}, the total cost is ${total_cost:.2f}")

print("\n" + "="*40 + "\n")

# PART 2: Working with Text Data
print("PART 2: Text Processing")
print("-" * 25)

# Given data
customer_name = "  JOHN SMITH  "
email = "john.smith@EMAIL.COM"

print(f"Original name: '{customer_name}'")
print(f"Original email: '{email}'")
print()

# Solution: Clean the customer name
clean_name = customer_name.strip().title()
print(f"Clean name: '{clean_name}'")

# Solution: Clean the email
clean_email = email.strip().lower()
print(f"Clean email: '{clean_email}'")
print()

# Solution: Create welcome message
welcome_message = f"Welcome {clean_name}! We'll send confirmations to {clean_email}"
print(welcome_message)

print("\n" + "="*40 + "\n")

# PART 3: Decision Making
print("PART 3: Business Logic")
print("-" * 20)

# Given data
customer_age = 65
is_member = True
booking_amount = 150

print(f"Customer age: {customer_age}")
print(f"Is member: {is_member}")
print(f"Original booking amount: ${booking_amount}")
print()

# Solution: Implement discount logic
final_amount = booking_amount
discounts_applied = []

# Apply senior discount if applicable
if customer_age >= 65:
    senior_discount = final_amount * 0.10
    final_amount -= senior_discount
    discounts_applied.append(f"Senior discount: -${senior_discount:.2f}")

# Apply member discount if applicable
if is_member:
    member_discount = final_amount * 0.05
    final_amount -= member_discount
    discounts_applied.append(f"Member discount: -${member_discount:.2f}")

# Print results
print("Discounts applied:")
for discount in discounts_applied:
    print(f"  • {discount}")

if not discounts_applied:
    print("  • No discounts applied")

print(f"\nFinal amount: ${final_amount:.2f}")
savings = booking_amount - final_amount
print(f"Total savings: ${savings:.2f}")

print("\n" + "="*40)
print("Great job! These are the correct solutions.")
print("Key concepts practiced:")
print("• Variables and data types")
print("• String methods (.strip(), .title(), .lower())")
print("• Mathematical operations")
print("• Conditional logic (if statements)")
print("• String formatting")
print("="*40)