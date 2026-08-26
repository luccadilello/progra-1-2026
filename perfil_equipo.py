def modificaciones(nombre, nombre_equipo):
    for i in range(len(nombre)):
        nombre[i] = nombre[i].title()

    nombre_equipo = nombre_equipo.upper()
    letras = len(nombre_equipo)

    sigla = []
    palabra = nombre_equipo.split()
    for i in palabra:
        sigla.append(i[0])

    tiene_digito = False
    for caracter in nombre_equipo:
        if caracter.isdigit():
            tiene_digito = True

    return nombre, nombre_equipo, letras, sigla, tiene_digito

def main():
    equipo = int(input("Ingrese numero del equipo: "))
    nombre_equipo = input("Ingrese nombre del equipo: ")
    integrantes = int(input("Ingrese cant. de integrantes: "))

    grupo_nombre = []
    grupo_comision = []
    grupo_rol = []
    for i in range(integrantes):
        nombre = input("Ingrese nombre del integrante: ")
        grupo_nombre.append(nombre)
        comision = input("Ingrese comision del integrante: ")
        grupo_comision.append(comision)
        rol = input("Ingrese rol del integrante: ")
        grupo_rol.append(rol)

    grupo_nombre, nombre_equipo, letras, sigla, tiene_digito = modificaciones(grupo_nombre, nombre_equipo)
    print(f"nombre equipo: {nombre_equipo}")
    print(f"cant letras: {letras}")
    for i in range(len(grupo_nombre)):
        print(f"{grupo_nombre[i]} - {grupo_comision[i]} - {grupo_rol[i]}")
    print(f"Siglas con nombre del equipo: {sigla}")
    print(f"el nombre del equipo contiene digitos: {tiene_digito}")
main()
