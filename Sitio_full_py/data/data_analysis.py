
""" crear diccionario https://www.simplilearn.com/dictionary-in-python-article"""

test_dict = {}
test_dict ['width'] = 5.2

# print (test_dict)



"""llenar listaa con diccioarios
    https://www.askpython.com/python/list/list-of-dictionaries
"""

ls_dict_test = []


dict_1 = {'x': 50, 'y': 45, 'z': 65}
dict_2 = {'x': 66, 'y': 22, 'z': 89}

ls_dict_test.append(dict_1)
ls_dict_test.append(dict_2)

# print(ls_dict[1])


"""Se genera grafica"""
import pandas as pd
import os

file_name = "iris.csv"

# casa
# direction = "C:/Users/Casa/PSW/Python/App_Py_FullStack/Sitio_full_py/data"

# laptop
direction = "C:/Users/Laptop/SWF/Python/App_Py_FullStack/Sitio_full_py/data"
# fullpath = os.path.join(direction, file_name)

fullpath = "Sitio_full_py/pages/iris.csv"           # Debe funcionar en cualquier equipo

data_frame = pd.read_csv(fullpath)
# dictionary = data_frame.to_dict()

# print(data_frame.columns.values)

ls_dict_changed = []

 
def data_procesing_setosa ():

    test_dict = {}
    ls_dict : list = []
    

    for index, row in data_frame.iterrows():
        # print(f"Fila: {index}")
        # print(f"150: {row['150']}, 4: {row['4']}, versicolor: {row['versicolor']}")
        
        # if index < 150:
        if row['virginica'] == 0: 
            # print(f"150: {row['150']}, 4: {row['4']}, versicolor: {row['versicolor']}")

            # test_dict ['150'] = row['150']
            # test_dict ['4'] = row['4']

            test_dict = {

            'x': row['setosa'],
            'y': row['versicolor'],

            }

            ls_dict.append(test_dict)


    return ls_dict
    # return print(ls_dict)



def data_procesing_versicolor ():

    test_dict = {}
    ls_dict : list = []
    
    for index, row in data_frame.iterrows():
        
        if row['virginica'] == 1: 

            test_dict = {
            'x': row['setosa'],
            'y': row['versicolor'],
            }

            ls_dict.append(test_dict)

    return ls_dict
    # return print(ls_dict)


def data_procesing_virginica ():

    test_dict = {}
    ls_dict : list = []
    
    for index, row in data_frame.iterrows():
        
        if row['virginica'] == 2: 

            test_dict = {
            'x': row['setosa'],
            'y': row['versicolor'],
            }

            ls_dict.append(test_dict)

    return ls_dict
    # return print(ls_dict)



data_procesing_virginica()
    

# def dictionary_processed ():

#     data_procesing()
#     print (ls_dict)

#     # for x in data_procesing.ls_dic
        

