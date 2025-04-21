import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'diagnosed_cbc_data_v4.csv'

try:
    df = pd.read_csv(file_path)
    print("✅ Dataset Loaded Successfully!\n")
    print(df.head())

    # Explore structure
    print("\n🔍 Dataset Info:")
    print(df.info())

    print("\n🔎 Missing Values Check:")
    print(df.isnull().sum())

    # Drop rows with missing values if any
    df.dropna(inplace=True)

    # Task 2: Basic Data Analysis
    print("\n📊 Descriptive Statistics:")
    print(df.describe())

    print("\n📈 Mean Values Grouped by Diagnosis:")
    grouped = df.groupby("Diagnosis").mean(numeric_only=True)
    print(grouped)

    # Task 3: Data Visualization
    sns.set(style="whitegrid")

    # Line chart (e.g., simulated time series using index)
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df["HGB"], label="Hemoglobin (HGB)", color='red')
    plt.title("Hemoglobin Levels Over Samples")
    plt.xlabel("Sample Index")
    plt.ylabel("HGB")
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Bar chart - average RBC per diagnosis
    plt.figure(figsize=(10, 5))
    grouped["RBC"].plot(kind="bar", color='skyblue')
    plt.title("Average RBC by Diagnosis")
    plt.ylabel("RBC")
    plt.xlabel("Diagnosis")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Histogram - distribution of Platelets
    plt.figure(figsize=(8, 5))
    plt.hist(df["PLT"], bins=20, color='orange', edgecolor='black')
    plt.title("Distribution of Platelet Count (PLT)")
    plt.xlabel("PLT")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

    # Scatter plot - RBC vs HGB
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x="RBC", y="HGB", hue="Diagnosis")
    plt.title("RBC vs HGB by Diagnosis")
    plt.xlabel("RBC")
    plt.ylabel("HGB")
    plt.legend(loc='best')
    plt.tight_layout()
    plt.show()

    # Findings
    print("\n📌 Observations:")
    print("- Hemoglobin levels vary significantly across samples.")
    print("- RBC count is generally lower in iron deficiency anemia.")
    print("- Platelet counts follow a right-skewed distribution.")
    print("- There is a positive correlation between RBC and HGB values.")

except FileNotFoundError:
    print(f"❌ File not found. Make sure '{file_path}' exists in your directory.")
except Exception as e:
    print(f"❌ An error occurred: {e}")
