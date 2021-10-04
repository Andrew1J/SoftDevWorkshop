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

app.debug = True
app.run()

# This app version is the same as v2 except for the app.debug=True line. We expect
# that some debugger will actively reload our program upon code change.

# Results
# In the terminal after you go to the website in the terminal it says Debugger
# is active! and gives a debugger pin. When we change code, the program auto reloads
# as expected. 
