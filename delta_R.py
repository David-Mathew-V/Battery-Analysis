import pandas as pd

# Read the CSV
df = pd.read_csv("output/delta_V.csv")

# Keep only cycles 50 and 51
df = df[df["cycleID"].isin([50, 51])]

# Pivot so each SampleID has Resistance at cycles 50 and 51
pivot = df.pivot_table(
    index=["SampleID","dev_unit_chl","test_id"],
    columns="cycleID",
    values="Resistance",
    aggfunc="first"
)

# Rename columns for clarity
pivot = pivot.rename(columns={50: "Resistance_50", 51: "Resistance_51"})

# Calculate percent change
pivot["Percent_Change"] = (
    (pivot["Resistance_51"] - pivot["Resistance_50"])
    / pivot["Resistance_50"]
) * 100

# Reset index if desired
result = pivot.reset_index()

# Save to CSV
result.to_csv("output/delta_R.csv", index=False)