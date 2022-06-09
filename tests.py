from faker import Faker
from datetime import datetime
import random
def creating_fake_timestamp():
    fake = Faker()
    some_data = fake.date_time_between(start_date='-15y', end_date='now')
    some_data=some_data.replace(microsecond=random.randint(0,999_999))
    some_data=some_data.timestamp()
    value = some_data
    return value
    #TODO: add miliseconds
print(creating_fake_timestamp())