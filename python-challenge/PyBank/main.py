#import pandas as pd

import os
import csv

# importing bank file
budget_csv = './Resources/budget_data.csv'
#budget_df = pd.read_csv(file)
#budget_df.head()
total_months = 0
net_amount = 0
change = []
total_change = 0
max_profit = 0
min_profit = 0
dates = []
with open(budget_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row_list in csvreader:
        total_months += 1
        net_amount += int(row_list[1])
        date = row_list[0]
        dates.append(date)
        if total_months == 1:

            initial = int(row_list[1])
        else:
            diff = int(row_list[1])-initial
            change.append(diff)
            initial = int(row_list[1])
    for index,item in enumerate(change):
        total_change += item
        if item >  max_profit:
            max_profit = item
            max_date = index
        if item < min_profit:
            min_profit = item
            min_date = index
    avg_chg = round(total_change / len(change),2)
    


print(f'''
Financial Analysis
----------------------------------------------------
  Total Months: {total_months}
  Total: ${net_amount}
  Average  Change: ${avg_chg}
  Greatest Increase in Profits: {dates[max_date+1]} (${max_profit})
  Greatest Decrease in Profits: {dates[min_date+1]} (${min_profit})


''')

with open('./analysis/financials.txt','w') as file:
    file.write(f'''
Financial Analysis
----------------------------------------------------
  Total Months: {total_months}
  Total: ${net_amount}
  Average  Change: ${avg_chg}
  Greatest Increase in Profits: {dates[max_date+1]} (${max_profit})
  Greatest Decrease in Profits: {dates[min_date+1]} (${min_profit})



''')
