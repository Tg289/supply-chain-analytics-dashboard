<div align="center">

  <!-- PROJECT BANNER HEADER -->
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0e1117,50:1e222d,100:00F5FF&height=220&section=header&text=Supply%20Chain%20%26%20Inventory%20Analytics&fontSize=38&fontColor=ffffff&fontAlignY=40&desc=Interactive%20Business%20Intelligence%20%26%20Logistics%20Optimization%20Dashboard&descAlignY=65&descSize=16" width="100%" alt="Supply Chain Analytics Banner"/>

  <!-- TECH STACK & DEPLOYMENT BADGES -->
  <p align="center">
    <a href="https://streamlit.io/">
      <img src="https://img.shields.io/badge/Streamlit-1.31+-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white" alt="Streamlit">
    </a>
    <a href="https://python.org">
      <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
    </a>
    <a href="https://plotly.com/python/">
      <img src="https://img.shields.io/badge/Plotly-Express-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly">
    </a>
    <a href="https://pandas.pydata.org/">
      <img src="https://img.shields.io/badge/Pandas-Data%20Engineering-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
    </a>
    <a href="https://github.com/Tg289/supply-chain-analytics-dashboard">
      <img src="https://img.shields.io/badge/Deployment-Streamlit%20Cloud-00C853?style=for-the-badge&logo=github&logoColor=white" alt="Deployment Status">
    </a>
  </p>

  <!-- LIVE APPLICATION ACCESS BUTTON -->
  <h3>
    <a href="https://supply-chain-analytics-dashboard-vqegkiegbuq3zciwstgyvq.streamlit.app">
      🚀 Launch Live Production Application
    </a>
  </h3>

  <p><b>Production Application URL:</b> <code>https://supply-chain-analytics-dashboard-vqegkiegbuq3zciwstgyvq.streamlit.app</code></p>

</div>

---

## 📌 Executive Summary

This enterprise-ready **Supply Chain & Inventory Analytics Dashboard** provides real-time business intelligence and decision-support capabilities across 15,000+ transaction records. Designed for supply chain operations managers and executive stakeholders, this application automates inventory health auditing, tracks operational profit margins, measures regional fulfillment efficiency, and benchmarks supplier delivery lead times.

---

## 🔑 Key Features & Business Impact

- **Executive KPI Monitoring**: Track high-level metrics, including Total Revenue, Gross Profit Margin %, Units Sold, and Critical Reorder Alerts.
- **Automated Inventory Health Auditing**: Dynamic categorization engine that tags stock into actionable states (`Healthy`, `Overstock`, `Understock / Reorder Required`, and `Out of Stock`) based on inventory safety buffers.
- **Logistics & Supplier Performance Benchmarking**: Evaluate supplier transit times and identify warehouse bottlenecks using multi-dimensional heatmaps.
- **Interactive Multi-Variable Control Panel**: Real-time filtering across Date Ranges, Product Categories, Regional Warehouses, and Suppliers.
- **Data Governance & Export**: Self-service raw data explorer with automated CSV export capabilities for downstream reporting.

---

## 📐 System Architecture

┌─────────────────────────────────────────────────────────────────────────────┐
│                       SUPPLY CHAIN ANALYTICS PLATFORM                       │
├───────────────────┬───────────────────┬───────────────────┬─────────────────┤
│  📈 Executive     │  📦 Inventory    │  🚚 Logistics &  │  📄 Data        │
│     Overview      │     Health        │     Suppliers     │     Explorer    │
├───────────────────┼───────────────────┼───────────────────┼─────────────────┤
│ • Revenue Trajectory│ • Stock Status    │ • Supplier Lead   │ • Raw Records │
│ • Profit Margin % │ • Safety Margins  │   Time Metrics    │ • CSV Extraction│
│ • Top Products    │ • Threshold Alerts│ • Warehouse Maps  │ • Column Filters│
└───────────────────┴───────────────────┴───────────────────┴─────────────────┘

🛠️ Technology StackDomainTechnology / LibraryDescriptionLanguagePython 3.10+Core Application RuntimeUser InterfaceStreamlitWeb Framework & Interactive ControlsData EngineeringPandas, NumPyData Cleaning, Wrangling, & TransformationData VisualizationPlotly ExpressDynamic Cross-Filtering & VisualsDeploymentStreamlit Community CloudContinuous Cloud Hosting & Integration📦 Local Deployment & Environment SetupTo clone and run this application locally on your machine:Bash# 1. Clone the repository
git clone [https://github.com/Tg289/supply-chain-analytics-dashboard.git](https://github.com/Tg289/supply-chain-analytics-dashboard.git)
cd supply-chain-analytics-dashboard

# 2. Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# 3. Install required dependencies
pip install -r requirements.txt

# 4. Launch the local Streamlit development server
streamlit run app.py
📄 Dataset SpecificationsThe underlying analytical model evaluates transaction logs containing:Financial Metrics: Purchase_Cost, Selling_Price, Calculated Total_Revenue, Total_Profit, Profit_Margin_%Inventory Metrics: Stock_Quantity, Reorder_Level, Units_Sold, Derived Stock_StatusLogistics & Fulfillment: Warehouse_Location, Supplier_Name, Order_Date, Delivery_Date, Actual_Shipping_Days
