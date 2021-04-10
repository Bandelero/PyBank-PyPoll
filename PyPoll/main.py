import os
import csv

pypoll_dict = {}

election_data = os.path.join("Resources/PyPoll_Resources_election_data.csv")

print("Election Results \n------------------------------")

# Read in the CSV file
with open(election_data, 'r') as csvfile:

	# Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    #Skip header row when reading
    header = next(csvreader)


    total_votes = 0

    for row in csvreader:    #row = [ID, County, Candidate]
    	total_votes += 1
    	candidate = row[2]
    	if candidate not in pypoll_dict:
    		pypoll_dict[candidate] = 0
    	pypoll_dict[candidate] += 1

   		 	
    print("Total Votes: {}\n------------------------------".format(total_votes))
    for candidate in pypoll_dict:
    	percentage_vote = format((pypoll_dict[candidate] / total_votes)*100, '.3f')
    	print("{}: {}% ({})".format(candidate,percentage_vote,pypoll_dict[candidate]))
    print("------------------------------")

    winner = max(pypoll_dict,key=pypoll_dict.get)
    print("Winner: {}\n------------------------------".format(winner))


#write to text file
output_path = os.path.join("analysis/textOutputPypoll.txt")
with open(output_path, 'w', newline='') as csvfile:
	csvwriter = csv.writer(csvfile, delimiter=',')

	csvwriter.writerow(['Election Results']) 
	csvwriter.writerow(['------------------------------'])

	csvwriter.writerow(['Total Votes: {}'.format(total_votes)])
	csvwriter.writerow(['------------------------------'])
	for candidate in pypoll_dict:
		percentage_vote = format((pypoll_dict[candidate] / total_votes)*100, '.3f')
		csvwriter.writerow(["{}: {}% ({})".format(candidate,percentage_vote,pypoll_dict[candidate])])
	csvwriter.writerow(['------------------------------'])

	csvwriter.writerow(['Winner: {}'.format(winner)])
	csvwriter.writerow(['------------------------------'])