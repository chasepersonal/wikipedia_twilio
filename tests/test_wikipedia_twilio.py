from unittest import TestCase
from wikipedia_twilio import app
from flask import request

class TestWikipediaTwilio(TestCase):

    def setUp(self):
        # Ensure all tests stay in testing mode
        app.testing = True

    def test_receiving_request(self):
        with app.test_request_context(data = {'Body': 'test body'}):

            message_body = request.form['Body']

            self.assertEqual(message_body, 'test body')

