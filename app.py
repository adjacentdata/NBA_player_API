from flask import Flask 
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy
from database import Player_Schema

#Load environment variables
load_dotenv()

# Configure PostgreSQL to SQL Alchemy with environment variable
app= Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("POSTGRE_PATH")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create the database object - (To move later)
db = SQLAlchemy(app)

class Player(db.Model):
    player_id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(80), nullable=False)
    team_id = db.Column(db.Integer, nullable=False)
    season = db.Column(db.Date)

    def __init___(self, player_name, team_id, player_id, season):
        self.player_id = player_id
        self.player_name = player_name
        self.team_id = team_id
        self.season = season

    def __repr__(self) -> str:
        return self.player_name

    #Get all players in the NBA 
    @classmethod
    def all_players(cls):
        return cls.query.all()
    
    @classmethod
    def get_player_by_name(cls, name):
        return cls.query.get_or_404(name)
    
    def get_player_by_id(cls, id):
        return cls.query.get_or_404(id)
    
    def add_player(self):
        db.session.add(self)
        db.session.commit()

    
@app.route('/')
def hello():
    """
     Returns the application test hello 
    """
    return "Hello"
