set_countries = {'Col', 'Mex', 'Bol'}

size = len(set_countries)
print(size)

print('Col' in set_countries)
print('Pe' in set_countries)

#add
set_countries.add('Pe')
print(set_countries)
set_countries.add('Pe')
print(set_countries)

#update
set_countries.update({'Arg', 'Ecua', 'Pe'})
print(set_countries)

#remove
set_countries.remove('Col')
print(set_countries)

#set_countries.remove('Arg')
set_countries.discard('Arg')
print(set_countries)

#clean 
set_countries.clear()
print(set_countries)
