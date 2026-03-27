from functions import add_product, show_inventory, calculate_statistics_inventory

def menu():
    while True:
        print("** Menu **")
        print("1. agregar")
        print("2. Mostrar")
        print("3. calcular estadisticas")
        print("4. salir")
        option = int(input("Ingrese el numero de la opcion que desea realizar:"))
        
        match option:
            case 1:
                add_product()
            case 2:
                show_inventory()
            case 3:
                calculate_statistics_inventory()
            case 4:
                print("saliendo del programa...")
                break
            case _:
                print("Error, intentalo de nuevo")