# First we'll import the necessary modules
import os   # This will allow us to create file paths across operating systems
import csv  # This will allow us to read from and write to csv files

# Indicate the location and filename of the csv file and assign it to a variable
budget_path = os.path.join('Resources', 'budget_data.csv')

# Read in the CSV file
with open(budget_path) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    # Create a list of months, profits and another list to store profits
    month_list = []
    profit_list = []
    profit_shift_list = []  # This list is the same as profit_list but we will remove the first item.
                            # We will use this list to calculate change in profits
        
    for row in csvreader:
        month_list.append(row[0])
        profit_list.append(int(row[1]))
        profit_shift_list.append(int(row[1]))
            
# Calculate the change in profits and put it in a list

profit_shift_list.pop(0)    # Removed the first item in the list
change_list = []

# Calculate the change in profits
for i in range(len(profit_list)-1):
    change=profit_shift_list[i]-profit_list[i]        
    change_list.append(change)
        
# Calculate Total Months, Profits, Average Change, Max and Min Profits
total_months = len(month_list)
total_profits = sum(profit_list)
average_change = round(sum(change_list)/len(change_list),2)
max_increase = max(change_list)
max_decrease = min(change_list)
max_increase_month = month_list[change_list.index(max_increase)+1]
max_decrease_month = month_list[change_list.index(max_decrease)+1]

# Print our results
output = f"""Financial Analysis
---------------------------------------------------
Total Months: {total_months}
Total: ${total_profits}
Average Change: ${average_change}
Greatest Increase in Profits: {max_increase_month} (${max_increase})
Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})"""
print(output)

# Write our results to a text file
# Specify the file to write to
output_path = os.path.join("pybank_results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:
    txtfile.write(output)
