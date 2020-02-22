import os
import csv 
import numpy as np

csvpath = os.path.join("..", "PyElections", "election_data.csv")
exportresults = os.path.join("..", "PyElections", "Election Results")


All_Candidates = []
County_total = []
Voter_ID = []

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        All_Candidates.append(row[0])
        County_total.append(row[1])
        Voter_ID.append(row[2])
        

Unique_Candidates = []
for x in All_Candidates:
    if x not in Unique_Candidates:
        Unique_Candidates.append(x)

Ind_count =[]
perc_per =[]
Total_Votes = len(All_Candidates)
for i in range(len(Unique_Candidates)):
    Ind_count.append(All_Candidates.count(Unique_Candidates[i]))
    perc_per.append(round((Ind_count[i]/len(All_Candidates))*100,2))
    
perc_per, Unique_Candidates = zip(*sorted(zip(perc_per, Unique_Candidates)))
perc_per, Unique_Candidates = (list(t) for t in zip(*sorted(zip(perc_per, Unique_Candidates))))
Unique_Candidates.append(Unique_Candidates.reverse())
perc_per.append(perc_per.reverse())
Ind_count.sort()
Ind_count.append(Ind_count.reverse())

Firstcandidate = Unique_Candidates[0]
Secondcandidate = Unique_Candidates[1]


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

with open(exportresults, "w") as txt_file:    
        txt_file.write(Election_summary1)
        for i in range(len(Unique_Candidates)-1):
            txt_file.write(f"{Unique_Candidates[i]}: {perc_per[i]}% ({Ind_count[i]}) \n")
        txt_file.write(Election_summary3)

