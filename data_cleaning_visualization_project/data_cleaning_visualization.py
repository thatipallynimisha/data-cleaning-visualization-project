
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("raw_sales_data.csv")

print("Original Shape:", df.shape)

# Handle missing values
df['Sales'] = df['Sales'].fillna(df['Sales'].mean())
df['Quantity'] = df['Quantity'].fillna(df['Quantity'].median())

# Remove duplicates
df = df.drop_duplicates()

# Simple outlier handling (cap very large sales values)
q99 = df['Sales'].quantile(0.99)
df.loc[df['Sales'] > q99, 'Sales'] = q99

print("Cleaned Shape:", df.shape)

# Save cleaned dataset
df.to_csv("cleaned_sales_data.csv", index=False)

# Visualization 1: Sales by Region
sales_region = df.groupby("Region")["Sales"].sum()
sales_region.plot(kind="bar", title="Total Sales by Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("sales_by_region.png")
plt.clf()

# Visualization 2: Sales distribution
df["Sales"].plot(kind="hist", bins=20, title="Sales Distribution")
plt.xlabel("Sales")
plt.tight_layout()
plt.savefig("sales_distribution.png")
plt.clf()

# Visualization 3: Quantity vs Sales
plt.scatter(df["Quantity"], df["Sales"])
plt.xlabel("Quantity")
plt.ylabel("Sales")
plt.title("Quantity vs Sales")
plt.tight_layout()
plt.savefig("quantity_vs_sales.png")
plt.clf()

print("Project completed. Cleaned data and charts generated.")
