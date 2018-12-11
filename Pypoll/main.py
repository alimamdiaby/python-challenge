import os
import csv

#path for the CSV file in PyBankcsv
pyPollcsv = os.path.join('election_data.csv')
#lists for data
vote_data = []

with open(pyPollcsv, newline= '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        vote_data.append(row)
print(vote_data)