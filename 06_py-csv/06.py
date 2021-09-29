# The Best Team: Andrew Juang, Alif Abdullah, Joshua Kloepfer
# SoftDev
# K06 -- Weighted Occupation Picker
# 2021-9-28

import csv
import random

finalDict = {}

def randomJob(reader):
        # Pick some random int x (0,1000)
        x = random.randint(0, 1000)
        y = 0

        # Find where the x falls in the class/job intervals
        for i in reader:
                y += reader[i] * 10
                if (y > x):
                        print(i)
                        break

# Read in CSV file
with open('occupations.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
                finalDict[row['Job Class']] = float(row['Percentage'])

randomJob(finalDict)
