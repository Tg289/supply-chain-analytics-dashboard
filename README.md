# 📦 Supply Chain & Inventory Analytics Dashboard

A production-ready, interactive Data Analysis Dashboard built using Python, Streamlit, and Plotly. Designed to evaluate stock health, supplier performance, shipping lead times, and product profitability over 15,000+ transaction records.

---

## 🌟 Key Features

* **Interactive Control Panel**: Dynamic multi-variable sidebar filtering by Date Range, Product Category, Warehouse Location, and Supplier.
* **Executive Overview**: High-level financial KPIs (Total Revenue, Profit, Units Sold, Margin %) with monthly trendlines and product profitability rankings.
* **Inventory Health Monitoring**: Automated automated stock classification (`Healthy`, `Overstock`, `Understock / Reorder`, and `Out of Stock`) based on real-time reorder thresholds.
* **Logistics & Supplier Performance**: Supplier lead time benchmarks and warehouse shipping efficiency heatmaps.
* **Data Explorer**: In-app data viewer with one-click CSV export capabilities for filtered data.

---

## 🛠️ Tech Stack & Libraries

* **Language**: Python 3.10+
* **Frontend/Dashboard**: [Streamlit](https://streamlit.io/)
* **Data Processing**: [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
* **Data Visualization**: [Plotly Express](https://plotly.com/python/plotly-express/)

---

## 📁 Repository Structure

├── app.py                                       # Main Streamlit Dashboard application code
├── supply_chain_inventory_dataset_15000_rows 2.xlsx  # Dataset Included)
├── requirements.txt                             # Python package dependencies
└── README.md                                    # Project documentation

