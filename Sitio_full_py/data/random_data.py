
from datetime import timedelta

import datetime
import string

data_to_generate = 5 # 16100

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

cantidad_temperaturas = len (temperaturas)



# list_year = []
# for i in range (data_to_generate):
#     # list_year.append(i+1000)
#     list_year.append(i)

list_year = [0,1,2,3,4] 


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

# generated_temperatures()

def generated_temperatures_years ():

    diccionario_temp = {}
    ls_diccionario : list = []
    
    for index in range(data_to_generate):
    
        diccionario_temp = {
        'x': list_year[index],
        'y': temperaturas[index],
        }

        ls_diccionario.append(diccionario_temp)

    return ls_diccionario
    # return print(ls_diccionario)

# generated_temperatures_years()