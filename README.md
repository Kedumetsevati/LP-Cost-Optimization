# 💰 LP Cost Optimization
### Linear Programming Model to Minimize Total Supply Chain Cost

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![PuLP](https://img.shields.io/badge/PuLP-003366?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-217346?logo=microsoft-excel&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?logo=powerbi&logoColor=black)
![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white)

---

## 📘 Project Overview
This project develops a **Linear Programming (LP)** optimization model that identifies the lowest-cost strategy for transporting goods from warehouses to Costco business centres.  
The model automatically allocates shipping quantities to minimize transportation and storage cost while meeting all demand and capacity constraints.

---

## 🎯 Objectives
- 📦 Minimize total logistics cost (transport + storage + penalty)  
- 🏬 Ensure each Costco branch’s demand is fully satisfied  
- 🚚 Respect capacity and production constraints  
- 📊 Visualize the results in Power BI / Streamlit dashboards

---

## 🧰 Tools & Technologies
| Category | Tools |
|-----------|-------|
| Language | **Python** (Pandas, NumPy) |
| Optimization | **PuLP** (Linear Programming Solver) |
| Visualization | **Streamlit**, **Power BI**, **Excel** |
| Environment | Jupyter Notebook • VS Code • Anaconda • GitHub |

---

## 📂 Project Structure
```
LP-Cost-Optimization/
│
├── data/                <- sample cost, demand, and capacity CSVs
├── notebooks/           <- Jupyter notebooks with LP formulation
├── app_lp_cost.py       <- Streamlit dashboard app
├── images/              <- charts & dashboard screenshots
└── README.md
```

---

## 📈 Methodology
1. **Data Input**  
   Collected synthetic logistics data: unit costs, capacities, demands.  

2. **Model Formulation**  
   Defined decision variables `x[i,j]` = units shipped from warehouse *i* to centre *j*  
   Objective:  
   \[
   \min \sum c_{ij}x_{ij}
   \]
   subject to demand and capacity constraints.  

3. **Optimization**  
   Solved using the `PuLP` solver (`LpMinimize`).  

4. **Visualization**  
   Created a **Streamlit app** and **Power BI dashboard** showing optimal routes, costs, and sensitivity results.

---

## 🧩 Key Results & Insights
- 💡 Total logistics cost reduced by **14.7 %** vs baseline allocation.  
- 🚛 Optimal plan favored two central warehouses → lower distance + capacity balance.  
- 📊 Sensitivity analysis showed minor cost increase (< 2 %) under ± 10 % demand fluctuation.

```
![Dashboard Preview](images/dashboard.png)
![Model Output](images/model_chart.png)
```

---

## 🚀 How to Run the Project
1. Clone this repo:
   ```bash
   git clone https://github.com/Kedumetsevati/LP-Cost-Optimization.git
   cd LP-Cost-Optimization
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit dashboard:
   ```bash
   streamlit run app_lp_cost.py
   ```

---

## 🧮 Skills Demonstrated
**Linear Programming | Optimization Modeling | Data Analytics | Visualization | Python Automation | Business Operations Analysis**

---

## 📄 Future Improvements
- [ ] Add multi-period demand scenario analysis  
- [ ] Integrate AWS S3 data loading pipeline  
- [ ] Deploy Streamlit app online for interactive demo  

---

## 👨‍💻 Author
**Kedumetse Nadour Vati, PhD**  
📍 Edmonton / St Albert — Alberta, Canada  
📧 [drkedumvati@gmail.com](mailto:drkedumvati@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/kedumetsevati1991/) | [GitHub](https://github.com/Kedumetsevati)
