import os
import csv


file_path = os.path.join("PyBank", "Resources", "budget_data.csv")
print(file_path)

# reading the file

with open(file_path,"r") as data:
    data_read = csv.reader(data)
    data_read = list(data_read)

#pulling data for the column
data_read = data_read[1:]
#find total of months and profit/loss
total_months = len(data_read)

total_amount = 0 
for single_list in data_read:
    total_amount = total_amount + int(single_list[1])

print(total_months)
print(total_amount)

total_change = 0
min_change = 0
max_change = 0 

for i in range(1, len(data_read)):   
    current_change =int(data_read[i][1]) - int(data_read[i-1][1])
    total_change = total_change + current_change

    if current_change > max_change:
        max_change = current_change
        max_index = i

    if current_change < min_change:
        min_change = current_change 
        min_index = i





avg_change = total_change / (len(data_read) -1)
avg_change = round(avg_change, 2)
print(avg_change)
print(min_change)
print(max_change)

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(total_amount))
print("Average Change: $" + str(avg_change))
print("Greatest Increase in Profits: " + data_read[max_index][0] + " ($" + str(max_change) + ")")
print("Greatest Decrease in Profits: " + data_read[min_index][0] + " ($" +  str(min_change) + ")")



    