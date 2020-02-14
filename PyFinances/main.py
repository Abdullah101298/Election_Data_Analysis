import os
import csv 

csvpath = os.path.join(". .","Desktop","python_challenge", "PyFinances", "budget_data.csv")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    Num_Months=0
    Profit_list= []
    Months = []
    for row in csvreader:
        Num_Months=(Num_Months+1)
        Profit_list.append(int(row[0]))
        Months.append(row[1])

import numpy 
Profit_sum = numpy.sum(Profit_list)

Profit_change = []

for i in range(len(Profit_list)-1):
    Profit_change.append(Profit_list[i+1]-Profit_list[i])

Average_Change = sum(Profit_change)/(len(Profit_change))

max_change = max(Profit_change)
min_change = min(Profit_change)

max_change_month = Profit_change.index(max_change)+1
Max_month = Months[max_change_month]

min_change_month = Profit_change.index(min_change)+1
Min_month = Months[min_change_month]

print("Financial Analysis")
print(f"Total Months: {Num_Months}")
print(f"Total: ${Profit_sum}")
print(f"Average Change: ${round(Average_Change,2)}")
print(f"Greatest Increase in Profits:{Max_month} (${max_change})")
print(f"Greatest Decrease in Profits:{Min_month} (${min_change})")


