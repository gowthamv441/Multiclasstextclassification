import csv

with open('pp.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        for col in row:
            print (col)