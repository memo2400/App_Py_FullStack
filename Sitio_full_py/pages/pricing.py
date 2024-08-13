
import reflex as rx

from .. ui.base import base_page


""" Se genera nueva pagina de precios """

def pricing_page() -> rx.Component:    

    # Documentacion aqui https://reflex.dev/docs/library/layout/stack/#vstack
    my_child = rx.vstack(
            rx.heading("Quote", size="9"),
            rx.text(
                "Get the pricing here ",                
            ),
           
            spacing="5",
            justify="center", # tenia centar en lugar de center
            align="center", # podemos usar end, strech et etc
            
            min_height="85vh",
            id="my_child"
        )

    # Base page gets my_child
    return base_page(my_child)
