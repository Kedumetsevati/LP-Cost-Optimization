import streamlit as st
import pandas as pd
import numpy as np
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpStatus, PULP_CBC_CMD

@st.cache_data
def load_data():
    W = pd.read_csv("warehouses.csv")
    S = pd.read_csv("stores.csv")
    C = pd.read_csv("costs.csv")
    return W, S, C

def solve_lp(Wdf, Sdf, Cdf):
    W = list(Wdf["warehouse"])
    S = list(Sdf["store"])
    cap = dict(zip(Wdf["warehouse"], Wdf["capacity"]))
    dem = dict(zip(Sdf["store"], Sdf["demand"]))
    cost = {(row["warehouse"], row["store"]): float(row["cost_per_unit"])} | {
        (r["warehouse"], r["store"]): float(r["cost_per_unit"]) for _, r in Cdf.iterrows()
    } if False else {(r["warehouse"], r["store"]): float(r["cost_per_unit"]) for _, r in Cdf.iterrows()}

    model = LpProblem("Retail_MinCost_Distribution", LpMinimize)
    x = {(w, s): LpVariable(f"x_{w}_{s}", lowBound=0) for w in W for s in S}
    model += lpSum(cost[(w, s)] * x[(w, s)] for w in W for s in S)

    for w in W: model += lpSum(x[(w, s)] for s in S) <= cap[w]
    for s in S: model += lpSum(x[(w, s)] for w in W) == dem[s]

    status = model.solve(PULP_CBC_CMD(msg=False))
    status_str = LpStatus[status]
    total_cost = sum(cost[(w, s)] * x[(w, s)].value() for w in W for s in S)
    ship = pd.DataFrame({s: [x[(w, s)].value() for w in W] for s in S}, index=W)
    ship.index.name = "warehouse"
    return status_str, total_cost, ship

st.title("Linear Programming for Cost Optimization")
st.caption("Minimize distribution cost subject to capacity and demand constraints.")

W, S, C = load_data()
c1, c2 = st.columns(2)
cap_mult = c1.slider("Capacity multiplier", 0.5, 1.5, 1.0, 0.05)
dem_mult = c2.slider("Demand multiplier", 0.5, 1.5, 1.0, 0.05)

W_adj = W.copy(); W_adj["capacity"] = (W_adj["capacity"] * cap_mult).round().astype(int)
S_adj = S.copy(); S_adj["demand"]   = (S_adj["demand"] * dem_mult).round().astype(int)

status, total, ship = solve_lp(W_adj, S_adj, C)
st.subheader(f"Status: {status}")
st.subheader(f"Total Cost: ${total:,.2f}")

st.markdown("**Adjusted Warehouses**"); st.dataframe(W_adj)
st.markdown("**Adjusted Stores**"); st.dataframe(S_adj)
st.markdown("**Optimal Shipments (units)**"); st.dataframe(ship)

st.download_button("Download shipments CSV", ship.to_csv().encode("utf-8"),
                   "solution_shipments.csv", "text/csv")
