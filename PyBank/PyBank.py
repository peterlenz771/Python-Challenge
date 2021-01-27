#Dependencies
import os
import csv

#Name Variables
date = []
money = []

sum_total = 0

#Reading csv
with open('Resources/budget_data.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
#Looping through Data
    for row in csvreader:
        date.append(row[0])
        money.append(int(row[1]))
        sum_total += float(row[1])
        print(row)



#total months
months = len(date)

#Finding the greatest increase and decrease
increase=money[0]
decrease=money[0]

for i in range(len(money)):
    if money [i]>=increase:
        increase=money [i]
        increase_month =date[i]
    elif  money[i] <= decrease:
        decrease = money[i]
        decrease_month = date[i]
    else:
        print('Increase/Decrease')

#Average of those changes
avg_money = round(sum_total/months, 2)

#Print statements
with open('output_financial.txt', "w", newline = '') as textfile:
    print("Financial Analysis", file = textfile)
    print("------------------------------------", file = textfile)
    print(f'Total Months: {months}', file = textfile)
    print(f'Total Revenue: ${sum_total}', file = textfile)
    print(f'Average Profit/Loss Change: ${avg_money}', file = textfile)
    print(f'Greatest Increase Profit/Loss: {increase_month}(${increase})', file = textfile)
    print(f'Greatest Decrease Profit/Loss: {decrease_month}(${decrease})', file = textfile)
    print("------------------------------------", file = textfile)

with open('output_financial.txt', newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    for row in csvreader:
        print(row)
