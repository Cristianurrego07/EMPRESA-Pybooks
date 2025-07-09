# proyecto.py

from desarrollo import stock_marca, busqueda_precio, actualizar_precio

# Diccionario principal
INFOR = {
    "8475HD": ["HP", 15.6, "8GB", "DD", "1T", "Intel core i5", "Nvidia GTX1050"],
    "2175HD": ["lenovo", 14, "4GB", "SSD", "512GB", "Intel core i5", "Nvidia GTX1050"],
    "JjfFHD": ["Asus", 14, "16GB", "SSD", "256GB", "Intel core i7", "Nvidia RTX2080Ti"],
    "fgdxFHD": ["HP", 15.6, "8GB", "DD", "1T", "Intel core i3", "integrada"],
    "GF75HD": ["Asus", 15.6, "8GB", "DD", "1T", "Intel core i7", "Nvidia GTX1050"],
    "123FHD": ["lenovo", 14, "6GB", "DD", "1T", "AMD Ryzen 5", "integrada"],
    "342FHD": ["lenovo", 15.6, "8GB", "DD", "1T", "AMD Ryzen 7", "Nvidia GTX1050"],
    "UWU131HD": ["Dell", 15.6, "8GB", "DD", "1T", "AMD Ryzen 3", "Nvidia GTX1050"],
}

# Diccionario de stock (normalizado a mayúsculas)
stock_original = {
    "8475Hd": [387990, 10], "2175HD": [327990, 4], "JjfFHD": [424990, 1],
    "fgdxFHd": [664990, 21], "123FHD": [290890, 32], "342FHD": [444990, 7],
    "GF75Hd": [749990, 2], "UWU131HD": [349990, 1], "FS1230HD": [249990, 0],
}
# Normalizar claves a mayúsculas
stock = {k.upper(): v for k, v in stock_original.items()}

# Menú principal
while True:
    print("\n------ MENÚ PROYECTO ------")
    print("1. Stock por marca")
    print("2. Búsqueda por precio")
    print("3. Actualizar precio")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        marca = input("\nIngrese la marca: ")
        stock_marca(INFOR, stock, marca)

    elif opcion == "2":
        while True:
            try:
                p_min = int(input("\nIngrese el precio mínimo: "))
                p_max = int(input("Ingrese el precio máximo: "))
                if p_min > p_max:
                    print("El precio mínimo no puede ser mayor que el máximo.")
                    continue
                break
            except ValueError:
                print("Debe ingresar valores enteros!!")
        busqueda_precio(INFOR, stock, p_min, p_max)

    elif opcion == "3":
        while True:
            modelo = input("\nIngrese el modelo que desea actualizar: ")
            try:
                nuevo_precio = int(input("Ingrese el nuevo precio: "))
            except ValueError:
                print("Debe ingresar un precio válido (entero)!")
                continue

            actualizado = actualizar_precio(stock, modelo, nuevo_precio)
            if actualizado:
                print("Precio actualizado!!")
            else:
                print("El modelo no existe!!")

            continuar = input("¿Desea actualizar otro precio? (si/no): ").strip().lower()
            if continuar != "si":
                break

    elif opcion == "4":
        print("\nPrograma finalizado.")
        break

    else:
        print("Debe seleccionar una opción válida!!")

