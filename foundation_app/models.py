from sqlalchemy_utils import URLType
from foundation_app.extensions import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    """Donor model."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    phone_number = db.Column(db.String(100), nullable=True)
    donations = db.relationship('Donation', back_populates='donor')

    def __str__(self):
        return self.username
    
class Campaign(db.Model):
    """Campaign  model."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    donations = db.relationship('Donation', back_populates='campaign')

    def __str__(self):
        return self.name
    
class Donation(db.Model):
    """Donation  model."""
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    donated_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    donor = db.relationship('User', back_populates='donations')
    donated_to = db.Column(db.Integer, db.ForeignKey('campaign.id'))
    campaign = db.relationship('Campaign', back_populates='donations')

    def __str__(self):
        return str(self.amount)
