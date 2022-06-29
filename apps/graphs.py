import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import ptitprince as pt
def scatter_plot(df,fig):
    hobbies = []

    for col in df.columns:
        hobbies.append(col)
        print(col)
    st.title(" Scatter Plot")
    hobby = st.selectbox("X-axis: ", hobbies)
    # print the selected hobby
    st.write("You have selected X-axis: ", hobby)
    hobby1 = st.selectbox("Y-axis: ", hobbies)
    st.write("You have selected Y-axis: ", hobby1)
    if (st.button("scatter plot")):
        st.text("scatter plot")
        ax = sns.regplot(x=hobby, y=hobby1, data=df)
        st.pyplot(fig)
def group_histogram(df,fig):
    st.title("Grouped Histogram")

    if (st.button("Grouped Histogram")):
        st.text("Grouped Histogram")
        for condition in df.TrialType.unique():
            cond_data = df[(df.TrialType == condition)]
            ax = sns.distplot(cond_data.RT, kde=False)
        ax.set(xlabel='Response Time', ylabel='Frequency')
        st.pyplot(fig)
def bar_plot(df,fig,hobbies):
    st.title("Bar Plot")
    hobby = st.selectbox("X-axis for barplot: ", hobbies)
    # print the selected hobby
    st.write("You have selected X-axis: ", hobby)
    hobby1 = st.selectbox("Y-axis for barplot: ", hobbies)
    st.write("You have selected Y-axis: ", hobby1)
    if (st.button("Bar plot")):
        st.text("Bar plot")
        sns.barplot(x=hobby, y=hobby1, data=df)
        st.pyplot(fig)
def box_plot1(df,fig,hobbies):
    st.title("Box Plot")
    hobby = st.selectbox("X-axis for boxplot: ", hobbies)
    # print the selected hobby
    st.write("You have selected X-axis: ", hobby)
    hobby1 = st.selectbox("Y-axis for boxplot: ", hobbies)
    st.write("You have selected Y-axis: ", hobby1)
    if (st.button("Box plot")):
        st.text("Box plot")
        sns.boxplot(x=hobby, y=hobby,data=df)
        st.pyplot(fig)
def heat_map(df,fig,hobbies):
    st.title("Heatmap Plot")
    col2 = st.multiselect(
        "Blah:", sorted(list(hobbies)), sorted(list(hobbies))
    )
    if (st.button("Heatmap plot")):
        st.text("Heatmap plot")
        ax = sns.heatmap(df[col2])
        st.pyplot(fig)
def violine_plot(df,fig,hobbies):
    st.title("Violin Plot")
    hobby = st.selectbox("X-axis for Violinplot: ", hobbies)
    # print the selected hobby
    st.write("X-axis for Violinplot: ", hobby)
    hobby1 = st.selectbox("Y-axis for Violinplot: ", hobbies)
    st.write("You have selected Y-axis: ", hobby1)
    if (st.button("Violin plot")):
        st.text("Violin plot")
        sns.violinplot(x=hobby, y=hobby1, data=df)
        st.pyplot(fig)
def rain_cloudplot(df,fig,hobbies):
    st.title("Raincloud Plot")
    hobby = st.selectbox("X-axis for Raincloudplot: ", hobbies)
    # print the selected hobby
    st.write("You have selected X-axis: ", hobby)
    hobby1 = st.selectbox("Y-axis for Raincloudplot: ", hobbies)
    st.write("You have selected Y-axis: ", hobby1)
    if (st.button("Raincloud plot")):
        st.text("Raincloud plot")
        ax = pt.RainCloud(x=hobby, y=hobby1,
                          data=df,
                          width_viol=.8,
                          width_box=.4,
                          figsize=(12, 8), orient='h',
                          move=.0)
        st.pyplot(fig)
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
    hobbies=[]
    try:
        fig = plt.figure(figsize=(12, 8))
        for col in df.columns:
            hobbies.append(col)
            print(col)

        fig = plt.figure(figsize=(12, 8))
        st.dataframe(data=df, width=None, height=None)

        scatter_plot(df,fig)
        group_histogram(df, fig)
        bar_plot(df, fig, hobbies)
        heat_map(df, fig, hobbies)
        violine_plot(df, fig, hobbies)
        box_plot1(df, fig, hobbies)
        rain_cloudplot(df, fig, hobbies)
    except:
        None
