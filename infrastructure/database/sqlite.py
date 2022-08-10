from contextvars import ContextVar

from peewee import SqliteDatabase

from .peewee_connection_state import PeeweeConnectionState

DATABASE_NAME = 'test.db'
db_state_default = {"closed": None, "conn": None,
                    "ctx": None, "transactions": None}
db_state = ContextVar("db_state", default=db_state_default.copy())

db = SqliteDatabase(DATABASE_NAME, check_same_thread=False)
db._state = PeeweeConnectionState(db_state)
