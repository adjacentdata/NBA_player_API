from dataclasses import field
from marshmallow import Schema, fields

class Player_Schema(Schema):
    player_id = fields.Integer()
    team_id = fields.Integer()
    name = fields.String()
    season = fields.Date()
