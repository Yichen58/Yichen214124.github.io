"""
Data Cleaning and Preparation - Module 5
=========================================

Real-world data is often messy! In this module, you'll learn essential data cleaning
techniques that every business analyst needs to know.

Learning Goals:
- Handle missing values (NaN)
- Remove or fix duplicate records
- Deal with outliers
- Standardize text data
- Validate data ranges
- Create clean datasets for analysis
"""

import pandas as pd
import numpy as np

print("=== LESSON 1: Detecting Data Quality Issues ===")
print()

# Load our data
df = pd.read_csv('data/airbnb_sample.csv')

print("Original dataset shape:", df.shape)
print()

# Let's artificially introduce some common data issues for learning purposes
df_messy = df.copy()

# Add some missing values
df_messy.loc[5, 'host_response_rate'] = np.nan
df_messy.loc[12, 'review_score'] = np.nan
df_messy.loc[18, 'bathrooms'] = np.nan

# Add some duplicate rows
df_messy = pd.concat([df_messy, df_messy.iloc[[2, 7]]], ignore_index=True)

# Add some inconsistent text data
df_messy.loc[3, 'neighborhood'] = 'manhattan'  # lowercase
df_messy.loc[8, 'property_type'] = 'APARTMENT'  # uppercase
df_messy.loc[15, 'neighborhood'] = 'Brooklyn '  # trailing space

# Add some outliers
df_messy.loc[20, 'price'] = 5000  # Extremely high price
df_messy.loc[25, 'bedrooms'] = 0   # Zero bedrooms

print("Dataset after introducing issues:", df_messy.shape)
print()

print("Data quality assessment:")
print("-" * 30)
print(f"Missing values: {df_messy.isnull().sum().sum()}")
print(f"Duplicate rows: {df_messy.duplicated().sum()}")
print(f"Unique neighborhoods: {df_messy['neighborhood'].nunique()}")
print(f"Price range: ${df_messy['price'].min()} - ${df_messy['price'].max()}")

print("\n" + "="*50 + "\n")

# ============================================================================
# 2. HANDLING MISSING VALUES
# ============================================================================

print("=== LESSON 2: Handling Missing Values ===")
print()

# Check missing values by column
missing_summary = df_messy.isnull().sum()
print("Missing values by column:")
for column, missing_count in missing_summary.items():
    if missing_count > 0:
        percentage = (missing_count / len(df_messy)) * 100
        print(f"{column}: {missing_count} ({percentage:.1f}%)")
print()

# Strategy 1: Drop rows with missing values (use carefully!)
df_dropped = df_messy.dropna()
print(f"After dropping rows with missing values: {len(df_dropped)} rows (was {len(df_messy)})")
print()

# Strategy 2: Fill missing values with appropriate replacements
df_cleaned = df_messy.copy()

# Fill missing host_response_rate with the median
median_response_rate = df_cleaned['host_response_rate'].median()
df_cleaned['host_response_rate'].fillna(median_response_rate, inplace=True)
print(f"Filled missing host_response_rate with median: {median_response_rate}")

# Fill missing review_score with the mean
mean_review_score = df_cleaned['review_score'].mean()
df_cleaned['review_score'].fillna(mean_review_score, inplace=True)
print(f"Filled missing review_score with mean: {mean_review_score:.2f}")

# Fill missing bathrooms based on bedrooms (business rule)
# Assumption: 1 bathroom per bedroom is reasonable
df_cleaned['bathrooms'].fillna(df_cleaned['bedrooms'], inplace=True)
print("Filled missing bathrooms with number of bedrooms")
print()

# Verify no missing values remain
print(f"Missing values after cleaning: {df_cleaned.isnull().sum().sum()}")

print("\n" + "="*50 + "\n")

# ============================================================================
# 3. REMOVING DUPLICATES
# ============================================================================

print("=== LESSON 3: Handling Duplicate Records ===")
print()

print(f"Total rows before removing duplicates: {len(df_cleaned)}")

# Check which rows are duplicated
duplicated_rows = df_cleaned[df_cleaned.duplicated(keep=False)]
if len(duplicated_rows) > 0:
    print("Duplicated rows found:")
    print(duplicated_rows[['listing_id', 'neighborhood', 'price']])
    print()

# Remove duplicates (keep the first occurrence)
df_cleaned = df_cleaned.drop_duplicates()
print(f"Total rows after removing duplicates: {len(df_cleaned)}")

print("\n" + "="*50 + "\n")

# ============================================================================
# 4. STANDARDIZING TEXT DATA
# ============================================================================

print("=== LESSON 4: Standardizing Text Data ===")
print()

print("Neighborhood values before cleaning:")
print(df_cleaned['neighborhood'].value_counts())
print()

# Standardize text: remove spaces, convert to title case
df_cleaned['neighborhood'] = df_cleaned['neighborhood'].str.strip()  # Remove spaces
df_cleaned['neighborhood'] = df_cleaned['neighborhood'].str.title()  # Title case

df_cleaned['property_type'] = df_cleaned['property_type'].str.strip()
df_cleaned['property_type'] = df_cleaned['property_type'].str.title()

print("Neighborhood values after cleaning:")
print(df_cleaned['neighborhood'].value_counts())
print()

print("Property type values after cleaning:")
print(df_cleaned['property_type'].value_counts())

print("\n" + "="*50 + "\n")

# ============================================================================
# 5. HANDLING OUTLIERS
# ============================================================================

