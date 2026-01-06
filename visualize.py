import pandas as pd
import matplotlib.pyplot as plt
import os

# Path to CSV file
path = os.path.join("data", "sample_ipl_players_2025.csv")
df = pd.read_csv(path)

# Columns to plot
players = ["Shreyas_Iyer", "Priyansh_Arya", "Abhishek_Sharma"]

# Ensure output folders exist
os.makedirs("output/graphs", exist_ok=True)


# =======================
# 1) MATCH-WISE LINE PLOT
# =======================

plt.figure(figsize=(10, 5))

for p in players:
    plt.plot(df["Match"], df[p], marker='o', label=p.replace("_", " "))

plt.xlabel("Match")
plt.ylabel("Runs")
plt.title("Match-wise Runs")
plt.grid()
plt.legend()

# Save AND Show
plt.savefig("output/graphs/matchwise_runs.png")
plt.show()    # <-- THIS OPENS THE IMAGE AUTOMATICALLY
plt.close()


# =======================
# 2) TOTAL RUNS BAR CHART
# =======================

totals = df[players].sum()

plt.figure(figsize=(7, 5))
plt.bar(["Shreyas", "Priyansh", "Abhishek"], totals)

plt.ylabel("Runs")
plt.title("Total Runs")

# Save AND Show
plt.savefig("output/graphs/total_runs.png")
plt.show()    # <-- THIS OPENS THE IMAGE AUTOMATICALLY
plt.close()

