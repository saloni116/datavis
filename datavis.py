
# BDA Experiment 4
# Data Visualization using Python

import pandas as pd
import matplotlib.pyplot as plt

# 1. Create a sample dataset
sales_data = pd.DataFrame({
    "Product": [
        "Laptop", "Mobile", "Tablet", "Headphones", "Keyboard"
    ],
    "Price": [55000, 25000, 18000, 3000, 1500],
    "Sales": [25, 40, 30, 60, 50],
    "Advertising_Hours": [5, 8, 4, 7, 3]
})

# 2. Display the dataset
print("Sales Dataset:")
print(sales_data)

# 3. Display summary statistics
print("\nSummary Statistics:")
print(sales_data.describe())

# 4. Bar chart of product sales
plt.figure(figsize=(8, 5))
plt.bar(
    sales_data["Product"],
    sales_data["Sales"],
    color="skyblue"
)
plt.title("Product Sales")
plt.xlabel("Products")
plt.ylabel("Units Sold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 5. Scatter plot of advertising hours vs sales
plt.figure(figsize=(8, 5))
plt.scatter(
    sales_data["Advertising_Hours"],
    sales_data["Sales"],
    color="red",
    marker="o"
)
plt.title("Advertising Hours vs Sales")
plt.xlabel("Advertising Hours")
plt.ylabel("Units Sold")
plt.tight_layout()
plt.show()

# 6. Histogram of product prices
plt.figure(figsize=(8, 5))
plt.hist(
    sales_data["Price"],
    color="lightgreen",
    edgecolor="black"
)
plt.title("Distribution of Product Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 7. Boxplot of product prices
plt.figure(figsize=(8, 5))
plt.boxplot(
    sales_data["Price"],
    patch_artist=True
)
plt.title("Boxplot of Product Prices")
plt.ylabel("Price")
plt.tight_layout()
plt.show()

# 8. Display a message
print("\nData Visualization Completed Successfully!")


#cmds  1.python -m pip install pandas matplotlib  /  py -m pip install pandas matplotlib    ,2.python datavis.py 