print("=== LESSON 5: Detecting and Handling Outliers ===")
print()

# Method 1: Statistical approach (IQR method)
def detect_outliers_iqr(column):
    Q1 = column.quantile(0.25)
    Q3 = column.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return (column < lower_bound) | (column > upper_bound)

# Check for price outliers
price_outliers = detect_outliers_iqr(df_cleaned['price'])
print(f"Price outliers detected: {price_outliers.sum()}")

if price_outliers.sum() > 0:
    print("Outlier prices:")
    outlier_prices = df_cleaned[price_outliers][['listing_id', 'price', 'neighborhood', 'property_type']]
    print(outlier_prices)
    print()

# Method 2: Business logic approach
print("Data validation checks:")
print("-" * 25)

# Check for impossible values
zero_bedrooms = df_cleaned['bedrooms'] == 0
print(f"Properties with 0 bedrooms: {zero_bedrooms.sum()}")

negative_prices = df_cleaned['price'] < 0
print(f"Properties with negative prices: {negative_prices.sum()}")

invalid_reviews = (df_cleaned['review_score'] < 1) | (df_cleaned['review_score'] > 5)
print(f"Properties with invalid review scores: {invalid_reviews.sum()}")

# Fix the issues
print("\nFixing data issues:")
print("-" * 20)

# Fix zero bedrooms (assume studio = 1 bedroom for analysis)
df_cleaned.loc[df_cleaned['bedrooms'] == 0, 'bedrooms'] = 1
print("✅ Fixed zero bedrooms (changed to 1)")

# For the extremely high price, let's cap it at 3 times the median
price_median = df_cleaned['price'].median()
price_cap = price_median * 3
extreme_prices = df_cleaned['price'] > price_cap
df_cleaned.loc[extreme_prices, 'price'] = price_cap
print(f"✅ Capped extreme prices at ${price_cap:.0f}")

print("\n" + "="*50 + "\n")

# ============================================================================
# 6. DATA VALIDATION
# ============================================================================

print("=== LESSON 6: Final Data Validation ===")
print()

# Comprehensive validation checks
validation_results = {
    'Total records': len(df_cleaned),
    'Missing values': df_cleaned.isnull().sum().sum(),
    'Duplicate rows': df_cleaned.duplicated().sum(),
    'Price range': f"${df_cleaned['price'].min():.0f} - ${df_cleaned['price'].max():.0f}",
    'Valid review scores': ((df_cleaned['review_score'] >= 1) & (df_cleaned['review_score'] <= 5)).sum(),
    'Properties with bedrooms': (df_cleaned['bedrooms'] > 0).sum(),
    'Unique neighborhoods': df_cleaned['neighborhood'].nunique(),
    'Unique property types': df_cleaned['property_type'].nunique()
}

print("Data validation summary:")
print("-" * 30)
for check, result in validation_results.items():
    print(f"{check}: {result}")

print("\n" + "="*50 + "\n")

# ============================================================================
# 7. CREATING A CLEAN DATASET
# ============================================================================

print("=== LESSON 7: Creating Production-Ready Data ===")
print()

# Final cleaning steps
df_final = df_cleaned.copy()

# Ensure consistent data types
df_final['instant_bookable'] = df_final['instant_bookable'].astype(bool)
df_final['listing_id'] = df_final['listing_id'].astype(int)
df_final['bedrooms'] = df_final['bedrooms'].astype(int)
df_final['bathrooms'] = df_final['bathrooms'].astype(float)

# Sort by listing_id for consistency
df_final = df_final.sort_values('listing_id').reset_index(drop=True)

print("Final dataset info:")
print(df_final.info())
print()

print("Sample of cleaned data:")
print(df_final.head(10))
print()

# Save the cleaned dataset
df_final.to_csv('data/airbnb_cleaned.csv', index=False)
print("✅ Cleaned dataset saved as 'data/airbnb_cleaned.csv'")

print("\n" + "="*50 + "\n")

# ============================================================================
# 8. BEFORE/AFTER COMPARISON
# ============================================================================

print("=== LESSON 8: Before and After Comparison ===")
print()

print("BEFORE CLEANING:")
print("-" * 20)
print(f"Original dataset: {len(df)} rows")
print(f"With artificial issues: {len(df_messy)} rows")
print(f"Missing values: {df_messy.isnull().sum().sum()}")
print(f"Duplicates: {df_messy.duplicated().sum()}")
print(f"Price range: ${df_messy['price'].min()} - ${df_messy['price'].max()}")
print()

print("AFTER CLEANING:")
print("-" * 20)
print(f"Final dataset: {len(df_final)} rows")
print(f"Missing values: {df_final.isnull().sum().sum()}")
print(f"Duplicates: {df_final.duplicated().sum()}")
print(f"Price range: ${df_final['price'].min()} - ${df_final['price'].max()}")
print()

print("QUALITY IMPROVEMENTS:")
print("-" * 20)
print("✅ All missing values handled appropriately")
print("✅ Duplicate records removed")
print("✅ Text data standardized (proper capitalization)")
print("✅ Outliers identified and handled")
print("✅ Data types optimized")  
print("✅ Business rules applied (e.g., minimum bedrooms)")
print("✅ Clean dataset saved for future analysis")

print("\n" + "="*50)
print("Excellent! You now know how to clean messy data!")
print("Next: Run 06_basic_statistics.py to analyze your clean data")
print("="*50)