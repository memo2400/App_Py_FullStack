"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from tkinter.tix import Tree
from turtle import position
import reflex as rx
from sqlalchemy import true

from rxconfig import config

# Se necesita poner el punto antes de "ui", para que no falle
from .ui.base import base_page



class State(rx.State):
    """The app state."""
    label = "hola Gordooo!! "

    def handle_title_input_change(self, val):
        self.label = val
    
    def did_clic(self):
        # esta impresion se haria en consola y no se muestra en el front
        print ("hello worl")

    



    

# este es el fron end de nuestra app
def index() -> rx.Component:
    # Welcome Page (Index) , return our base_page   
    # return base_page("Hola")

    # El contenido de base_page se movio aqui
    # para poder centrar el cuerpo de la pagina ,se uso fragment y luego Stack
    # my_child = rx.fragment(

    # Documentacion aqui https://reflex.dev/docs/library/layout/stack/#vstack
    my_child = rx.vstack(
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
            justify="center", # tenia centar en lugar de center
            align="center", # podemos usar end, strech et etc
            text_align="center",
            min_height="85vh",
            id="my_child"
        )

    # Base page gets my_child
    return base_page(my_child)


""" Se genera nueva pagina acerca de nosotros """

def about_page() -> rx.Component:    

    # Documentacion aqui https://reflex.dev/docs/library/layout/stack/#vstack
    my_child = rx.vstack(
            rx.heading("About us", size="9"),
            rx.text(
                "Conozca mas sobre nosotros ",                
            ),
           
            spacing="5",
            justify="center", # tenia centar en lugar de center
            align="center", # podemos usar end, strech et etc
            
            min_height="85vh",
            id="my_child"
        )

    # Base page gets my_child
    return base_page(my_child)


app = rx.App()
app.add_page(index)

# Agregamos nuestra pagina nueva (*** /ruta)
app.add_page(about_page, route='/aboutus')
