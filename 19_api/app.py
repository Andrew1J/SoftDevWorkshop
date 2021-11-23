from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def main():
    r = requests.get('https://api.nasa.gov/planetary/apod?api_key=IUUsoN7GY95hS6q7OxbuxPfjih8xyDg9AAW6MhxH')
    print(r.json())
    print(r.json()['url'])
    return render_template('main.html',picture=r.json()['url'])


app.run()
