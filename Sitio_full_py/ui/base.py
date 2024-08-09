import reflex as rx

# importamos la barra d enavegacion de nav.py
from .nav import navigator_bar

# cada argumento corresponde a un rx.**
#def base_page(a, b, c) -> rx.Component:

# aqui los argumentos se catalogan en dos, argumento y KeyArgumentos
# sin importar cuantos tengamos se cargan en automatico
# Child RX component se puede reemplazar por cualquier otro componente rx.***
def base_page(child: rx.Component, hide_navbar =False, *args, **kwargs) -> rx.Component:
    # si no es un compponent manda mensaje, se probo con "hola" como parametro, puedo hacer condiciones d ecualquier argumento
    if not isinstance(child, rx. Component):
        child = rx.heading("This is not a valid Child element here")
    
    if hide_navbar:        
        print("navbar is true")

    # impirmo en cosola los tres argumentos que recibi de index ()
    print([type(x) for x in args])


    # debo abrir el parentesis arriba para evitar errores
    return rx.container(
        # con pasar los argumentos ya se despliega la pagina
        #*args,

        # otra forma de en lugar de args es agregar child: rx.Component en los parametros y:
        # invocamos el nuevo codigo
        navigator_bar(),
        child,

        rx.color_mode.button(position="top-left"),
        rx.logo()
    )

