# The Best Team: Andrew Juang, Alif Abdullah, Joshua Kloepfer
# SoftDev
# Oct 2021

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()

# Same as V0 but there is a missing print(__name__) statement, so we expect
# that the flask app will not print to terminal.

# Results
# Works as expected, prints "No hablo queso!" to the webpage but does not print
# __main__ to the terminal.
