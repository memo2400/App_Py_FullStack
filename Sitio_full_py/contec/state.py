
import reflex as rx
import asyncio
import sqlalchemy


from tkinter.tix import Tree


from sqlmodel import Field

from datetime import datetime, timezone

def get_utc_time_now() -> datetime:
    return datetime.now(timezone.utc) 


# Cada vez que se haga cambios debemos ejecutar el db makemigrations, etc
class ContactEntryModel(rx.Model, table=True):  # nombre de la tabla o libreo, sheet ContactEntryModel
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

        data_transformed = {}
        for k, v in form_data.items():      # recoroo los itsten del formulario
            if v == "" or v is None:
                continue

            data_transformed [k] = v
            print(data_transformed)         # con esta impresion veo como se va llenando
 

        # Creamos la instancia del DB
        with rx.session() as session:
            db_entry = ContactEntryModel (

            # aqui dentro colocamos lo que aneviaremos a BD ** para unpackage
            **data_transformed

            )
            session.add(db_entry)   # Preparop Envio a BD
            session.commit()        # Hago el envio a BD

            self.did_sumitted = True # actualizo bandera
            yield

        # no usar
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
