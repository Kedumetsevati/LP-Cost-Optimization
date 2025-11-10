# 🧮 Linear Programming for Cost Optimization (Streamlit + PuLP)

An interactive **Streamlit web app** that uses **Linear Programming (PuLP)** to minimize total distribution cost between warehouses and stores.  
This project demonstrates practical optimization and data analysis skills relevant to **operations, logistics, and data science** roles.

---

## 📊 Project Overview
This project models a **Cost Minimization Problem** — determining the optimal shipment plan between multiple warehouses and stores while minimizing total cost.

### Objective Function
\[
\text{Minimize: } Z = \sum_{i,j} C_{ij} \times X_{ij}
\]
where  
- \( C_{ij} \) = unit cost to ship from warehouse *i* to store *j*  
- \( X_{ij} \) = units shipped from warehouse *i* to store *j*

### Constraints
- Each warehouse can supply up to its capacity  
- Each store’s demand must be fully satisfied  
- No negative shipments

---

## ⚙️ Tech Stack
| Tool | Purpose |
|------|----------|
| **Python** | Main programming language |
| **PuLP** | Linear optimization solver |
| **Streamlit** | Interactive web dashboard |
| **Pandas** | Data manipulation |
| **NumPy** | Numerical calculations |

---

## 🧰 Files Included
| File | Description |
|------|--------------|
| `app_lp_cost.py` | Streamlit dashboard |
| `lp_cost_optimization.py` | Core LP optimization logic |
| `warehouses.csv` | Warehouse data (capacity, location) |
| `stores.csv` | Store demand data |
| `costs.csv` | Cost matrix |
| `solution_summary.txt` | Output summary |
| `solution_shipments.csv` | Shipment plan |
| `solution_allocation.png` | Visualization |
| `requirements.txt` | Required Python libraries |

---

## 🧠 How to Run Locally
```bash
# Clone the repository
git clone git@github.com:Kedumetsevati/LP-Cost-Optimization.git
cd LP-Cost-Optimization

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app_lp_cost.py
