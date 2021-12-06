from app import db
from datetime import datetime

from app.database.models.asset import Asset

""" 
Site database Model
@date December 4th 
@author Mama
"""


class Site(db.Model):
    uid = db.Column(db.String(200), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    max_power = db.Column(db.Float(), nullable=False)
    manager_id = db.Column(
        db.String(200), db.ForeignKey("manager.uid", ondelete="CASCADE")
    )
    assets = db.relationship(Asset, backref="site", cascade="all, delete")
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())

    def __repr__(self) -> str:
        return "<Site %r>" % self.name
