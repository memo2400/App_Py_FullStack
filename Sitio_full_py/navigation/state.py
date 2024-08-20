

import reflex as rx

from . import routes

class NavState(rx.State):

    def to_home(self):
        
        # vamos a la pagina home
        return rx.redirect(routes.HOME_ROUTE)
    
    def to_about_us (self):

        return rx.redirect(routes.ABOUT_US_ROUTE)
    
    def to_pricing (self):

        return rx.redirect(routes.PRICING_ROUTE)
    
    def to_contact (self):

        return rx.redirect(routes.CONTACT_ROUTE)
    
    def to_mis_dispositivos (self):

        return rx.redirect(routes.MIS_DISPOSITIVOS_ROUTE)
    
    def to_suscripciones (self):

        return rx.redirect(routes.SUSCRIPCIONES_ROUTE)
    

    # Pagina Data
    
    def to_date (self):

        return rx.redirect(routes.DATE_ROUTE)
    
    
        
