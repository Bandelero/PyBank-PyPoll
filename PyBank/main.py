import os
import csv

#Variable used for storing the months
date = []
#Variable used for storing the profit/losses values
profit_losses = []
#Variable for storing the difference between the row and next row below
#There should be 85 values
monthly_changes = []

#Line for reading a file
budget_data = os.path.join("Resources/budget_data.csv")

#First two lines to print as stated in instructions
print("Financial Analysis")
print("---------------------")


# Read in the CSV file
with open(budget_data, 'r') as csvfile:

	
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    #Skip header row when reading
    header = next(csvreader)
    #Append month and profit losses into the empty lists of above.
    for row in csvreader:
    	date.append(row[0])
    	profit_losses.append(int(row[1]))
#Now that we have lists of date variables and profit/loss values, we can manipulate that data.   	

#This loop calculates the changes in "Profit/Losses" over the entire period
#We are taking into account that there are 85 values in the monthly_changes list
for i in range(len(profit_losses)-1):
	previous_row = profit_losses[i]
	next_row = profit_losses[i+1]
	#monthly_change = 0
	profit_loss_avg_change = next_row - previous_row
	monthly_changes.append(profit_loss_avg_change)
'''
	if(previous_row < next_row ) & (previous_row > 0) & (next_row > 0 ):
		monthly_change = next_row - previous_row
		monthly_changes.append(monthly_change)
	elif(previous_row > next_row ) & (previous_row > 0) & (next_row > 0 ):
		monthly_change = next_row - previous_row
		monthly_changes.append(monthly_change)	
	elif(previous_row > next_row ) & (previous_row > 0) & (next_row < 0 ):
		monthly_change = next_row - previous_row
		monthly_changes.append(monthly_change)
	elif(previous_row < next_row ) & (previous_row < 0) & (next_row > 0 ):
		monthly_change = next_row - previous_row
		monthly_changes.append(monthly_change)
	elif(previous_row < next_row ) & (previous_row < 0) & (next_row < 0 ):
		monthly_change = next_row - previous_row
		monthly_changes.append(monthly_change)  
	elif(previous_row > next_row ) & (previous_row < 0) & (next_row < 0 ):
		monthly_change = next_row - previous_row
		monthly_changes.append(monthly_change)
'''
#This function finds the average of the values in the monthly_changes list and rouncs by 2 decimals
def Average(monthly_changes):
	return sum(monthly_changes) / len(monthly_changes)

changes = round(Average(monthly_changes),2)

#Variables for greatest increase in profits & greatest decrease in losses
max_value = max(monthly_changes)
min_value = min(monthly_changes)

#Print to terminal
print(f'Total Months: {len(date)}')
print(f'Total: ${sum(profit_losses)}')
print(f'Average  Change: ${changes}')

#This loop goes through the date and monthly_changes list and prints the month associated with the greatest increase and decrease values
for (month_value, avg_value) in zip(date, range(len(monthly_changes)+1)):
	new_avg_value = monthly_changes[avg_value-1]
	if(max_value == new_avg_value):
		print(f'Greatest Increase in Profits: {month_value} ({max_value})')
	if(min_value == new_avg_value):
		print(f'Greatest Decrease in Profits: {month_value} ({min_value})')



#write to text file
output_path = os.path.join("textOutput.txt")

with open(output_path, 'w', newline='') as csvfile:

	csvwriter = csv.writer(csvfile, delimiter=',')

	#Similar to printing to the terminal
	csvwriter.writerow(['Financial Analysis'])
	csvwriter.writerow(['---------------------'])

	# %s' % found on stack overflow
	csvwriter.writerow(['Total Months: %s' % len(date)])
	csvwriter.writerow(['Total: $%s' %  sum(profit_losses)])
	csvwriter.writerow(['Average Change: $%s' % changes])

	for (month_value, avg_value) in zip(date, range(len(monthly_changes)+1)):
		new_avg_value = monthly_changes[avg_value-1]
		if(max_value == new_avg_value):
			csvwriter.writerow(['Greatest Increase in Profits: %s' % (month_value), (max_value)])
		if(min_value == new_avg_value):
			csvwriter.writerow(['Greatest Decrease in Profits: %s' % (month_value), (min_value)])





