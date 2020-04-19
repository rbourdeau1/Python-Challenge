# First we'll import the necessary modules
import os   # This will allow us to create file paths across operating systems
import csv  # This will allow us to read from and write to csv files

# Indicate the location and filename of the csv file and assign it to a variable
elect_path = os.path.join('Resources', 'election_data.csv')

# Read in the CSV file
with open(elect_path) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    # Create a list of voters and a list of candidates they voted for
    voter_list = []
    candidate_list = []
       
    for row in csvreader:
        voter_list.append(row[0])
        candidate_list.append(row[2])

# Create a list that contains only the unique candidate names 
unique_list = []
for candidate in candidate_list:
    if candidate not in unique_list:
        unique_list.append(candidate)

# Count the number of votes each candidate received
total_votes = len(voter_list)
votes = 0
num_votes_list=[]
percent_votes_list=[]

for i in range(len(unique_list)):
    for j in range(total_votes):
        if unique_list[i] == candidate_list[j]:
            votes=votes+1
    num_votes_list.append(votes)
    percent_votes_list.append(votes/total_votes*100)  
    votes=0

# Determine the winner i.e. candidate who received the most votes.
max_votes=max(num_votes_list)
winner_index=num_votes_list.index(max_votes)
winner=unique_list[winner_index]

# Prepare and print our results
output1 = f"""Election Results
---------------------------------------------------
Total Votes: {total_votes}
---------------------------------------------------"""
output2 = f"""---------------------------------------------------
Winner: {winner}
---------------------------------------------------"""

print(output1)

# Print each candidate, the number of votes they received and its percentage to the total number of votes cast
final_vote_list=[]
for candidate, percent_votes, num_votes in zip(unique_list,percent_votes_list,num_votes_list):
    row=f"{candidate}: {round(percent_votes,1)}% ({num_votes})"
    print(row)
    final_vote_list.append(row)

print(output2)

# Print our results to a text file
output_path = os.path.join("pypoll_results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:
    txtfile.write(output1)
    txtfile.write("\n")
    for candidate in final_vote_list:
        txtfile.write(candidate)
        txtfile.write("\n")
    txtfile.write(output2)
