





import streamlit as st
import pandas as pd
import plotly.express as px

# App Title
st.title("📊 The Best Way to Build Python Apps - Streamlit!")

# Sidebar
st.sidebar.header("Navigation")
st.sidebar.write("Explore the best features of Streamlit")

# Input Section
st.header("🚀 What is Streamlit?")
st.write("Streamlit is a powerful Python library that allows you to build interactive web apps with minimal code.")

# Data Upload
st.header("📂 Upload Your Data")
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())

    # Visualization
    st.header("📈 Data Visualization")
    chart_type = st.selectbox("Choose Chart Type", ["Line", "Bar", "Scatter"])
    
    if chart_type == "Line":
        fig = px.line(df, x=df.columns[0], y=df.columns[1])
    elif chart_type == "Bar":
        fig = px.bar(df, x=df.columns[0], y=df.columns[1])
    else:
        fig = px.scatter(df, x=df.columns[0], y=df.columns[1])

    st.plotly_chart(fig)

# Footer
st.markdown("---")
st.write("🔗 Learn more at [Streamlit Documentation](https://docs.streamlit.io/)")








# import streamlit as st

# st.balloons()
# st.balloons()
# st.markdown(
#     """
#     <style>
#     .stApp {
#         background-color: #FFDDC1; /* Light peach background */
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# st.title("Hello everyone, nice to meet you!")

# for i in range(5):
#     st.balloons()
#     st.balloons()


# slider1 = st.slider("Select first number", 100, 500)
# slider2 = st.slider("Select second number", 100, 500)


# import datetime

# st.date_input("enter your date of birth",datetime.date(1990,1,1))







# st.date_input("Enter your text")
# st.time_input("Enter your text")
# st.camera_input("Enter your text")
# st.number_input("Enter your text")


# st.sidebar.header("user input")

# user_input=st.sidebar.slider('select your number',1 , 100,10)

# st.write('this is title')

# st.title("hello world")
# st.header("this is a header")
# st.markdown("# this is a markdown header")

# st.code("""st.sidebar.header("user input")

# user_input=st.sidebar.slider('select your number',1 , 100,10)

# st.write('this is title')

# st.title("hello world")
# st.header("this is a header")
# st.markdown("# this is a markdown header")""")



