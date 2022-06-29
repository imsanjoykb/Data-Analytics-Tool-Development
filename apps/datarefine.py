import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def app():
    filename = st.text_input('Enter a file path:')
    try:
        df = pd.read_csv(filename)
    except:
        None
    uploaded_files = st.file_uploader("Upload CSV", type="csv", accept_multiple_files=True)
    if uploaded_files:
        for file in uploaded_files:
            file.seek(0)
        uploaded_data_read = [pd.read_csv(file) for file in uploaded_files]
        df = pd.concat(uploaded_data_read)
    hobbies = []
    try:
        st.dataframe(data=df, width=None, height=None)
        hobbies=[]
        for col in df.columns:
            hobbies.append(col)
            print(col)

        options = ["Scatter Plot", "Histogram", "Bar Plot", "Time Series Plot","Box Plot","Heat Map","Correlogram","Violin Plot","Raincloud Plot"]

        st.title("Dropping Column")
        col2= st.multiselect(
            "Blah:", sorted(list(hobbies)), sorted(list(hobbies))
        )
        #st.dataframe(data=df, width=None, height=None)
        if (st.button("Dropping column")):
            st.text("column has been dropped")
            df.drop(col2, inplace=True, axis=1)
            st.dataframe(data=df, width=None, height=None)
        st.title("Delete Duplicate Data")
        hobbies = []
        for col in df.columns:
            hobbies.append(col)
            print(col)
        hobby2 = st.selectbox("X-axis1: ", hobbies)
        if (st.button("Delete Duplicate Data")):
            st.text("Delete Duplicate Data")
            df.drop_duplicates(subset=hobby2,keep="first",inplace=True)
            st.dataframe(data=df, width=None, height=None)
        st.title("Missing Value Treatment")
        if (st.button("check missing Data")):
            st.text("here missing data")
            missing=df.isna()
            st.dataframe(data=missing, width=None, height=None)
        if (st.button("Drop null Data")):
            st.text("refine data")
            missing=df.dropna()
            st.dataframe(data=missing, width=None, height=None)
        st.title("Rename Column")
        rename=st.radio(
            "Blah blah:", hobbies, index=2
        )
        user_input = st.text_input("new name")
        if (st.button("Rename column")):
            st.text("refine data")
            df.rename(columns={rename:user_input},inplace=True)
            st.dataframe(data=df, width=None, height=None)
    except:
        None
