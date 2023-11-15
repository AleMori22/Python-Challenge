import os

import csv

dataset = r'PyBank\Resources\budget_data.csv'

Nmonth = 0
Total = 0
Min = 0
Max = 0

with open(dataset, 'r') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     header = next(csvreader)
     
     for row in csvreader:
          Nmonth = Nmonth+1
          Total = Total + int(row[1])
          
          if int(row[1]) <= Min:
              Min=int(row[1])
              Name_min = row[0]

          if int(row[1]) >= Max:
              Max = int(row[1])
              Name_max = row[0]

Average = Total/Nmonth


print('Financial Analysis')

print('-------------------------')

print('Total Months: ', Nmonth)

print('Total: $', Total )

print('Average: $', round(Average, 2))

print('Greatest Increase in Profits: ',Name_max, ' ($', Max,')')

print('Greatest Decrease in Profits: ', Name_min , ' ($', Min,')')

budget_results = r'PyBank\Analysis\budget_results.txt'

with open(budget_results, 'w') as txtfile:
     
     txtfile.write('Financial Analysis')
     txtfile.write('\n')
     
     txtfile.write('-------------------------')
     txtfile.write('\n')
     
     txtfile.write(f'Total Months: {str(Nmonth)}')
     txtfile.write('\n')
     
     txtfile.write(f'Total: $  {str(Total)}')
     txtfile.write('\n')
     
     txtfile.write(f'Average: $ {round(Average, 2)}')
     txtfile.write('\n')

     txtfile.write(f'Greatest Increase in Profits: {str(Name_max)} ($ {str(Max)})')
     txtfile.write('\n')

     txtfile.write(f'Greatest Decrease in Profits: {str(Name_min)} (${str(Min)})')