"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""
    label = "Etiqueta de pruebas, "
    original_label = "Etiqueta de pruebas, "

    def cambiar_etiqueta(self):
        if self.label == "Etiqueta Modificada ":
            self.label = self.original_label

        else:
            self.label = "Etiqueta Modificada "

    

# este es el fron end de nuestra app
def index() -> rx.Component:
    # Welcome Page (Index)    
    return rx.container(
        rx.color_mode.button(position="top-left"),
        rx.vstack(
            rx.heading(State.label, "Hola mundo (app creada con reflex)!", size="9"),
            rx.text(
                "Usted puede iniciar por editar: ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="4",
            ),

            # On clik es un evento, s eme habia olvidado la coma despues de parentesis
            rx.button("hacer algo", on_click=State.cambiar_etiqueta),

            # Esto es algo dinamico
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
