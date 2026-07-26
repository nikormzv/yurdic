from config import EXPORT_FILE
from config import PASSWORD_LENGTH

from storage import Storage
from vault import Vault
from crypto import Crypto
from generator import Generator
from exporter import Exporter
from utils import Utils

accounts = Storage().load()

crypto = Crypto()

print()

print("Password Vault\n")

for account in accounts:

    print(account.service)

    print(

        f"User: {account.username}"

    )

    print(

        f"Password: {crypto.mask(account.password)}"

    )

    print()

strong = sum(

    Utils().strong(

        item.password

    )

    for item in accounts

)

print(

    f"Accounts: {len(accounts)}"

)

print(

    f"Strong passwords: {strong}"

)

print()

print(

    "Generated password:"

)

print(

    Generator().create(

        PASSWORD_LENGTH

    )

)

Exporter().save(

    accounts,

    EXPORT_FILE

)
