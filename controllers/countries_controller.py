from flask import Flask, render_template, redirect
from models.country import Country
from models.city import City

from flask import Blueprint

countries_blueprint = Blueprint("countries", __name__)