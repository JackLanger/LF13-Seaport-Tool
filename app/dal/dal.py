import json,os

class Dal:
    def serialize(data):
        classname = type(data)
        filename = "%.json" %classname
        
        with open(os.path.join('/tmp/',filename),'w') as f:
            json.dumps(data, f, sort_keys=True)
            
    def deSerialize(data):
        classname = type(data)
        filename = "%.json" %classname
        
        with open(os.path.join('/tmp/',filename),'r') as f:
            return json.load(f)