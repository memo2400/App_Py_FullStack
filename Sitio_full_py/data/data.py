
""" crear diccionario https://www.simplilearn.com/dictionary-in-python-article"""

test_dict = {}
test_dict ['width'] = 5.2

# print (test_dict)



"""llenar listaa con diccioarios
    https://www.askpython.com/python/list/list-of-dictionaries
"""

ls_dict = []


dict_1 = {'x': 50, 'y': 45, 'z': 65}
dict_2 = {'x': 66, 'y': 22, 'z': 89}

ls_dict.append(dict_1)
ls_dict.append(dict_2)

# print(ls_dict[1])


"""Se genera grafica"""
import pandas as pd

file_name = "Sitio_full_py/pages/iris.csv"
direction = " "

data_frame = pd.read_csv(file_name)
# dictionary = data_frame.to_dict()

# print(data_frame.columns.values)

def data_procesing ():

    test_dict = {}
    ls_dict = []

    for index, row in data_frame.iterrows():
        print(f"Fila: {index}")
        print(f"150: {row['150']}, 4: {row['4']}, versicolor: {row['versicolor']}")
        test_dict ['150'] = {row['150']}
        test_dict ['4'] = {row['4']}
        ls_dict.append(test_dict)

    return ls_dict
        

