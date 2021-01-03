#The data we need to retrieve"
# 1. The total number of votes casts
# 2. Complete list of candidates that received votes
# 3. The percentage of votes each canddidate won
# 4. The total number of votes each canddiate won
# 5. The winner of the election based on popular vote
import csv
import os


#Assign file variable and load path
file_to_load= os.path.join("Resources", "election_results.csv")
#create file name and path to file
file_to_save= os.path.join("analysis", "election_analysis.txt")

#initialize a total votes variable
total_votes = 0

#delcare candidate list
candidate_options = []
#declare a dictionarey
candidate_votes = {}

#declare winning candidate and count trackrt
winning_candidate =""
winning_count = 0
winning_percentage = 0
#open election results and read file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    #read and print headers
    headers = next(file_reader)


    #print each row in csv
    for row in file_reader:
        #add to the total vote count
        total_votes += 1

        #candidates name
        candidate_name = row[2]
        
        #add if not existing
        if candidate_name not in candidate_options:

            #add can names
            candidate_options.append(candidate_name)

            #begin tracking votes
            candidate_votes[candidate_name] = 0

        #add to that candidates count
        candidate_votes[candidate_name] += 1

    #Derermine the percentage of votes for each candidate
    for candidate_name in candidate_votes:
        #retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #calculate % of votes
        vote_percentages = float(votes)/float(total_votes)*100
        
        #each voters stuff
        print(f"{candidate_name}: {vote_percentages:.1f}% ({votes:,}) \n")

        #determine if vote count is greater than winning count
        if (votes>winning_count) and (vote_percentages>winning_percentage):
            #set counts and percentages
            winning_count=votes
            winning_percentage = vote_percentages
            #set candidate
            winning_candidate = candidate_name
    winning_candidate_summary= (
        f"-----------------\n"
        f"Winner: {winning_candidate} \n"
        f"Winning Vote Count: {winning_count:,} \n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------\n")
    #print(winning_candidate_summary)
        
        




#use open and w to write the data to this file
with open(file_to_save, "w") as txt_file:
    #print Final Vote Count
    election_results =(
        f"\nElection Results\n"
        f"--------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------\n"
    )
    print(election_results, end="")
    #save to text file
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        #retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        vote_percentages = float(votes)/float(total_votes)*100
        
        candidate_results = (f"{candidate_name}: {vote_percentages:.1f}% ({votes:,}) \n")
        txt_file.write(candidate_results)
    txt_file.write(winning_candidate_summary)
    