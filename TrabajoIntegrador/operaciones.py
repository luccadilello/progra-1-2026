import datos

def listar_contenidos():
    print("\n--- LISTA DE CONTENIDOS ---")

    for i in range(len(datos.contenidos)):
        print("Código:", datos.codigosContenidos[i])
        print("Título:", datos.contenidos[i])
        print("Género:", datos.generos[i])
        print("Tipo:", datos.tipos[i])
        print("-------------------------")

def registrar_visualizacion(usuario_actual):
    contenido_ingresado = input(
        "\nIngrese el código o título del contenido: "
    ).strip()

    posicion_contenido = -1

    for i in range(len(datos.contenidos)):
        if (contenido_ingresado.lower() == datos.contenidos[i].lower()
                or contenido_ingresado.lower() == datos.codigosContenidos[i].lower()):
            posicion_contenido = i

    if posicion_contenido == -1:
        print("Contenido no existente.")

    else:
        posicion_usuario = datos.usuarios.index(usuario_actual)

        datos.visualizaciones[posicion_usuario][posicion_contenido] += 1

        print("\nVisualización registrada correctamente.")
        print(
            usuario_actual,
            "ahora tiene",
            datos.visualizaciones[posicion_usuario][posicion_contenido],
            "visualizaciones de",
            datos.contenidos[posicion_contenido]
        )

def buscar_contenido():
    busqueda = input(
        "\nIngrese el código o título del contenido: "
    ).strip()

    encontrado = False

    for i in range(len(datos.contenidos)):
        if (busqueda.lower() == datos.contenidos[i].lower()
                or busqueda.lower() == datos.codigosContenidos[i].lower()):

            print("\n--- CONTENIDO ENCONTRADO ---")
            print("Código:", datos.codigosContenidos[i])
            print("Título:", datos.contenidos[i])
            print("Género:", datos.generos[i])
            print("Tipo:", datos.tipos[i])

            encontrado = True

    if encontrado == False:
        print("Contenido no encontrado.")

def estadisticas_indicadores():

    print("\n--- ESTADÍSTICAS E INDICADORES ---")
    print("1. Visualizaciones totales por contenido")
    print("2. Porcentaje de usuarios que vio cada contenido")
    print("3. Contenido más visto por cada usuario")

    opcion = input("\nIngrese una opción: ")


    # 1. VISUALIZACIONES TOTALES POR CONTENIDO
    if opcion == "1":

        print("\n--- VISUALIZACIONES TOTALES ---")

        for columna in range(len(datos.contenidos)):

            total = 0

            for fila in range(len(datos.usuarios)):
                total += datos.visualizaciones[fila][columna]

            print(datos.contenidos[columna], ":", total)


    # 2. PORCENTAJE DE USUARIOS QUE VIO CADA CONTENIDO
    elif opcion == "2":

        print("\n--- PORCENTAJE DE USUARIOS ---")

        for columna in range(len(datos.contenidos)):

            cantidad_usuarios = 0

            for fila in range(len(datos.usuarios)):

                if datos.visualizaciones[fila][columna] > 0:
                    cantidad_usuarios += 1

            porcentaje = cantidad_usuarios * 100 / len(datos.usuarios)

            print(
                datos.contenidos[columna],
                "-",
                cantidad_usuarios,
                "usuarios -",
                porcentaje,
                "%"
            )


    # 3. CONTENIDO MÁS VISTO POR USUARIO
    elif opcion == "3":

        print("\n--- CONTENIDO MÁS VISTO POR USUARIO ---")

        for fila in range(len(datos.usuarios)):

            mayor = max(datos.visualizaciones[fila])

            print("\n", datos.usuarios[fila], ":")

            for columna in range(len(datos.contenidos)):

                if datos.visualizaciones[fila][columna] == mayor:
                    print(
                        datos.contenidos[columna],
                        "-",
                        mayor,
                        "visualizaciones"
                    )

    else:
        print("Opción inexistente.")

