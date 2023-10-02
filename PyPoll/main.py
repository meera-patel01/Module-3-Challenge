import os
import csv

#beginning format for output
print("Election Results")
print("-------------------------")
#path for both reading from csv file and writing to text file
election_csv = os.path.join("Resources", "election_data.csv")
output = os.path.join("analysis", "PyPoll_Output.txt")

#variable declaration for lists and totals
total_votes = 0
candidates_dict = {}
most_votes = 0
winner = ''

#opening csv for reading 
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    
    #iterating through all rows of csv file
    for row in csvreader:
        #calculating total votes
        total_votes += 1
        #making list of candidates
        candidate = row[2]
        if candidate not in candidates_dict:
            candidates_dict[candidate] = 1
        #total votes per candidate
        else:
            candidates_dict[candidate] += 1

#printing total votes
print(f"Total Votes: {total_votes}")
print("-------------------------")

#iterating through dictionary to print candidate and total votes while also calculating the percentage of votes
for i in candidates_dict:
    print(f"{i}: {round((candidates_dict[i]/total_votes)*100, 3)}% ({candidates_dict[i]})")
    #conditional to find which candidate has the most votes
    if candidates_dict[i] > most_votes:
        most_votes = candidates_dict[i]
        winner = i

#printing winner
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#writing to text file
with open(output, 'w') as textfile:
    textwriter = textfile.write("Election Results\n")
    textwriter = textfile.write("-------------------------\n")
    textwriter = textfile.write(f"Total Votes: {total_votes}\n")
    textwriter = textfile.write("-------------------------\n")
    for i in candidates_dict:
        textwriter = textfile.write(f"{i}: {round((candidates_dict[i]/total_votes)*100, 3)}% ({candidates_dict[i]})\n")
    textwriter = textfile.write("-------------------------\n")
    textwriter = textfile.write(f"Winner: {winner}\n")
    textwriter = textfile.write("-------------------------\n")