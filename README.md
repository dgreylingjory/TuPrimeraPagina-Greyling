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

============================= Ejecución =====================================

Se creará una página web (con la idea de luego usarla cono base para aplicación móvil) basada en una aplicación que tendrá el objetivo de controlar movimientos de combustible dentro de una empresa aeronáutica, del rubro de trabajo aéreo con helicópteros.

El fin es reemplazar el sistema actual que se basa en registros escritos en papel.

====== Funcionalidad esperada ======
-Registro de usuarios gestionado por un superuser.
-Login de usuarios.
-Ingreso de movimientos de combustible (carguío, trasvasije entre camiones/estanques flota propia, prestamos desde y hacia flotas de terceros, compras de combustible desde abastecedores externos).
-Generación de comprobantes de carguíos/movimientos de combustible con firma digital por usuario emisor y usuario receptor.
-Manejo de inventario de combustible.
-Generar archivos PDF para comprobantes de combustible, inventario de combustible. (No requerido para entrega, investigar implementación)
-Crear app móvil que permita uso fuera de la red, que permita actualizar inventarios una vez se vuelva a conectar a la red. (No requerido para entrega, investigar implementación)

====== Plan de Estructura ======
-Usuarios como clases:
    1. Una clase padre genérica (podría ser para invitado, no requiere login, solo puede firmar recepción de documentos)
    2. Clase usuario interno, receptor (hereda de clase 1): requiere login, puede firmar recepción de movimientos de combustible, tiene acceso para visualizar movimientos e inventarios, descargar comprobantes de estos.
    3. Clase usuario interno, emisor (hereda de clase 2): además de lo que puede realizar receptor, puede generar movimientos de combustible e inventarios.
    4. Clase usuario 'supervisor' (hereda todo lo anterior): además de todo lo anterior, puede crear usuarios, eliminar y modificar movimientos, modificar inventarios de combustible. No tiene privilegios admin. Puede agregar o modificar lista de despachadores de combustible (estanque/camión/tambores/aeronave).

    Atributos de clase se pueden utilizar para definir acceso, metodos de clase para la ejecución de funciones

-Despachadores como clases:
    -Clase para cada despachador de combustible (estanque/camion/tambor/aeronave) que contenga capacidad de combustible, tipo, vencimiento certificación como atributos, métodos para determinar carguío inválido (se carga más que capacidad máxima), certificación vencida; deberían generar alerta en registro de movimiento.
    -Podría utilizarse misma clase como receptor físico de carguíos.
    -En aeronave podría generarse clase separada por modelo (H125, H135, H145, otros), y tambores aparte, para que capacidad sea atributo de clase y no de instancia.

-App dedicada a movimientos de combustible:
    -Debe requerir login:
        -Este debe tener zona de invitado para externos que solo firmen recepción.
    -Según privilegios de usuario ofrecer distintas opciones:
        -Firmar recepción (todos los usuarios)
        -Generar movimiento (emisor, supervisor)
        -Ver movimientos (receptor, emisor, supervisor)
            -Podría incluir vista por lista, filtros según usuario de emisor/receptor, número de movimiento, despachador de combustible, receptor físico de combustible, fecha.
            -Generar y descargar comprobante del movimiento requerido.
            -Podría ser llevado a cabo con querys a la db.
        -Modificar movimientos (supervisor)
            Misma UI que ver, pero da opción de editar/eliminar en vez de ver comprobante.
    -Los movimientos una vez ingresados deben quedar guardados en la db
    -Opción para registrar drenajes para test por agua de combustible (estanque/tambor/camión).
    -Opción para registrar merma por drenaje.
    -Opción para ingresar ingresos (compra) de combustible.
        -Considerar dashboard costos de combustible (complejo, requiere valorizar el combustible por cada compra, precio muy variable)
    -Opción para registrar préstamos/devoluciones de combustible (quizás solo para supervisor?)

-App dedicada a inventario:
    -Requiere login, emisor o supervisor.
    -Genera documento de 'flujo de caja' de combustibles, por rango de fecha.
        -Una opción por despachador, separado, no debe incluir aeronaves.
        -Una opción por flota de despachadores.
        -Se debe generar automáticamente a base de los movimientos ingresados en db
    -'Flujo de caja' de combustible: debe dar resumen de datos de combustibles abastecidos a aeronaves, cantidad de combustible de merma en drenajes para test por agua o por derrame, cantidad de combustible que ingresa (comprado), alerta de préstamos de combustible no resueltos.
    

    