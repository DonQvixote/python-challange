#Import the module needed to read csv files and OS to be able to work with different operative systems
import os
import csv

#Declare the path in which the csv is saved
budget_csv = os.path.join(".", "Resources", "budget_data.csv") 

#define the lists that will be used later
months=[]
profit_loss_list=[]

#read the csv file and stablish a pointer for the rows
with open(budget_csv) as csvfile:
    csvpointer = csv.reader(csvfile, delimiter=",")

    header=next(csvpointer) #store the header and remove it from the iteration

    for row in csvpointer:
        months.append(row[0]) #iterate in the csv file and append the months which are located in the first(0) positions of each row

        profit_loss_list.append(float(row[1])) #iterate in the csv file and append the Profits/Losses which are located in the second(1) position of each row
                                               #it's necessary to convert to float to be able to perform mathematical operations with the list


#The algebraic addition of the profits and losses will be the net amount of Profits/Losses for the entire period
profit_loss_sum = sum(profit_loss_list)

#define a list which will store the values of the monthly changes in Profits/Losses
changes=[]

for x in range(0,len(profit_loss_list)-1): #iterate in the range 0 to the number of data points in the list minus one beacause the first month wont be compared to a previous one
    change=profit_loss_list[(x+1)]-profit_loss_list[x] #compare the value of Profits/Losses of each month to the next one 
    changes.append(change) #store the result in the previously defined list
    
#calculate the average change for the entire period
average = sum(changes)/len(changes)

#locate the value for the max increase in profits
gincrease = max(changes)

#locate the index for the month with the greatest increase in profits please note that it's necessary to add one to the index 
# because the changes in profits/losses list has one less value then the months list
gincrease_month_index = changes.index(max(changes))+1 

#determine the month of the greatest positive change
month_increase = months[gincrease_month_index]

#repeat the process but for the greatest decrease
gdecrease = min(changes)
gdecrease_month_index = changes.index(min(changes))+1
month_decrease = months[gdecrease_month_index]

#define a list with the results to be printed and exported
lines=[
    '',
    'Financial Analysis',
    '-'*55,
    '',
    f'Total Months: {len(months)}',#The number of items in the months list will be the number of months for the analysis
                                   #Please note that the header is not being counted
    f'Total: ${profit_loss_sum}',
    f'Average Change: ${average:.2f}',
    f'Greatest Increase in Profits: {month_increase} (${gincrease})',
    f'Greatest Decrease in Profits: {month_decrease} (${gdecrease})' 
    ]
#iterate through, printing each item of the list
for line in lines:
    print(line)

#determine the output path in which the results will be exported
outputpath= os.path.join('.','analysis','Results.txt')

#iterate in the list writing each of the items in a txt file
with open(outputpath,'w',encoding='utf-8') as f:
    for line in lines:
        f.write(line)
        f.write('\n') #indicates that a new line will be created otherwise all the strings would go in one line
    