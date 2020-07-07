#Project Goals (The data we need to retrieve):
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote

#Code To-Do List
# 1. Open the data file.
# 2. Write down the names of all the candidates.
# 3. Add a vote count for each candidate.
# 4. Get the total votes for each candidate.
# 5. Get the total votes cast for the election.

#Coding Assignment Start
# 1. Add our dependencies.
import csv
import os
# 2. Assign a variable for the file to load and the path.
file_to_load = os.path.join ("Resources", "election_results.csv")

# 3. Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 4. Open the election results and read the file.
with open(file_to_load) as election_data:

# 5. To do: read and analyze the data here.
    # 1. Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # 2. Read and print the header row.
    headers = next(file_reader)
    print(headers)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:

# Write three counties to the file (method one).
    #txt_file.write("Arapahoe\n")
    #txt_file.write("Denver\n")
    #txt_file.write("Jefferson")

# Write three counties to the file (method two).
    #txt_file.write("Arapahoe, Denver, Jefferson")
#Alternate for code above:
    #txt_file.write("Arapahoe\nDenver\nJeferson")

#SkillDrill
    txt_file.write("Counties in the Election\n")
    txt_file.write("------------------------\n")
    txt_file.write("Arapahoe\n")
    txt_file.write("Denver\n")
    txt_file.write("Jefferson")
