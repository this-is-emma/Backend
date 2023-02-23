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

#CREATE CAMPAIGN

class MainTests(unittest.TestCase):
 
    def setUp(self):
        """Executed prior to each test."""
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.drop_all()
        db.create_all()


    def test_create_campaign(self):
        """Test creating a campaign."""

        #Create a user & login
        create_user()
        login(self.app, 'moi', 'password')

        #POST request to the /new_campaign route
        post_data = {
            'name': 'third campaign',
            'description': 'A description for this',
        }
        self.app.post('/new_campaign', data=post_data)

        # Verify campaign was updated in the database
        created_campaign = Campaign.query.filter_by(name='third campaign').first()
        self.assertIsNotNone(created_campaign)
        self.assertEqual(created_campaign.name, 'third campaign')

    #make donation
'''
    def test_create_author(self):
            """Test creating an author."""

            # TODO: Create a user & login (so that the user can access the route)
            create_user()
            login(self.app, 'me1', 'password')

            # TODO: Make a POST request to the /create_author route
            post_data = {
                'name': 'Frank Herbert',
                'biography': 'He wrote a lot of stuff',
            }
            self.app.post('/create_author', data=post_data)

            # TODO: Verify that the author was updated in the database
            created_author = Author.query.filter_by(name='Frank Herbert').one()
            self.assertIsNotNone(created_author)
            self.assertE


    # TEST HOMEPAGE LOGGED OUT

    def test_book_detail_logged_out(self):
            """Test that the book appears on its detail page."""
            # TODO: Use helper functions to create books, authors, user
            create_books()
            create_user()
            login(self.app, 'me1', 'password')

            # TODO: Make a GET request to the URL /book/1, check to see that the
            # status code is 200
            response = self.app.get('/book/1', follow_redirects=True)
            self.assertEqual(response.status_code, 200)


            # TODO: Check that the response contains the book's title, publish date,
            # and author's name
            response_text = response.get_data(as_text=True)
            self.assertIn("<h1>To Kill a Mockingbird</h1>", response_text)
            self.assertIn("Harper Lee", response_text)

            # TODO: Check that the response does NOT contain the 'Favorite' button
            # (it should only be shown to logged in users)
            self.assertNotIn("
'''