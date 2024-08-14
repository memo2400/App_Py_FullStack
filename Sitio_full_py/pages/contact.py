
import reflex as rx

from .. ui.base import base_page

from .. import navigation


""" Se genera nueva pagina acerca de nosotros """

#@rx.page(route=navigation.NavState.to_contact)
@rx.page(route=navigation.routes.CONTACT_ROUTE)

def contact_page() -> rx.Component:    

    # Documentacion aqui https://reflex.dev/docs/library/layout/stack/#vstack
    # puedo usar my_child pero si uso el nombre repetido de la pagina contact falla
    my_child_contact = rx.vstack(
            rx.heading("Contact us", size="8"),
            rx.text(
                "Contacte con nosotros",                
            ),
           
            spacing="5",
            justify="center", # tenia centar en lugar de center
            align="center", # podemos usar end, strech et etc
            
            min_height="85vh",
            id="my_child"
        )

    # Base page gets my_child
    return base_page(my_child_contact)
