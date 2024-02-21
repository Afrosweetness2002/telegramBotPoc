import db;

def get_users():
    return db.get("SELECT * FROM user")