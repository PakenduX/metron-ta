from marshmallow import Schema, fields, validate

""" 
Manager Validation Schema
@date December 4th 
@author Mama
"""


class ManagerSchema(Schema):
    name = fields.Str(
        validate=validate.Length(min=2, max=80),
        required=True,
    )
    email = fields.Email(required=True)
    password = fields.Str(
        validate=validate.Length(min=7),
        required=True,
    )
