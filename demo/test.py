import csv
import os
#def rcsv(filename):
filename = r'orgin_user.csv'
result = []
with open(filename, 'r') as f:
    reader = csv.reader(f)
    x = 0
    for row in reader:
        if x == 0:
            pass
        else:
            result.append(row)
        x = x + 1
        print(x)
#return result

