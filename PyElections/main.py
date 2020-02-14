import os
import csv 
import numpy as np

csvpath = os.path.join("..", "PyElections", "houston_election_data.csv")


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
Ind_votes = [] 
Total_Votes = len(All_Candidates)
for i in range(len(Unique_Candidates)-1):
    Ind_count.append(All_Candidates.count(Unique_Candidates[i]))
    perc_per.append(round((Ind_count[i]/len(All_Candidates))*100,2))
    Ind_votes.append(round((perc_per[i]/100) * Total_Votes))


perc_per, Unique_Candidates = zip(*sorted(zip(perc_per, Unique_Candidates)))
perc_per, Unique_Candidates = (list(t) for t in zip(*sorted(zip(perc_per, Unique_Candidates))))
Unique_Candidates.append(Unique_Candidates.reverse())
perc_per.append(perc_per.reverse())
Ind_votes.sort()
Ind_votes.append(Ind_votes.reverse())

Firstcandidate = Unique_Candidates[0]
Secondcandidate = Unique_Candidates[1]

print("Houston Mayoral Election Results")
print("---------------------------------------")
print(f"Total Cast Votes: {Total_Votes}")
print("---------------------------------------")

for i in range(len(Unique_Candidates)-1):
    print(f"{Unique_Candidates[i]}: {perc_per[i]}% ({Ind_votes[i]})")

print("----------------------------------------")
print(f"1st Advancing Candidate: {Firstcandidate}")
print(f"2nd Advancing Candidate: {Secondcandidate}")
print("----------------------------------------")