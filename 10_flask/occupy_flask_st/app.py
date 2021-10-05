'''
The Best Team - Alif Abdullah, Andrew Juang, Joshua Kloepfer
SoftDev
K10 -- To review several iterations of a flask app, and to make our own flask app that displays the results of the random occupation picker code we wrote.
2021-10-04
'''

import csv
import random
from flask import Flask

# Declaration of dictionary to store CSV File contents
finalDict = {}
# Create instance of flask app
app = Flask(__name__)

# Read in CSV file
def fileReader():
    with open('occupations.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            finalDict[row['Job Class']] = float(row['Percentage'])

# Choose random job from dictionary
def randomJob(reader):
    x = random.randint(0, 1000)
    y = 0
    for i in reader:
        y += reader[i] * 10
        if y > x:
            return i
            break

# Running the flask app with displayApp function
@app.route("/")
def displayApp():
    fileReader()
    return ("The Best Team -- Alif Abdullah, Andrew Juang, Joshua Kloepfer <br><br>List of occupations: <br>" +
        str(list(finalDict.keys())[:len(list(finalDict.keys()))-1]) +
        "<br><br>Chosen Occupation: " + str(randomJob(finalDict)))

app.debug = True
app.run()
