from flask import Flask, render_template, request
from weather_info import WeatherInfo

app = Flask(__name__)


@app.route('/weather/city')
def weather_information_by_city():
    city, state = request.args.get('city', 'Los Angeles'), request.args.get('state', 'CA')
    return WeatherInfo().weather_information_city(city, states)


if __name__ == '__main__':
    app.run()
