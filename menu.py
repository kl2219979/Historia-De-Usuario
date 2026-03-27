from services.functions import add_product,show_product,search_product,update_product,remove_product,calculate_statistics_inventory

def menu():
    while True:
        print("\n*** MENU ***")
        print("1. Agregar")
        print("2. Mostar")
        print("3. Buscar")
        print("4. Actualizar")
        print("5. Eliminar")
        print("6. Estadisticas")
        print("7. Guardar CSV")
        print("8. Cargar CSV")
        print("9. Salir")
        option = int(input("Ingrese el numero de la opcion que desea realizar: "))
        
        match option:
            case 1:
                add_product()
            case 2:
                show_product()
            case 3:
                search_product()
            case 4:
                update_product()
            case 5:
                remove_product()
            case 6:
                calculate_statistics_inventory()
            case 7:
                pass
            case 8:
                pass
            case 9:
                print("Saliendo del Programa ....")
                break
            case _:
                print("Error, intentalo de nuevo")

menu()