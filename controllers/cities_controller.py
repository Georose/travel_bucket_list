from flask import Flask, render_template, redirect
from models.city import City
from repositories import city_repository

from flask import Blueprint

cities_blueprint = Blueprint("cities", __name__)