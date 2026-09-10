import datos
import operaciones


def main():
    salir = False

    while salir == False:

        # LISTADO DE USUARIOS
        print("\n--- LISTA DE USUARIOS ---")

        for i in range(len(datos.usuarios)):
            print(
                str(i + 1) + ".",
                datos.codigosUsuarios[i],
                "-",
                datos.usuarios[i]
            )


        # SELECCIÓN Y VALIDACIÓN DEL USUARIO
        usuario_actual = None

        while usuario_actual == None:

            ingreso = input(
                "\nIngrese el nombre o código del usuario: "
            ).strip()

            for i in range(len(datos.usuarios)):

                if (
                    ingreso.lower() == datos.usuarios[i].lower()
                    or
                    ingreso.lower() == datos.codigosUsuarios[i].lower()
                ):
                    usuario_actual = datos.usuarios[i]

            if usuario_actual == None:
                print("Usuario o código no válido. Intente nuevamente.")


        print("\nUsuario seleccionado:", usuario_actual)


        # MENÚ PRINCIPAL
        cambiar_usuario = False

        while salir == False and cambiar_usuario == False:

            print("\n--- MENÚ PRINCIPAL ---")
            print("1. Listar contenidos")
            print("2. Registrar visualización")
            print("3. Buscar contenido")
            print("4. Estadísticas e indicadores")
            print("5. Ranking e informes")
            print("6. Cambiar usuario")
            print("7. Salir")

            opcion = input("\nIngrese una opción: ").strip()


            if opcion == "1":
                operaciones.listar_contenidos()


            elif opcion == "2":
                operaciones.registrar_visualizacion(usuario_actual)


            elif opcion == "3":
                operaciones.buscar_contenido()


            elif opcion == "4":
                operaciones.estadisticas_indicadores()


            elif opcion == "5":
                operaciones.ranking_informes()


            elif opcion == "6":
                cambiar_usuario = True
                print("\nCambiando usuario...")


            elif opcion == "7":
                salir = True
                print("\nPrograma finalizado.")


            else:
                print("\nOpción inexistente. Intente nuevamente.")


if __name__ == "__main__":
    main()