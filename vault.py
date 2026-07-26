class Vault:

    def search(

        self,

        accounts,

        service

    ):

        return [

            item

            for item in accounts

            if item.service.lower()

            == service.lower()

        ]
