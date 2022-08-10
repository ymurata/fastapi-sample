from contextvars import ContextVar

from peewee import PostgresqlDatabase

from .peewee_connection_state import PeeweeConnectionState

db_state_default = {"closed": None, "conn": None,
                    "ctx": None, "transactions": None}
db_state = ContextVar("db_state", default=db_state_default.copy())
db = PostgresqlDatabase("test", user="postgres",
                        password="password", host="localhost")
db._state = PeeweeConnectionState(db_state)
