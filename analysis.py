import pandas as pd
import os

path = os.path.join("data", "sample_ipl_players_2025.csv")

df = pd.read_csv(path)

for col in ["Shreyas_Iyer","Priyansh_Arya","Abhishek_Sharma"]:
    df[col] = pd.to_numeric(df[col], errors='coerce')

print("\nTotal Runs:")
print(df[["Shreyas_Iyer","Priyansh_Arya","Abhishek_Sharma"]].sum())

print("\nAverage:")
print(df[["Shreyas_Iyer","Priyansh_Arya","Abhishek_Sharma"]].mean())

print("\nHighest Score:")
print(df[["Shreyas_Iyer","Priyansh_Arya","Abhishek_Sharma"]].max())
