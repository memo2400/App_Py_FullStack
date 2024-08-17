
import reflex as rx
import asyncio


from tkinter.tix import Tree
from .. ui.base import base_page
from .. import navigation


class ContactEntryModel(rx.Model, table=True):  # nombre de la tabla o libreo, sheet ContactEntryModel
    first_name: str
    last_name: str
    email: str
    message: str

""" Se genera nueva pagina acerca de nosotros """

class ContactState(rx.State):
    form_data: dict = {}        # para guardar los datos en diccionario
    did_sumitted: bool = False  # bandera
    time_delay: int = 20         # cuento hasta 4 seg

    @rx.var
    def time_delay_label(self):
        if self.time_delay < 1:
            return "no time left | 沒有時間了"
        return f"{self.time_delay} seconds | 秒"
    
    
    @rx.var    
    def thank_you (self):

        first_name_submitted = self.form_data.get("first_name") or ""
        return f"thank you | 謝謝 {first_name_submitted}" # Uso el string sustitution
    
    @rx.var
    def before_submit (self):

        return "fill out the form | 填寫表格"
        

    
    # debe ser una funcion asincrona
    async def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        print (form_data)
        self.form_data = form_data
        self.did_sumitted = True # actualizo bandera
        yield

        # Set a timmer to change the flag, de 3 seg , no fucciona con time ni con async solo
        # se debe hacer uso del yield
        await asyncio.sleep(3)
        self.did_sumitted = False
        yield
    

    # Funcion que dimunuye un segundo en cada ciclo, 
    # si es menor a 0 se detiene 

    async def star_timer(self):

        # la condicion fuera de parentesis causo error
        while (self.time_delay > 0):
            yield
            await asyncio.sleep(1)
            self.time_delay -= 1
            yield

#@rx.page(route=navigation.NavState.to_contact)
# para estilizar la pagina usamos
#  se carga la funcion del timer de incio
@rx.page(on_load=ContactState.star_timer, route=navigation.routes.CONTACT_ROUTE)

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

    # Documentacion aqui https://reflex.dev/docs/library/layout/stack/#vstack
    # puedo usar my_child pero si uso el nombre repetido de la pagina contact falla

    my_child_contact = rx.vstack(
            rx.heading("Contact us | 联系我们", size="8"),

            rx.text(ContactState.time_delay),

            # agrego condicional (despues de cambio True , default false), ambos deben ser texto o objeto
            rx.cond(ContactState.did_sumitted, ContactState.thank_you, ContactState.before_submit),

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
