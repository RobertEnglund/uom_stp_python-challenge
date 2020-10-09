# py file 
import os
import csv

# specify path to input file
input_filepath = os.path.join('.', 'Resources', 'election_data.csv')
output_filepath = os.path.join(".", "Analysis", "election_analysis.csv")

# Analyze the records from election_data input to calculate each of the following:

# * The total number of votes cast
# * A complete list of candidates who received votes
# * The percentage of votes each candidate won
# * The total number of votes each candidate won
# * The winner of the election based on popular vote.

# initialize working variables
total_votes = 0
found_count = 0
not_found_count = 0
winner = ""
winning_tally = 0
pct_total = 0.0
vote_tallies = {}


with open(input_filepath) as electionfile:

    csvreader = csv.reader(electionfile, delimiter=',')

    # Read past the header 
    election_header = next(csvreader)
    #print(f"Election Header: {election_header}")

    # for each row from the budget input file
    for row in csvreader:

        # count total votes
        total_votes = total_votes + 1
        candidate = row[2]

        # count votes by candidate
        if row[2] not in vote_tallies:
            vote_tallies[row[2]] = 1
            not_found_count = not_found_count + 1
        else:
            vote_tallies[row[2]] = vote_tallies[row[2]] + 1
            found_count = found_count + 1


# write results to output file
with open(output_filepath, 'w', newline='') as analysisfile:

    # Initialize csv.writer
    csvwriter = csv.writer(analysisfile)

    # write results to terminal and to output file
    line = "Election results"
    csvwriter.writerow([line])
    print (line)

    line = "------------------------"
    csvwriter.writerow([line])
    print (line)

    display_total = '{:,.0f}'.format(total_votes)
    line = "Total votes: " + display_total 
    csvwriter.writerow([line])
    print (line)

    line = "------------------------"
    csvwriter.writerow([line])
    print (line)

    # calc percent total for all candidates and identify winner
    for name in vote_tallies:
        if vote_tallies[name] > winning_tally:
            # current candidate has most votes
            winning_tally = vote_tallies[name]
            winner = name

        # calc percent of total votes for current candidate
        pct_total = (vote_tallies[name] / total_votes) * 100
        display_tally = '{:,.0f}'.format(vote_tallies[name])
        display_pct = '{:,.1f}'.format(pct_total)

        # write results for current candidate
        line = name + ": " + display_pct + "% (" + display_tally + ")"
        csvwriter.writerow([line])
        print (line)

    # write winner
    line = ("------------------------")
    csvwriter.writerow([line])
    print (line)

    line = "Winner: " + winner
    csvwriter.writerow([line])
    print (line)

    line = ("------------------------")
    csvwriter.writerow([line])
    print (line)

