with open('./text.txt', 'r+') as file:
  for line in file:
    print(line)
  file.write('New things in this file \n')
  file.write('New line 1 \n')
  file.write('New line 2 \n')

file.close()
