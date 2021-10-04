# The Best Team: Andrew Juang, Alif Abdullah, Joshua Kloepfer
# SoftDev
# Oct 2021

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.run()

# There are two print statements, so when you go to the website it will print the
# first string and __name__ in succession.

# Results
# Works as predicted. Prints both the string and __name__ in the terminal when
# the website is loaded.
