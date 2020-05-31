#The data we need to retrieve from voting data.
#Add our dependencies.
import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Create a filename variable to a direct or indirect path to the file. 
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Initialize candidate list.
candidate_options = []

# Initialize candidate vote count.
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Using the open() function with the "r" mode to open a file and read the data.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Read the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        
        # Print candidate name from each row and add to options
        candidate_name = row[2]
        
        # If the candidate does not match any existing canidate,
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Track candidate's vote count
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

#Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"--------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------\n")
    print (election_results, end="")
    #Save the final vote count to the text file.
    txt_file.write(election_results)        

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate in candidate_votes:
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate]
        # Calculate the percentage of votes.
        vote_percentage = int(votes) / int(total_votes) * 100
        # Print the candidate name and percentage of votes.
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        # Save the candidate rsults to our text file.
        txt_file.write(candidate_results)
    # Determine winning vote count and candidate
        # Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # Set the winning_candidate equal to teh candidate's name.
            winning_candidate = candidate

    # Print out winning candidate summary.
    winning_candidate_summary = (
        f"-----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
