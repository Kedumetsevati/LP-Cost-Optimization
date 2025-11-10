import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpStatus, PULP_CBC_CMD

# ---------- Load data ----------
warehouses = pd.read_csv("warehouses.csv")   # columns: warehouse, capacity
stores     = pd.read_csv("stores.csv")       # columns: store, demand
costs      = pd.read_csv("costs.csv")        # columns: warehouse, store, cost_per_unit

W = list(warehouses["warehouse"])
S = list(stores["store"])

cap = dict(zip(warehouses["warehouse"], warehouses["capacity"]))
dem = dict(zip(stores["store"], stores["demand"]))

# cost dictionary (w,s) -> c
cost = {(row["warehouse"], row["store"]): float(row["cost_per_unit"]) for _, row in costs.iterrows()}

# ---------- Build LP ----------
model = LpProblem("Retail_MinCost_Distribution", LpMinimize)

# decision variables x[w,s] >= 0 (units shipped from w to s)
x = {(w, s): LpVariable(f"x_{w}_{s}", lowBound=0) for w in W for s in S}

# objective: minimize sum(cost * x)
model += lpSum(cost[(w, s)] * x[(w, s)] for w in W for s in S)

# supply constraints: shipments out of each warehouse <= capacity
for w in W:
    model += lpSum(x[(w, s)] for s in S) <= cap[w], f"supply_{w}"

# demand constraints: shipments into each store == demand
for s in S:
    model += lpSum(x[(w, s)] for w in W) == dem[s], f"demand_{s}"

# ---------- Solve ----------
status = model.solve(PULP_CBC_CMD(msg=False))
status_str = LpStatus[status]
total_cost = sum(cost[(w, s)] * x[(w, s)].value() for w in W for s in S)

print(f"Status: {status_str}")
print(f"Total Cost: {total_cost:,.2f}")

# ---------- Outputs ----------
# shipments table
ship_df = pd.DataFrame({s: [x[(w, s)].value() for w in W] for s in S}, index=W)
ship_df.index.name = "warehouse"
ship_df.to_csv("solution_shipments.csv")

# summary text
with open("solution_summary.txt", "w") as f:
    f.write(f"Status: {status_str}\n")
    f.write(f"Total Cost: {total_cost:,.2f}\n\n")
    f.write("Total shipped per warehouse:\n")
    for w in W:
        f.write(f"  {w}: {ship_df.loc[w].sum():.0f}\n")
    f.write("\nTotal received per store:\n")
    for s in S:
        f.write(f"  {s}: {ship_df[s].sum():.0f}\n")

# heatmap visualization of allocation
fig, ax = plt.subplots(figsize=(6, 4.5))
im = ax.imshow(ship_df.values, aspect="auto")
ax.set_xticks(np.arange(len(S))); ax.set_xticklabels(S)
ax.set_yticks(np.arange(len(W))); ax.set_yticklabels(W)
for i in range(len(W)):
    for j in range(len(S)):
        ax.text(j, i, f"{ship_df.values[i, j]:.0f}", ha="center", va="center")
ax.set_title("Optimal Shipments (units)")
ax.set_xlabel("Stores"); ax.set_ylabel("Warehouses")
plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
plt.tight_layout()
plt.savefig("solution_allocation.png", dpi=200)
print("Wrote: solution_shipments.csv, solution_summary.txt, solution_allocation.png")
