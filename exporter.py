class Exporter:

    def save(

        self,

        accounts,

        filename

    ):

        with open(

            filename,

            "w",

            encoding="utf-8"

        ) as file:

            file.write(

                "Password Vault\n\n"

            )

            for account in accounts:

                file.write(

                    f"{account.service} "

                    f"({account.username})\n"

                )
