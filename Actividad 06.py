Productos = {}
def ingreso_Productos():
    while True:
        try:
            cantidad = int(input("\nIngrese la cantidad de productos que desea ingresar: "))
            for i in range(cantidad):
                while True:
                    codigo = int(input("\nIngrese el codigo del producto: "))
                    if codigo > 0:
                        break
                    else:
                        print("\nEl codigo del producto no es valido")
                while True:
                    nombre = input("Ingrese el nombre del producto: ")
                    if nombre or nombre.isspace():
                        break
                    else:
                        print("\nEl nombre del producto no es valido")
                while True:
                    categoria = input("Ingrese la categoria del producto: ")
                    if categoria or categoria.isspace():
                        break
                    else:
                        print("\nLa categoria del producto no es valida")
                while True:
                    talla = input("Ingrese la talla del producto (S,M,L,XL): ")
                    if talla or talla.isspace():
                        break
                    else:
                        print("\nLa talla del producto no es valida")
                b = 0
                while b == 0:
                    try:
                        precio = float(input("Ingrese el precio del producto: "))
                        if precio > 0:
                            b = 1
                        else:
                            print("\nEl precio del producto no es valido")
                    except Exception as ex2:
                        print(f"Ocurrió un error: {ex2}")
                b = 0
                while b == 0:
                    try:
                        stock = int(input("Ingrese el stock del producto en tienda: "))
                        if stock > 0:
                            b = 1
                        else:
                            print("\nEl stock del producto no es valido")
                    except Exception as ex3:
                        print(f"Ocurrió un error: {ex3}")
        except Exception as ex:
            print(f"\nHa ocurrido un error: {ex}")
def menu():
    print("\n- - - - INVENTARIO - - - -\n1. Agregar productos\n2. Buscar producto (por codigo)\n3. Valor total del inventario\n4. Mostrar total de productos en tienda\n5. Salir")

def main():
    while True:
        try:
            menu()
            opcion = int(input("Seleccione una opción: "))
            match opcion:
                case 1:
                    ingreso_Productos()
                case 5:
                    print("\nSaliendo...")
                    break
                case _:
                    print("Esa opcion no existe, reintente")
        except Exception as ex:
            print(f"\nHa ocurrido un error: {ex}")
main()