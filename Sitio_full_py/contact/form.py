
import reflex as rx

from .state import ContactState


#@rx.page(route=navigation.NavState.to_contact)
# para estilizar la pagina usamos
#  se carga la funcion del timer de incio
# @rx.page(on_load= contact.ContactState.star_timer, route=navigation.routes.CONTACT_ROUTE)

def contact_form() -> rx.Component:    

    # tuve un error al declarar dos veces el form
    # Con esta configuracion, la forma mantendra su proporcion sin
    # importar si esta en mbile o desktop

    # my_form = rx.form(        
    return rx.form(        
            rx.vstack(
                # creamos horizontal stack
                rx.hstack(
                    rx.input(
                        name="first_name",
                        placeholder="First Name | 姓名",
                        # hacemos que el elemento sea requerido
                        required=True,  
                        width="50%",                  
                    ),
                    # <imput type=text> 
                    rx.input(
                        name="last_name",
                        placeholder="Last Name | 姓",  
                        width="50%",                  
                    ),
                    width='100%',
                ),
                # <imput type=email> 
                rx.input(
                    name="email",
                    placeholder="Your Email | 您的电子邮件", 
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
                    placeholder='Your Messsage | 您的留言',
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
