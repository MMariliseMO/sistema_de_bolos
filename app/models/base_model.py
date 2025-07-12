from peewee import Model, PostgresqlDatabase

psql_db = PostgresqlDatabase('my_database', user='postgres')

class BaseModel(Model):
    class Meta:
        database = psql_db