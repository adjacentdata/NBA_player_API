from flask_sqlalchemy import SQLAlchemy
from app import app

app.config["SQLALCHEMY_DATABASE_URI"] = "config"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False



db1 = SQLAlchemy(app)

class Players(db1.Model):
    player_id = db1.Column(db1.Integer, primary_key=True)
    player_name = db1.Column(db1.String(80), nullable=False)
    team_id = db1.Column(db1.Integer, nullable=False)
    season = db1.Column(db1.Date)