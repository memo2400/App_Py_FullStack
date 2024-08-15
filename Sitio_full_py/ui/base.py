from os import name
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

    # Si colocomeo  # comentario despues de abrir parentesis se omite este return
    # Usar fragment en lugar de container, acomoda mejor la nav bar, pero el contenido se 
    # queda mal colocado
    # return rx.container( 
    # https://reflex.dev/docs/library/layout/fragment/#fragment
    #return rx.fragment( 
    return rx.vstack( 
        # con pasar los argumentos ya se despliega la pagina
        #*args,

        # otra forma de en lugar de args es agregar child: rx.Component en los parametros y:
        # invocamos el nuevo codigo
        navigator_bar(),
        
        # El error era que no estaba identado lo del parentesis
        # es la caja donde coloco todo el cuerpo de la pagina, Sin Header ni Footer
        rx.box(
            child,
            # Aqui estan las propiedades de el contenido de la pagina
        
            # era un color cian, borre
            # bg=rx.color("accent", 3),
            padding="1em",       
            width="100%",
            # text_align="center", 
            id="my_content_ele_area",            
            
        ),

        rx.color_mode.button(position="button-left"),
        rx.logo(),
        
        # Baja el combo donde incia la pagina
        # padding="10em",
        
        id = "my_base_container", # habia usado name en lugar de id
        # text_align="center" # no funciono
    )



