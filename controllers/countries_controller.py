from crypt import methods
from flask import Flask, render_template, redirect, request
from models.country import Country
from models.city import City
import repositories.country_repository as country_repository
from flask import Blueprint

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries", methods = ['GET'])
def countries():
    countries = country_repository.select_all() 
    return render_template("countries/index.html", countries = countries)

@countries_blueprint.route('/countries/new', methods = ["GET"])
def new_country():
    return render_template('/countries/new.html')

@countries_blueprint.route('/countries/create', methods = ['POST'])
def create_country():
    name = request.form['country']
    city = request.form['city']
    visit = True if "visit" in request.form else False
    country = Country(name, city, visit)
    country_repository.save(country)
    return redirect('/countries')

@countries_blueprint.route('/countries/<id>/edit', methods = ["GET"])
def edit_country(id):
    country = country_repository.select(id)
    return render_template('/countries/edit.html', country = country)





