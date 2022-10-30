from flask import Flask 
from database import db1

app= Flask(__name__)

@app.route('/')
def hello():
    return "Hello"
