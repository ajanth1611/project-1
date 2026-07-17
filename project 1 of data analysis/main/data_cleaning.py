import pandas as pd
import numpy as np
df = pd.read_csv('data/Dataset for Data Analytics - Sheet1.csv')
#phase 1
print(df.head())
print(df.info())
print(df.shape)
print(df.columns)
#handling missing values

df["CouponCode"] = df["CouponCode"].fillna("No Coupon")
print(df.isnull().sum())

# duplicate values phase 2
duplicate_rows = df.duplicated().sum()

print("Duplicate Rows:", duplicate_rows)
df = df.drop_duplicates()
print("Duplicate Rows after removing:", df.duplicated().sum())
duplicate_order_ids = df["OrderID"].duplicated().sum()

print("Duplicate Order IDs:", duplicate_order_ids)
duplicate_orders = df[df.duplicated(subset="OrderID", keep=False)]

print(duplicate_orders)

print("Total Records :", len(df))
print("Unique Order IDs :", df["OrderID"].nunique())

# verification before moving
print("=" * 40)
print("PHASE 2 VERIFICATION")
print("=" * 40)

print("Duplicate Rows:", df.duplicated().sum())
print("Duplicate Order IDs:", df["OrderID"].duplicated().sum())
print("Unique Order IDs:", df["OrderID"].nunique())
print("Total Records:", len(df))

# phase 3
print(df.dtypes)
text_columns = df.select_dtypes(include="object").columns

for col in text_columns:
    df[col] = df[col].str.strip()
print(df.head())
# standardizing text data
cols_to_title = ["CustomerID", "Product", "Category", "PaymentMethod", "OrderStatus", "ReferralSource"]
for col in cols_to_title:
    if col in df.columns and df[col].dtype == object:
        df[col] = df[col].str.title()
print(df.head())
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")
print(df.head())

invalid_dates = df["Date"].isnull().sum()

print("Invalid Dates:", invalid_dates)
print(df.select_dtypes(include=["int64","float64"]).columns)
numeric_columns = df.select_dtypes(include=["float64"]).columns

df[numeric_columns] = df[numeric_columns].round(2)
print(df.head())
print("="*40)
print("PHASE 3 VERIFICATION")
print("="*40)

print("Missing Values")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

print("Duplicate Order IDs:", df["OrderID"].duplicated().sum())

print("Invalid Dates:", df["Date"].isnull().sum())

df.to_csv("cleaned_orders.csv", index=False)

print("Cleaned dataset saved successfully.")