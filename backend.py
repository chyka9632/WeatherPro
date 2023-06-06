import requests as rs

api_key = "86a8a1b81ac6c8f15753c9704c7d2a04"


def get_data(location, forecast_days=None, weather_parameter=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}"
    response = rs.get(url)
    content_data = response.json()
    filtered_data = content_data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    if weather_parameter == "Temperature":
        filtered_data = [x["main"]["temp"] for x in filtered_data]  # x is just a variable name
    if weather_parameter == "Sky":
        filtered_data = [y["weather"][0]["main"] for y in filtered_data]

    return filtered_data


if __name__ == "__main__":
    print(get_data(location="Tokyo", forecast_days=2, weather_parameter="Temperature"))
