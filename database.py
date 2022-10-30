from flask_sqlalchemy import SQLAlchemy
from app import app

app.config["SQLALCHEMY_DATABASE_URI"] = "config"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False



db1 = SQLAlchemy(app)

