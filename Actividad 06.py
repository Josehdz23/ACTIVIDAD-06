Productos = {}
def ingreso_Productos():
    while True:
        try:
            cantidad = int(input("\nIngrese la cantidad de productos que desea ingresar: "))
            if cantidad > 0:
                for i in range(cantidad):
                    while True:
                        try:
                            codigo = int(input(f"\nIngrese el codigo del producto {i+1}: "))
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
                        nombre = input(f"Ingrese el nombre del producto {i+1}: ")
                        if nombre or nombre.isspace():
                            break
                        else:
                            print("\nEl nombre del producto no es valido, reintente")
                    while True:
                        categoria = input(f"Ingrese la categoria del producto {i+1} (Hombre,Mujer,Niño): ")
                        if categoria or categoria.isspace():
                            categoria = categoria.upper()
                            if (categoria == "HOMBRE" or categoria == "MUJER" or categoria == "NIÑO"):
                                break
                            else:
                                print("\nLa categoria del producto no es valida, reintente")
                        else:
                            print("\nLa categoria del producto no es valida, reintente")
                    while True:
                        talla = input(f"Ingrese la talla del producto {i+1} (S,M,L,XL): ")
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
                            precio = float(input(f"Ingrese el precio del producto {i+1}: "))
                            if precio > 0:
                                b = 1
                            else:
                                print("\nEl precio del producto no es valido, reintente")
                        except Exception as ex2:
                            print(f"Ocurrió un error: {ex2}")
                    b = 0
                    while b == 0:
                        try:
                            stock = int(input(f"Ingrese el stock del producto {i+1} en tienda: "))
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
    print("\n- - - - INVENTARIO - - - -\n1. Agregar productos\n2. Buscar producto (por codigo)\n3. Valor total del inventario\n4. Mostrar total de productos por categoria\n5. Mostrar todo el inventario\n6. Salir")

def buscar_producto():
    if Productos:
        while True:
            try:
                busqueda = int(input("\nIngrese el codigo del producto a buscar: "))
                if busqueda in Productos:
                    print(
                        f"\nNombre: {Productos[busqueda]['Nombre']}, Categoria: {Productos[busqueda]['Categoria']}, Talla: {Productos[busqueda]['Talla']}, Precio: {Productos[busqueda]['Precio']}, Stock: {Productos[busqueda]['Stock']}")
                    break
                else:
                    print("\nEl producto no existe")
                    break
            except Exception as ex:
                print(f"\nHa ocurrido un error: {ex}")
    else:
        print("\nNo hay productos para buscar! ")

def valor_Total_inventario():
    suma = 0
    for codigo, datos in Productos.items():
        suma += datos["Precio"] * datos["Stock"]
    print(f"\nValor total del inventario: Q{suma}")

def mostrar_Inventario_Categoria():
    stockNiños = 0
    stockMujeres = 0
    stockHombres = 0
    for clave, datos in Productos.items():
        if datos["Categoria"] == "HOMBRE":
            stockHombres += datos["Stock"]
        if datos["Categoria"] == "MUJER":
            stockMujeres += datos["Stock"]
        if datos["Categoria"] == "NIÑO":
            stockNiños += datos["Stock"]
    print(f"\n- - - - CATEGORIAS - - - -\nStock de Hombres: {stockHombres}\nStock de Mujeres: {stockMujeres}\nStock de Niños: {stockNiños}")

def mostrar_Inventario_Completo():
    if Productos:
        for codigo, datos in Productos.items():
            print(
                f"\nCodigo: {codigo}, Nombre: {datos['Nombre']}, Categoria: {datos['Categoria']}, Talla: {datos['Talla']}, Precio: {datos['Precio']}, Stock: {datos['Stock']}")
    else:
        print("\nNo hay productos en el inventario!")

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
                    mostrar_Inventario_Categoria()
                case 5:
                    mostrar_Inventario_Completo()
                case 6:
                    print("Saliendo...")
                    break
                case _:
                    print("Esa opcion no existe, reintente")
        except Exception as ex:
            print(f"\nHa ocurrido un error: {ex}")
main()