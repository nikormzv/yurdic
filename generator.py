import random

import string

class Generator:

    def create(

        self,

        length

    ):

        alphabet = (

            string.ascii_letters +

            string.digits +

            "!@#$%"

        )

        return "".join(

            random.choice(alphabet)

            for _ in range(length)

        )
