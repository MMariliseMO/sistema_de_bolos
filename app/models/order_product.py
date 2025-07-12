from base_model import BaseModel
from peewee import UUIDField, DateField, ForeignKeyField
from order import Order
from product import Product


class OrderProduct(BaseModel):
    id = UUIDField()
    order = ForeignKeyField(Order, backref= 'order_products')
    product = ForeignKeyField(Product, backref='order_products')
    created = DateField()


