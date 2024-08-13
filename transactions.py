from faker import Faker
import json

fake = Faker()

def details(unique):
    return {
        "account number": str(unique),
        "account name": fake.company(),
        "iban": fake.iban(),
        "address": fake.address(),
        "amount": fake.random_number(),
        "type": fake.random_element(["sending", "receiving"])
    }

def generate(count):
    return [details(i) for i in range(1, count + 1)]

numbers= generate(110)

with open('Storing accounting information.json', 'w') as f:
    json.dump(numbers, f, indent=4)


