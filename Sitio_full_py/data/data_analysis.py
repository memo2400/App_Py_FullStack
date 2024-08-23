
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

file_name = "Sitio_full_py/pages/iris.csv"
direction = " "

data_frame = pd.read_csv(file_name)
# dictionary = data_frame.to_dict()

# print(data_frame.columns.values)

ls_dict_changed = []

 
def data_procesing ():

    test_dict = {}
    ls_dict = []
    

    for index, row in data_frame.iterrows():
        # print(f"Fila: {index}")
        #print(f"150: {row['150']}, 4: {row['4']}, versicolor: {row['versicolor']}")
        
        test_dict ['x'] = row['150']
        test_dict ['y'] = row['4']
        ls_dict.append(test_dict)


    return print (ls_dict)


    

# def dictionary_processed ():

#     data_procesing()
#     print (ls_dict)

#     # for x in data_procesing.ls_dic
        

# dictionary_processed()