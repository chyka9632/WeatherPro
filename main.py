import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
location = st.text_input("Location: ")
forecast_days = st.slider("Forecast Days: ", min_value=1, max_value=5,
                 help="Select the number of forecast days: ")
weather_parameter = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{weather_parameter} for the next {forecast_days} days in {location}")


d, t = get_data(location, forecast_days, weather_parameter)

figure = px.line(x=d, y=t, labels={"x": "Dates", "y": "Temperatures (C)"})
st.plotly_chart(figure)
