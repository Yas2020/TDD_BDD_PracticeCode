"""
Test Cases TestAccountModel
"""
import json
from unittest import TestCase
from models.app import db
from models.account import Account

ACCOUNT_DATA = {}

class TestAccountModel(TestCase):
    """Test Account Model"""

    @classmethod
    def setUpClass(cls):
        """ Connect and load data needed by tests """
        db.create_all()
        global ACCOUNT_DATA
        with open('tests/fixtures/account_data.json') as json_data:
            ACCOUNT_DATA = json.load(json_data)

    @classmethod
    def tearDownClass(cls):
        """Disconnect from database"""
        db.session.close()

    def setUp(self):
        """Truncate the tables"""
        db.session.query(Account).delete()
        db.session.commit()

    def tearDown(self):
        """Remove the session"""
        db.session.remove()

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################

    def test_create_an_account(self):
        """ Test create a single Account """
        data = ACCOUNT_DATA[0] # get the first account
        account = Account(**data)
        account.create()
        self.assertEqual(len(Account.all()), 1)

    def test_create_all_accounts(self):
        """ Test create a single Account """
        for data in ACCOUNT_DATA:
            account = Account(**data)
            account.create()
        self.assertEqual(len(Account.all()), len(ACCOUNT_DATA))

    def test_represent_as_string(self):
        """ Test string representation """
        a = Account(name="Foo")
        self.assertEqual(str(a), "<Account 'Foo'>")

    def test_to_dict(self):
        """ Test to dictionary"""
        data = ACCOUNT_DATA[0] # get the first account
        account = Account(**data)
        result = account.to_dict()
        self.assertEqual(result['name'], account.name)
        self.assertEqual(result['phone_number'], account.phone_number)
        self.assertEqual(result['disabled'], account.disabled)
        self.assertEqual(result['date_joined'], account.date_joined)
        self.assertEqual(result['email'], account.email)