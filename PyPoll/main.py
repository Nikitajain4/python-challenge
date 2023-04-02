import random
import string
import csv
import pathlib


from pathlib import Path

csvPath = Path("Resources/election_data.csv")


with open(csvPath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    total_rows = 0
    
    candidate_list = []
    percentage_of_votes = 0
    winner = 0
    for row in csvreader:
#The total number of votes cast 
        total_rows +=1
 # A complete list of candidates who received votes  
     
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
    print("Election Results")
    print("-------------------------")
    print("Total Votes :",total_rows)
    print("-------------------------")   

 # The percentage of votes each candidate won

#The total number of votes each candidate won    
    for candidate_index in range(len(candidate_list)):
        votes = 0  
        csvfile.seek(0)   

        for row in csvreader:

            if str(candidate_list[candidate_index]) == str(row[2]):
                votes +=1    
   
        percentage_of_votes=round(votes/total_rows*100,3,)
        
#The winner of the election based on popular vote
        if votes > winner :
          winner = votes
          winner_name = (str(candidate_list[candidate_index]))
          
# printing the results
        print ((str(candidate_list[candidate_index])),percentage_of_votes,"%","(",votes,")") 

    print("-------------------------") 
    print("Winner : ",winner_name)   
    print("-------------------------") 
