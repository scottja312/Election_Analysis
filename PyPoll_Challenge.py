# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Initialize candidate options and candidate votes.
candidate_options = []
candidate_votes = {}

# Challenge assignment - intialize county options and county votes list.
county_names = []
county_votes = {} 

# Initiaize variables to track the winning candidate, vote count, and percentage of votes.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Challenge assignment: track the largest county vote turnout and its percentage.
largest_county_turnout = ""
largest_county_votes = 0

# Read the csv file and convert into a county list of dictionaries.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    #print(headers)
    
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count as it loops through each row.
        total_votes += 1
        # Get the candidate name from each row in index 2 column.
        candidate_name = row[2]
        # Get the county name from each row in index 1 column.
        county_name = row[1]

        # If the candidate does not match any existing candidate, add the
        # to the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            #Initialize variable to begin tracking the candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a candidate vote count to each candidate's name.
        candidate_votes[candidate_name] += 1

        #Challenge assignment: create a list for counties.
        if county_name not in county_names:
            #Challenge-assignment : add county names to the list.
            county_names.append(county_name)

            # Track the candidate voter count.
            county_votes[county_name] = 0
        county_votes[county_name] += 1

# Save the election results to the text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count.
    election_results = (
        f"\nElection Results"
        f"\n-------------------\n"
        f"Total Votes: {total_votes:,}"
        f"\n-------------------\n\n"
        f"County Votes:\n"
    ) 
    print(election_results, end="")
    txt_file.write(election_results)
        

    # Challenge Assignment - Save the final county vote count to the text file.
    for county in county_votes:
        #Retrieve vote count and and vote percentage.
        county_vote = county_votes[county]
        county_percent = int(county_vote) / int(total_votes) * 100
        county_results = (
            f"{county}: {county_percent:.1f}% ({county_vote:,})\n"
        )
        print(county_results, end="")
        txt_file.write(county_results)

        # Determine the winning vote count and candidate
        if(county_vote > largest_county_votes): 
            largest_county_votes = county_vote
            largest_county_turnout = county

    # Print the county with the largest voter turnout.
    largest_county_turnout = (
        f"\n-----------------------------\n"
        f"Largest County Turnout: {largest_county_turnout}\n"
        f"--------------------------------\n"
    )
    print(largest_county_turnout)
    txt_file.write(largest_county_turnout)
    
    #Retrieve candidate vote count and percentage of votes candidates received.
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)