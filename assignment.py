import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
file_path = 'diagnosed_cbc_data_v4.csv'

try:
    df = pd.read_csv(file_path)
    print("✅ Dataset Loaded Successfully!\n")
    print(df.head())

    # Explore dataset
    print("\n🔍 Dataset Info:")
    print(df.info())

    print("\n🔎 Missing Values:")
    print(df.isnull().sum())

    # Clean missing values (if any)
    df.dropna(inplace=True)

    # Task 2: Basic Data Analysis
    print("\n📊 Descriptive Statistics:")
    print(df.describe())

    print("\n📈 Mean Values by Diagnosis:")
    group_means = df.groupby("Diagnosis").mean(numeric_only=True)
    print(group_means)

    # Task 3: Data Visualization

    # 1. Line chart (e.g. HGB over sample index)
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df["HGB"], color='blue', label='Hemoglobin (HGB)')
    plt.title("Hemoglobin Levels Across Samples")
    plt.xlabel("Sample Index")
    plt.ylabel("Hemoglobin (g/dL)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # 2. Bar chart: Average RBC per Diagnosis
    plt.figure(figsize=(10, 5))
    group_means["RBC"].plot(kind='bar', color='green')
    plt.title("Average RBC Count by Diagnosis")
    plt.xlabel("Diagnosis")
    plt.ylabel("Average RBC (x10^6/μL)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # 3. Histogram: PLT distribution
    plt.figure(figsize=(8, 5))
    plt.hist(df["PLT"], bins=20, color='orange', edgecolor='black')
    plt.title("Distribution of Platelet Count (PLT)")
    plt.xlabel("Platelets (x10^3/μL)")
    plt.ylabel("Frequency")
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

    # 4. Scatter plot: RBC vs HGB
    plt.figure(figsize=(8, 5))
    plt.scatter(df["RBC"], df["HGB"], color='purple', alpha=0.6)
    plt.title("Scatter Plot: RBC vs Hemoglobin")
    plt.xlabel("RBC (x10^6/μL)")
    plt.ylabel("Hemoglobin (g/dL)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Findings
    print("\n📌 Observations:")
    print("- Hemoglobin levels fluctuate across the dataset, possibly reflecting anemia types.")
    print("- RBC values differ by diagnosis, especially lower in iron deficiency anemia.")
    print("- Platelet count (PLT) has a right-skewed distribution.")
    print("- There's a positive linear trend between RBC and Hemoglobin levels.")

except FileNotFoundError:
    print(f"❌ File not found. Make sure the file '{file_path}' is in the correct folder.")
except Exception as e:
    print(f"❌ An error occurred: {e}")
