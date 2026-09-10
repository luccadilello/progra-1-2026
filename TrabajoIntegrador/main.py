import datos
import operaciones

def main():
    salir = False

    while salir == False:

        # INGRESO Y VALIDACIÓN DEL USUARIO
        usuario_actual = None   

        while usuario_actual == None:
            nombre = input("Ingrese su nombre de usuario: ").strip()

            for usuario in datos.usuarios:
                if usuario.lower() == nombre.lower():
                    usuario_actual = usuario

            if usuario_actual == None:
                print("Usuario no válido. Intente nuevamente.")

        print("\nBienvenido/a,", usuario_actual)


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

            opcion = input("\nIngrese una opción: ")

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
                print("\nCambiando usuario...")
                cambiar_usuario = True

            elif opcion == "7":
                print("\nPrograma finalizado.")
                salir = True

            else:
                print("\nOpción inexistente. Intente nuevamente.")


main()