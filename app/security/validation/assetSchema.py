from marshmallow import Schema, fields, validate
from app.constants.asset_types import AssetTypes

""" 
Asset Validation Schema using Marshmallow
@date December 4th 
@author Mama
"""


class AssetSchema(Schema):
    name = fields.Str(
        validate=validate.Length(min=2, max=80),
        required=True,
    )
    power = fields.Float(
        required=True,
    )
    asset_type = fields.Str(
        validate=validate.OneOf(
            [
                AssetTypes.CHILLER.value,
                AssetTypes.COMPRESSOR.value,
                AssetTypes.FURNACE.value,
                AssetTypes.ROLLING_MILL.value,
            ]
        ),
        required=True,
    )
    site_id = fields.Str(
        required=True,
    )
