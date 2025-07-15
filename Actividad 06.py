Productos = {}
def ingreso_Productos():
    while True:
        try:
            cantidad = int(input("\nIngrese la cantidad de productos que desea ingresar: "))
            if cantidad > 0:
                for i in range(cantidad):
                    while True:
                        try:
                            codigo = int(input("\nIngrese el codigo del producto: "))
                            if codigo > 0:
                                if codigo in Productos.keys():
                                    print("\nEste codigo ya existe, reintente")
                                else:
                                    break
                            else:
                                print("\nEl codigo del producto no es valido, reintente")
                        except Exception as e:
                            print(f"Ha ocurrido un error: {e}")
                    while True:
                        nombre = input("Ingrese el nombre del producto: ")
                        if nombre or nombre.isspace():
                            break
                        else:
                            print("\nEl nombre del producto no es valido, reintente")
                    while True:
                        categoria = input("Ingrese la categoria del producto(Hombre,Mujer,Niño): ")
                        if categoria or categoria.isspace():
                            categoria = categoria.upper()
                            if (categoria == "HOMBRE" or categoria == "MUJER" or categoria == "NIÑO"):
                                break
                            else:
                                print("\nLa categoria del producto no es valida, reintente")
                        else:
                            print("\nLa categoria del producto no es valida, reintente")
                    while True:
                        talla = input("Ingrese la talla del producto (S,M,L,XL): ")
                        if talla or talla.isspace():
                            talla = talla.upper()
                            if (talla == "S" or talla == "M" or talla == "L" or talla == "XL"):
                                break
                            else:
                                print("\nLa talla del producto no es valida, reintente")
                        else:
                            print("\nLa talla del producto no es valida, reintente")
                    b = 0
                    while b == 0:
                        try:
                            precio = float(input("Ingrese el precio del producto: "))
                            if precio > 0:
                                b = 1
                            else:
                                print("\nEl precio del producto no es valido, reintente")
                        except Exception as ex2:
                            print(f"Ocurrió un error: {ex2}")
                    b = 0
                    while b == 0:
                        try:
                            stock = int(input("Ingrese el stock del producto en tienda: "))
                            if stock > 0:
                                b = 1
                            else:
                                print("\nEl stock del producto no es valido, reintente")
                        except Exception as ex3:
                            print(f"Ocurrió un error: {ex3}")
                    Productos[codigo] = {
                        "Nombre": nombre,
                        "Categoria": categoria,
                        "Talla": talla,
                        "Precio": precio,
                        "Stock": stock,
                    }
                    print("Se ha guardado el producto")
                break
            else:
                print("Dato invalido, reintente")
        except Exception as ex:
            print(f"\nHa ocurrido un error: {ex}")
def menu():
    print("\n- - - - INVENTARIO - - - -\n1. Agregar productos\n2. Buscar producto (por codigo)\n3. Valor total del inventario\n4. Mostrar total de productos en tienda\n5. Salir")

def buscar_producto():
    while True:
        try:
            busqueda = int(input("\nIngrese el codigo del producto a buscar: "))
            if busqueda in Productos:
                print(
                    f"Nombre: {Productos[busqueda]['Nombre']}, Categoria: {Productos[busqueda]['Categoria']}, Talla: {Productos[busqueda]['Talla']}, Precio: {Productos[busqueda]['Precio']}, Stock: {Productos[busqueda]['Stock']}")
                break
            else:
                print("\nEl producto no existe")
                break
        except Exception as ex:
            print(f"\nHa ocurrido un error: {ex}")
def valor_Total_inventario():
    suma = 0
    for codigo, datos in Productos.items():
        suma += datos["Precio"] * datos["Stock"]
    print(f"Valor total del inventario: Q{suma}")
def main():
    while True:
        try:
            menu()
            opcion = int(input("Seleccione una opción: "))
            match opcion:
                case 1:
                    ingreso_Productos()
                case 2:
                    buscar_producto()
                case 3:
                    valor_Total_inventario()
                case 4:
                    for codigo, datos in Productos.items():
                        print(f"Codigo: {codigo}, Nombre: {datos["Nombre"]}, Categoria: {datos["Categoria"]}, Talla: {datos["Talla"]}, Precio: {datos["Precio"]}, Stock: {datos["Stock"]}")
                case 5:
                    print("\nSaliendo...")
                    break
                case _:
                    print("Esa opcion no existe, reintente")
        except Exception as ex:
            print(f"\nHa ocurrido un error: {ex}")
main()