from flask_login import UserMixin, LoginManager
from data.sql_request import users_get_by_id
from data.db_session import GlobalDBManager


class AuthUser(UserMixin):

    def __init__(self, idd, username, email):
        self.id = idd
        self.username = username
        self.email = email

    @classmethod
    def get(cls, idd):
        user = users_get_by_id(GlobalDBManager, idd)
        user_id = user[0]
        user_email = user[1]
        user_login = user[3]
        return AuthUser(user_id, user_login, user_email)


login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return AuthUser.get(user_id)
