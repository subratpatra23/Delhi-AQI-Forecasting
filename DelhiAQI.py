
import streamlit as st
import pandas as pd 
import plotly.express as px
import pickle

pickle_in = open('C:\\Users\\SUBRAT PATRA\\model.pkl', 'rb') 
classifier = pickle.load(pickle_in)


rawdata = pd.read_excel("D:\\project new\\Delhi.xlsx", header=2)
cleaneddata = pd.read_csv("D:\\project new\\delhi_AQIclean.csv",index_col=0)


st.title("DELHI AQI FORECASTING")
html_temp = """
<div style="background-color:tomato;padding:10px">
<h1 style="color:white;text-align:center;">PM2.5 Value Prediction </h2>
</div>
"""
st.markdown(html_temp,unsafe_allow_html=True)
#st.image("D:\\Study\\Projects\\Delhi AIr Pollution\\Deployment\\Har Har Mahadev.jpg",width = 800)

nav = st.sidebar.radio("Navigation",["None","Raw Data","Cleaned Data","Prediction"])

if nav == "None":
    st.write("Welcome To Delhi AQI Future PM2.5 Value Prediction with Stremlit")

if nav == "Raw Data":
    
    if st.checkbox("Show Raw Data"):
        st.dataframe(rawdata, width = 500 , height = 200 )
    
    graph = st.selectbox("What kind of Graph ? ",["None","Time Series Plot"])

    if graph == "None":
       st.write() 
    
    if graph == "Time Series Plot":
       
        
        fig = px.line(rawdata, x = 'date', y = 'pm25', title = 'PM2.5 Value On Monthly With Slider', width = 800)

        fig.update_xaxes(
            rangeslider_visible = True,
            rangeselector = dict(
                buttons = list([
                    dict(count=1, label= "1m", step="month", stepmode= "backward"),
                    dict(count=2, label= "2m", step="month", stepmode= "backward"),
                    dict(count=3, label= "3m", step="month", stepmode= "backward"),
                    dict(count=4, label= "4m", step="month", stepmode= "backward"),
                    dict(step= "all")
                ])
            )
        )
        st.plotly_chart(fig)
       
    
       
if nav == "Cleaned Data":
    
    if st.checkbox("Show Cleaned Data"):
        st.dataframe(cleaneddata, width = 500 , height = 200 )
    
    graph = st.selectbox("What kind of Graph ? ",["None","Time Series Plot"])

    if graph == "None":
       st.write() 
    
    if graph == "Time Series Plot":
       
        
        fig = px.line(cleaneddata, x = cleaneddata.index , y = 'pm25', title = 'PM2.5 Value On Monthly With Slider', width = 800)

        fig.update_xaxes(
            rangeslider_visible = True,
            rangeselector = dict(
                buttons = list([
                    dict(count=1, label= "1m", step="month", stepmode= "backward"),
                    dict(count=2, label= "2m", step="month", stepmode= "backward"),
                    dict(count=3, label= "3m", step="month", stepmode= "backward"),
                    dict(count=4, label= "4m", step="month", stepmode= "backward"),
                    dict(step= "all")
                ])
            )
        )
        st.plotly_chart(fig)

if nav == "Prediction":
    st.header("Know Predicted PM2.5 Value")
    val = st.number_input('How many hours forecast do you want?', min_value = 1, max_value = 365)
    prediction = classifier.forecast(val)
    if st.button("Predict"):
        #st.success(f"Your predicted PM2.5 value is {round(prediction)}") 
        st.dataframe(round(prediction), width = 500 , height = 200 )
        
     
        
        
        
        
        
        
        