
# import reflex as rx


# from tkinter.tix import Tree
# from .. ui.base import base_page
# from .. import navigation
# from .. import contact


# #@rx.page(route=navigation.NavState.to_contact)
# # para estilizar la pagina usamos
# #  se carga la funcion del timer de incio
# @rx.page(on_load= contact.ContactState.star_timer, route=navigation.routes.CONTACT_ROUTE)




# def contact_page() -> rx.Component:    

#     # tuve un error al declarar dos veces el form
#     # Con esta configuracion, la forma mantendra su proporcion sin
#     # importar si esta en mbile o desktop

#     # my_form = contact.contact_form          # en lugar de cargar la forma aqui ahora se llama via contact.***

#     # Documentacion aqui https://reflex.dev/docs/library/layout/stack/#vstack
#     # puedo usar my_child pero si uso el nombre repetido de la pagina contact falla

#     my_child_contact = rx.vstack(
#             rx.heading("Contact us | 联系我们", size="8"),

#             rx.text(contact.ContactState.time_delay),

#             # agrego condicional (despues de cambio True , default false), ambos deben ser texto o objeto
#             rx.cond(contact.ContactState.did_sumitted, contact.ContactState.thank_you, contact.ContactState.before_submit),

#             # solo renderizo en escritorio y mobile separado
#             rx.desktop_only(
#                 rx.box(
#                     contact.contact_form(),
#                     id='my_form_box_desktop',
#                     width='50vw' # vertical and width
#                 )
                
#             ),

#             # rx.mobile only = no funciono
#             rx.mobile_and_tablet(
#                 rx.box(
#                     contact.contact_form(),
#                     width='65vw',
#                 )            
#             ),
            
#             # agregamos aqui la nueva form
#             # contac.contact_form(),

#             rx.text(
#                 "Contáctenos | 联系我们",                
#             ),
           
#             spacing="5",
#             justify="center", # tenia centar en lugar de center
#             align="center", # podemos usar end, strech et etc
            
#             min_height="85vh",
#             id="my_child"
#         )

#     # Base page gets my_child
#     return base_page(my_child_contact)
