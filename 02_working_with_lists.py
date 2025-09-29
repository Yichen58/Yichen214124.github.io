"""
Working with Lists - Module 2
==============================

Lists are one of the most important data structures in Python. They're perfect 
for storing multiple pieces of related data, like a list of prices or neighborhoods.

Learning Goals:
- Create and work with lists
- Access individual items in lists
- Add and remove items from lists
- Calculate statistics from lists
- Use loops to process data
"""

# ============================================================================
# 1. CREATING AND ACCESSING LISTS
# ============================================================================

print("=== LESSON 1: Creating Lists ===")
print()

# Lists store multiple items in order
# Perfect for storing data about multiple Airbnb properties!

prices = [150, 200, 120, 90, 250]
neighborhoods = ["Manhattan", "Brooklyn", "Queens", "Bronx", "Staten Island"]
property_types = ["Apartment", "House", "Condo", "Loft"]

print("Prices:", prices)
print("Neighborhoods:", neighborhoods)
print("Property types:", property_types)

# Access individual items using index (starting from 0!)
print(f"\nFirst price: ${prices[0]}")
print(f"Second neighborhood: {neighborhoods[1]}")
print(f"Last property type: {property_types[-1]}")  # -1 gets the last item

print("\n" + "="*50 + "\n")

# ============================================================================
# 2. LIST OPERATIONS FOR BUSINESS ANALYSIS
# ============================================================================

print("=== LESSON 2: Analyzing Lists of Data ===")
print()

# Let's analyze some business data!
monthly_bookings = [12, 18, 15, 22, 9, 25, 20, 16, 19, 14, 21, 17]
print("Monthly bookings for the year:", monthly_bookings)

# Basic statistics
total_bookings = sum(monthly_bookings)
average_bookings = total_bookings / len(monthly_bookings)
highest_month = max(monthly_bookings)
lowest_month = min(monthly_bookings)

print(f"Total bookings this year: {total_bookings}")
print(f"Average bookings per month: {average_bookings:.1f}")
print(f"Best month: {highest_month} bookings")
print(f"Worst month: {lowest_month} bookings")

# Working with multiple lists together
property_ids = [1001, 1002, 1003, 1004, 1005]
property_prices = [150, 200, 120, 90, 250]
property_neighborhoods = ["Manhattan", "Brooklyn", "Manhattan", "Queens", "Brooklyn"]

print(f"\nProperty Analysis:")
for i in range(len(property_ids)):
    print(f"Property {property_ids[i]}: ${property_prices[i]} in {property_neighborhoods[i]}")

print("\n" + "="*50 + "\n")

# ============================================================================
# 3. FILTERING AND SORTING DATA
# ============================================================================

print("=== LESSON 3: Filtering and Sorting ===")
print()

# Find expensive properties (over $150)
expensive_properties = []
for price in property_prices:
    if price > 150:
        expensive_properties.append(price)

print("Expensive properties (>$150):", expensive_properties)

# Count properties by neighborhood
manhattan_count = property_neighborhoods.count("Manhattan")
brooklyn_count = property_neighborhoods.count("Brooklyn")

print(f"Manhattan properties: {manhattan_count}")
print(f"Brooklyn properties: {brooklyn_count}")

# Sort prices (this creates a new sorted list)
sorted_prices = sorted(property_prices)
print("Prices from lowest to highest:", sorted_prices)

# Sort in descending order
sorted_prices_desc = sorted(property_prices, reverse=True)
print("Prices from highest to lowest:", sorted_prices_desc)

print("\n" + "="*50 + "\n")

# ============================================================================
# 4. ADDING AND REMOVING DATA
# ============================================================================

print("=== LESSON 4: Updating Lists ===")
print()

# Start with a list of review scores
review_scores = [4.8, 4.5, 4.9, 4.2]
print("Original review scores:", review_scores)

# Add new review scores
review_scores.append(4.7)  # Add to the end
review_scores.append(4.6)
print("After adding new reviews:", review_scores)

# Remove the lowest score
lowest_score = min(review_scores)
review_scores.remove(lowest_score)
print(f"After removing lowest score ({lowest_score}):", review_scores)

# Insert a score at a specific position
review_scores.insert(0, 5.0)  # Insert 5.0 at the beginning
print("After inserting perfect score at beginning:", review_scores)

print("\n" + "="*50 + "\n")

# ============================================================================
# 5. BUSINESS INSIGHTS WITH LISTS
# ============================================================================

print("=== LESSON 5: Business Insights ===")
print()

# Real business scenario: analyzing property performance
property_names = ["Cozy Studio", "Family House", "Luxury Loft", "Budget Room", "Modern Apt"]
weekly_revenue = [1050, 1400, 2100, 630, 1200]
occupancy_rates = [0.85, 0.75, 0.60, 0.95, 0.80]  # as decimals (85%, 75%, etc.)

print("Property Performance Analysis:")
print("-" * 40)

for i in range(len(property_names)):
    revenue = weekly_revenue[i]
    occupancy = occupancy_rates[i] * 100  # Convert to percentage
    
    print(f"{property_names[i]:<15} | ${revenue:>6} | {occupancy:>5.1f}%")

# Find the best performing property
best_revenue_index = weekly_revenue.index(max(weekly_revenue))
best_property = property_names[best_revenue_index]
best_revenue = max(weekly_revenue)

print(f"\nTop performer: {best_property} with ${best_revenue} weekly revenue")

# Calculate total portfolio performance
total_revenue = sum(weekly_revenue)
average_occupancy = sum(occupancy_rates) / len(occupancy_rates) * 100

print(f"Total portfolio revenue: ${total_revenue}")
print(f"Average occupancy rate: {average_occupancy:.1f}%")

print("\n" + "="*50 + "\n")

# ============================================================================
# 6. PRACTICE EXERCISE
# ============================================================================

print("=== PRACTICE EXERCISE ===")
print()

print("Try this yourself!")
print("1. Create a list of your own property prices")
print("2. Calculate the average price")
print("3. Find properties above and below average")
print()

# Your turn! Try modifying these lists:
my_prices = [100, 150, 200, 75, 300, 125, 175]
my_neighborhoods = ["Area A", "Area B", "Area A", "Area C", "Area B", "Area A", "Area C"]

# Calculate average
average_price = sum(my_prices) / len(my_prices)
print(f"Your average price: ${average_price:.2f}")

# Find above and below average
above_average = [price for price in my_prices if price > average_price]
below_average = [price for price in my_prices if price <= average_price]

print(f"Above average prices: {above_average}")
print(f"Below average prices: {below_average}")

print("\n" + "="*50)
print("Excellent! You've mastered lists!")
print("Next: Run 03_reading_data.py to learn about reading CSV files")
print("="*50)