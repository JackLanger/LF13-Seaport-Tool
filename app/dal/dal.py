import pickle

class Dal:
    def save(data):
        with open(f"app/dal/save/{data.id}.pkl",'wb') as f:
            pickle.dump(data,f,pickle.HIGHEST_PROTOCOL)
            
    def load(id):
        with open(f"app/dal/save/{id}.pkl",'rb') as f:
            return pickle.load(f)