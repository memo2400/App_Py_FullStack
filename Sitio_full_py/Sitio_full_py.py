"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from tkinter.tix import Tree
from turtle import position
import click
import reflex as rx
from sqlalchemy import true

from rxconfig import config

# Se necesita poner el punto antes de "ui", para que no falle
from .ui.base import base_page

# Ya no sera necesario debido a la importacion de toda la carpeta
# from .pages.about import about_page

# importo la carperta entera y dejo de usar la linea de arriba
from . import pages



class State(rx.State):
    """The app state."""
    label = "hola Gordooo!! "

    def handle_title_input_change(self, val):
        self.label = val
    
    def did_clic(self):
        # esta impresion se haria en consola y no se muestra en el front
        print ("You did a clic")
        return rx.redirect('/about_us')

    



    

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
            
            # Nuevo codigo para menus

            # no se recomienda hace uso del boton
            # rx.button("about us", on_click=rx.redirect('/about_us/')),

            # es mejor tener el boton dentro de un link, eso nos permite copiar el link dando clic derecho al boton
            rx.link(rx.button("About us", href='/about_us')),






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



app = rx.App()
app.add_page(index)

# Agregamos nuestra pagina nueva (*** /ruta) , si tenemos los funciones del mismo nombre puede generar confilcto
app.add_page(pages.about_page, route='/about_us')
app.add_page(pages.pricing_page, route='/pricing')
