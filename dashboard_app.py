import streamlit as st
import pandas as pd
import plotly.express as px

# Page title
st.title("Requirement Fulfillment Dashboard")

# File uploader
#st.sidebar.header("Upload Excel File")
uploaded_file =True# st.sidebar.file_uploader("Upload your Excel file", type=["xlsx", "xls"])
print ("hi...")
tab1, tab2 ,tab3= st.tabs(["Requirements", "Panelists","Skills Required"])
    # Display data preview
# st.subheader("Uploaded Data Preview")
# st.dataframe(df.head())

with tab1:
    # Load data\
    df = pd.read_excel("gcc_analysis.xlsx")
    df.rename({i: i.strip() for i in df.columns },inplace=True)
    print (df.columns)
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            # Convert column to numeric, coerce invalid values (like '\xa0') to NaN, then fill NaN with 0
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)
        else:
            # Replace '\xa0' with empty string for non-numeric columns
            df[col] = df[col].replace("\xa0", "").fillna("")
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(0)
        else:
            df[col] = df[col].fillna("")

    # Sidebar filters
    st.sidebar.header("Filters")
    account_filter = st.sidebar.selectbox("Select Account", options=["All"] + list(df["Account"].unique()))
    priority_filter = st.sidebar.selectbox("Select Priority", options=["All"] + list(df["Priority"].unique()))
    status_filter = st.sidebar.selectbox("Select Status", options=["All"] + list(df["Status"].unique()))
    # Apply filters
    filtered_df = df.copy()
    if account_filter != "All":
        filtered_df = filtered_df[filtered_df["Account"] == account_filter]
    if priority_filter != "All":
        filtered_df = filtered_df[filtered_df["Priority"] == priority_filter]
    if status_filter != "All":
        filtered_df = filtered_df[filtered_df["Status"] == status_filter]

    # Key metrics
    print (filtered_df)
    st.subheader("Key Metrics")

    total_positions = filtered_df["No of Positions"].sum()
    fulfilled_positions = filtered_df["Fulfilled"].sum()
    net_open_positions = filtered_df["Net Open Positions"].sum()
    conversion_rate = (fulfilled_positions / total_positions) * 100 if total_positions > 0 else 0
    
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Positions", total_positions)

    with col2:
        st.metric("Fulfilled Positions", fulfilled_positions)

    with col3:
        st.metric("Net Open Positions", net_open_positions)

    with col4:
        st.metric("Conversion Rate (%)", f"{conversion_rate:.2f}")


    
with tab2:
    df = pd.read_excel("panel.xlsx")
    st.subheader("Data Preview")
    st.dataframe(df.head())

    # st.sidebar.header("Filters")
    # account_filter = st.sidebar.selectbox("Select Skill Account", options=["All"] + list(df["Account"].unique()))
    # priority_filter = st.sidebar.selectbox("Select Skill Priority", options=["All"] + list(df["Priority"].unique()))
    # status_filter = st.sidebar.selectbox("Select Skill Status", options=["All"] + list(df["Status"].unique()))
    # # Apply filters
    # filtered_df = df.copy()
    # if account_filter != "All":
    #     filtered_df = filtered_df[filtered_df["Account"] == account_filter]
    # if priority_filter != "All":
    #     filtered_df = filtered_df[filtered_df["Priority"] == priority_filter]
    # if status_filter != "All":
    #     filtered_df = filtered_df[filtered_df["Status"] == status_filter]

    # # Key metrics
    # print (filtered_df)
    # st.subheader("Key Metrics")

    # total_positions = filtered_df["No of Positions"].sum()
    # fulfilled_positions = filtered_df["Fulfilled"].sum()
    # net_open_positions = filtered_df["Net Open Positions"].sum()
    # conversion_rate = (fulfilled_positions / total_positions) * 100 if total_positions > 0 else 0
    
    # col1, col2, col3, col4 = st.columns(4)

    # with col1:
    #     st.metric("Total Positions", total_positions)

    # with col2:
    #     st.metric("Fulfilled Positions", fulfilled_positions)

    # with col3:
    #     st.metric("Net Open Positions", net_open_positions)

    # with col4:
    #     st.metric("Conversion Rate (%)", f"{conversion_rate:.2f}")
with tab3:
    df = pd.read_excel("skills_required.xlsx")
    st.subheader("Data Preview")
    st.dataframe(df.head())

