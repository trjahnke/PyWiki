from flask import Flask
from config import Config

app = Flask(__name__)

@app.route("/")
def hello():
    return Config.SECRET_KEY

@app.route("/<name>")
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == "__main__":
    app.run()