import json
import subprocess

api_key = "default.PWSM_wtV5Ri9X6l7PKt0Lg.yPI3fOEtb_3Kjcz3SOb0AWYUSW6r2vAwZLKkUsNKROvkc8ZI"
url = "https://vault.immudb.io/ics/api/v1/ledger/default/collection/default/document"
path = "C:\\Users\\ErolCesko\\PycharmProjects\\Vault\\transactions.json"


def upload(transaction):
    transactions_json = json.dumps(transaction)

    curl = [
        "curl", "-X", "PUT", url,
        "-H", "accept: application/json",
        "-H", f"X-API-Key: {api_key}",
        "-H", "Content-Type: application/json",
        "-d", transactions_json
    ]

    subprocess.run(curl)


with open(path, 'r') as file:
    transactions = json.load(file)

for transaction in transactions:
    upload(transaction)


