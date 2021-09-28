# Andrew Juang
# SoftDev
# K06 Reading in CSV File
# 2021-09-28

import csv

file = open("occupations.csv")
lines = csv.reader(file)
next(lines)

OCCUPATIONS = {}
for line in lines:
    OCCUPATIONS[line[0]] = float(line[1])
print(OCCUPATIONS)
