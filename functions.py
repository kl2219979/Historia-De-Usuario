# functions module contains functions for handling product information and cost calculation.
from models import inventory
from validations import name_validation, price_validation, quantity_validation

def add_product():
    """Description"""
    name = name_validation()
    price = price_validation()
    quantity = quantity_validation()
    
    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    inventory.append(product)

def show_inventory():
    if not inventory:
        print("El inventario esta vacio")
        return
    for i,product in enumerate(inventory):
        print(f"{i+1} - Name: {product['name']} | Price: {product['price']} | Quantity: {product['quantity']}")
    
    
def calculate_statistics_inventory():
    """ description """
    total_value = 0
    for p in inventory:
        subtotal = p['price']*p['quantity']
        total_value += subtotal
    
    total_quantity = 0
    for p in inventory:
        quantity = p['quantity']
        total_quantity += quantity
        
    print("\n*** calculate statistics inventory ***")
    print(f"total value: {total_value}")
    print(f"total quantity: {total_quantity}")

