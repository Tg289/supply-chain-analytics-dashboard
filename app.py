import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import os

# Page Configuration
st.set_page_config(
    page_title="Supply Chain & Inventory Analytics Dashboard",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Dark UI Enhancement
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric {
        background: linear-gradient(135deg, #1e222d 0%, #2a2e3d 100%);
        border: 1px solid #363c4e;
        padding: 18px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }
    .stMetric label { color: #a0a5b5 !important; font-weight: 600; }
    .stMetric div { color: #ffffff !important; font-weight: 700; }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data(source):
    df = pd.read_excel(source)
    df = df.drop_duplicates()
    
    # Dates
    df['Order_Date'] = pd.to_datetime(df['Order_Date'])
    df['Delivery_Date'] = pd.to_datetime(df['Delivery_Date'])
    df['Actual_Shipping_Days'] = (df['Delivery_Date'] - df['Order_Date']).dt.days.clip(lower=0)
    
    # Numeric Columns Validation
    num_cols = ['Stock_Quantity', 'Reorder_Level', 'Units_Sold', 'Purchase_Cost', 'Selling_Price']
    for c in num_cols:
        df[c] = pd.to_numeric(df[c], errors='coerce').fillna(0)
    
    # Key Financial Metrics
    df['Total_Revenue'] = df['Units_Sold'] * df['Selling_Price']
    df['Total_Cost'] = df['Units_Sold'] * df['Purchase_Cost']
    df['Total_Profit'] = df['Total_Revenue'] - df['Total_Cost']
    df['Profit_Margin_%'] = np.where(df['Total_Revenue'] > 0, (df['Total_Profit'] / df['Total_Revenue']) * 100, 0)
    
    # Stock Status Classification
    def categorize_stock(row):
        if row['Stock_Quantity'] == 0:
            return 'Out of Stock'
        elif row['Stock_Quantity'] <= row['Reorder_Level']:
            return 'Understock / Reorder'
        elif row['Stock_Quantity'] > (row['Reorder_Level'] * 2.5):
            return 'Overstock'
        return 'Healthy'

    df['Stock_Status'] = df.apply(categorize_stock, axis=1)
    return df

# Data Load Handler
default_file = "supply_chain_inventory_dataset_15000_rows 2.xlsx"

st.sidebar.title("🎯 Control Panel")
st.sidebar.markdown("---")

if os.path.exists(default_file):
    df_raw = load_data(default_file)
else:
    uploaded = st.sidebar.file_uploader("Upload Excel Dataset", type=["xlsx", "xls"])
    if uploaded:
        df_raw = load_data(uploaded)
    else:
        st.error("Dataset missing! Please upload the Excel dataset file in the sidebar to proceed.")
        st.stop()

# Dynamic Filters
min_d = df_raw['Order_Date'].min().date()
max_d = df_raw['Order_Date'].max().date()
dates = st.sidebar.date_input("Order Date Range", value=(min_d, max_d), min_value=min_d, max_value=max_d)

cats = st.sidebar.multiselect("Category Filter", sorted(df_raw['Category'].unique()), default=df_raw['Category'].unique())
warehouses = st.sidebar.multiselect("Warehouse Filter", sorted(df_raw['Warehouse_Location'].unique()), default=df_raw['Warehouse_Location'].unique())
suppliers = st.sidebar.multiselect("Supplier Filter", sorted(df_raw['Supplier_Name'].unique()), default=df_raw['Supplier_Name'].unique())

if len(dates) == 2:
    s_date, e_date = dates
    df = df_raw[
        (df_raw['Order_Date'].dt.date >= s_date) & 
        (df_raw['Order_Date'].dt.date <= e_date) & 
        (df_raw['Category'].isin(cats)) & 
        (df_raw['Warehouse_Location'].isin(warehouses)) &
        (df_raw['Supplier_Name'].isin(suppliers))
    ]
else:
    df = df_raw.copy()

# Header & High-Level KPIs
st.title("📊 Supply Chain & Inventory Analytics Dashboard")
st.markdown("Real-time Operational Performance, Stock Health, and Supplier Analytics Dashboard.")

kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)
kpi1.metric("Total Revenue", f"${df['Total_Revenue'].sum():,.0f}")
kpi2.metric("Total Profit", f"${df['Total_Profit'].sum():,.0f}")
kpi3.metric("Units Sold", f"{df['Units_Sold'].sum():,.0f}")
kpi4.metric("Avg Profit Margin", f"{df['Profit_Margin_%'].mean():.1f}%")
reorder_count = (df['Stock_Status'] == 'Understock / Reorder').sum()
kpi5.metric("Reorder Alerts", f"{reorder_count:,}", delta_color="inverse")

st.markdown("---")

# Dashboard Navigation Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📈 Executive Overview", 
    "📦 Inventory & Stock Health", 
    "🚚 Logistics & Supplier Performance", 
    "📄 Data Explorer"
])

# Tab 1: Executive Overview
with tab1:
    col_a, col_b = st.columns(2)
    
    with col_a:
        monthly = df.set_index('Order_Date').resample('ME')[['Total_Revenue', 'Total_Profit']].sum().reset_index()
        fig_line = px.line(
            monthly, x='Order_Date', y=['Total_Revenue', 'Total_Profit'],
            labels={'value': 'USD ($)', 'variable': 'Metric', 'Order_Date': 'Timeline'},
            title="Monthly Revenue & Profit Trajectory",
            color_discrete_map={'Total_Revenue': '#00F5FF', 'Total_Profit': '#FF007F'},
            markers=True,
            template="plotly_dark"
        )
        fig_line.update_traces(line=dict(width=3), marker=dict(size=8))
        st.plotly_chart(fig_line, use_container_width=True)

    with col_b:
        cat_rev = df.groupby('Category')['Total_Revenue'].sum().reset_index()
        fig_bar = px.bar(
            cat_rev, x='Category', y='Total_Revenue', color='Category',
            title="Revenue Distribution Across Categories",
            color_discrete_sequence=px.colors.qualitative.Vivid,
            template="plotly_dark"
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    top_p = df.groupby('Product_Name')['Total_Profit'].sum().nlargest(10).reset_index()
    fig_top = px.bar(
        top_p, x='Total_Profit', y='Product_Name', orientation='h',
        color='Total_Profit', color_continuous_scale='Viridis',
        title="Top 10 Most Profitable Products", template="plotly_dark"
    )
    fig_top.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig_top, use_container_width=True)

# Tab 2: Inventory Health
with tab2:
    c1, c2 = st.columns(2)
    with c1:
        st_status = df['Stock_Status'].value_counts().reset_index()
        st_status.columns = ['Status', 'Count']
        fig_pie = px.pie(
            st_status, names='Status', values='Count', hole=0.4,
            title="Inventory Health Status Breakdown",
            color='Status',
            color_discrete_map={
                'Healthy': '#00E676',
                'Overstock': '#FFB300',
                'Understock / Reorder': '#FF1744',
                'Out of Stock': '#D500F9'
            },
            template="plotly_dark"
        )
        st.plotly_chart(fig_pie, use_container_width=True)
        
    with c2:
        fig_scatter = px.scatter(
            df, x='Reorder_Level', y='Stock_Quantity', color='Stock_Status',
            title="Stock Quantity vs Reorder Thresholds",
            opacity=0.8, template="plotly_dark"
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

# Tab 3: Logistics & Supplier Performance
with tab3:
    col_x, col_y = st.columns(2)
    with col_x:
        sup_time = df.groupby('Supplier_Name')['Actual_Shipping_Days'].mean().reset_index()
        fig_sup = px.bar(
            sup_time, x='Supplier_Name', y='Actual_Shipping_Days', color='Actual_Shipping_Days',
            color_continuous_scale='Turbo', title="Average Shipping Lead Time (Days) by Supplier",
            template="plotly_dark"
        )
        st.plotly_chart(fig_sup, use_container_width=True)
        
    with col_y:
        wh_hm = df.groupby(['Warehouse_Location', 'Category'])['Actual_Shipping_Days'].mean().reset_index()
        fig_hm = px.density_heatmap(
            wh_hm, x='Warehouse_Location', y='Category', z='Actual_Shipping_Days',
            title="Shipping Lead Time Heatmap (Warehouse vs Category)",
            color_continuous_scale='Plasma', template="plotly_dark"
        )
        st.plotly_chart(fig_hm, use_container_width=True)

# Tab 4: Data Explorer
with tab4:
    st.subheader("Filtered Dataset View")
    st.dataframe(df, use_container_width=True)
    
    csv_data = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Filtered Data CSV",
        data=csv_data,
        file_name="filtered_supply_chain_data.csv",
        mime="text/csv"
    )
