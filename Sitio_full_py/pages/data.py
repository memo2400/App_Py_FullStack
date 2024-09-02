
import reflex as rx

from .. import navigation
from ..ui.base import base_page
# from ..data.data_analysis import data_procesing
from ..data import data_analysis

from ..data.data_analysis import ls_dict_changed
from Sitio_full_py.data import data_analysis
from ..data.random_data import generated_temperatures_years

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
data03 = data_analysis.data_procesing_setosa()
data04 = data_analysis.data_procesing_versicolor()
data05 = data_analysis.data_procesing_virginica()

data06 = generated_temperatures_years()
data07 = [{'x': 0, 'y': 41}, {'x': 1, 'y': 49}]

def scatter_simple():
    
    return rx.recharts.scatter_chart(
        rx.recharts.scatter(
            # data=data01,
            data=data03,
            fill="#009aff",
            name="setosa",
        ),
        rx.recharts.scatter(
            # data=data01,
            data=data04,
            fill="#46A758",
            name="versicolor",
        ),
        rx.recharts.scatter(
            # data=data01,
            data=data05,
            fill="#EF5F00",
            name="virginica",
        ),
        rx.recharts.x_axis(
            data_key="x",                                       # poner el header necesario
            type_="number",
            ),
        rx.recharts.y_axis(data_key="y"),                       # poner el header necesario
        rx.recharts.cartesian_grid(stroke_dasharray="3 3"),     # grid
        rx.recharts.legend(),                                   # legenda
        width="100%",
        height=200,
    ),

def scatter_temperature():
    
    return rx.recharts.scatter_chart(
        rx.recharts.scatter(
            # data=data01,
            data=data06,
            # fill="#EF5F00",
            fill="brown",
            name="temperatura",
        ),
        rx.recharts.x_axis(
            data_key="x",                                       # poner el header necesario
            type_="number",
            ),
        rx.recharts.y_axis(
            data_key="y"
        ),                       # poner el header necesario
        rx.recharts.cartesian_grid(stroke_dasharray="3 3"),     # grid
        rx.recharts.legend(),                                   # legenda
        width="100%",
        height=200,
    ),



""" Se genera nueva pagina datos """

# @rx.page (route=navigation.routes.DATA_ROUTE)

def data_page() -> rx.Component:    

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

                rx.text(
                    "here is a graphic of temperatures",                
                    ),

                rx.hstack(
                    scatter_temperature(),
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



