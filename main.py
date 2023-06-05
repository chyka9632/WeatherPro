import streamlit as st
import plotly.express as px


st.title("Weather Forecast for the Next Days")
location = st.text_input("Location: ")
days = st.slider("Forecast Days: ", min_value=1, max_value=5,
                 help="Select the number of forecast days: ")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {location}")


dates = ["2023-05-06", "2023-06-06", "2023-07-06", "2023-08-06", "2023-09-06"]
temps = [14, 17, 13, 15, 19]
temps = [days * i for i in temps]

figure = px.line(x=dates, y=temps, labels={"x": "Dates", "y": "Temperatures (C)"})
st.plotly_chart(figure)