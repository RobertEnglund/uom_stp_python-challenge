# py file 
import os
import csv

# specify path to input file
input_filepath = os.path.join('.', 'Resources', 'budget_data.csv')
output_filepath = os.path.join(".", "Analysis", "results.csv")

# Analyze the records from budget_data input to calculate each of the following:
#  * The total number of months included in the dataset
#  * The net total amount of "Profit/Losses" over the entire period
#  * The average of the changes in "Profit/Losses" over the entire period
#  * The greatest increase in profits (date and amount) over the entire period
#  * The greatest decrease in losses (date and amount) over the entire period
#
#  Assumptions
#  * One input record per month (i.e. record count = count of months)

# initialize working variables
total_months = 0
net_amount = 0
greatest_increase_amt = 0
greatest_increase_month =""
greatest_decrease_amt = 0
greatest_decrease_month = ""


with open(input_filepath) as budgetfile:

    csvreader = csv.reader(budgetfile, delimiter=',')

    # Read past the header 
    budget_header = next(csvreader)
    #print(f"Budget Header: {budget_header}")

    # for each row from the budget input file
    for row in csvreader:
        # increment count of months (records)
        total_months = total_months + 1

        input_amt = int(row[1])
        # accumulate total amount of profits/losses
        net_amount = net_amount + input_amt
        # check for greatest increase
        if greatest_increase_amt < input_amt:
            greatest_increase_month = row[0]
            greatest_increase_amt = input_amt
        # check for greatest decrease
        if greatest_decrease_amt > input_amt:
            greatest_decrease_month = row[0]
            greatest_decrease_amt = input_amt
    
    # after reading all rows, calculate average change in profits/losses
average_change = net_amount / total_months

line_1 = "Total Months: " + str(total_months)
line_2 = "Total: $" + '{:,.0f}'.format(net_amount)
line_3 = "Average Change: $" + '{:,.2f}'.format(average_change)
#line_3 = "Average Change: $" + str(round(average_change,2))
line_4 = "Greatest Increase in Profits: " + greatest_increase_month + " ($" + '{:,.0f}'.format(greatest_increase_amt) + ")"
line_5 = "Greatest Decrease in Profits: " + greatest_decrease_month + " ($" + '{:,.0f}'.format(greatest_decrease_amt) + ")"

# print results to terminal
print (line_1)
print (line_2)
print (line_3)
print (line_4)
print (line_5)

# write results to output file
with open(output_filepath, 'w', newline='') as analysisfile:

    # Initialize csv.writer
    csvwriter = csv.writer(analysisfile)

    # write results 
    csvwriter.writerow([line_1])
    csvwriter.writerow([line_2])
    csvwriter.writerow([line_3])
    csvwriter.writerow([line_4])
    csvwriter.writerow([line_5])

