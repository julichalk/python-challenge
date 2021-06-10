import os
import csv

csvpath = os.path.join("election_data.csv")

candidates = []
number_votes = []
percent_votes = []
total_votes = 0

with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None)

    for row in csvreader:
        total_votes +=1

        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            number_votes.append(1)

        else:
            index = candidates.index(row[2])
            number_votes[index] +=1

    for votes in number_votes:
        percentage = round((votes/total_votes) * 100)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)

    winner = max(number_votes)
    index = number_votes.index(winner)
    winning_candidate = candidates[index]


print("Election Results")

print(f"Total votes: {str(total_votes)}")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
print(f"Winner: {winning_candidate}")


filename = 'results.txt'
with open(filename, "w") as file:
    for result in results:
        print(result)
        file.write(result)

        

    
     