
from datetime import timedelta

import datetime
import string

data_to_generate = 10 # 16100

fecha = "01-01-1980"
# fecha = "01-01-1980 18:00:20"

fecha_processed = datetime.datetime.strptime(
    fecha,
    "%d-%m-%Y",
    # "%d-%m-%Y %H:%M:%S",                # full date-time
    )

list_dates: list = []

for x in range (data_to_generate):
    fecha_processed = fecha_processed + timedelta(days=1)
    list_dates.append(fecha_processed)


import numpy as np
temperaturas = np.random.randint(6,55,data_to_generate)

print(temperaturas)
cantidad_temperaturas = len (temperaturas)

def generated_temperatures ():

    diccionario_temp = {}
    ls_diccionario : list = []
    
    for index in range(cantidad_temperaturas):
    
        diccionario_temp = {
        'x': list_dates[index],
        'y': temperaturas[index],
        }

        ls_diccionario.append(diccionario_temp)

    # return ls_diccionario
    return print(ls_diccionario)

generated_temperatures()