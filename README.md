[airbnb_analysis_blog.md](https://github.com/user-attachments/files/22876675/airbnb_analysis_blog.md)
# 🏡 Exploring Airbnb Data: A Visual and Analytical Deep Dive

Data tells stories — and the Airbnb dataset is no exception. In this project, I set out to uncover patterns in room types, pricing trends, and hosting behaviors across Airbnb listings. My goal was not just to visualize the numbers, but to understand what drives pricing, what differentiates room types, and how data cleaning can sharpen our insights.

---

## Table of Contents
1. [Introduction](#introduction)
2. [Dataset Overview](#dataset-overview)
3. [Room Type Distribution](#room-type-distribution)
4. [Price Analysis](#price-analysis)
   - [Raw Price Distribution](#raw-price-distribution)
   - [Outlier Removal with IQR](#outlier-removal-with-iqr)
5. [Minimum Nights and Pricing Relationship](#minimum-nights-and-pricing-relationship)
6. [Host Analysis](#host-analysis)
7. [Key Takeaways](#key-takeaways)
8. [Conclusion](#conclusion)
9. [References](#references)

---

## Introduction

In this project, I analyzed Airbnb data to explore **how room types, minimum night requirements, and host behaviors influence pricing**. I used Python with libraries such as `pandas`, `matplotlib`, and `seaborn` for data manipulation and visualization.  

The focus was on turning raw data into business-relevant insights — such as identifying how much room type impacts price and where hosts may optimize their listing strategy.

---

## Dataset Overview

I began by importing and exploring two CSV files:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

airbnb_df = pd.read_csv('airbnb_data.csv')
location_df = pd.read_csv('location.csv')
```

The `airbnb_df` contained **14 columns and 16,228 rows**, while the `location_df` had **5 columns and 16,228 rows** — confirming both datasets were aligned by index.

A quick look at the head of the dataset revealed fields such as:
- `id`, `name`, `host_id`, `host_name`
- `room_type`, `price`, `minimum_nights`

These form the backbone of the Airbnb listing structure.

---

## Room Type Distribution

Understanding the breakdown of room types was my first step. I used a simple bar chart to show how listings are distributed by room type.

```python
room_type_counts = df['room_type'].value_counts()
plt.figure(figsize=(10, 6))
room_type_counts.plot(kind='bar')
plt.title('Distribution of Room Types')
plt.xlabel('Room Type')
plt.ylabel('Count')
plt.show()
```

📊 **Visualization:**  
![Bar chart showing counts of room types](room-type-distribution.png)

**Interpretation:**  
Entire homes/apartments tend to dominate Airbnb markets, followed by private rooms — a pattern consistent with urban travel demand for privacy and convenience.

---

## Price Analysis

Next, I explored how prices vary across room types. The boxplot visualization provided a strong initial view.

### Raw Price Distribution

```python
plt.figure(figsize=(10, 6))
sns.boxplot(x='room_type', y='price', data=df)
plt.title('Price Distribution by Room Type')
plt.xlabel('Room Type')
plt.ylabel('Price')
plt.show()
```

📊 **Visualization:**  
![Boxplot of price distribution by room type](price-distribution-raw.png)

**Observation:**  
The spread of prices was **highly skewed** — with extreme outliers. This suggested the need for deeper analysis to avoid misleading averages.

---

### Outlier Removal with IQR

To clean the price data, I applied the **Interquartile Range (IQR)** method:

```python
Q1 = df.groupby('room_type')['price'].transform('quantile', 0.25)
Q3 = df.groupby('room_type')['price'].transform('quantile', 0.75)
IQR = Q3 - Q1

lower_bounds = Q1 - 1.5 * IQR
upper_bounds = Q3 + 1.5 * IQR

mask = (df['price'] >= lower_bounds) & (df['price'] <= upper_bounds)
```

Then, I replotted the cleaned data:

```python
plt.figure(figsize=(12, 6))
sns.boxplot(x='room_type', y='price', data=df[mask])
plt.title('Price Distribution by Room Type (Outliers Removed)')
plt.xlabel('Room Type')
plt.ylabel('Price')
plt.show()
```

📊 **Visualization:**  
![Cleaned boxplot of price distribution by room type](price-distribution-clean.png)

**Insight:**  
After outlier removal, **private rooms showed a tighter price range**, while **entire homes remained the most expensive category**. This step improved interpretability significantly.

---

## Minimum Nights and Pricing Relationship

A key question was whether listings that require more minimum nights tend to be priced higher.

```python
plt.figure(figsize=(10, 6))
sns.scatterplot(x='minimum_nights', y='price', hue='room_type', data=df)
plt.title('Price vs Minimum Nights')
plt.xlabel('Minimum Nights')
plt.ylabel('Price')
plt.show()
```

📈 **Visualization:**  
![Scatterplot showing price vs minimum nights](price-vs-minimum-nights.png)

**Observation:**  
The data suggested that **higher minimum night requirements do not necessarily lead to higher prices**. Instead, luxury listings often had flexible minimum stays, driven more by location and amenities than duration.

---

## Host Analysis

Although less explored in this notebook, host-related features such as `host_id` and `host_name` can reveal **superhost dominance** and **multi-listing patterns**. Future analysis could examine:
- The number of listings per host  
- Host pricing consistency  
- Correlation between host experience and price  

---

## Key Takeaways

- **Data cleaning is critical** — outliers can distort price insights.
- **Room type strongly affects price**, with entire homes being the premium tier.
- **Minimum night requirements** are not a major price driver.
- Visual storytelling through **boxplots and scatterplots** transforms abstract data into actionable understanding.

---

## Conclusion

This Airbnb analysis offered a clear window into how **property type and data quality shape pricing perception**. By removing outliers and visualizing clean data, we gain a more realistic picture of what travelers pay — and what hosts can expect.  

Ultimately, blending data science with business context helps turn exploration into strategy. The next step could involve predictive modeling for price estimation or geographic segmentation using the `location_df`.

---

## References

- Airbnb public dataset samples (Kaggle)
- Seaborn and Matplotlib documentation  
- Pandas Data Analysis Guide  
