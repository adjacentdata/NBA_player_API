from flask import Flask 
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy

#Load environment variables
load_dotenv()

# Configure PostgreSQL to SQL Alchemy with environment variable
app= Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("POSTGRE_PATH")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create the database object - (To move later)
db = SQLAlchemy(app)

class Players(db.Model):
    player_id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(80), nullable=False)
    team_id = db.Column(db.Integer, nullable=False)
    season = db.Column(db.Date)

@app.route('/')
def hello():
    """
     Returns the application test hello 
    """
    return "Hello"
