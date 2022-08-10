from contextvars import ContextVar

import peewee


class PeeweeConnectionState(peewee._ConnectionState):
    def __init__(self, db_state: ContextVar, **kwargs):
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]
