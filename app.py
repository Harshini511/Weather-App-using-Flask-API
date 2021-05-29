import requests
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET', 'POST'])
def index():
    new_city='California'
    if request.method == 'POST':
        new_city = request.form.get('city')
    url='https://api.openweathermap.org/data/2.5/weather?q={}&appid=5fc587b126d3fc559f1fc39fbc758e41'
    r = requests.get(url.format(new_city)).json()
    weather = {
        'city' : new_city,
        'temperature' : r['main']['temp'],
        'pressure':r['main']['pressure'],
        'humidity':r['main']['humidity'],
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon'],
    }

    return render_template('weather.html', weather=weather)
if __name__=="__main__":
    app.run(debug=True)
