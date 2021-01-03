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

#open election results and read file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    #read and print headers
    headers = next(file_reader)
    print(headers)








#use open and w to write the data to this file
with open(file_to_save, "w") as txt_file:

    #wrrite to
    txt_file.write("Arapahoe\nJefferson\nDenver")