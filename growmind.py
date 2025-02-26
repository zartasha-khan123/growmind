# import streamlit as st
# import pandas as pd
# import os
# from io import BytesIO
# # import plotly.express as px

# # App Title
# st.title("📊 The Best Way to Build Python Apps - Streamlit!")

# # Sidebar
# st.sidebar.header("Navigation")
# st.sidebar.write("Explore the best features of Streamlit")

# # Input Section
# st.header("🚀 What is Streamlit?")
# st.write("Streamlit is a powerful Python library that allows you to build interactive web apps with minimal code.")

# # Data Upload
# st.header("📂 Upload Your Data")
# uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
# if uploaded_file:
#     df = pd.read_csv(uploaded_file)
#     st.write(df.head())

#     # Visualization
#     st.header("📈 Data Visualization")
#     chart_type = st.selectbox("Choose Chart Type", ["Line", "Bar", "Scatter"])
    
#     if chart_type == "Line":
#         fig = px.line(df, x=df.columns[0], y=df.columns[1])
#     elif chart_type == "Bar":
#         fig = px.bar(df, x=df.columns[0], y=df.columns[1])
#     else:
#         fig = px.scatter(df, x=df.columns[0], y=df.columns[1])

#     st.plotly_chart(fig)

# # Footer
# st.markdown("---")
# st.write("🔗 Learn more at [Streamlit Documentation](https://docs.streamlit.io/)")


import streamlit as st
import pandas as pd
import os
from io import BytesIO

# Set up our App
st.set_page_config(page_title="Data Sweeper", layout="wide")
st.title("Data Sweeper")
st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization!")

uploaded_files = st.file_uploader("Upload your files (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file type: {file_ext}")
            continue

        # Display info about the file
        st.write(f"*File Name:* {file.name}")
        st.write(f"*File Size:* {file.size / 1024:.2f} KB")

        # Show 5 rows of our df
        st.write("Preview the head of the dataframe")
        st.dataframe(df.head())

        # Options for data cleaning
        st.subheader("Data Cleaning Options")
        if st.checkbox(f"Clean Data for {file.name}"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"Remove Duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("Duplicates Removed!")

            with col2:
                if st.button(f"Fill Missing Values for {file.name}"):
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("Missing Values have been Filled!")

            # Choose Specific Columns to keep or convert
            st.subheader("Select Columns to Convert")
            columns = st.multiselect(f"Choose Columns for {file.name}", df.columns, default=df.columns)
            df = df[columns]

            # Create some visualization
            st.subheader("Data Visualization")
            if st.checkbox(f"Show Visualization for {file.name}"):
                st.bar_chart(df.select_dtypes(include='number').iloc[:, :2])

        # Convert the file -> CSV to Excel
        st.subheader("Conversion Options")
        conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)
        if st.button(f"Convert {file.name}"):
            buffer = BytesIO()
            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(file_ext, ".csv")
                mime_type = "text/csv"
            elif conversion_type == "Excel":
                df.to_excel(buffer, index=False)
                file_name = file.name.replace(file_ext, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

            buffer.seek(0)

            # Download Button
            st.download_button(
                label=f"Download {file.name} as {conversion_type}",
                data=buffer,
                file_name=file_name,
                mime=mime_type
            )

st.success("All files processed successfully!")
