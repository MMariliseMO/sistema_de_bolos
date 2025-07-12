from base_model import BaseModel
from peewee import UUIDField, DateField, ForeignKeyField
from user import User

class Order (BaseModel):
    id = UUIDField()
    created = DateField()
    due_date = DateField()
    user = ForeignKeyField(User, backref='orders')
    order_product_id = UUIDField()
