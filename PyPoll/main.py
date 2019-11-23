import os
import csv
csvpath = os.path.join("PyPoll.csv")

# Create lists and variables
candidates = []
total_votes = 0
candidate_votes = []
election_data = ['1', '2']


      
# Open CSV
with open(csvpath) as csvfile:
       csvreader = csv.reader(csvfile, delimiter=',')
       line = next(csvreader,None)
        
    # Iterate through
       for line in csvreader:        

            # Determine vote count and candidate count
            total_votes = total_votes +1
            
            candidate = line[2]
          
            # Assign votes to candidates
            if candidate in candidates:
                candidate_index = candidates.index(candidate)
                candidate_votes[candidate_index] = candidate_votes[candidate_index] + 1

            # Append votes to candidate and total votes
            else:
                candidates.append(candidate)
                candidate_votes.append(1)
               
# Variables percent of votes per candidate 
percentages = []
max_votes = candidate_votes[0]
max_index = 0
    
#Work out percentages and winner (in a For Loop)
for count in range(len(candidates)):
    vote_percentage = candidate_votes[count]/total_votes*100
    percentages.append(vote_percentage)
    if candidate_votes[count] > max_votes:
        max_votes = candidate_votes[count]
        print(max_votes)
        max_index = count
winner = candidates[max_index]
   
percentages = [round(i,2) for i in percentages]
    
# Summary print test of election results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({candidate_votes[count]})")
print("--------------------------")
print(f"Winner:  {winner}")
print("--------------------------")

#Export file name and open as text file
output_file = csvpath[0:-4]
write_csvpath = f"{output_file}PyPoll_results.txt"
filewriter = open(write_csvpath, mode = 'w')
    
# Write results to export text file
filewriter.write("Election Results\n")
filewriter.write("-----------------------------\n")
filewriter.write(f"Total Votes:  {total_votes}\n")
filewriter.write("-----------------------------\n")
for count in range(len(candidates)):
    filewriter.write(f"{candidates[count]}: {percentages[count]}% ({candidate_votes[count]})\n")
filewriter.write("-----------------------------\n")
filewriter.write(f"Winner:  {winner}\n")
filewriter.write("-----------------------------\n")
    
# Close the text file
filewriter.close()