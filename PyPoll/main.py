#----Modules----
import os
import csv

#----Set path for file (works with Resources folder in same directory as main.py)----
csv_path = os.path.join(".", "Resources", "election_data.csv")

#----Open the CSV----(for candidate name check)
with open(csv_path, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    #skip and store header
    header = next(csv_reader)
    
    #initiate empty candidate_list
    candidate_list = []
    
#----Iterate over each row in the csv file to collect the needed list---
    #figuring out all the candidate names
    for row in csv_reader:
        
        #if name is already in candidate_list, check next row, otherwise
        #    append new name to candidate_list
        if row[2] in candidate_list:
            continue
        candidate_list.append(row[2])

#----Initiate a count_list for the candidates, to keep track of vote counts in next loop
count_list = [0] * len(candidate_list)

#----Open the CSV again----(for vote counts)
with open(csv_path, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    #skip and store header
    header = next(csv_reader)
    
    #go through rows in csv file again
    for row in csv_reader:
        
        #in each row, cycle through candidate names to check for match
        for name in candidate_list:
            
            #if the names match add 1 vote to their count list
            if row[2] == name:
                count_list[candidate_list.index(name)] += 1
        

#----Last calculations after loops----

#total votes is the final number of lines, minus the header
#   (just used csvreader's built in line counter)
total_votes = csv_reader.line_num - 1

#creating precent list off of vote counts divided by total counts
#   can't divide list by integer?
percent_list = list(map(lambda x: 100*x/total_votes, count_list))

#getting the index or location of the winner or highest precent
winner_index = percent_list.index(max(percent_list))

#----Printing to terminal----
print("Election Results")
print("-------------------------")
print("Total Votes: %d" % total_votes)
print("-------------------------")
for i in range(0, len(candidate_list)):
    print("%s: %.3f%% (%d)" % (candidate_list[i], percent_list[i], count_list[i]))
print("-------------------------")
print("Winner: %s" % candidate_list[winner_index])
print("-------------------------")


#----Write to txt file----
with open("output.txt", 'w') as txt_file:
    print("Election Results", file=txt_file)
    print("-------------------------", file=txt_file)
    print("Total Votes: %d" % total_votes, file=txt_file)
    print("-------------------------", file=txt_file)
    for i in range(0, len(candidate_list)):
        print("%s: %.3f%% (%d)" % (candidate_list[i], percent_list[i], count_list[i]), file=txt_file)
    print("-------------------------", file=txt_file)
    print("Winner: %s" % candidate_list[winner_index], file=txt_file)
    print("-------------------------", file=txt_file)
