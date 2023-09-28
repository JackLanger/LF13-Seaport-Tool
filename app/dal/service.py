class UserService:
    def __init__(self, datasource=""):
        self.InvalidUserDetailsError = None
        self.datasource = datasource

    def register_new_user(self, username: str, password: str, email: str) -> bool:
        return True

    def verify_credentials(self, username: str, password: str) -> bool:
        return True
