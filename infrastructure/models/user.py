from peewee import Model, IntegerField, TextField


from ..database.postgres import db


class User(Model):

    id = IntegerField(primary_key=True)
    name = TextField(unique=True)

    class Meta:
        database = db
        table_name = 'users'
