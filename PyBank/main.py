# Import Modules and set path

import os
import csv

csvpath = os.path.join("PyBank.csv")

# create lists and variables

profit = []
profit_change = []
date = []
total_change_profits = 0
count = 0
total_profit = 0
beginning_profit = 0
ending_profit = 0
# Open CSV

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # Total months
    for row in csvreader:
      count = count + 1 

      # Append dates for greatest increa/decrease
      date.append(row[0])

      # Total profit formula
      profit.append(row[1])
      total_profit = total_profit + int(row[1])

      # Average change over entire period
      ending_profit = int(row[1])
      profit_changes = ending_profit - beginning_profit

      #Store these monthly changes in a list
      profit_change.append(profit_changes)

      total_change_profits = total_change_profits + profit_changes
      beginning_profit = ending_profit

      # Avg change in profits
      avg_change_profits = (total_change_profits/count)

      #Find the max and min change in profits and the corresponding dates these changes were obeserved
      greatest_increase_profits = max(profit_change)
      greatest_decrease_profits = min(profit_change)

      increase_date = date[profit_change.index(greatest_increase_profits)]
      decrease_date = date[profit_change.index(greatest_decrease_profits)]
    

      
   
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(avg_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")

    f = open('Financial_analysis.txt', 'w+') as text:
    text.write("----------------------------------------------------------\n")
    text.write("    Financial Analysis"+ "\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(avg_change_profits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
