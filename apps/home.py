import streamlit as st
import pandas as pd
import numpy as np

def app():
    st.title("Datapen")
    st.write("A no code data visualization and data cleaning platform")
    st.image("https://dimensionless.in/wp-content/uploads/2018/11/cover_updated.jpg", width=400)
    st.title("Plot")
    st.write("scatter plot")
    st.write("group histogram plot")
    st.write("bar plot")
    st.write("heatmap plot")
    st.write("violine plot")
    st.write("box plot")
    st.write("raincloud plot")
    st.title("Data cleaning")
    st.write("drop column")
    st.write("Delete Duplicate Data")
    st.write("Missing Value Treatment")
    st.write("Drop null Data")
    st.write("Rename column")



