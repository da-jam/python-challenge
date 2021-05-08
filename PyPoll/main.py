# Import modules
import os
import csv

# access file
csvpath = os.path.join('.','PyPoll','Resources','election_data.csv')
#print (csvpath)

# variables
candidate = [] #all votes
vote = [] #votes
percent = [] #percentage

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
        candidate.append(row[2])

    #print(candidate)
    
    ucands = set(candidate)
    #print(ucands)
    ucandl = list(ucands)
    #print(ucandl)

    ucan = len(ucandl)
    #print(ucan)

    total = len(candidate)

    for i in range(ucan):
        #get votes for each candidate
        vote.append(candidate.count(ucandl[i]))
        #print(f"{ucandl[i]} has {vote[i]} votes")
        #calculte vote%
        percent.append("{:.2f}".format((vote[i]*100)/total))
        #print(percent)
    
    #locate winner
    maxvote = max(vote)
    winner = ucandl[vote.index(maxvote)]
    #print(f"{winner}")

    #output to terminal
    print("Election Results")
    print("----------------------------------------------")
    print(f"Total Votes Cast: {total}")
    print("----------------------------------------------")
    for i in range(ucan):
        print(f"{ucandl[i]} received {percent[i]}% of the vote ({vote[i]})")
    print("----------------------------------------------")
    print(f"Winner is {winner}")
    print("----------------------------------------------")

    # output to file
    outf = open('PyPoll/analysis/Election_results.txt','w')
    outf.write("Election Results\n")
    outf.write("-------------------------------------------------\n")
    outf.write(f"Total Votes Cast: {total}\n")
    outf.write("-------------------------------------------------\n")
    outf.write(f"Total: ${total}\n")
    outf.write(f"Average Change: ${ave_diff}\n")
    outf.write(f"Greatest Increase in Profits: {max_date} (${max_diff})\n")
    outf.write(f"Greatest Decrese in Profits: {min_date} (${min_diff})\n")
    outf.close