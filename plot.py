import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("output/delta_R.csv")

plt.figure(figsize=(10, 6))

plt.scatter(df.index, df["Percent_Change"], s=20)

plt.xlabel("Row Index")
plt.ylabel("Percentage Change (%)")
plt.title("Percentage Change Between Cycle 50 and 51")

plt.grid(True)
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