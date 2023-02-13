import csv

def read_csv(path):
   sum = 0
   with open(path, 'r') as csvfile:
      reader = csv.reader(csvfile)
      for data_set in reader:
         sum += int(data_set[1])
   return sum

response = read_csv('./data.csv')
print(response)