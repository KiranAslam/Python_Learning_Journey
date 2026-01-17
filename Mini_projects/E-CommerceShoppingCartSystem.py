import uuid
import json
import os
from datetime import datetime

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def reduce_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        return False

class Electronics(Product):
    def __init__(self, name, price, stock, warranty):
        super().__init__(name, price, stock)
        self.warranty = warranty

class Clothing(Product):
    def __init__(self, name, price, stock, size):
        super().__init__(name, price, stock)
        self.size = size

class ShoppingCart:
    def __init__(self, customer_name):
        self.customer = customer_name
        self.__items = []
        self.__total = 0.0

    def add_item(self, product, quantity):
        if product.reduce_stock(quantity):
            self.__items.append({
                "product": product.name, 
                "price": product.price, 
                "qty": quantity
            })
            self.__total += product.price * quantity
            print(f"Added {quantity} x {product.name} to cart.")
        else:
            print(f"Stock Alert: {product.name} is out of stock!")

    def __save_transaction(self, order_id):
        record = {
            "order_id": order_id,
            "customer": self.customer,
            "date": datetime.now().strftime('%Y-%m-%d %H:%M'),
            "total": self.__total,
            "items": self.__items
        }
        
        file_name = "sales_history.json"
        data = []
        
        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                data = json.load(f)
        
        data.append(record)
        
        with open(file_name, 'w') as f:
            json.dump(data, f, indent=4)

    def checkout(self):
        if not self.__items:
            print("Cart is empty!")
            return
        
        order_id = uuid.uuid4().hex[:8].upper()
        
        print("\n" + "="*35)
        print(f"       🛒 OFFICIAL INVOICE")
        print("="*35)
        print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print(f"Order ID: {order_id}")
        print(f"Customer: {self.customer}")
        print("-" * 35)
        
        for item in self.__items:
            print(f"{item['product']} (x{item['qty']})".ljust(20) + f"Rs.{item['price'] * item['qty']}")
            
        print("-" * 35)
        print(f"GRAND TOTAL:".ljust(20) + f"Rs.{self.__total}")
        print("="*35)
        
        self.__save_transaction(order_id)
        print("Order saved to sales_history.json!")

laptop = Electronics("MacBook M2", 350000, 5, 12)
shirt = Clothing("Denim Jacket", 4500, 10, "Large")

my_cart = ShoppingCart("Kiran")
my_cart.add_item(laptop, 1)
my_cart.add_item(shirt, 2)
my_cart.checkout()