from controller.users_controller import UserController


class OpenTableCommand:
    def __init__(self, user_controller: UserController):
        self.user_controller = user_controller

    def __call__(self, key, table_id):
        self.user_controller.open_table(key, table_id)