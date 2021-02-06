from os import environ
from weatherbit.api import Api


class WeatherInfo:
    def __init__(self):
        self.api = Api(environ.get('WEATHER_BIT_API'))

    def get_weather_information_city(self, city, state):
        self.api.set_granularity('daily')
        forecast = self.api.get_forecast(city=city, state=state)
        return forecast.get_series(['temp', 'precip'])
