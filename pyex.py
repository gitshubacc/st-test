import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import base64
import requests
from streamlit_lottie import st_lottie
import plotly.express as px


st.set_page_config(page_title = "Data analysis",
                   page_icon="📊",
                   layout="wide")
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_anime=load_lottie("https://assets6.lottiefiles.com/private_files/lf30_vuwn0sih.json")
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"]{
background-image:url("https://img.freepik.com/free-photo/cool-geometric-triangular-figure-neon-laser-light-great-backgrounds-wallpapers_181624-9331.jpg?w=2000");
background-size: cover;
}
[data-testid="stHeader"]{
   background-color: rgba(0, 0, 0, 0);
}
'''
st.markdown(page_bg_img, unsafe_allow_html=True)
with st.sidebar:
    select = option_menu(
           menu_title="Menu",
           options=["Home", "Scatter Plot", "Line Chart", "Bar Chart"],
           icons=["house", "three-dots", "bar-chart-steps", "bar-chart"]

        )
sdata = pd.read_csv('Instagram_data.csv',encoding='mac_roman')
def interactive_plot(dataframe):
        x_axis = st.selectbox('select x-axis', options=sdata.columns)
        y_axis = st.selectbox('select y-axis', options=sdata.columns)
        chart_data = px.line(dataframe, x=x_axis, y=y_axis)
        st.plotly_chart(chart_data)

if select =="Scatter Plot":
    
    st.title('Scatter plot')
    st.subheader('Relation between impression and various other mediums')
    global numeric_columns

    numeric_columns = list(sdata.select_dtypes(['float','int']).columns)
    

    st.sidebar.subheader("Scatterplot settings")
    x_values = st.sidebar.selectbox('X axis', options = numeric_columns)
    y_values = st.sidebar.selectbox('Y axis', options = numeric_columns)

    plot = px.scatter(data_frame = sdata, x = x_values , y = y_values)
    st.plotly_chart(plot)
if select =="Line Chart":
    st.subheader('Line Chart')
    
    interactive_plot(sdata)
if select =="Bar Chart":
    x =  sdata['Hashtags'].str.split('†')


    newA = sdata.assign(NewHash = x)

    y = x.explode().value_counts()
    st.header('Hashtags')
    z = y.head(20)
    st.write(y)
    st.header("Top 20 Hashtags used in dataset")
    st.bar_chart(z)
    

    

    
if select =="Home":
    st.title("DATA ANALAYSIS OF CSV FILE")
    st.subheader("By Aditya and Ishan")
    with st.container():
        st.write("—--")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("About The Project")
            st.write("""The purpose of this project is to show data analaysis of the given csv file different graphs,charts etc , are used for this purpose to show data analysis of the csv file, we have used streamlit module of python to make this possible and we have incorprated html using st.markdown() function.Using this we have incorprated both html and css into our application our project is located in project tab""")

        with right_column:
            st_lottie(lottie_anime, height=300, key="coding")

