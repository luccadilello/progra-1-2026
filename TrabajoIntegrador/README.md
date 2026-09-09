Alcance del proyecto
El sistema permite registrar, consultar y analizar el consumo de películas y series de un grupo de 10 usuarios, utilizando las visualizaciones realizadas por el grupo para generar estadísticas, rankings e información que facilite la elección de contenidos. 
Limite: datos no persistentes. Los datos ingresados solamente tienen vida útil mientras el sistema esté ejecutándose. Al tocar la opción de “Salir”, todos los datos que no están en las matrices iniciales, se borran.
El sistema contempla las siguientes capacidades:
Presentación general: al iniciar el sistema se muestra en terminal un menú con las opciones disponibles que el usuario puede realizar: 
Listar Contenidos 
Registrar visualización 
Buscar contenido
Estadísticas e indicadores
Ranking e informes
Salir.
Va a haber una matriz preexistente de los contenidos vistos por cada usuario y listas de series o películas, géneros y tipos.

Lista de títulos:
[“Game Of Thrones”, “Shrek”, “Cars”]

Lista de géneros:
[“Fantasía”, “Ciencia Ficción”, “Acción”]

Tupla de tipos:
(“Película”, “Serie”, “Show”)

Lista de códigos de contenidos:
[“C01”, “C02”, “C03”]

Lista de Usuarios: 
[“Esteban”, “Sofi”, “Lucca”,”Mariangel”, “Pepe”, “Roberto”, “Andres”, “Luciana”, “Micaela”, “Tomas”]
Los usuarios van a poder agregar películas o series.
Registro de datos: El usuario carga qué contenido vio y el nombre de la persona, y se le suma +1 a las visualizaciones de ese usuario del contenido. En caso de que no exista el contenido, se muestra un mensaje de error: “Contenido no existente”


Consulta de datos cargados: El usuario puede listar los contenidos con sus respectivos géneros y tipos.


Cálculos e indicadores (mínimo 3): El usuario va a poder visualizar:
cantidad de visualizaciones por título: suma de todas las visualizaciones realizadas por todos los usuarios para ese contenido. 
porcentaje de usuarios que hayan visto por lo menos una vez cada contenido, según la cantidad de usuarios totales.. 
Contenido más visto por cada usuarios 


Búsqueda: por código o título.


Detección de condición destacable: 
Contenidos con 5 o más visualizaciones totales. 
Top 5 menos vistos: ordenar de menor a mayor solamente los contenidos que posean al menos una visualización total y mostrar hasta los primeros cinco. 


Informes finales (mínimo 5): 
Contenidos ordenados de mayor a menor cantidad de visualizaciones. (lambda)
Contenidos ordenados de menor a mayor cantidad de visualizaciones. (lambda)
Ranking Top 5 de contenidos más vistos. (slicing) 
Top 5 de contenidos menos vistos, excluyendo los que tengan 0. (slicing) 
Total y porcentaje de usuarios que visualizó cada contenido.
Contenidos con 5 o más visualizaciones y cantidad total de ellos.
Contenido/s más visto/s por género.
Contenido/s más visto/s por usuario.
Listado con título, género, tipo y visualizaciones. 


Menú activo: el sistema y los datos adicionales cargados a las matrices permanecen disponibles hasta que el usuario selecciona la opción de salir.
Validaciones: 
El usuario fue no seleccionado al intentar registrar una reproducción
Código de contenido repetido.
No permitir agregar dos veces el mismo título al catálogo.
No permitir títulos vacíos.
Validar los géneros permitidos.
Al registrar una visualización, verificar que el contenido exista.
Evitar problemas de mayúsculas/minúsculas en las búsquedas: "Shrek", "shrek" y "SHREK" deberían encontrar el mismo contenido.
Opción de menú inexistente.
Al seleccionar Salir, termina el programa.
Fuera de Alcance 
Persistencia de datos / Base de datos 
inicio de sesión 
Agregar o eliminar contenidos, géneros, tipos o usuarios
