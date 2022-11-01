from dataclasses import field
from marshmallow import Schema, fields

class player_schema(Schema):
    player_id = fields.Integer()
    team_id = fields.Integer()
    name = fields.String()
    season = fields.Date()
    