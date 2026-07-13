
def mostrar_menu():
    print("""
========== MENÚ PRINCIPAL ==========
1. Stock por plataforma
2. Búsqueda de juegos por rango de precio
3. Actualizar precio de juego
4. Agregar juego
5. Eliminar juego
6. Salir
=====================================
""")


def leer_opcion():
    return input("Ingrese opción: ")


def buscar_codigo(codigo, juegos):
    codigo = codigo.upper()

    for cod in juegos:
        if cod.upper() == codigo:
            return cod

    return None


def stock_plataforma(plataforma, juegos, inventario):
    total = 0

    for codigo, datos in juegos.items():
        if datos[1].lower() == plataforma.lower():
            total += inventario[codigo][1]

    print(f"El total de stock disponibles es: {total}")


def busqueda_precio(p_min, p_max, juegos, inventario):
    lista = []

    for codigo, datos in inventario.items():
        precio = datos[0]
        stock = datos[1]

        if p_min <= precio <= p_max and stock > 0:
            titulo = juegos[codigo][0]
            lista.append(f"{titulo}--{codigo}")

    lista.sort()

    if len(lista) == 0:
        print("No hay juegos en ese rango de precios.")
    else:
        print("Los juegos encontrados son:", lista)


def actualizar_precio(codigo, nuevo_precio, juegos, inventario):
    codigo = buscar_codigo(codigo, juegos)

    if codigo is None:
        return False

    inventario[codigo][0] = nuevo_precio
    return True




def validar_codigo(codigo):
    return codigo.strip() != ""


def validar_titulo(titulo):
    return titulo.strip() != ""


def validar_plataforma(plataforma):
    return plataforma.strip() != ""


def validar_genero(genero):
    return genero.strip() != ""


def validar_clasificacion(clasificacion):
    return clasificacion.upper() in ["E", "T", "M"]


def validar_multiplayer(opcion):
    return opcion.lower() in ["s", "n"]


def validar_editor(editor):
    return editor.strip() != ""


def validar_precio(precio):
    return precio > 0


def validar_stock(stock):
    return stock >= 0


def agregar_juego(codigo, titulo, plataforma, genero,
                  clasificacion, multiplayer, editor,
                  precio, stock, juegos, inventario):

    if buscar_codigo(codigo, juegos) is not None:
        return False

    juegos[codigo] = [
        titulo,
        plataforma,
        genero,
        clasificacion,
        multiplayer,
        editor
    ]

    inventario[codigo] = [precio, stock]

    return True


def eliminar_juego(codigo, juegos, inventario):

    codigo = buscar_codigo(codigo, juegos)

    if codigo is None:
        return False

    del juegos[codigo]
    del inventario[codigo]

    return True




def main():

    juegos = {
        "G001": ["Eclipse Runner", "PC", "Acción", "T", True, "Nova"],
        "G002": ["Sky Battle", "PS5", "Acción", "M", True, "Sony"],
        "G003": ["Magic World", "Switch", "Aventura", "E", False, "Nintendo"],
        "G004": ["Racing Pulse", "PC", "Carreras", "E", True, "EA"],
        "G005": ["Mystic Farm", "PC", "Simulación", "E", False, "Blue"]
    }

    inventario = {
        "G001": [15000, 5],
        "G002": [25000, 3],
        "G003": [30000, 0],
        "G004": [18000, 2],
        "G005": [17000, 5]
    }

    while True:

        mostrar_menu()
        opcion = leer_opcion()

        if opcion == "1":

            plataforma = input("Ingrese plataforma a consultar: ")
            stock_plataforma(plataforma, juegos, inventario)

        elif opcion == "2":

            while True:

                try:
                    minimo = int(input("Ingrese precio mínimo: "))
                    maximo = int(input("Ingrese precio máximo: "))

                    if minimo >= 0 and maximo > minimo:
                        break

                except:
                    print("Debe ingresar valores enteros")

            busqueda_precio(minimo, maximo, juegos, inventario)

        elif opcion == "3":

            while True:

                codigo = input("Ingrese código del juego: ")

                while True:
                    try:
                        precio = int(input("Ingrese nuevo precio: "))
                        if precio > 0:
                            break
                    except:
                        pass

                if actualizar_precio(codigo, precio, juegos, inventario):
                    print("Precio actualizado")
                else:
                    print("El código no existe")

                otra = input("¿Desea actualizar otro precio (s/n)? ")

                if otra.lower() == "n":
                    break

        elif opcion == "4":

            codigo = input("Ingrese código del juego: ")
            titulo = input("Ingrese título: ")
            plataforma = input("Ingrese plataforma: ")
            genero = input("Ingrese género: ")
            clasificacion = input("Ingrese clasificación: ")
            multi = input("¿Es multiplayer? (s/n): ")
            editor = input("Ingrese editor: ")

            try:
                precio = int(input("Ingrese precio: "))
                stock = int(input("Ingrese stock: "))
            except:
                print("Precio o stock inválido")
                continue

            if not validar_codigo(codigo):
                print("Código inválido")
                continue

            if not validar_titulo(titulo):
                print("Título inválido")
                continue

            if not validar_plataforma(plataforma):
                print("Plataforma inválida")
                continue

            if not validar_genero(genero):
                print("Género inválido")
                continue

            if not validar_clasificacion(clasificacion):
                print("Clasificación inválida")
                continue

            if not validar_multiplayer(multi):
                print("Multiplayer inválido")
                continue

            if not validar_editor(editor):
                print("Editor inválido")
                continue

            if not validar_precio(precio):
                print("Precio inválido")
                continue

            if not validar_stock(stock):
                print("Stock inválido")
                continue

            multiplayer = multi.lower() == "s"

            if agregar_juego(
                codigo.upper(),
                titulo,
                plataforma,
                genero,
                clasificacion.upper(),
                multiplayer,
                editor,
                precio,
                stock,
                juegos,
                inventario
            ):
                print("Juego agregado")
            else:
                print("El código ya existe")

        elif opcion == "5":

            codigo = input("Ingrese código del juego: ")

            if eliminar_juego(codigo, juegos, inventario):
                print("Juego eliminado")
            else:
                print("El código no existe")

        elif opcion == "6":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida")


main()