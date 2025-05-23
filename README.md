# CBC Data Analysis Assignment
This project performs data analysis and basic visualizations on a Complete Blood Count (CBC) dataset with medical diagnoses.
# Objective
- Load and explore the dataset using `pandas`.
- Clean missing data.
- Perform basic statistical analysis.
- Visualize trends and distributions using `matplotlib`.
- 
# Dataset

The dataset used is `diagnosed_cbc_data_v4.csv`, which contains CBC parameters and corresponding medical diagnoses.

# Features Analyzed

- Hemoglobin (HGB)
- Red Blood Cell Count (RBC)
- Platelet Count (PLT)
- Diagnosis (categorical)

# Visualizations

1. Line Chart – Hemoglobin levels over sample index.
2. Bar Chart – Average RBC count per diagnosis.
3. Histogram – Distribution of platelet counts.
4. Scatter Plot – Relationship between RBC and Hemoglobin.

# How to Run

1. Clone or download this repository.
2. Ensure `diagnosed_cbc_data_v4.csv` is in the same folder as the script.
3. Run the Python script:

# Observations

- Hemoglobin levels vary across the dataset.
- RBC values are lower in iron deficiency anemia.
- Platelet count is right-skewed.
- There is a positive correlation between RBC and Hemoglobin.

# Dependencies

- Python 3.x
- pandas
- matplotlib

Install required packages if not already installed:

```bash
pip install pandas matplotlib
```
