from flask import Flask, request

from weather_info import WeatherInfo

app = Flask(__name__)


@app.route('/weather/city')
def weather_information_by_city():
    city, state = request.args.get('city', 'Los Angeles'), request.args.get('state', 'CA')
    return WeatherInfo().get_weather_information_city(city, state)


if __name__ == '__main__':
    app.run()
