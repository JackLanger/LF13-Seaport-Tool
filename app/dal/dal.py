import json
import os


class Dal:
    @staticmethod
    def serialize(data):
        classname = type(data).__name__
        filename = f"{classname}.json"

        directory = '/tmp/'
        os.makedirs(directory, exist_ok=True)

        with open(os.path.join(directory, filename), 'w') as f:
            json.dump(data, f, default=lambda o: o.__dict__, sort_keys=True)

    @staticmethod
    def deSerialize(data_class):
        classname = data_class.__name__
        filename = f"{classname}.json"

        directory = '/tmp/'
        os.makedirs(directory, exist_ok=True)

        with open(os.path.join(directory, filename), 'r') as f:
            return json.load(f, object_hook=lambda d: data_class(**d))
