#Dependencies
import os 
import csv

def output(candidates, votes, total):
    print('Election Results\n'\
        '----------------------\n'\
        f'Total Votes: {total}')
    for i, candidate in enumerate(candidates):
        print(f'{candidates[i]}: {votes[i] / total * 100}% ({votes[i]})')
    winner = candidates[votes.index(max(votes))]
    print(f'Winner {winner}')

#variable
candidate_list = []
candidate_votes = dict()
percentage = []

total_votes = 0

#Open csv
with open('Resources/Election Data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #Looping through the data 
    for row in csvreader:
        # Get candidate name
        candidate_name = row[2]

        total_votes = total_votes +1
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] = candidate_votes[candidate_name] +1

percentage = [voters_count / total_votes for voters_count in candidate_votes.values()]

#print([type(candidate_votes.values())])
output(candidate_list, list(candidate_votes.values()), total_votes)
print(candidate_list)
print(list(candidate_votes.values()))
# output()
# print(percentage)
#     # {'Khan': 2218231, 'Correy': 704200, 'Li': 492940, "O'Tooley": 105630} / 3240000

# print(f'candidate_list: {candidate_list}\n'\
#     f'candidate_votes: {candidate_votes}\n'\
#         f'total_votes {total_votes}\n')
