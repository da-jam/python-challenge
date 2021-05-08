# Import modules
import os
import csv

# access file
csvpath = os.path.join('.','PyBank','Resources','budget_data.csv')
#print (csvpath)

# variables
k = 0 # row counter
budget = []
dates = []
diff = []

#read file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        k = k + 1 # count rows
        #if float(row[1]) <= 0:
        #print(row[0])
        #separte columns to lists for operation
        budget.append(int(row[1]))
        dates.append(row[0])
        
    #print(k)
    #print(budget[2])
    #print(dates[2])

    for i in range(k-1):
        diff.append((budget[i+1]-budget[i]))

    print(diff)



