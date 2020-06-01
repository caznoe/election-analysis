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

# Initialize county list.
county_options = []

# Initialize county vote count.
county_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# County vote count tracker
highest_county_turnout = ""
highest_county_count = 0
highest_county_percentage = 0

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
        
        # Print county name from each row and add to options
        county_name = row[1]
        
        # If the candidate does not match any existing canidate,
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Track candidate's vote count
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        
        # If the county does not match any existing county,
        if county_name not in county_options:
            # Add it to the list of counties.
            county_options.append(county_name)
            # Track county's vote count
            county_votes[county_name] = 0
        # Add a vote to that candidate's count.
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    #Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"--------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------\n\n"
        f"County Votes:\n")
    print (election_results, end="")
    #Save the final vote count to the text file.
    txt_file.write(election_results)        
    
    # Determine the percentage of votes for each county by looping through the counts.
    for county in county_votes:
        # Retrive vote count of a county
        county_vote = county_votes[county]
        # Calculate the percentage of votes by county.
        county_vote_percentage = int(county_vote) / int(total_votes) * 100
        # Print the county name and county percentage of votes.
        county_results = (f"{county}: {county_vote_percentage:.1f}% ({county_vote:,})\n")
        print (county_results, end = "")
        txt_file.write(county_results)       
    # Determine the largest county turnout with vote count and percentage.
        # Determine if the county votes are greater than the largest county count.
        if (county_vote > highest_county_count) and (county_vote_percentage > highest_county_percentage):
            # If true, then set highest_county
            highest_county_count = county_vote
            highest_county_percentage = county_vote_percentage
            highest_county = county
# Print out highest county summary.
    highest_county_summary = (
        f"----------------------\n"
        f"Largest County Turnout: {highest_county}\n"
        f"-----------------------\n")
    print(highest_county_summary)
    txt_file.write(highest_county_summary)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate in candidate_votes:
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate]
        # Calculate the percentage of votes.
        vote_percentage = int(votes) / int(total_votes) * 100
        # Print the candidate name and percentage of votes.
        candidate_results = (f"{candidate}: {vote_percentage: .1f}% ({votes:,})\n")
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
