from flask import Blueprint, request, render_template, redirect, url_for, flash
from datetime import date, datetime

from flask_login import current_user, login_required
from foundation_app.models import Campaign, Donation
from foundation_app.main.forms import CampaignForm, DonationForm

from foundation_app.extensions import app, db

main = Blueprint('main', __name__)

# Create your routes here.

@main.route('/')
def homepage():
    all_campaigns = Campaign.query.all()
    donation_dict = {}
    for campaign in all_campaigns:
        i = campaign.id
        donation_dict[i] = []
        for donation in campaign.donations:
            donation_dict[i].append(donation.amount)
    
    print(donation_dict)

        
    return render_template('home.html', all_campaigns=all_campaigns, donation_dict = donation_dict)


@main.route('/new_campaign', methods=['GET', 'POST'])
@login_required
def new_campaign():
    form = CampaignForm()
    if form.validate_on_submit():
        new_campaign = Campaign (
            name = form.name.data, 
            description = form.description.data
        )
            
        db.session.add(new_campaign)
        db.session.commit()
        flash('New campaign was created successfully.')
        return redirect(url_for('main.homepage'))
    return render_template('new_campaign.html', form = form)


@main.route('/donate', methods=['GET', 'POST'])
@login_required
def donate():
    form = DonationForm()
    if form.validate_on_submit():
        donation = Donation(
            amount = form.amount.data, 
            donated_by_id = current_user.id,
            donated_to = form.donated_to.data.id
        )

        db.session.add(donation)
        db.session.commit()
        flash('Thank you for your donation!')
        return redirect(url_for('main.homepage'))
    return render_template('donate.html', form = form)
