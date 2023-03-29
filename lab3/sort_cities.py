# Author: Alexander Marcoux
# Date: 1 March 2023
# Purpose: sorting the cities in world_cities
from city import City
from quicksort import *

# cities_alpha.txt contains the list of cities sorted alphabetically.
# cities_population.txt contains the list of cities sorted by population, from most to least populous.
# cities_latitude.txt contains the list of cities sorted by latitude, from south to north.

cities_list = open("world_cities.txt", "r")
cities_alpha = open("cities_alpha.txt", "w")
cities_population = open("cities_population.txt", "w")
cities_latitude = open("cities_latitude.txt", "w")

# empty list to add info to
cities = []

for line in cities_list:
    line.strip()
    city_info = line.split(",")

    # adding the parsed info into the empty list
    cities.append(City(city_info[0], city_info[1], city_info[2], city_info[3], city_info[4], city_info[5]))


# sorting based on alphabetical order
def compare_alpha(city1, city2):
    return city1.name.lower() <= city2.name.lower()


sort(cities, compare_alpha)
for city in cities:
    # adding each city to new txt file
    cities_alpha.write(str(city)+"\n")


# sorting based on pop (decreasing)
def compare_pop(city1, city2):
    return city2.population <= city1.population


sort(cities, compare_pop)
for city in cities:
    cities_population.write(str(city)+"\n")


# sorting based on latitude (south to north)
def compare_lat(city1, city2):
    return city1.latitude <= city2.latitude


sort(cities, compare_lat)
for city in cities:
    cities_latitude.write(str(city) + "\n")

# closing the files
cities_list.close()
cities_alpha.close()
cities_population.close()
cities_latitude.close()
