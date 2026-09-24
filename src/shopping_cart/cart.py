from products import Product
from pymongo import MongoClient
from loguru import logger

class ShoppingCart:
    def __init__(self):
        mongo_url = 'mongodb+srv://guffranjgshaik_db_user:zFMHm7NoVSVvHUky@studentattendance.u8cdbrl.mongodb.net/?appName=StudentAttendance'
        mongo_client = MongoClient(mongo_url)
        cart_db = mongo_client['cart']
        self.cart_collection = cart_db['cart_collection']

    def add_product(self,product:Product):
        self.cart_collection.insert_one(product.to_dict())
        logger.success(f"{product.name} is added")

    def remove_product(self,product_name:str):
        self.cart_collection.delete_many({"name": product_name})
        logger.warning(f"{product_name} is removed")

    def calculate_total(self,):
        all_items_cursor =  self.cart_collection.find()
        total = 0
        for item in all_items_cursor:
            total += item['price'] * item['quantity']
        logger.info(f"Total: {total}")
        return total