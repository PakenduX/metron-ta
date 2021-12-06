from app import db
from datetime import datetime

""" 
Asset database Model
@date December 4th 
@author Mama
"""


class Asset(db.Model):
    uid = db.Column(db.String(200), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    power = db.Column(db.Float(), nullable=False)
    asset_type = db.Column(db.String(100), nullable=False)
    site_id = db.Column(db.String(200), db.ForeignKey("site.uid", ondelete="CASCADE"))
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())

    def __repr__(self) -> str:
        return "<Asset %r>" % self.name
