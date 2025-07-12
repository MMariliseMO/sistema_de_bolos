from base_model import BaseModel
from peewee import CharField, UUIDField

class User(BaseModel):
    id = UUIDField()
    name = CharField(max_length=1000)
    email = CharField(max_length=255)
    password = CharField(max_length=255)
    phone = CharField(max_length=100)

