from db.run_sql import run_sql
from models.city import City
from models.country import Country
import repositories.country_repository as country_repository

def save(city):
    sql = """
    INSERT INTO cities (name, visit)
    Values (%s, %s)
    RETURNING *
    """
    values = [city.name, city.visit]
    results = run_sql(sql, values)
    id = results [0]["id"]
    city.id = id
    return city

def delete():
    sql = """
    DELETE FROM cities
    WHERE id = %s
    """
    values = [id]
    run_sql(sql, values)

def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        city =  City(row['name'], row['visit'], row['id'])
        cities.append(city)
    return cities

def select(id):
    city = None
    sql = "SELECT * FROM city WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        city = City(result['name'], result['visit'], result['id'] )
    return city

def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)


    