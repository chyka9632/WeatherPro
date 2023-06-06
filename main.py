import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, tex_input, slider, select_box and sub_header
st.title("Weather Forecast for the Next Days")
location = st.text_input("Location: ")
forecast_days = st.slider("Forecast Days: ", min_value=1, max_value=5,
                          help="Select the number of forecast days: ")
weather_parameter = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{weather_parameter} for the next {forecast_days} days in {location}")

if location:
    # Get the temperature/sky data
    try:
        filtered_data = get_data(location, forecast_days)

        if weather_parameter == "Temperature":
            temperature = [(x["main"]["temp"] - 273.15) for x in filtered_data]  # x is just a variable name
            dates = [z["dt_txt"] for z in filtered_data]

            # Create a temperature plot
            figure = px.line(x=dates, y=temperature, labels={"x": "Dates", "y": "Temperatures (C)"})
            st.plotly_chart(figure)

        if weather_parameter == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [y["weather"][0]["main"] for y in filtered_data]
            image_paths = [images[w] for w in sky_conditions]

            # Render a sky image
            st.image(image_paths, width=110)
    except KeyError:
        st.write("Location does not exist")
