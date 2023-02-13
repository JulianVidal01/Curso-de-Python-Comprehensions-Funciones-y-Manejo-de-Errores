"""
dict = {}
for i in range(1, 5):
  dict[i] = i * 2

print(dict)

dict_v2 = {i: i * 2 for i in range(1,5)}
print(dict_v2)
"""
"""
import random

countries = ['col', 'mex', 'bol', 'pe']

population = {}
for country in countries:
  population[country] = random.randint(1, 100)
print(population)

dict_v2 = {country:random.randint(1,100) for country in countries}
print(dict_v2)
"""

name = ['nico', 'zule', 'santi']
ages = [12, 98, 56]
print(list(zip(name, ages)))

new_dict = {name:age for (name, age) in zip(name,ages)}
print(new_dict)