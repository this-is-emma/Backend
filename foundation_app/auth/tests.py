# Create your tests here.

import os
import unittest
import app

from datetime import date
from foundation_app.extensions import app, db, bcrypt
from foundation_app.models import Campaign, Donation, User

"""
Run these tests with the command:
python -m unittest books_app.main.tests
"""

#################################################
# Setup
#################################################

def login(client, username, password):
    return client.post('/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)

def logout(client):
    return client.get('/logout', follow_redirects=True)

def create_campaign():
    c1 = Campaign(
        name='first campaign',
        description='description goes here',
    )
    db.session.add(c1)

    c2 = Campaign(
        name='second campaign',
        description='another description goes here',
    )

    db.session.add(c2)
    db.session.commit()

def create_user():
    # Creates a user with username 'me1' and password of 'password'
    password_hash = bcrypt.generate_password_hash('password').decode('utf-8')
    user = User(username='moi', password=password_hash)
    db.session.add(user)
    db.session.commit()

#################################################
# Tests
#################################################


#CREATE USER



#USER PROFILE

def test_profile_page(self):
    # TODO: Make a GET request to the /profile/me1 route
    create_user()
    login(self.app, 'me1', 'password')
    response = self.app.get('/profile/me1', follow_redirects=True)
    self.assertEqual(response.status_code, 200)

    # TODO: Verify that the response shows the appropriate user info
    response_text = response.get_data(as_text=True)
    self.assertIn('me1', response_text) 


#test homepage logged in 

 def test_homepage_logged_in(self):
        """Test that the books show up on the homepage."""
        # Set up
        create_books()
        create_user()
        login(self.app, 'me1', 'password')

        # Make a GET request
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        # Check that page contains all of the things we expect
        response_text = response.get_data(as_text=True)
        self.assertIn('To Kill a Mockingbird', response_text)
        self.assertIn('The Bell Jar', response_text)
        self.assertIn('me1', response_text)
        self.assertIn('Create Book', response_text)
        self.assertIn('Create Author', response_text)
        self.assertIn('Create Genre', response_text)

        # Check that the page doesn't contain things we don't expect
        # (these should be shown only to logged out users)
        self.assertNotIn('Log In', response_text)
        self.assertN


