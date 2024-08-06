"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""
    label = "Bienvenido a Reflex "

    def handle_title_input_change(self, val):
        self.label = val
    
    def did_clic(self):
        # esta impresion se haria en consola y no se muestra en el front
        print ("hello worl")


    # Banco de pruebas
    # original_label = "Etiqueta de pruebas, "

    # def cambiar_etiqueta(self):
    #     if self.label == "Etiqueta Modificada ":
    #         self.label = self.original_label

    #     else:
    #         self.label = "Etiqueta Modificada "

    

# este es el fron end de nuestra app
def index() -> rx.Component:
    # Welcome Page (Index)    
    return rx.container(
        rx.color_mode.button(position="top-left"),
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
        ),
        rx.logo(),
    )


app = rx.App()
app.add_page(index)
