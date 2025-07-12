from base_model import BaseModel
from peewee import UUIDField, CharField, DateField

class Product(BaseModel):
    id = UUIDField()
    name = CharField(max_length=1000)
    created = DateField()