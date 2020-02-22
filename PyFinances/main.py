#Abdullah Almasri - PyFinances Challenge

import os
import csv 

#Importing data from the csv file 
csvpath = os.path.join("..", "PyFinances", "budget_data.csv")
exportresults = os.path.join("..", "PyFinances", "Financial Analysis")


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
#seperating columns of csv file into different variables as well as counting the number of rows 
    Num_Months=0      
    Profit_list= []
    Months = []
    for row in csvreader:
        Num_Months=(Num_Months+1)
        Profit_list.append(int(row[0]))
        Months.append(row[1])

#Finding the profit sum using numpy 
import numpy 
Profit_sum = numpy.sum(Profit_list)

#Finding the change in profits between consecutive months 
Profit_change = []
for i in range(len(Profit_list)-1):
    Profit_change.append(Profit_list[i+1]-Profit_list[i])

#Average of the profit changes we found before 
Average_Change = sum(Profit_change)/(len(Profit_change))

#Max and min of the profit change and their respected months 
max_change = max(Profit_change)
min_change = min(Profit_change)

max_change_month = Profit_change.index(max_change)+1
Max_month = Months[max_change_month]

min_change_month = Profit_change.index(min_change)+1
Min_month = Months[min_change_month]

#Printing out the results from the above code in an organized fashion 
Summary = (
    "\n"
    "Financial Analysis \n"
    f"Total Months: {Num_Months}\n"
    f"Total: ${Profit_sum}\n"
    f"Average Change: ${round(Average_Change,2)}\n"
    f"Greatest Increase in Profits:{Max_month} (${max_change})\n"
    f"Greatest Decrease in Profits:{Min_month} (${min_change})\n")
print(Summary)

#Exporting the results to a txt file 
with open(exportresults, "w") as txt_file:    
    txt_file.write(Summary)




