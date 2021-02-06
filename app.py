import logging
import yaml

from flask import Flask, request
from weather_info import WeatherInfo

app = Flask(__name__)

with open('config.yaml') as config_file:
    try:
        config = yaml.safe_load(config_file)
    except yaml.YAMLError as exc:
        print(exc)

# Adding basic config values to the logger
logging.basicConfig(
    filename=config['logging']['filename'],
    format=config['logging']['format'],
    level=logging.INFO,
    datefmt=config['logging']['datefmt']
)


@app.route('/weather/city')
def weather_information_by_city():
    city, state = request.args.get('city', 'Los Angeles'), request.args.get('state', 'CA')
    return WeatherInfo().get_weather_information_city(city, state)


if __name__ == '__main__':
    app.run()
