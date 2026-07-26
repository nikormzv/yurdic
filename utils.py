class Utils:

    def strong(

        self,

        password

    ):

        return (

            len(password) >= 8

            and

            any(c.isdigit() for c in password)

            and

            any(not c.isalnum() for c in password)

        )
