import pandas as pd

# Read the CSV
df = pd.read_csv("output/delta_V.csv")

# Keep only cycles 3 and 51
df = df[df["cycleID"].isin([3, 51])]

# Pivot so each SampleID has Resistance at cycles 50 and 51
pivot = df.pivot_table(
    index=["SampleID","dev_unit_chl","test_id"],
    columns="cycleID",
    values="Resistance",
    aggfunc="first"
)

# Rename columns for clarity
pivot = pivot.rename(columns={3: "Resistance_3", 51: "Resistance_51"})

# Calculate percent change
pivot["Percent_Change"] = (
    (pivot["Resistance_51"] - pivot["Resistance_3"])
    / pivot["Resistance_3"]
) * 100

# Reset index if desired
result = pivot.reset_index()

# Save to CSV
result.to_csv("output/delta_R(3-51).csv", index=False)