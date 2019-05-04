#import libraries
import os
import csv

#Already copied in to same directory 
elec_data = os.path.join("election_data.csv")

#Candidate List - each candidate names
#Vote List - each candidate received
#Percetage Total List - each candidate percentage of votes
    #defining arrays to store the data
candidates = []
eachcan_votes = []
percenttot_votes = []


# A counter for the total number of votes - initially it's 0
tot_votes = 0

with open(elec_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        
        tot_votes = tot_votes + 1 

        if row[2] not in candidates:
            candidates.append(row[2])
            placeholder = candidates.index(row[2])
            eachcan_votes.append(1)
        else:
        #else row[2] not in candidates:
            placeholder = candidates.index(row[2])
            eachcan_votes[placeholder] = eachcan_votes[placeholder] + 1
    
    #  The percentage of votes each candidate won
    for votes in eachcan_votes:
        percentage = round((votes/tot_votes) * 100)
        percenttot_votes.append(percentage)
    
    # The winner of the election based on popular vote.
    winner = max(eachcan_votes)
    placeholder = eachcan_votes.index(winner)
    winning_candidate = candidates[placeholder]

# Analysis should look similar to the one below:
print("'''text")
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(tot_votes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percenttot_votes[i])} ({str(eachcan_votes[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")
print("'''")

# Print the analysis to the terminal and export a text file with the results.
output = open("PyPollOutput.txt", "w")
line1 = "'''text"
line2 = "Election Results"
line3 = "--------------------------"
line4 = str(f"Total Votes: {str(tot_votes)}")
line5 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4,line5))
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {str(percenttot_votes[i])} ({str(eachcan_votes[i])})")
    output.write('{}\n'.format(line))
line6 = "--------------------------"
line7 = str(f"Winner: {winning_candidate}")
line8 = "--------------------------"
line9 = "'''"
output.write('{}\n{}\n{}\n{}\n'.format(line6, line7, line8,line9))