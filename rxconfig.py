# aqui importamos a reflex

import reflex as rx

config = rx.Config(
    app_name="Sitio_full_py",
    db_url="sqlite:///reflex.db",           # postgress, mySql, etc etc
    api_url="http://app.totalpy.com:8000",   # para la publicacion
)