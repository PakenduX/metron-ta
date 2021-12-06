from marshmallow import Schema, fields, validate

""" 
Site Validation Schema
@date December 4th 
@author Mama
"""


class SiteSchema(Schema):
    name = fields.Str(
        validate=validate.Length(min=2, max=80),
        required=True,
    )
    address = fields.Str(required=True, validate=validate.Length(min=2))
    max_power = fields.Float(
        required=True,
    )
