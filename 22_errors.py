try:
  print(0/0)
except ZeroDivisionError as Error:
  print(Error)

try:
  assert 1 != 1, 'Uno no es igual a uno'
except AssertionError as Error:
  print(Error)

try:
  age = 10
  if age < 10:
    raise Exception('No se permiten menores de edad')
except ZeroDivisionError as Error:
  print(Error)
except AssertionError as Error:
  print(Error)
except Exception as Error:
  print(Error)

print('Hola')