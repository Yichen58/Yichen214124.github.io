"""
Python Basics for Data Analysis - Module 1
===========================================

Welcome to your first Python lesson! In this script, you'll learn the fundamental 
concepts you need to start analyzing data.

Learning Goals:
- Understand variables and data types
- Work with numbers and strings
- Perform basic calculations
- Use print statements to display results
"""

# ============================================================================
# 1. VARIABLES AND DATA TYPES
# ============================================================================

print("=== LESSON 1: Variables and Data Types ===")
print()

# Variables store data that we can use later
# In Python, we don't need to declare the type - Python figures it out!

# Numbers (integers)
price = 150
bedrooms = 2
print(f"This Airbnb costs ${price} per night and has {bedrooms} bedrooms")

# Numbers (decimals/floats)
review_score = 4.8
tax_rate = 0.08
print(f"Review score: {review_score}")
print(f"Tax rate: {tax_rate}")

# Text (strings)
neighborhood = "Manhattan"
property_type = "Apartment"
print(f"Property type: {property_type} in {neighborhood}")

# Boolean (True/False)
instant_bookable = True
print(f"Instant bookable: {instant_bookable}")

print("\n" + "="*50 + "\n")

# ============================================================================
# 2. BASIC CALCULATIONS FOR BUSINESS ANALYSIS
# ============================================================================

print("=== LESSON 2: Business Calculations ===")
print()

# Let's calculate some business metrics!
nightly_rate = 150
nights_booked = 20
monthly_revenue = nightly_rate * nights_booked

print(f"Nightly rate: ${nightly_rate}")
print(f"Nights booked this month: {nights_booked}")
print(f"Monthly revenue: ${monthly_revenue}")

# Calculate total cost including tax
tax_amount = monthly_revenue * tax_rate
total_with_tax = monthly_revenue + tax_amount

print(f"Tax amount: ${tax_amount:.2f}")  # .2f rounds to 2 decimal places
print(f"Total with tax: ${total_with_tax:.2f}")

# Average calculation
total_bookings = 25
total_revenue = 3750
average_booking_value = total_revenue / total_bookings

print(f"Average booking value: ${average_booking_value:.2f}")

print("\n" + "="*50 + "\n")

# ============================================================================
# 3. WORKING WITH TEXT (STRINGS)
# ============================================================================

print("=== LESSON 3: Working with Text ===")
print()

# Business often involves working with text data
host_name = "Sarah Johnson"
listing_title = "Cozy Manhattan Apartment"

# String methods (functions that work on text)
print(f"Host name in uppercase: {host_name.upper()}")
print(f"Listing title in lowercase: {listing_title.lower()}")
print(f"Number of characters in title: {len(listing_title)}")

# Combining strings
full_description = listing_title + " - hosted by " + host_name
print(f"Full description: {full_description}")

# Checking if text contains certain words
if "Manhattan" in listing_title:
    print("This property is in Manhattan!")

print("\n" + "="*50 + "\n")

# ============================================================================
# 4. PRACTICE EXERCISE
# ============================================================================

print("=== PRACTICE EXERCISE ===")
print()

# Try this yourself! Fill in the values below
print("Now it's your turn! Try changing these values:")
print()

# Change these values and run the script again
your_property_price = 200
your_property_nights = 15
your_property_type = "House"
your_neighborhood = "Brooklyn"

# The calculations will update automatically
your_monthly_revenue = your_property_price * your_property_nights
your_tax = your_monthly_revenue * 0.08
your_total = your_monthly_revenue + your_tax

print(f"Your {your_property_type} in {your_neighborhood}:")
print(f"Price per night: ${your_property_price}")
print(f"Nights booked: {your_property_nights}")
print(f"Monthly revenue: ${your_monthly_revenue}")
print(f"Tax: ${your_tax:.2f}")
print(f"Total: ${your_total:.2f}")

print("\n" + "="*50)
print("Great job! You've completed Module 1!")
print("Next: Run 02_working_with_lists.py to learn about lists")
print("="*50)