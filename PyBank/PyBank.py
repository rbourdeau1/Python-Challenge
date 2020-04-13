# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# find csv file
budget_path = os.path.join('Resources', 'budget_data.csv')

# Read in the CSV file
with open(budget_path) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    # Determine the total number of months included in the dataset
    month_list = []
    profit_list = []
    profit_shift_list = []
        
    for row in csvreader:
        # print(row)
        if row != "":
            month_list.append(row[0])
            profit_list.append(int(row[1]))
            profit_shift_list.append(int(row[1]))
            
profit_shift_list.pop(0)

# print(profit_list)
# print(profit_shift_list)

change_list = []

#iterate through each item in list but end before the last row
for i in range(len(profit_list)-1):
    change=profit_shift_list[i]-profit_list[i]        
    change_list.append(change)
        # print(change)

# print(change_list)
 # print(profit_list[1])
    # print(profit_shift_list)

total_months = len(month_list)
total_profits = sum(profit_list)
average_change = round(sum(change_list)/len(change_list),2)
max_increase = max(change_list)
max_decrease = min(change_list)
max_increase_month = month_list[change_list.index(max_increase)+1]
max_decrease_month = month_list[change_list.index(max_decrease)+1]

output = f"""Financial Analysis
---------------------------------------------------
Total Months: {total_months}
Total: ${total_profits}
Average Change: ${average_change}
Greatest Increase in Profits: {max_increase_month} (${max_increase})
Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})"""
print(output)

# Specify the file to write to
output_path = os.path.join("pybank_results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:
    txtfile.write(output)

   
# print("Financial Analysis")
# print("---------------------------------------------------")

# print(f'Total Months: {total_months}')
# # # Calculate the net total amount of "Profit/Losses" over the entire period
# print(f'Total: ${total_profits}')

# # # Calculate the average of the changes in "Profit/Losses" over the entire period
# print(f'Average: ${average_change}')
# # # Calculate the greatest increase in profits (date and amount) over the entire period
# print(f'Greatest Increase in Profits: ${max_increase}')
# # # Calculate The greatest decrease in losses (date and amount) over the entire period
# print(f'Greatest Decrease in Profits: ${max_decrease}')
# Print results

# Create and export a text file with results

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)