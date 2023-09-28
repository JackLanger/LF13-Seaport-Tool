import uuid

from app.models.quest import QuestDTO, Resource
from app.models.ship import ShipDTO
from app.models.user import UserDTO


class UserService:
    user = UserDTO(
        uuid.uuid4(),
        "Template User",
        [
            QuestDTO("Quest 1", [Resource("Wood", 100)]),
            QuestDTO("Quest 2", [Resource("Wood", 100), Resource("Stone", 200)]),
        ],
        [ShipDTO(1, "Ship 1", 1, 5, 1), ShipDTO(2, "Ship 2", 10, 15, 5)],
    )

    def __init__(self, datasource=""):
        self.InvalidUserDetailsError = None
        self.datasource = datasource

    def register_new_user(self, username: str, password: str, email: str) -> UserDTO:
        return self.user

    def verify_credentials(self, username: str, password: str) -> UserDTO:
        return self.user

    def get(self, user_id):
        return self.user
