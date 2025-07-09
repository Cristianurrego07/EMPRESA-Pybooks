# desarrollo.py

def stock_marca(INFOR, stock, marca):
    marca = marca.lower()
    encontrados = False
    print(f"\nStock disponible para la marca {marca.upper()}:")
    for modelo_infor, info in INFOR.items():
        if info[0].lower() == marca:
            modelo_normalizado = modelo_infor.upper()
            for modelo_stock in stock:
                if modelo_stock.upper() == modelo_normalizado:
                    precio, cantidad = stock[modelo_stock]
                    print(f"Modelo: {modelo_normalizado} - Precio: ${precio:,} - Stock: {cantidad} unidades")
                    encontrados = True
                    break
    if not encontrados:
        print("No hay modelos disponibles para esa marca.")


def busqueda_precio(INFOR, stock, p_min, p_max):
    modelos_encontrados = []
    for modelo_stock, (precio, cantidad) in stock.items():
        if p_min <= precio <= p_max and cantidad > 0:
            modelo_normalizado = modelo_stock.upper()
            for modelo_info in INFOR:
                if modelo_info.upper() == modelo_normalizado:
                    marca = INFOR[modelo_info][0]
                    modelos_encontrados.append(f"{marca}--{modelo_normalizado}")
                    break
    if not modelos_encontrados:
        print("No hay notebooks en ese rango de precios.")
    else:
        modelos_encontrados.sort()
        print(f"\nModelos disponibles entre ${p_min:,} y ${p_max:,}:")
        for m in modelos_encontrados:
            print(m)


def actualizar_precio(stock, modelo, nuevo_precio):
    modelo_normalizado = modelo.upper()
    for key in stock:
        if key.upper() == modelo_normalizado:
            stock[key][0] = nuevo_precio
            return True
    return False
