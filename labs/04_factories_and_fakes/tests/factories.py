"""
AccountFactory class using FactoryBoy

Documentation on Faker Providers:
    https://faker.readthedocs.io/en/master/providers/baseprovider.html

Documentation on Fuzzy Attributes:
    https://factoryboy.readthedocs.io/en/stable/fuzzy.html

"""
import factory
from datetime import date
from factory.fuzzy import FuzzyChoice, FuzzyDate
import factory.fuzzy
from models.account import Account

class AccountFactory(factory.Factory):
    """ Creates fake Accounts """

    class Meta:
        model = Account

    # Add attributes here...
    id = factory.Sequence(lambda n: n+1)
    name = factory.Faker("name")
    email = factory.Faker("email")
    phone_number = factory.Faker("phone_number")
    disabled = FuzzyChoice(choices=[True, False])
    date_joined = FuzzyDate(date(2020,1,1))

