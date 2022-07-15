
from deta import Deta
#import requests

deta = Deta("c08p64s1_tEWDThMLRq72WYUgbFfgMx15WpDLjrXN")
#db = deta.Base("chat")

def buat_user(username):
    db = deta.Base(username)
    return db

def del_data(username, key):
    db = deta.Base(username)
    return db.delete(key)

# menambahkan data dari user
def add_data(username, data, key):
    db = deta.Base(username)
    db.put(data, key)
    return data

def get_data(username, key):
    db = deta.Base(username)
    data = db.get(key)
    return data

