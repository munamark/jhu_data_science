
import os
import csv

voter_csv = './Resources/election_data.csv'

with open(voter_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    candidates = {}
    total_votes = 0
    percents = {}
    votes = {}
    votes2 = {}
    for row in csvreader:
        candidate = row[2]
        total_votes += 1
        if candidate not in candidates.keys():
            candidates[candidate] = 1
        else:
            candidates[candidate] +=1 
    #votes = candidates.values()
    #khan_percent = int(votes[0])/total_votes

    for i in candidates:
        percents[i] = round((candidates[i]/total_votes)*100,3)

    votes = {key: [percents[key] , candidates[key]]for key in percents}
    
    print(votes)


    print(f'''
    Election Results
-------------------------
  Total Votes: {total_votes}
  -------------------------
  {votes}

  -------------------------
  Winner: Khan
  -------------------------
  ''')

with open('./analysis/elections.txt', 'w') as file:
    file.write(f'''
Election Results
-------------------------
  Total Votes: {total_votes}
  -------------------------
  {votes}

  -------------------------
  Winner: Khan
  -------------------------

''')
