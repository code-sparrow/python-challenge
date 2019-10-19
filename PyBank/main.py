#----Modules----
import os
import csv

#----Set path for file (works with Resources folder in same directory as main.py)----
csv_path = os.path.join(".", "Resources", "budget_data.csv")

#----Open the CSV----
with open(csv_path, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    #skip and store header
    header = next(csv_reader) 
    
    #skip and store first line of data
    first_line = next(csv_reader)
    
#----Initialize variables after moving past first line of data and header----
    
    #to accumulate total sum of profit and loss 
    net_total = int(first_line[1])
    
    #dummy to calculate change in for loop
    change = 0
    
    #an empty list to collect changes in profit/loss from one month to the previous
    change_list = []
    
    #an empty list to collect the month corresponding to change
    date_of_change = []
    
    #list that will allow easy access to previous month
    profit_loss_list = [int(first_line[1])]
    
#----Iterate over each row in the csv file to collect the needed lists---
    #and to calculate the needed values
    for row in csv_reader:
        
        #accumulates total sum of profit/loss
        net_total += int(row[1])
        
        #calculate change in profit/loss relative to previous month
        #  (previous month is at end of profit_loss_list for each iteration)
        change = int(row[1]) - profit_loss_list[-1]
        
        #collecting changes into a list
        change_list.append(change)
        
        #collecting the corresponding month of the change
        #     (chosen as new date, not previous)
        date_of_change.append(row[0])
        
        #adding to profit_lost_list for new "previous-month" in next iteration
        profit_loss_list.append(int(row[1]))

#----Final calculations after csv read loop----

#number of months is the final number of lines, minus the header
#   (just used csvreader's built in line counter)
months = csv_reader.line_num - 1

#net_total was accumulated in for loop

#average of the changes in "Profit/Losses"
average_change = sum(change_list)/len(change_list)

#greatest increase and decrease in profits (date and amount)
greatest_inc = max(change_list)
month_inc = date_of_change[change_list.index(greatest_inc)]
greatest_dec = min(change_list)
month_dec = date_of_change[change_list.index(greatest_dec)]

#----Print to terminal----
print("Financial Analysis")
print("----------------------------")
print("Total Months: %d" % months)
print("Total: $%d" % net_total)
print("Average Change: $%.2f" % average_change)
print("Greatest Increase in Profits: %s ($%d)" % (month_inc, greatest_inc))
print("Greatest Decrease in Profits: %s ($%d)" % (month_dec, greatest_dec))

#----Write to txt file----
with open("output.txt", 'w') as txt_file:
    print("Financial Analysis", file=txt_file)
    print("----------------------------", file=txt_file)
    print("Total Months: %d" % months, file=txt_file)
    print("Total: $%d" % net_total, file=txt_file)
    print("Average Change: $%.2f" % average_change, file=txt_file)
    print("Greatest Increase in Profits: %s ($%d)" % (month_inc, greatest_inc), file=txt_file)
    print("Greatest Decrease in Profits: %s ($%d)" % (month_dec, greatest_dec), file=txt_file)
