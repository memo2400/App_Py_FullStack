
import reflex as rx

from .. ui.base import base_page


""" Se genera nueva pagina acerca de nosotros """

# @rx.page(route='/about_us')
def about_page() -> rx.Component:    

    # Documentacion aqui https://reflex.dev/docs/library/layout/stack/#vstack
    cuerpo_pagina_about = rx.vstack(
            rx.heading("About us", size="9"),
            rx.text(
                "Conozca mas sobre nosotros, somos una empresa dedicada a la resolucion de problemas mediante aplicaciones",                
            ),
           
            spacing="5",
            justify="center", # tenia centar en lugar de center
            align="center", # podemos usar end, strech et etc
            
            min_height="85vh",
            id="my_child"
        )

    # Base page gets my_child
    return base_page(cuerpo_pagina_about)
