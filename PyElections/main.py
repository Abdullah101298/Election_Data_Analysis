# Abdullah Almasri - PyElections challenge 

import os
import csv 
import numpy as np

#Importing data from the csv file as well as defining export path 
csvpath = os.path.join("..", "PyElections", "election_data.csv")
exportresults = os.path.join("..", "PyElections", "Election Results")

#creating empy matrices to fill later 
All_Candidates = []
County_total = []
Voter_ID = []

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
#Splitting the rows into different matrices 
    for row in csvreader:
        All_Candidates.append(row[0])
        County_total.append(row[1])
        Voter_ID.append(row[2])
        
#Finding the unique candiadates in the list of all candidates 
Unique_Candidates = []
for x in All_Candidates:
    if x not in Unique_Candidates:
        Unique_Candidates.append(x)

#Finding the total count for each candidate as well as the percentage of vote they recieved. 
Ind_count =[]
perc_per =[]
Total_Votes = len(All_Candidates)
for i in range(len(Unique_Candidates)):
    Ind_count.append(All_Candidates.count(Unique_Candidates[i]))
    perc_per.append(round((Ind_count[i]/len(All_Candidates))*100,2))

#Sorting the data so that can it can come out properly as I want it
perc_per, Unique_Candidates = zip(*sorted(zip(perc_per, Unique_Candidates)))
perc_per, Unique_Candidates = (list(t) for t in zip(*sorted(zip(perc_per, Unique_Candidates))))
Unique_Candidates.append(Unique_Candidates.reverse())
perc_per.append(perc_per.reverse())
Ind_count.sort()
Ind_count.append(Ind_count.reverse())

#Finding the leading candidate and the second leading candidate 
Firstcandidate = Unique_Candidates[0]
Secondcandidate = Unique_Candidates[1]


#Defining and printing the strings I want to print 
Election_summary1 = ( 
    "Houston Mayoral Election Results \n"
    "---------------------------------------\n"
    f"Total Cast Votes: {Total_Votes}\n"
    "---------------------------------------\n")

print(Election_summary1)

Election_summary3 = (
    "---------------------------------------- \n"
    f"1st Advancing Candidate: {Firstcandidate} \n"
    f"2nd Advancing Candidate: {Secondcandidate} \n"
    "---------------------------------------- \n")


for i in range(len(Unique_Candidates)-1):
    print(f"{Unique_Candidates[i]}: {perc_per[i]}% ({Ind_count[i]})")

    
print(Election_summary3)

#Exporting the results into a text file. 
with open(exportresults, "w") as txt_file:    
        txt_file.write(Election_summary1)
        for i in range(len(Unique_Candidates)-1):
            txt_file.write(f"{Unique_Candidates[i]}: {perc_per[i]}% ({Ind_count[i]}) \n")
        txt_file.write(Election_summary3)

