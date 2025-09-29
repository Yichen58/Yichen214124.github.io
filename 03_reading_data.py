"""
Reading Data from CSV Files - Module 3
=======================================

In the business world, data often comes in CSV (Comma Separated Values) files.
These are like Excel spreadsheets but in a simple text format. We'll use the 
pandas library to read and work with this data.

Learning Goals:
- Import the pandas library
- Read CSV files into DataFrames
- Explore the structure of your data
- Access columns and rows
- Get basic information about your dataset
"""

# ============================================================================
# 1. IMPORTING PANDAS AND READING DATA
# ============================================================================

print("=== LESSON 1: Reading CSV Data ===")
print()

# Import pandas - this is the most important library for data analysis in Python
import pandas as pd

# Read our Airbnb data
# Make sure the data/airbnb_sample.csv file exists in your folder!
try:
    df = pd.read_csv('data/airbnb_sample.csv')
    print("✅ Successfully loaded the Airbnb data!")
    print(f"Data loaded: {len(df)} properties")
except FileNotFoundError:
    print("❌ Could not find the data file. Make sure 'data/airbnb_sample.csv' exists!")
    print("You can create sample data or download it from the repository.")
    exit()

print("\n" + "="*50 + "\n")

# ============================================================================
# 2. EXPLORING YOUR DATA
# ============================================================================

print("=== LESSON 2: First Look at Your Data ===")
print()

# Look at the first few rows
print("First 5 rows of data:")
print(df.head())
print()

# Get basic information about the dataset
print("Dataset Information:")
print(f"Number of rows (properties): {len(df)}")
print(f"Number of columns (features): {len(df.columns)}")
print()

print("Column names:")
for i, column in enumerate(df.columns, 1):
    print(f"{i}. {column}")

print("\n" + "="*50 + "\n")

# ============================================================================
# 3. ACCESSING COLUMNS AND BASIC STATISTICS
# ============================================================================

print("=== LESSON 3: Working with Columns ===")
print()

# Access individual columns
prices = df['price']
neighborhoods = df['neighborhood']
property_types = df['property_type']

print("Price column (first 10 values):")
print(prices.head(10))
print()

# Basic statistics for numerical columns
print("Price Statistics:")
print(f"Average price: ${prices.mean():.2f}")
print(f"Median price: ${prices.median():.2f}")
print(f"Minimum price: ${prices.min():.2f}")
print(f"Maximum price: ${prices.max():.2f}")
print(f"Standard deviation: ${prices.std():.2f}")
print()

# Count unique values in categorical columns
print("Neighborhood Distribution:")
neighborhood_counts = neighborhoods.value_counts()
print(neighborhood_counts)
print()

print("Property Type Distribution:")
property_type_counts = property_types.value_counts()
print(property_type_counts)

print("\n" + "="*50 + "\n")

# ============================================================================
# 4. FILTERING DATA
# ============================================================================

print("=== LESSON 4: Filtering Data ===")
print()

# Filter for expensive properties (over $150)
expensive_properties = df[df['price'] > 150]
print(f"Expensive properties (>$150): {len(expensive_properties)} out of {len(df)}")
print()

# Filter for Manhattan properties
manhattan_properties = df[df['neighborhood'] == 'Manhattan']
print(f"Manhattan properties: {len(manhattan_properties)}")
print(f"Average Manhattan price: ${manhattan_properties['price'].mean():.2f}")
print()

# Multiple conditions - Manhattan apartments under $200
manhattan_apartments = df[(df['neighborhood'] == 'Manhattan') & 
                        (df['property_type'] == 'Apartment') & 
                        (df['price'] < 200)]
print(f"Manhattan apartments under $200: {len(manhattan_apartments)}")
print()

# Show these properties
if len(manhattan_apartments) > 0:
    print("These properties:")
    print(manhattan_apartments[['listing_id', 'price', 'bedrooms', 'review_score']])

print("\n" + "="*50 + "\n")

# ============================================================================
# 5. SORTING AND RANKING
# ============================================================================

print("=== LESSON 5: Sorting and Ranking ===")
print()

# Sort by price (ascending)
sorted_by_price = df.sort_values('price')
print("5 Cheapest properties:")
print(sorted_by_price[['listing_id', 'property_type', 'neighborhood', 'price']].head())
print()

# Sort by price (descending)
sorted_by_price_desc = df.sort_values('price', ascending=False)
print("5 Most expensive properties:")
print(sorted_by_price_desc[['listing_id', 'property_type', 'neighborhood', 'price']].head())
print()

# Sort by review score
sorted_by_reviews = df.sort_values('review_score', ascending=False)
print("5 Highest rated properties:")
print(sorted_by_reviews[['listing_id', 'property_type', 'neighborhood', 'price', 'review_score']].head())

print("\n" + "="*50 + "\n")

# ============================================================================
# 6. GROUPING DATA FOR BUSINESS INSIGHTS
# ============================================================================

print("=== LESSON 6: Business Analysis by Groups ===")
print()

# Average price by neighborhood
avg_price_by_neighborhood = df.groupby('neighborhood')['price'].mean()
print("Average price by neighborhood:")
for neighborhood, avg_price in avg_price_by_neighborhood.items():
    print(f"{neighborhood}: ${avg_price:.2f}")
print()

# Count properties by type
properties_by_type = df.groupby('property_type').size()
print("Number of properties by type:")
for prop_type, count in properties_by_type.items():
    print(f"{prop_type}: {count}")
print()

# Average review score by property type
avg_reviews_by_type = df.groupby('property_type')['review_score'].mean()
print("Average review score by property type:")
for prop_type, avg_score in avg_reviews_by_type.items():
    print(f"{prop_type}: {avg_score:.2f}")

print("\n" + "="*50 + "\n")

# ============================================================================
# 7. BUSINESS QUESTIONS TO EXPLORE
# ============================================================================

print("=== LESSON 7: Answering Business Questions ===")
print()

# Question 1: What's the most profitable neighborhood?
print("1. Most profitable neighborhood (by average price):")
most_profitable = avg_price_by_neighborhood.max()
most_profitable_neighborhood = avg_price_by_neighborhood.idxmax()
print(f"   {most_profitable_neighborhood}: ${most_profitable:.2f}")
print()

# Question 2: Do more bedrooms mean higher prices?
price_by_bedrooms = df.groupby('bedrooms')['price'].mean()
print("2. Average price by number of bedrooms:")
for bedrooms, avg_price in price_by_bedrooms.items():
    print(f"   {bedrooms} bedrooms: ${avg_price:.2f}")
print()

# Question 3: What's the relationship between price and review score?
high_rated = df[df['review_score'] >= 4.5]
low_rated = df[df['review_score'] < 4.5]
print("3. Price vs Review Score:")
print(f"   High-rated properties (4.5+): ${high_rated['price'].mean():.2f}")
print(f"   Lower-rated properties (<4.5): ${low_rated['price'].mean():.2f}")

print("\n" + "="*50)
print("Great work! You can now read and explore data files!")
print("Next: Run 04_data_exploration.py for more advanced exploration")
print("="*50)