def ranking_informes():

    print("\n--- RANKINGS E INFORMES ---")
    print("1. Contenidos ordenados de mayor a menor")
    print("2. Contenidos ordenados de menor a mayor")
    print("3. Top 5 de contenidos más vistos")
    print("4. Top 5 de contenidos menos vistos")
    print("5. Total y porcentaje de usuarios por contenido")
    print("6. Contenidos con 5 o más visualizaciones")
    print("7. Contenido más visto por género")
    print("8. Contenido más visto por usuario")
    print("9. Listado general")

    opcion = input("\nIngrese una opción: ")


    # CALCULAR VISUALIZACIONES TOTALES
    totales = []

    for columna in range(len(datos.contenidos)):

        total = 0

        for fila in range(len(datos.usuarios)):
            total += datos.visualizaciones[fila][columna]

        totales.append(total)


    # CREAR LISTA PARA LOS RANKINGS
    ranking = []

    for i in range(len(datos.contenidos)):
        ranking.append((datos.contenidos[i], totales[i]))


    # 1. MAYOR A MENOR
    if opcion == "1":

        ordenados = sorted(
            ranking,
            key=lambda contenido: contenido[1],
            reverse=True
        )

        print("\n--- MAYOR A MENOR ---")

        for contenido in ordenados:
            print(contenido[0], "-", contenido[1])


    # 2. MENOR A MAYOR
    elif opcion == "2":

        ordenados = sorted(
            ranking,
            key=lambda contenido: contenido[1]
        )

        print("\n--- MENOR A MAYOR ---")

        for contenido in ordenados:
            print(contenido[0], "-", contenido[1])


    # 3. TOP 5 MÁS VISTOS
    elif opcion == "3":

        ordenados = sorted(
            ranking,
            key=lambda contenido: contenido[1],
            reverse=True
        )

        top5 = ordenados[:5]

        print("\n--- TOP 5 MÁS VISTOS ---")

        for contenido in top5:
            print(contenido[0], "-", contenido[1])


    # 4. TOP 5 MENOS VISTOS
    elif opcion == "4":

        contenidos_vistos = []

        for contenido in ranking:

            if contenido[1] > 0:
                contenidos_vistos.append(contenido)

        ordenados = sorted(
            contenidos_vistos,
            key=lambda contenido: contenido[1]
        )

        top5 = ordenados[:5]

        print("\n--- TOP 5 MENOS VISTOS ---")

        for contenido in top5:
            print(contenido[0], "-", contenido[1])


    # 5. TOTAL Y PORCENTAJE DE USUARIOS
    elif opcion == "5":

        print("\n--- USUARIOS POR CONTENIDO ---")

        for columna in range(len(datos.contenidos)):

            cantidad_usuarios = 0

            for fila in range(len(datos.usuarios)):

                if datos.visualizaciones[fila][columna] > 0:
                    cantidad_usuarios += 1

            porcentaje = cantidad_usuarios * 100 / len(datos.usuarios)

            print(
                datos.contenidos[columna],
                "-",
                cantidad_usuarios,
                "usuarios -",
                porcentaje,
                "%"
            )


    # 6. CONTENIDOS CON 5 O MÁS VISUALIZACIONES
    elif opcion == "6":

        cantidad = 0

        print("\n--- CONTENIDOS CON 5 O MÁS VISUALIZACIONES ---")

        for contenido in ranking:

            if contenido[1] >= 5:
                print(
                    contenido[0],
                    "-",
                    contenido[1],
                    "visualizaciones"
                )

                cantidad += 1

        print("\nCantidad total:", cantidad)


    # 7. CONTENIDO MÁS VISTO POR GÉNERO
    elif opcion == "7":

        print("\n--- CONTENIDO MÁS VISTO POR GÉNERO ---")

        generos_revisados = []

        for i in range(len(datos.generos)):

            genero_actual = datos.generos[i]

            if genero_actual not in generos_revisados:

                mayor = -1

                for j in range(len(datos.contenidos)):

                    if datos.generos[j] == genero_actual:

                        if totales[j] > mayor:
                            mayor = totales[j]

                print("\nGénero:", genero_actual)

                for j in range(len(datos.contenidos)):

                    if datos.generos[j] == genero_actual and totales[j] == mayor:
                        print(
                            datos.contenidos[j],
                            "-",
                            totales[j],
                            "visualizaciones"
                        )

                generos_revisados.append(genero_actual)


    # 8. CONTENIDO MÁS VISTO POR USUARIO
    elif opcion == "8":

        print("\n--- CONTENIDO MÁS VISTO POR USUARIO ---")

        for fila in range(len(datos.usuarios)):

            mayor = max(datos.visualizaciones[fila])

            print("\n", datos.usuarios[fila], ":")

            for columna in range(len(datos.contenidos)):

                if datos.visualizaciones[fila][columna] == mayor:

                    print(
                        datos.contenidos[columna],
                        "-",
                        mayor,
                        "visualizaciones"
                    )


    # 9. LISTADO GENERAL
    elif opcion == "9":

        print("\n--- LISTADO GENERAL ---")

        for i in range(len(datos.contenidos)):

            print(
                datos.codigosContenidos[i],
                "-",
                datos.contenidos[i],
                "-",
                datos.generos[i],
                "-",
                datos.tipos[i],
                "-",
                totales[i],
                "visualizaciones"
            )

    else:
        print("Opción inexistente.")

