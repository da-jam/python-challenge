# Import modules
import os
import csv

# access file
csvpath = os.path.join('.','PyBank','Resources','budget_data.csv')
#print (csvpath)

# variables
k = 0 # row counter
budget = [] #profit/loss
dates = []
diff = [] #difference from previous date

#read file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    #skip header
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        k = k + 1 # count rows
        #print(row[0])
        #separte columns to lists for operation
        budget.append(int(row[1]))
        dates.append(row[0])
        
    #print(k)
    #print(budget[2])
    #print(dates[2])

    for i in range(k-1):
        diff.append((budget[i+1]-budget[i]))

    #print(diff)

    #sum budget for net total of Profit/Loss
    total = sum(budget)
    #print(total)

    # max of the differences
    max_diff = max(diff)
    #print(max_diff)

    #min of the differences
    min_diff = min(diff)
    #print(min_diff)

    #locate min and max values
    #print(diff.index(max_diff))
    #print(diff.index(min_diff))

    #dates for min and max values
    max_date = dates[(diff.index(max_diff)+1)]
    min_date = dates[(diff.index(min_diff)+1)]

    #average of differences formatted
    ave_diff = "{:.2f}".format(float(sum(diff)/len(diff)))
    #print(ave_diff)

    #output to terminal
    print("Financial Analysis")
    print("-------------------------------------------------")
    print(f"Total Months: {k}")
    print(f"Total: ${total}")
    print(f"Average Change: ${ave_diff}")
    print(f"Greatest Increase in Profits: {max_date} (${max_diff})")
    print(f"Greatest Decrese in Profits: {min_date} (${min_diff})")

    # output to file
    outf = open('PyBank/analysis/financial_analysis.txt','w')
    outf.write("Financial Analysis\n")
    outf.write("-------------------------------------------------\n")
    outf.write(f"Total Months: {k}\n")
    outf.write(f"Total: ${total}\n")
    outf.write(f"Average Change: ${ave_diff}\n")
    outf.write(f"Greatest Increase in Profits: {max_date} (${max_diff})\n")
    outf.write(f"Greatest Decrese in Profits: {min_date} (${min_diff})\n")
    outf.close



    



