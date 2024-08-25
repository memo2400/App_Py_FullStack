import reflex as rx

#   IMPORTO LA CARPETA NAVEGACION
from .. import navigation



def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )

#  Sorce https://reflex.dev/docs/recipes/layout/navbar/

def navigator_bar() -> rx.Component:
    return rx.box(
        #position=="top-left",
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    # Hacemos que al presionar el logo, regresamos a /Home
                    rx.link(
                        rx.image(                                                
                            src="/chiplinear_106231.png",
                            width="2.25em",
                            height="auto",
                            border_radius="25%",
                        ),
                        href=navigation.routes.HOME_ROUTE # Go home
                    ),

                    # Hacemos que el head sea in link a /Home 
                    rx.link(
                        rx.heading(
                            "TecnoTower", size="7", weight="bold"
                        ),
                        href=navigation.routes.HOME_ROUTE
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", navigation.routes.HOME_ROUTE),
                    navbar_link("About", navigation.routes.ABOUT_US_ROUTE),
                    navbar_link("Pricing", navigation.routes.PRICING_ROUTE),
                    navbar_link("Contact", navigation.routes.CONTACT_ROUTE),
                    navbar_link("Data", navigation.routes.DATE_ROUTE),
                    navbar_link("Suscripciones", navigation.routes.SUSCRIPCIONES_ROUTE),
                    spacing="5",
                ),
                rx.hstack(
                    rx.button(
                        "Sign Up",
                        size="3",
                        variant="outline",
                    ),
                    rx.button("Log In", size="3"),
                    spacing="4",
                    justify="end",
                ),
                justify="between",
                align_items="center",
                id="my_nav_var_hstack_desktop"
            ),
        ),
        # estos son para cuando se ajusta exactamente al tamaño
        # rx.mobile_only(),
        # rx.tablet_only(),

        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/chiplinear_106231.png",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Tower", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),

                    # para el menu de mobile usaremos el evento click para hacer la navegacion
                    
                    rx.menu.content(
                        rx.menu.item("Home", on_click=navigation.NavState.to_home),
                        rx.menu.item("About", on_click=navigation.NavState.to_about_us),
                        rx.menu.item("Pricing", on_click=navigation.NavState.to_pricing),
                        rx.menu.item("Contact", on_click=navigation.NavState.to_contact),

                        rx.menu.item("Data", on_click=navigation.NavState.to_date),
                        rx.menu.item("Suscripciones", on_click=navigation.NavState.to_suscripciones),

                        rx.menu.separator(),
                        rx.menu.item("Log in"),
                        rx.menu.item("Sign up"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),

        # Aqui estan las propiedades de la barra de navegacion
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
        id = "my_main_nav"
    )




