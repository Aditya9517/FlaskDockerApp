import logging
import yaml

from flask import Flask, request
from weather_info import WeatherInfo

app = Flask(__name__)

with open('/Users/rohitravishankar/PyCharmProjects/FlaskDockerApp/config.yaml', 'r') as config_file:
    try:
        config = yaml.safe_load(config_file)
    except yaml.YAMLError as exc:
        print(exc)

# Adding basic config values to the logger
# logging.basicConfig(
#     filename=config['logging']['filename'],
#     format=config['logging']['format'],
#     level=logging.INFO,
#     datefmt=config['logging']['datefmt']
# )


@app.route('/weather/<string:city>/<string:state>', methods=['GET'])
def weather_information_by_city(city, state):
    return WeatherInfo().get_weather_information_city(city, state)


if __name__ == '__main__':
    app.run()
