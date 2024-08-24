
import reflex as rx

from .. import navigation
from ..ui.base import base_page
from ..data.data_analysis import data_procesing
from ..data.data_analysis import ls_dict_changed
from Sitio_full_py.data import data_analysis

"""Se genera grafica"""
import pandas as pd

file_name = "Sitio_full_py/pages/iris.csv"
direction = " "

data_frame = pd.read_csv(file_name)
dictionary = data_frame.to_dict()
# data_frame = pd.read_excel("data.xlsx")
#data.head()

# df_reduced = df[["petal length (cm)", "petal width (cm)", "target"]]
# df_reduced = df_reduced.loc[df_reduced["target"].isin([0, 1])]          # el target hace que solo usemos dos tipos de flor
# df_reduced

# la aplicacion solo toma los dos primeros elementos (0 y 1), {0, 1, 2 ...}

data01 = [
    {"x": 10.5, "y": 200, "z": 200},
    {"x": 120, "y": 100, "z": 260},
    {"x": 170, "y": 300, "z": 400},
    {"x": 170, "y": 250, "z": 280},
    {"x": 150, "y": 400, "z": 500},
    {"x": 110, "y": 280, "z": 200},
    ]

# data_procesing ()
data03 = data_procesing()

def scatter_simple():
    
    return rx.recharts.scatter_chart(
        rx.recharts.scatter(
            # data=data01,
            data=data03,
            fill="#009aff",
        ),
        rx.recharts.x_axis(
            data_key="150",                     # poner el header necesario
            type_="number",
            ),
        rx.recharts.y_axis(data_key="4"),       # poner el header necesario
        width="100%",
        height=200,
    ),



""" Se genera nueva pagina datos """

@rx.page (route=navigation.routes.DATE_ROUTE)

def date_page() -> rx.Component:    

    # Documentacion aqui https://reflex.dev/docs/library/layout/stack/#vstack
    my_child = rx.vstack(
            
                rx.heading("Data", size="8"),
                rx.text(
                    "here is a graphic from dataframe",                
                    ),

                rx.hstack(
                    scatter_simple(),
                    width="50%",
                    ),

                spacing="5",
                justify="center", # tenia centar en lugar de center
                align="center", # podemos usar end, strech et etc
            
                min_height="85vh",
                id="my_child_devices",
                width="90%",
            
        )

    # Base page gets my_child
    return base_page(my_child)
