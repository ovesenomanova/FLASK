from routing import app
from data.sql_request import users_create_table
from data.db_session import GlobalDBManager

from secrets import token_urlsafe

if __name__ == "__main__":
    users_create_table(db_manager=GlobalDBManager)
    app.config['SECRET_KEY'] = token_urlsafe(16)
    app.run()

