
import reflex as rx

from .. ui.base import base_page

"""Se genera grafica"""
import pandas as pd

file_name = "Sitio_full_py/pages/iris.csv"
direction = " "

data_frame = pd.read_csv(file_name)
# data_frame = pd.read_excel("data.xlsx")
#data.head()

data01 = [
    {"x": 100, "y": 200, "z": 200},
    {"x": 120, "y": 100, "z": 260},
    {"x": 170, "y": 300, "z": 400},
    {"x": 170, "y": 250, "z": 280},
    {"x": 150, "y": 400, "z": 500},
    {"x": 110, "y": 280, "z": 200},
]

def scatter_simple():
    return rx.recharts.scatter_chart(
        rx.recharts.scatter(
            data=data01,
            # data=data_frame,
            fill="#8884d8",
        ),
        rx.recharts.x_axis(data_key="x", type_="number"),
        rx.recharts.y_axis(data_key="y"),
        width="100%",
        height=300,
    )

""" Se genera nueva pagina de precios """

def pricing_page() -> rx.Component:    

    # Documentacion aqui https://reflex.dev/docs/library/layout/stack/#vstack
    my_child = rx.vstack(
            rx.heading("Quote", size="9"),
            rx.text(
                "Get the pricing here ",                
            ),
            scatter_simple(),


           
            spacing="5",
            justify="center", # tenia centar en lugar de center
            align="center", # podemos usar end, strech et etc
            
            min_height="85vh",
            id="my_child"
        )

    # Base page gets my_child
    return base_page(my_child)
