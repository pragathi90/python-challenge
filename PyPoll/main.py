#import libraries
import os
import csv

#Already copied in to same directory 
elec_data = os.path.join("election_data.csv")

#Candidate List - each candidate names as CN
#Vote List - each candidate received CV
#Percetage Total List - each candidate percentage of votes PV
    #defining arrays to store the data
CN = []
CV= []
PV = []


# A counter for the total number of votes as TV- initially it's 0
TV = 0

with open(elec_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        
        TV = TV + 1 
        # Getting the different candidate names 
        # Same as getting the unique values from the csv given 
        # as we've asked to make the code run in any list, had to write this piece to get the values from that column

        if row[2] not in CN:
            CN.append(row[2])
            placeholder = CN.index(row[2])
            CV.append(1)
        else:
        #else row[2] not in candidates:
            placeholder = CN.index(row[2])
            CV[placeholder] = CV[placeholder] + 1
    
    #  The percentage of votes each candidate won
    for votes in CV:
        percentage = "%.3f%%" %(round((votes/TV) * 100))
        PV.append(percentage)
    
    # The winner of the election based on popular vote. as Winning candidate as WC & Winner as W
    W = max(CV)
    placeholder = CV.index(W)
    WC = CN[placeholder]

# Analysis should look similar to the one below:
print("'''text")
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(TV)}")
print("--------------------------")
for i in range(len(CN)):
    print(f"{CN[i]}: {str(PV[i])} ({str(CV[i])})")
print("--------------------------")
print(f"Winner: {WC}")
print("--------------------------")
print("'''")

# Print the analysis to the terminal and export a text file with the results.
output = open("PyPollOutput.txt", "w")
l1 = "'''text"
l2 = "Election Results"
l3 = "--------------------------"
l4 = str(f"Total Votes: {str(TV)}")
l5 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n{}\n'.format(l1, l2, l3, l4,l5))
for x in range(len(CN)):
    line = str(f"{CN[x]}: {str(PV[x])} ({str(CV[x])})")
    output.write('{}\n'.format(line))
l6 = "--------------------------"
l7 = str(f"Winner: {WC}")
l8 = "--------------------------"
l9 = "'''"
output.write('{}\n{}\n{}\n{}\n'.format(l6, l7, l8,l9))