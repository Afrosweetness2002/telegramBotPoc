import db
from user import User

def get_users() -> list[User]:
    result = db.get("SELECT * FROM user")
    users = [User(*x) for x in result]
    return users