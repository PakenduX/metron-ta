from app import db
from app.database.models.site import Site

""" 
Manager database Model
@date December 4th 
@author Mama
"""


class Manager(db.Model):
    uid = db.Column(db.String(200), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Text(), nullable=False)
    sites = db.relationship(Site, backref="manager", cascade="all, delete")

    def __repr__(self) -> str:
        return "<Manager %r>" % self.name
