import pickle
from dal import Dal
import hashlib


class localObject:
    def __init__(self,id,password):
        self.id = id
        self.password = password

class login:    
    def makehash(password):
        salt = hashlib.md5(password.encode())
        saltyPassword = password+salt
        return hashlib.md5(saltyPassword.encode())
        
    def save(self,id,password):
        data = localObject(id,self.makehash(password))
        with open(f"app/dal/login/{data.id}.pkl",'wb') as f:
            pickle.dump(data,f,pickle.HIGHEST_PROTOCOL)
            
    def load(self,id,password):
        with open(f"app/dal/login/{id}.pkl",'rb') as f:
            user = pickle.load(f)
            if user:
                if user.id == id and user.password == self.makehash(password):
                    return Dal.load(id)
                else:
                    return False
            else:
                return False
        