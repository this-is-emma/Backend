# Create your forms here.
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField, fields
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL
from foundation_app.models import Campaign

class CampaignForm(FlaskForm):
    """Form for creating/updating campaigns."""
    name = StringField('Name:', 
        validators=[
            DataRequired(), 
            Length(min=3, max=80, message="name must be between 3 and 50 chars")
        ]) 
    description = StringField('Description:', 
        validators=[
            DataRequired(), 
            Length(min=3, max=80, message="description should be at least 50 chars")
        ])
    submit = SubmitField('Submit')

class DonationForm(FlaskForm):
    """Form for adding a donation."""
    amount = FloatField('amount')
    donated_to = QuerySelectField('Select a campaign to donate:', query_factory=lambda: Campaign.query, allow_blank=False)

    submit = SubmitField('Submit')
    