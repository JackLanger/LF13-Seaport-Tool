import json

class Dal:
    def serialize(data):
        with open('/tmp/datatransfer.json','w') as f:
            json.dumps(data, f, sort_keys=True)
            
    def deSerialize():
        with open('/tmp/datatransfer.json','r') as f:
            return json.load(f)