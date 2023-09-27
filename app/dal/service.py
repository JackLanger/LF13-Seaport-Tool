class UserService:
    def __init__(self, datasource=""):
        self.InvalidUserDetailsError = None
        self.datasource = datasource

    def register_new_user(self, username, password) -> bool:
        return True
