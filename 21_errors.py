#print(0 / 0)
#print(result)
print('Hola')

#suma = lambda x,y: x + (y * 2)
suma = lambda x,y: x + y 
assert suma(2,2) == 4

age = 10
if age < 18:
  raise Exception('No se permite menres de edad')

print('Holla 2')