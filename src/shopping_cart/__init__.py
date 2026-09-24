from cart import ShoppingCart
from products import Product
import time

def main():
    cart = ShoppingCart()
    p1 = Product("TVS XL 100", 80000, 2)
    p2 = Product("HP Pavillion 14", 780000, 5)
    p3 = Product("Huawei Phone", 110000, 5)
    cart.add_product(p1)
    time.sleep(2)
    cart.add_product(p2)
    time.sleep(2)
    cart.add_product(p3)
    time.sleep(2)
    cart.calculate_total()
    
if __name__ == "__main__":
    main()