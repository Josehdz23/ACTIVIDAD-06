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
                categoria = input("Ingrese la categoria del producto: ")
                talla = input("Ingrese la talla del producto (S,M,L,XL): ")
                precio = float(input("Ingrese el precio del producto: "))
                stock = int(input("Ingrese el stock del producto en tienda: "))
        except Exception as ex:
            print(f"\nHa ocurrido un error: {ex}")