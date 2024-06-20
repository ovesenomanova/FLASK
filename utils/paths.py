from os.path import join, abspath, dirname

ROOT_PATH = dirname(
    dirname(abspath(__file__))
)
DB_FILE_PATH = join(ROOT_PATH, "data", "global.db")





