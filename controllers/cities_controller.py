from flask import Flask, render_template, redirect, request
from models.city import City
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

from flask import Blueprint

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities")
def home():
    cities = city_repository.select_all() 
    countries = country_repository.select_all()
    return render_template("cities/index.html", cities = cities, countries = countries)

@cities_blueprint.route("/cities", methods=['POST'])
def create_city():
    name = request.form['city name']
    visit = True if "visit" in request.form else False
    country = country_repository.select(request.form['country_id'])
    city = City(name, country, visit)
    city_repository.save(city)
    return redirect('/cities')

@cities_blueprint.route('/cities/<id>/delete', methods = ['GET'])
def delete_city(id):
    city_repository.delete(id)
    return redirect ('/countries')


# @cities_blueprint.route("/cities/<id>")
# def show(id):
#     city = city_repository.select(id)
#     return render_template("cities/show.html", city=city)

