"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from tkinter.tix import Tree
from turtle import position
import reflex as rx
from sqlalchemy import true

from rxconfig import config


class State(rx.State):
    """The app state."""
    label = "Bienvenido a Reflex "

    def handle_title_input_change(self, val):
        self.label = val
    
    def did_clic(self):
        # esta impresion se haria en consola y no se muestra en el front
        print ("hello worl")

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )

#  Sorce https://reflex.dev/docs/recipes/layout/navbar/

def navigator_bar() -> rx.Component:
    return rx.box(
        #position=="top-left",
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Reflex", size="7", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", "/#"),
                    navbar_link("About", "/#"),
                    navbar_link("Pricing", "/#"),
                    navbar_link("Contact", "/#"),
                    spacing="5",
                ),
                rx.hstack(
                    rx.button(
                        "Sign Up",
                        size="3",
                        variant="outline",
                    ),
                    rx.button("Log In", size="3"),
                    spacing="4",
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        # estos son para cuando se ajusta exactamente al tamaño
        rx.mobile_only(),
        rx.tablet_only(),
        
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Reflex", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home"),
                        rx.menu.item("About"),
                        rx.menu.item("Pricing"),
                        rx.menu.item("Contact"),
                        rx.menu.separator(),
                        rx.menu.item("Log in"),
                        rx.menu.item("Sign up"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),

        # Aqui estan las propiedades de la barra de navegacion
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )



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

    # Banco de pruebas
    # original_label = "Etiqueta de pruebas, "

    # def cambiar_etiqueta(self):
    #     if self.label == "Etiqueta Modificada ":
    #         self.label = self.original_label

    #     else:
    #         self.label = "Etiqueta Modificada "

    

# este es el fron end de nuestra app
def index() -> rx.Component:
    # Welcome Page (Index) , return our base_page   
    # return base_page("Hola")
    return base_page(
        
        rx.vstack(
            rx.heading(State.label, size="9"),
            rx.text(
                "Usted puede iniciar por editar: ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="4",
            ),

            # On clik es un evento, s eme habia olvidado la coma despues de parentesis
            # rx.button("hacer algo", on_click=State.cambiar_etiqueta),

            # Esto es algo dinamico



            rx.input(
                # guardamos el texto escrito en el texbox, y no se borra aunque recargues
                default_value=State.label,
                on_click=State.did_clic(),
                on_change= State.handle_title_input_change),


            rx.link(
                rx.button("Para mayor informacion puede ir a: "),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        )        
        
    )


app = rx.App()
app.add_page(index)
