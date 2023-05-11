
import string
import csv
import pathlib


from pathlib import Path

csvPath = Path("Resources/budget_data.csv")


with open(csvPath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    

    #initializing the variables
    total=0
    total_rows = 0
    totalchange_rows = 0
    diff=0
    total_diff = 0
    max_profit = 0
    min_profit = 0
#The total number of months included in the dataset
    for row in csvreader:
        total +=int(row[1])
        total_rows +=1
        current_plvalue = float(row[1])

  # The net total amount of "Profit/Losses" over the entire period     
        if total_rows > 1:
            diff = current_plvalue-prev_plvalue

#The changes in "Profit/Losses" over the entire period, and then the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period

            if diff > 0 and diff > max_profit: 
                max_profit = int(diff)
                max_profit_date = row[0]
                
            if diff < 0 and diff < min_profit:
                min_profit = int(diff)
                min_profit_date = row[0]
                
            total_diff += diff
            totalchange_rows +=1
            prev_plvalue = current_plvalue

        else:
            prev_plvalue = float(row[1])

   #formatting the average_change to decimal place
        
    Average_change=round(total_diff/totalchange_rows,2)
    
#printing the results
    outputFile = open('analysis/pybank.txt', 'w')
    print("Financial Analysis", file = outputFile)
    print("-----------------------------", file = outputFile)
    print("Total Months :",total_rows, file = outputFile)
    print("Total :","$",total, file = outputFile)  
    print("Average Change : ","$",Average_change, file = outputFile )
    print("Greatest Increase in Profits : ",max_profit_date,"( $",max_profit,")", file = outputFile)
    print("Greatest Decrease in Profits : ",min_profit_date,"( $",min_profit,")", file = outputFile)
  


outputFile.close()


  