from peewee import SqliteDatabase, Model, CharField, DateField

database = SqliteDatabase('Usuarios')

class BaseModel(Model):
    class Meta:
        database = database


class User(BaseModel):
    usuario = CharField(unique=True)
    clave = CharField ()

def create_tables(*tables):
    with database:
        database.create_tables(tables)


if __name__ == '__main__':
    create_tables(User)