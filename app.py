from flask import Flask
import config
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

@app.route("/")
def hello():
    return "Hello Wolrd!"

@app.route("/<name>")
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == "__main__":
    app.run()