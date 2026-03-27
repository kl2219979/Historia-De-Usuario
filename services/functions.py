from models import inventory

def add_product():
    name = input("ingrese el nombre del producto")
    price = float(input("Ingrese el precio del producto:"))
    quantyti = int(input("Ingrese la cantidad del producto:"))
    
    product = {"name":name,"price":price,"quantyti":quantyti}
    inventory.append(product)

def show_product():
    if len(inventory)<0:
        print("El inventario esta vacio")
        return
    for i,product in enumerate(inventory):
        print(f"{i+1} - name: {product['name']} | price: {product['price']} | quantyti: {product['quantyti']}")
        
def search_product():
    name = input("Ingrese el nombre del producto que desea buscar:")
    
    for i,product in enumerate(inventory):
        if product['name'] == name:
            print(f"{i+1} - name: {product['name']} | price: {product['price']} | quantyti: {product['quantyti']}")
            break

def update_product():
    update = input("desea modificar completa o parcialmente el producto (c/p):").lowwer()
    
    if update == "c":
        index = int(input("ingrese el indice del producto a modificar"))
        inventory[index]['name'] = input("ingrese el nombre del producto")
        inventory[index]['price'] = float(input("Ingrese el precio del producto:"))
        inventory[index]['quantyti'] = int(input("Ingrese la cantidad del producto:"))
        
    if update == "p":
        index = int(input("ingrese el indice del producto a modificar"))
        while True:
            print("Menu update product")
            print("1.name update")
            print("2.price update")
            print("3.quantyti update")
            print("4.salir")
            option = int(input("Ingrese el opcion que desea realizar:"))
            
            match option:
                case 1:
                    inventory[index]['name'] = input("ingrese el nombre del producto")
                case 2:
                    inventory[index]['price'] = float(input("Ingrese el precio del producto:"))
                case 3:
                    inventory[index]['quantyti'] = int(input("Ingrese la cantidad del producto:"))
                case 4:
                    print(f"product update - name: {inventory[index]['name']} | price: inventory[index]['price'] | quantyti: inventory[index]['quantyti']")
                    break
                case _:
                    print("Error, intenta de nuevo")

    if update != "c" and update != "p":
        print("Elija entre c o p")
        return update_product()

def remove_product():
    index = int(input("ingrese el indice del producto a eliminar"))
    inventory.pop(index)
    print(f"Producto eliminado - name: {inventory[index]['name']} | price: inventory[index]['price'] | quantyti: inventory[index]['quantyti']")

def calculate_statistics_inventory():
    total_units = 0
    for product in inventory:
        for i in product:
            total_units += i['quantyti']
    
    total_value = 0
    for product in inventory:
        for i in product:
            total_value += (lambda i: i['precio']*i['quantyti'])
    
    most_expensive_product = {"name":"","price":0,"quantyti":0}
    for product in inventory:
        for i in product:
            if i['price']>most_expensive_product['price']:
                most_expensive_product = i
            else:
                continue
    
    product_greater_quantity = {"name":"","price":0,"quantyti":0}
    for product in inventory:
        for i in product:
            if i['quantyti']>product_greater_quantity['quantyti']:
                product_greater_quantity = i
            else:
                continue
    
    print("*** STATISTICS INVENTORY ***")
    print(f"Total Units: {total_units}")
    print(f"Total Value: {total_value}")
    print(f"Most Expensive Product - name: {most_expensive_product['name']} | price: {most_expensive_product['price']}")
    print(f"Product With Greater Quantyti - name: {product_greater_quantity['name']} | quantyti: {product_greater_quantity['quantyti']}")