# importing libraries
import pandas as pd
from scipy.stats import f_oneway

# declaring dataframe w/ data
df = pd.DataFrame({
    "salary": [50000, 55000, 60000, 62500, 97500, 100000],
    "dept": ["HR", "HR", "Ops", "Ops", "Engineering", "Engineering"]
})

# creating dataframe filters and lookup
hr = df[df["dept"] == "HR"]["salary"]
ops = df[df["dept"] == "Ops"]["salary"]
engineering = df[df["dept"] == "Engineering"]["salary"]

# calling function f_oneway from library scipy.stats
f_stat, p_value = f_oneway(hr, ops, engineering)

# print results for F-Statistic and P-Value
print("F-Statistic:", f_stat)
print("P-Value:", p_value)
