import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'udemy_practice.settings')

import django
django.setup()

import random
from second_app.models import User
from faker import Faker


def populate(n=5):
    for entry in range(n):
        fake_fn = fake_gen.first_name()
        fake_ln = fake_gen.last_name()
        fake_email = fake_gen.email()

        user = User.objects.get_or_create(first_name=fake_fn, last_name=fake_ln, Email=fake_email)[0]


fake_gen = Faker()
topics = ['Social', 'Search', 'MarketPlace', 'News', 'Games']

if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating complete!")
