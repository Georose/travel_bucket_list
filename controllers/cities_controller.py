from flask import Flask, render_template, redirect
from models.city import City
import repositories.city_repository as city_repository

from flask import Blueprint

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/")
def home():
    cities = city_repository.select_all() 
    return render_template("/index.html", cities = cities)

@cities_blueprint.route("//<id>")
def show(id):
    location = city_repository.select(id)
    users = city_repository.city()
    return render_template("/show.html")

