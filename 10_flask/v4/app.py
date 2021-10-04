# The Best Team: Andrew Juang, Alif Abdullah, Joshua Kloepfer
# SoftDev
# Oct 2021

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()

# It is similar in function to V3. In the scope of our testing, we will not
# be able to determine a printed difference in the running of our code.
# However, based on the comments present within the code, in the case that
# a developer reprograms the website and hosts the new website code, the
# website will automatically reload to reflect the change.

# Results
# The printed results in the terminal reflect those of the printed results of
# the running of V3. The name of the program is main, as that is the default
# name set by instantiating the app variable as an object of class Flask.
