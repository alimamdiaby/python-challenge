import os
import csv

print(os.getcwd())
print("Financial Analysis")

#path for the CSV file in PyBankcsv
pbankcsv = os.path.join('..', 'Resources', 'budget_data.csv')

#lists for data
data = []
Months = []
Profits = []
Total= []
AvgChange = []
LrgIncProfits = []
LrgIncProfits = []

profits= 0

#total months
with open(pbankcsv, newline= '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
  #CSV File
        data.append(row)
        Months.append(row[0])
    print("Total Months" + str(len(Months)))

with open(pbankcsv, newline= '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    #Looping through profit
    for row in csvreader:
        Profits.append(int(row[1]))
    print(sum(Profits))
#The average change in "Profit/Losses" between months over the entire period
for m in range(len(Profits)-1):
    AvgChange.append(Profits[m+1]-Profits[m])
print(sum(AvgChange)/len(AvgChange))
 #The greatest increase in profits (date and amount) over the entire period
print(max(AvgChange))
 #The greatest decrease in losses (date and amount) over the entire period
print(min(AvgChange))
