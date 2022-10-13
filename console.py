import pdb
from models.country import Country
from models.city import City

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository


city_repository.delete_all()
country_repository.delete_all()




country1 = Country('Spain', True)
country_repository.save(country1)

country2 = Country('Scotland', False)
country_repository.save(country2)


city1 = City('Barcelona', country1, True)
city_repository.save(city1)

city2 = City('Madrid', country1, False)
city_repository.save(city2)

city3 = City('Seville', country1, True)
city_repository.save(city3)

city4 = City('Edinburgh', country2, True)
city_repository.save(city4)

city5 = City('Glasgow', country2, False)
city_repository.save(city5)

city6 = City('Aberdeen', country2, True)
city_repository.save(city6)








pdb.set_trace()