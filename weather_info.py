from os import environ
from weatherbit.api import Api


class WeatherInfo:
    def __init__(self):
        self.api = Api(environ.get('WEATHER_BIT_API'))

    def get_weather_information_city(self, city, state, country='US'):
        self.api.set_granularity('daily')
        forecast = self.api.get_forecast(city=city, state=state, country=country)
        forecast_data = forecast.get_series(['temp', 'precip'])
        print(type(forecast_data))
        return forecast_data[0]

