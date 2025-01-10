# TuPrimeraPagina-Greyling
- Crea una web en Django utilizando Herencia de plantillas, con un modelo de por lo menos 3 clases, un formulario para ingresar datos a las 3 clases y un formulario para buscar algo en la BD, no hace falta que sea sobre las tres clases, con realizar búsqueda sobre una alcanzará.

-Te sugerimos que hagas  una web estilo blog para ir preparando en la entrega final.

====== Objetivos ======
Desarrollar tu primer WEB en Django utilizando patrón MVT

====== Requisitos ======
-Link de GitHub con el proyecto totalmente subido a la plataforma.
-Proyecto Web Django con patrón MVT que incluya:
-Herencia de HTML.
-Por lo menos 3 clases en models.
-Un formulario para insertar datos a por cada model creado..
-Un formulario para buscar algo en la BD
-Readme que indique el orden en el que se prueban las cosas y/o donde están las funcionalidades.
====== Formato ======
Link al repositorio de GitHub con el nombre “TuPrimeraPagina+Apellido”  por ejemplo “TuPrimeraPagina+Fernandez”

====== Uso de página ======
La página creada es una plataforma de registro e inventario de movimientos de combustible aplicado a una empresa operativa de helicópteros. Cuenta con una app control_combustible que es para registrar y ver carguíos de combustible a aeronaves, con una página que permite ingresar clases a modelos usados.
La app 'inventario' aún no se desarrolla, pero no es necesaria según los requisitos de entrega.

El uso sugerido de la página es: seguir la UI desde el home a la página que aparece como "Movimientos de Combustible" en la UI (url control_combustible), usar "crear datos de combustible" para ingresar por lo menos una clase a cada modelo.
Orden:
    - Modelo:
        Se debe crear primero para poder luego crear aeronave que lo requiere.
        Ejemplo de datos: Nombre de modelo H125, capacidad 540
    - Aeronave:
        Instancia con matrícula de una aeronave.
        Ejemplo de datos: 
            Modelo: seleccionar de la lista (H125)
            Capacidad: Capacidad 540
            Matricula: Ej CC-DHM
    -Camion:
        Patente: tipo ABCD12
        Capacidad: máximo de combustible que puede tener, ej 5000
        Contenido: combustible que contiene, de momento no se usa pero ideal igual o menor a capacidad
        Los otros 2 campos seleccionar fecha arbitraria, no se usa aún.
    -Usuario: autoexplicativo, hacer por lo menos 2 para tener despachador y receptor

Crear vale: teniendo ya las clases, se puede ocupar el formulario, llenar todas los campos.
Ej fecha de hoy, 320 litros, a Aeronave matricula CC-DHM, desde camión ABCD12, motivo Conaf, despachador Juanito Perez y receptor Jorgito Soto. se generará un número de vale automáticamente.

Buscar vale: se ingresa número de vale, mostrará los detalles del movimiento de combustible