import requests as rs

api_key = "86a8a1b81ac6c8f15753c9704c7d2a04"


def get_data(location, days=None, option=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}"
    response = rs.get(url)
    content_data = response.json()
    return content_data


if __name__ == "__main__":
    print(get_data(location="Tokyo"))
