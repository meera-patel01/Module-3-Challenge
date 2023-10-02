import os
import csv

#beginning format for output
print("Financial Analysis")
print("----------------------------")
#path for both reading from csv file and writing to text file
budget_csv = os.path.join("Resources", "budget_data.csv")
output = os.path.join("analysis", "PyBank_Output.txt")

#variable declaration for lists and totals
total_months = 0
total_profit = 0
month = []
profit = []
profit_change = []
month_change = []

#opening csv for reading 
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    
    #iterating through all rows of csv file
    for row in csvreader:
        #calculating total months and total overall profit
        total_months += 1
        total_profit += int(row[1])
        #appending each month and profit to a list call month and a list called profit
        month.append(row[0])
        profit.append(row[1])

#iterating through profit list 
for i in range(len(profit)):
    #conditional for appending the profit change and month for the change to lists
    if i != (len(profit) - 1):
        profit_change.append(int(profit[i+1]) - int(profit[i]))
        month_change.append(month[i+1])

#getting the average profit change
average = sum(profit_change)/len(profit_change)

#finding the index for the max and min profit change in order to match it to the correct month
max_index = profit_change.index(max(profit_change))
min_index = profit_change.index(min(profit_change))

#printing to console
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${round(average, 2)}")
print(f"Greatest Increase in Profits: {month_change[max_index]} (${max(profit_change)})")
print(f"Greatest Decrease in Profits: {month_change[min_index]} (${min(profit_change)})")

#writing to text file
with open(output, 'w') as textfile:
    textwriter = textfile.write("Financial Analysis\n")
    textwriter = textfile.write("----------------------------\n")
    textwriter = textfile.write(f"Total Months: {total_months}\n")
    textwriter = textfile.write(f"Total: ${total_profit}\n")
    textwriter = textfile.write(f"Average Change: ${round(average, 2)}\n")
    textwriter = textfile.write(f"Greatest Increase in Profits: {month_change[max_index]} (${max(profit_change)})\n")
    textwriter = textfile.write(f"Greatest Decrease in Profits: {month_change[min_index]} (${min(profit_change)})\n")