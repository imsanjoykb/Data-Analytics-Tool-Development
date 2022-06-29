import streamlit as st
from multiapp import MultiApp
from apps import home,graphs,datarefine # import your app modules here

app = MultiApp()
def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

# Add all your application here
app.add_app("Home", home.app)
local_css("file.css")

t = "<div><span class='highlight blue'>Analysis your data at Amader Hospital Research Lab<span class='bold'></span></span></div>"

st.markdown(t, unsafe_allow_html=True)

#app.add_app("Data Stats", data_stats.app)
app.add_app("plot",graphs.app)
app.add_app("Data cleaning",datarefine.app)

# The main app
app.run()
