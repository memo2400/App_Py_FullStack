
# Desde fuera accedemos a estas funciones de los diferentes archivos .py

from .state import ContactState
from .form import contact_form
from .page import contact_page

__all__ = [
    'ContactState',
    'contact_form',
    'contact_page',
]



