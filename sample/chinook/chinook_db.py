import os.path as path
from database import get_pyqt_database_connection_sqlite

DB_FILE = path.join(path.dirname(__file__), "chinook.db")


def pyqt_connection():
    return get_pyqt_database_connection_sqlite(DB_FILE)
