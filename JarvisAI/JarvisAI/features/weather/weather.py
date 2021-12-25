import requests


def get_temperature(json_data):
    return json_data['main']['temp']


def get_weather_type(json_data):
    return json_data['weather'][0]['description']


def get_wind_speed(json_data):
    return json_data['wind']['speed']


def get_weather_data(json_data, city):
    description_of_weather = json_data['weather'][0]['description']
    weather_type = get_weather_type(json_data)
    temperature = get_temperature(json_data)
    wind_speed = get_wind_speed(json_data)
    weather_details = ''
    return weather_details + ("The weather in {} is currently {} with a temperature of {} degrees and wind speeds reaching {} km/ph".format(city, weather_type, temperature, wind_speed))


def main_weather(city):
    """
    City to weather
    :param city: City
    :return: weather
    """
    api_address = 'https://api.openweathermap.org/data/2.5/weather?q=Sydney,au&appid=a10fd8a212e47edf8d946f26fb4cdef8&q='
    units_format = "&units=metric"
    final_url = api_address + city + units_format
    json_data = requests.get(final_url).json()
    return get_weather_data(json_data, city)


def weather_app(city):
    return main_weather(city)
