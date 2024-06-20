from data.db_session import DatabaseManager


def users_create_table(db_manager: DatabaseManager):
    db_manager.execute(
        """CREATE TABLE IF NOT EXISTS "users" (
        "id"   INTEGER PRIMARY KEY AUTOINCREMENT,
        "password"    VARCHAR(32),
        "username"    VARCHAR(32)
        )"""
    )


def users_register(db_manager: DatabaseManager, username: str, password: str) -> int:
    db_manager.execute(
        f"""INSERT INTO "users" ("username", "password")
        VALUES ("{username}", "{password}"); """)
    return db_manager.get_last_id()


def users_check_if_exists(db_manager: DatabaseManager, username: str, password: str) -> int:
    query = db_manager.execute(
        f"""SELECT  "id" FROM "users" 
        WHERE ("password" = "{password}" AND "username"="{username}")
        """)
    if query:
        return query[0][0]
    else:
        return 0


def users_check_if_username_taken(db_manager: DatabaseManager, username: str) -> bool:
    query = db_manager.execute(
        f"""SELECT  "id" FROM "users" 
           WHERE ("username"="{username}")
           """)
    if query:
        return True
    return False

