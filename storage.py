from models import Account

from sample_data import DATA

class Storage:

    def load(self):

        return [

            Account(**item)

            for item in DATA

        ]
