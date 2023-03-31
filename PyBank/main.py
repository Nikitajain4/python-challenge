import random
import string
import csv
import pathlib


from pathlib import Path

csvPath = Path("Resources/budget_data.csv")


with open(csvPath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    

    
    total=0
    total_rows = 0
    totalchange_rows = 0
    diff=0
    total_diff = 0
    max_profit = 0
    min_profit = 0

    for row in csvreader:
        total +=int(row[1])
        total_rows +=1
        current_plvalue = float(row[1])
        
        if total_rows > 1:
            diff = current_plvalue-prev_plvalue

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
        
    Average_change=round(total_diff/totalchange_rows,2)
    

    print("Financial Analysis")
    print("-----------------------------")
    print("Total Months :",total_rows)
    print("Total :","$",total)  
    print("Average Change : ","$",Average_change )
    print("Greatest Increase in Profits : ",max_profit_date,"( $",max_profit,")")
    print("Greatest Decrease in Profits : ",min_profit_date,"( $",min_profit,")")
  



  