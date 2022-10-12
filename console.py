import pdb
from models.country import Country
from models.city import City

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

city_repository.delete_all()
country_repository.delete_all()

city1 = City('Barcelona', True)
city_repository.save(city1)

city2 = City('Madrid', False)
city_repository.save(city2)

city3 = City('Seville', True)
city_repository.save(city3)

city4 = City('Edinburgh', True)
city_repository.save(city4)

city5 = City('Glasgow', False)

city6 = City('Aberdeen', True)

country1 = Country('Spain', 'Barcelona', 'Madrid', 'Seville')
country_repository.save(country1)

country2 = Country('Scotland', 'Edinburgh', 'Glasgow', 'Aberdeen')







pdb.set_trace()