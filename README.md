## Nombre del proyecto = "Automatización de pruebas con Selenium en python para UrbanRoutes"

## Descripcion de proyecto:
# El presente trabajo está diseñado para automatizar la prueba de una aplicación web de rutas urbanas utilizando
# Selenium WebDriver en Python. El objetivo principal es validar diversas funcionalidades de la aplicación, como
# el proceso de reserva de un taxi, la introducción de información del usuario (como número de teléfono y tarjeta
# de crédito), y la selección de opciones adicionales para el viaje y la espera del conductor.

## Tecnologías y Técnicas Utilizadas
# En este proyecto se utiliza:
# "Python" como lenguaje de programación utilizado para escribir las pruebas automatizadas.
# "Selenium WebDriver" como herramienta para la automatización de pruebas de aplicaciones web, ya que, permite la interacción con los elementos de la página web y la simulación de acciones de usuario.
# "ChromeDriver" como controlador del navegador Chrome para interactuar con la aplicación web.
# JSON como formato de intercambio de datos utilizado para manejar la información del código y para la confirmación del teléfono.

## Estructura del Proyecto
# El archivo "data.py" contiene datos de prueba y configuraciones para realizar las pruebas.
# El archivo "main.py" contiene la clase:
# "UrbanRoutesPage" que encapsula las interacciones con la página de la aplicación web
# y la clase "TestUrbanRoutes" con las pruebas automatizadas que validan la funcionalidad de la aplicación.
# El archivo "README.md" contiene informacion del proyecto, describe las tecnologias y tecnicas utilizadas
# e instrucciones sobre como ejecutar la prueba.

## Instrucciones y funciones para realizar las pruebas
# Para el archivo "helpers.py" se cuenta con:
# La funcion "retrieve_phone_code" devuelve un número de confirmación de teléfono como un string, necesario en una
# de las pruebas que se explicaran mas adelante.
# Para el archivo "urban_routes_page.py" se cuenta con:
# La clase "UrbanRoutesPage" almacena los localizadores necesarios que permitiran interactuar con la pagina, asi
# como tambien a las funciones basicas (hacer click, rellenar un campo, esperar que aparezca un indicador, confirmar
# un dato colocado en un campo, etc.)
# Para el archivo "main.py" se cuenta con:
# La importacion de todas las librerias necesarias para correr las pruebas (en las primeras lineas de codigo).
# La clase "TestUrbanRoutes" contiene la subclase setup_class que permite mantener un registro adicional para
# recuperar el codigo enviado al numero de telefono registrado en la pagina.
# La clase "TestUrbanRoutes" almacena las pruebas a realizar dentro de la pagina.
# La prueba "test_start_navigator" abre el navegador "Chrome" llamando la direccion URL del archivo "data.py"
# La prueba "test_set_route" llama la prueba "test_start_navigator", asigna los valores de direccion almacenados
# en el archivo "data.py" y confirma que los valores colocados en los campos "from" y "to" sean iguales a los del
# archivo "data.py".
# La prueba "test_comfort_fee" llama la prueba "test_set_route" y presiona los botones de "flash mode", "comfort fee"
# y "pedir un taxi".
# La prueba "test_fill_phone_number" llama la prueba "test_comfort_fee", agrega el telefono almacenado en "data.py"
# y confirma que el numero agregado sea igual que al que se encuentra en el archivo "data.py", presiona el boton siguiente
# de la ventana de "agregar numero de telefono", llama la funcion "retrieve_phone_code", almacena el string de la funcion 
# en el campo "code", confirma que el dato almacenado en el codigo sea el mismo que arroja la funcion "retrieve_phone_code"
# y presiona el boton confirmar de la ventana para que los datos se registren.
# La prueba "test_add_credit_card" llama la prueba "test_fill_phone_number", presiona la opcion "agregar tarjeta de credito"
# agrega el numero de la tarjeta y el codigo de la misma almacenados en el archivo "data.py", confirma que los datos
# agregados coincidan con los indicados en el archivo "data.py" y cierran la ventana "agregar tarjeta de credito".
# La prueba "test_write_a_message_to_driver" llama la prueba "test_add_credit_card", agrega un mensaje para el conductor
# en el campo "mensaje para conductor" y confirma que el dato coincida con el mensaje almacenado en el archivo "data.py".
# La prueba "test_ask_for_a_blanket" llama la prueba "test_write_a_message_to_driver" y presiona el boton "Mantas y pañuelos"
# La prueba "test_ask_for_two_icecreams" llama la prueba "test_ask_for_a_blanket" y presiona dos veces en el boton "helado"
# agregando dos unidades de este producto.
# La prueba "test_taxi_modal_appearing" llama la prueba "test_ask_for_two_icecreams", presiona el boton "reservar",
# y confirma que la ventana que contiene el modal de la reserva si se presente.
# La prueba "test_driver_information_appearing" llama la prueba "test_taxi_modal_appearing" y confirma que despues de
# pasados 45 segundos aparezca la informacion del conductor.

# Los datos del archivo "data.py" son modificables para generar nuevas pruebas, sin embargo, añadir "requisitos de pedido"
# se requieren añadir pruebas adicionales.