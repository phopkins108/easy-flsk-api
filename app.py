# app.py 
# deploy from github demo from Ssali Jonathan 
# https://github.com/jod35/flask-deploy-demo
from logging import debug
from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return "Hello World"


if __name__ == "__main__":
    app.run(debug=True)