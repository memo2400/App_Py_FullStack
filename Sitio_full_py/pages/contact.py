
from tkinter.tix import Tree
import reflex as rx

from .. ui.base import base_page

from .. import navigation


""" Se genera nueva pagina acerca de nosotros """

class ContactState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        print (form_data)
        self.form_data = form_data


#@rx.page(route=navigation.NavState.to_contact)
# para estilizar la pagina usamos
@rx.page(route=navigation.routes.CONTACT_ROUTE)

def contact_page() -> rx.Component:    

    # tuve un error al declarar dos veces el form
    # Con esta configuracion, la forma mantendra su proporcion sin
    # importar si esta en mbile o desktop
    my_form = rx.form(        
            rx.vstack(
                # creamos horizontal stack
                rx.hstack(
                    rx.input(
                        name="first_name",
                        placeholder="First Name",
                        # hacemos que el elemento sea requerido
                        required=True,  
                        width="50%",                  
                    ),
                    # <imput type=text> 
                    rx.input(
                        name="last_name",
                        placeholder="Last Name",  
                        width="50%",                  
                    ),
                    width='100%',
                ),
                # <imput type=email> 
                rx.input(
                    name="email",
                    placeholder="Email", 
                    width='100%',
                    type="email",
                ),

                # borrar
                rx.hstack(
                    rx.checkbox("Checked", name="check"),
                    rx.switch("Switched", name="switch"),
                ),

                rx.text_area(
                    name ='message',
                    placeholder='Your Messsage',
                    width='100%',
                    required=True,
                ),

                # enviamos en consola lo datos como Json
                rx.button("Submit", type="submit"),
            ),
            on_submit=ContactState.handle_submit,

            # con este comando borramos los textbox luego de dar clic en submit
            reset_on_submit=True,
        )    

    # Documentacion aqui https://reflex.dev/docs/library/layout/stack/#vstack
    # puedo usar my_child pero si uso el nombre repetido de la pagina contact falla
    my_child_contact = rx.vstack(
            rx.heading("Contact us", size="8"),

            # solo renderizo en escritorio y mobile separado
            rx.desktop_only(
                rx.box(
                    my_form,
                    id='my_form_box_desktop',
                    width='50vw' # vertical and width
                )
                
            ),

            # rx.mobile only = no funciono
            rx.mobile_and_tablet(
                rx.box(
                    my_form,
                    width='65vw',
                )            
            ),
            
            # agregamos aqui la nueva form
            # my_form,

            rx.text(
                "Contáctenos | 联系我们",                
            ),
           
            spacing="5",
            justify="center", # tenia centar en lugar de center
            align="center", # podemos usar end, strech et etc
            
            min_height="85vh",
            id="my_child"
        )

    # Base page gets my_child
    return base_page(my_child_contact)
