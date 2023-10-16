import uuid

from app.models.quest import QuestDTO, Resource
from app.models.ship import ShipDTO
from app.models.user import UserDTO

ships = [
    ShipDTO(1, "Ship 1", 1, 5, 1),
    ShipDTO(2, "Ship 2", 10, 15, 5),
    ShipDTO(3, "Ship 3", 11, 7, 3),
    ShipDTO(4, "Ship 4", 9, 5, 2),
    ShipDTO(5, "Ship 5", 2, 1, 4),
]


class ShipService:
    def __int__(self):
        pass

    def get_by_id(self, ship_id) -> ShipDTO:
        return list(filter(lambda s: s.id == ship_id, ships))[0]

    def create_new(self, ShipDto) -> ShipDTO:
        pass

    def save(self, ShipDto):
        pass

    def delete(self, ship_id):
        pass


class UserService:
    user = UserDTO(
        uuid.uuid4(),
        "Template User",
        [
            QuestDTO(1, "Quest 1", [Resource("Wood", 100)]),
            QuestDTO(2, "Quest 2", [Resource("Wood", 100), Resource("Stone", 200)]),
        ],
        ships,
    )

    def __init__(self, datasource=""):
        self.InvalidUserDetailsError = None
        self.datasource = datasource

    def register_new_user(self, username: str, password: str, email: str) -> UserDTO:
        return self.user

    def verify_credentials(self, username: str, password: str) -> UserDTO:
        return self.user

    def save(self, user: UserDTO):
        pass

    def get_by_id(self, user_id):
        return self.user

    def delete(self, user):
        pass
