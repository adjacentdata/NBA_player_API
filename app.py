from flask import Flask, request, jsonify
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

    def __repr__(self):
        return self.player_name

    #Get all players in the NBA 
    @classmethod
    def all_players(cls):
        return cls.query.all()
    
    @classmethod
    def get_player_by_name(cls, name):
        return cls.query.get_or_404(name)
    
    def get_player_by_id(cls, player_id):
        return cls.query.get_or_404(player_id)
    
    def add_player(self):
        db.session.add(self)
        db.session.commit()

@app.get('/nba_players')
def get_nba_players():
    players = Player.all_players()
    schema=Player_Schema()
    list_of_players = schema.dump(players)
    return jsonify(list_of_players)

@app.get('/nba_players/<int:player_id>')
def get_player_by_id(player_id):
    player = Player.get_player_by_id(player_id)
    schema = Player_Schema()
    chosen_player = schema.dump(player)
    return jsonify(chosen_player),200
    
@app.route('/')
def hello():
    return "Hello, Welcome to the NBA Player API"

