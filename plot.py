import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("output/delta_R(3-51).csv")

bins = np.arange(60, 120, 5) 

plt.figure(figsize=(10, 6))

plt.hist(df["Percent_Change"], bins=bins, edgecolor="black")

plt.xlabel("Percentage Change (%)")
plt.ylabel("Number of Cells")
plt.title("Distribution of Percentage Change (Cycle 3 → 51)")

plt.grid(axis="y")
plt.tight_layout()
plt.show()

# fig, ax = plt.subplots(2, 1, figsize=(8, 8))

# # First plot: Delta V
# ax[0].plot(
#     df["cycleID"],
#     df["delta_V"]
# )

# ax[0].set_xlabel("Cycle no")
# ax[0].set_ylabel("Delta V (V)")
# ax[0].set_title("Voltage Drop - ANUF130626A12")
# ax[0].grid(True)


# # Second plot: Resistance
# ax[1].plot(
#     df["cycleID"],
#     df["Resistance"]
# )

# ax[1].set_xlabel("Cycle no")
# ax[1].set_ylabel("Resistance (Ohms)")
# ax[1].set_title("Resistance - ANUF130626A12")
# ax[1].grid(True)


# plt.tight_layout()
# plt.show()