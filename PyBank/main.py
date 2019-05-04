#libraries export 
import os
import csv

#tot_months as Str
#tot_pl as Double

#as the csv is in the loxal folder
budget_data = os.path.join("budget_data.csv")

#variables defined - initially 0
tot_months = 0
tot_pl = 0
val = 0
change = 0

#arrays defined
dates = []
profits = []


with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

   
    csv_header = next(csvreader)

    #first row
    first_row = next(csvreader)
    tot_months = tot_months + 1
    tot_pl = tot_pl  + int(first_row[1])
    val = int(first_row[1])
    
    #going through all the rows
    for row in csvreader:
        
        dates.append(row[0])
        
        
        change = int(row[1])-val
        #added it to the profits array I created
        profits.append(change)
        val = int(row[1])
        
        
        tot_months = tot_months + 1

        
        tot_pl = tot_pl + int(row[1])


    #The average of the changes in "Profit/Losses" over the entire period
    avg_change = sum(profits)/len(profits)

    #The greatest increase in profits (date and amount) over the entire period
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    #The greatest decrease in losses (date and amount) over the entire period
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    
    
    

#As an example, your analysis should look similar to the one below:
print("'''text")
print("Financial Analysis")
print("---------------------")
#The total number of months included in the dataset
print(f"Total Months: {str(tot_months)}")
#The net total amount of "Profit/Losses" over the entire period
print(f"Total: ${str(tot_pl)}")
#The average of the changes in "Profit/Losses" over the entire period
print(f"Average Change: ${str(round(avg_change,2))}")
#The greatest increase in profits (date and amount) over the entire period
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
#The greatest decrease in losses (date and amount) over the entire period
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
print("'''")

#print the analysis to the terminal and export a text file with the results.
output = open("PyBankOutput.txt", "w")

l1 = "'''text"
l2 = "Financial Analysis"
l3 = "---------------------"
l4 = str(f"Total Months: {str(tot_months)}")
l5 = str(f"Total: ${str(tot_pl)}")
l6 = str(f"Average Change: ${str(round(avg_change,2))}")
l7 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
l8 = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
l9 = "'''"
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(l1,l2,l3,l4,l5,l6,l7,l8,l9))