from importlib import resources
from typing import List


class Resource:
    def __init__(self, name: str, amount: int = 0):
        self.name = name
        self.amount: int = amount


class QuestDTO:
    def __init__(self, id: int, title: str, resources: List[Resource]):
        self.id = id
        self.title = title
        self.resources = resources

    @property
    def json(self):
        import json

        json_resources = []
        for res in self.resources:
            json_resources.append({"name": res.name, "amount": res.amount})

        return json.dumps(
            {"id": self.id, "title": self.title, "resources": json_resources}
        )
