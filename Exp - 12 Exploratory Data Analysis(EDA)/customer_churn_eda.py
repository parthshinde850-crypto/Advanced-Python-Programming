import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

# 1. Load the customer churn dataset
df = pd.read_csv("customer_churn.csv")

# 2. Display dataset information
print("First Five Records:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nColumn Names:")
print(df.columns)

# 3. Descriptive Statistics
print("\nDescriptive Statistics:")
print(df.describe())

numeric_df = df.select_dtypes(include="number")

print("\nMean:")
print(numeric_df.mean())

print("\nMedian:")
print(numeric_df.median())

print("\nMode:")
print(df.mode().iloc[0])

print("\nStandard Deviation:")
print(numeric_df.std())

print("\nVariance:")
print(numeric_df.var())

print("\nMinimum:")
print(numeric_df.min())

print("\nMaximum:")
print(numeric_df.max())

print("\nQuantiles:")
print(numeric_df.quantile([0.25, 0.50, 0.75]))

# 4. Data Visualization

# Histogram
numeric_df.hist(figsize=(12, 8), bins=10, edgecolor="black")
plt.suptitle("Histogram of Numerical Features")
plt.tight_layout()
plt.show()

# Box Plot
for column in numeric_df.columns:
    plt.figure()
    sns.boxplot(x=df[column])
    plt.title("Box Plot of " + column)
    plt.show()

# Scatter Plot
if len(numeric_df.columns) >= 2:
    plt.figure()
    plt.scatter(numeric_df.iloc[:, 0], numeric_df.iloc[:, 1])
    plt.xlabel(numeric_df.columns[0])
    plt.ylabel(numeric_df.columns[1])
    plt.title("Scatter Plot")
    plt.show()

# Correlation Heatmap
if len(numeric_df.columns) >= 2:
    plt.figure(figsize=(10, 6))
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()

# 5. Handle Missing Data
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Remove rows with missing values
df = df.dropna().copy()

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# 6. Detect and Handle Outliers Using Z-Score
numeric_cols = df.select_dtypes(include="number").columns

if len(numeric_cols) > 0:
    z_scores = df[numeric_cols].apply(
        lambda col: zscore(col, nan_policy="omit")
    )

    outliers = (z_scores.abs() > 3)

    print("\nDetected Outliers:")
    print(df[outliers.any(axis=1)])

    # Cap outliers using the IQR method
    for column in numeric_cols:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1

        lower_limit = Q1 - 1.5 * IQR
        upper_limit = Q3 + 1.5 * IQR

        df[column] = df[column].clip(
            lower=lower_limit,
            upper=upper_limit
        )

# 7. Verify Cleaned Dataset
print("\nMissing Values in Final Dataset:")
print(df.isnull().sum())

print("\nFinal Dataset:")
print(df.head())

print("\nFinal Dataset Shape:")
print(df.shape)

# 8. Save Cleaned Dataset
df.to_csv("cleaned_customer_churn.csv", index=False)

print("\nCleaned dataset saved successfully!")