import os
import csv

csvpath = os.path.join("Resources/budget_data.csv")

# create a python script that analyzes the records to calculate each of the following:

#The total number of months included in the dataset

#The net total amount of Profit/Losses over the entire period

#Calculate the changes in Profit/Losses over the entire period, then find the average of those changes


#the greatest increase in profits (data and amount) over the entire period

#The greatest decrease in losses (date and amount) over the entire period



with open(csvpath, 'r', encoding = 'utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)



