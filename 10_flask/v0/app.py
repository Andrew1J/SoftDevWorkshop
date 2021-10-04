# The Best Team: Andrew Juang, Alif Abdullah, Joshua Kloepfer
# SoftDev
# Oct 2021

from flask import Flask
app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q3: Will this appear anywhere? How u know?

app.run()  # Q4: Where have you seen similar construcs in other languages?

# Same code as app.py from K09. Creates instance of flask app and prints
# __name__ into the terminal. At http://127.0.0.1:5000/, the function prints
# "No hablo queso!"

# Results
# Works as expected!
