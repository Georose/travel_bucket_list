from flask import Flask
from controllers.cities_controller import cities_blueprint
from controllers.countries_controller import countries_blueprint


app = Flask(__name__)    

app.register_blueprint(cities_blueprint)
app.register_blueprint(countries_blueprint)

@app.route('/')
def home():
    return ('index.html')

if __name__ == '__main__':
    app.run(debug=True)

