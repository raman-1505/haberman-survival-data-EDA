                      #Count records in each survival-status category.
import numpy as np
import pandas as pd

df = pd.read_csv("/content/Patient.csv")
df.columns = ["age", "operation_year", "positive_axillary_nodes", "survival_status"]

#1. Count records in each survival-status category
df["survival_status"].value_counts().sort_index()

#2. Age
ages = df["age"].to_numpy()

print("Average:", np.mean(ages))
print("Median:", np.median(ages))
print("Minimum:", np.min(ages))
print("Maximum:", np.max(ages))

#3. Average positive axillary nodes
nodes = df["positive_axillary_nodes"].to_numpy()
np.mean(nodes)

#4. Compare average age and node counts by recorded status group
df.groupby("survival_status")[["age", "positive_axillary_nodes"]].mean()

#5. Operation year with the most records
year_counts = df["operation_year"].value_counts().sort_values(ascending=False)
print(year_counts)

#6. Missing values and duplicates
print(df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())

import matplotlib.pyplot as plt

# Chart 1: Count of each survival-status category
status_counts = df["survival_status"].value_counts().sort_index()

plt.bar(status_counts.index, status_counts.values, color=["skyblue", "orange"])
plt.title("Survival Status Category Count")
plt.xlabel("Survival Status")
plt.ylabel("Number of Records")
plt.xticks([1, 2])
plt.show()

# Chart 2: Average positive axillary nodes by survival-status category
avg_nodes = df.groupby("survival_status")["positive_axillary_nodes"].mean()

plt.bar(avg_nodes.index, avg_nodes.values, color=["green", "red"])
plt.title("Average Positive Axillary Nodes by Survival Status")
plt.xlabel("Survival Status")
plt.ylabel("Average Positive Axillary Nodes")
plt.xticks([1, 2])
plt.show()