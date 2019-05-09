from PyQt5.QtSql import QSqlDatabase
import os.path as path


def get_pyqt_database_connection_sqlite(sqlite_file):
    if not path.exists(sqlite_file):
        raise FileNotFoundError(f"sqlite file not found: {sqlite_file}")

    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(sqlite_file)

    if not db.open():
        raise Exception("Erro on opening connection to sqlite file")

    return db
