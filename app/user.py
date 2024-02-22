class User:
    def __init__(
        self,
        user_id,
        telegram_id,
        telegram_username,
        first_name,
        last_name,
        display_name,
        email,
        role_id
    ):
        self.user_id = user_id
        self.telegram_id = telegram_id
        self.telegram_username = telegram_username
        self.first_name = first_name
        self.last_name = last_name
        self.display_name = display_name
        self.email = email
        self.role_id = role_id