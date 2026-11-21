# haberman-survival-data-EDA

## Project Overview

This project performs basic Exploratory Data Analysis (EDA) on the Haberman Survival dataset using Python, NumPy, Pandas, and Matplotlib.

The analysis explores:

- Age at operation
- Year of operation
- Number of positive axillary nodes
- Recorded survival-status category

This project is descriptive only. It does not use machine learning or make medical predictions.

## Dataset

- File: `Patient.csv`
- Records: 306
- Columns: 4

| Column | Description |
|---|---|
| age | Age of patient at operation |
| operation_year | Year of operation |
| positive_axillary_node | Number of positive axillary nodes |
| survival_status | Recorded survival-status category |

## Tasks Performed

- Loaded the dataset using Pandas
- Displayed `head()`, `tail()`, `shape`, `info()`, and `describe()`
- Checked missing values and duplicate rows
- Used NumPy arrays for statistical calculations
- Used Pandas filtering, sorting, `value_counts()`, and `groupby()`
- Created two charts
- Wrote descriptive observations

## Key Results

- Status category 1 has 225 records.
- Status category 2 has 81 records.
- Average age is 52.46 years.
- Median age is 52 years.
- Minimum age is 30 years and maximum age is 83 years.
- Average positive axillary nodes is 4.03.
- Operation year 1958 has the most records, with 36 records.
- The dataset has no missing values.
- The dataset contains 17 duplicate rows.

## Charts

1. Survival-status category count
2. Average positive axillary nodes by survival-status category

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib

## How to Run

1. Clone this repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK

2. Install required libraries
pip install pandas numpy matplotlib

3. Run the python file
python haberman_survival_eda.py

```
## Observations

1. Survival status category 1 contains more records than category 2.
2. Status category 2 has a higher average positive-node count than status category 1.
3. The dataset is complete with no missing values, but it has 17 duplicate rows.


Author
Raman
