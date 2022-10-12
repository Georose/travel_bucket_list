from db.run_sql import run_sql
from models.city import City
from models.country import Country
import repositories.country_repository as country_repository

def save(city):
    sql = """
    INSERT INTO cities (name, visit, country_id)
    Values (%s, %s, %s)
    RETURNING *
    """

def delete():
    sql = """
    DELETE FROM cities
    WHERE id = %s
    """
    values = [id]
    run_sql(sql, values)