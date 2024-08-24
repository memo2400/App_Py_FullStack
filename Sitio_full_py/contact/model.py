

import reflex as rx
import asyncio
import sqlalchemy


from tkinter.tix import Tree


from sqlmodel import Field

from datetime import datetime, timezone

def get_utc_time_now() -> datetime:
    return datetime.now(timezone.utc) 


# Cada vez que se haga cambios debemos ejecutar el db makemigrations, etc
class ContactEntryModel(rx.Model, table=True):          # nombre de la tabla o libreo, sheet ContactEntryModel
    user_id : int | None = None                         # el defult none
    first_name: str                                     # se pude usar | None = None
    last_name: str      = Field(nullable=True)          # otra forma de manejar el espacio vacio
    email: str          = Field(nullable=True)
    message: str
    time_at: datetime   = Field(
        default_factory=get_utc_time_now,        
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs= {
            'server_default': sqlalchemy.func.now()
        },
        nullable= False,
    )
