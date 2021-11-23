# Yea! -- Andrew Juang, Eliza Knapp, Yuqing Wu
# SoftDev
# K19 -- A RESTful Journey Skyward
# 2021-11-23

from flask import Flask, render_template
import requests

app = Flask(__name__)

f = open("key_nasa.txt")
API_KEY = f.read().strip()

@app.route("/")
def main():
    print("API_KEY: " + API_KEY + "\n")
    r = requests.get('https://api.nasa.gov/planetary/apod?api_key=' + API_KEY)

    print("JSON:")
    print(r.json())

    URL = r.json()['url']
    print("\nURL: " + URL)

    return render_template('main.html',pic=URL)


if __name__ == "__main__":
    app.debug = True
    app.run()
