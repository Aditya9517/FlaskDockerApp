import logging

from os import environ
from weatherbit.api import Api


class WeatherInfo:
    def __init__(self):
        self.api = Api(environ.get('WEATHER_BIT_API'))

    def get_weather_information_city(self, city, state, country='US'):
        try:
            logging.info("Getting information for {0}, {1}, {2}".format(city, state, country))
            self.api.set_granularity('daily')
            forecast = self.api.get_forecast(city=city, state=state, country=country)
            forecast_data = forecast.get_series(['temp', 'precip'])
            return forecast_data[0]
        except Exception as e:
            logging.error("Error in retrieving data")

