import pandas as pd
import os
import pathlib
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import PIL


from pec4_modulo1 import parsename, new_columns, create_dataframe, parsefile
from pec4_modulo2 import check_yolo, check_image_file
from pec4_modulo3 import create_dataset, draw_boxes
from pec4_modulo4 import ParseFile_noerror, dataset_filtered, map_ids, histogram
from pec4_module42 import graphs
from pec4_modulo5 import car_graph
from pec4_modulo6 import scoring_maping, image_score, validate_img_file


current = os.getcwd()
path = r"\dataset_cities\labels\\"
path3 = r'\dataset_cities\\'
file2 = 'class_name.txt'
regex = '(?:(?<=^\d)|(?<=^\d{2}))\s'

if __name__ == '__main__':
    ## Ejercicio 1
    labels = pd.DataFrame()
    labels = parsefile(current, path, labels)
    print("EJERCICIO 1 : El dataframe que captura la informacion de los archivos es labels, cuyo formato es : ")
    labels.info()

    ##  Ejercicio 2
    print("EJERCICIO 2 : Los errores en los archivos de etiquetas encontrados son : ")
    list_errors = check_yolo(current,path)
    print('Los archivos que contienen esos errores son :')
    print(list_errors)


    ##  Ejercicio 3
    path2 = r'\dataset_cities\images\\'
    image1 = 'berlin_000001_000019_leftImg8bit_15-01-2018.png'
    image2 = 'bonn_000000_000019_leftImg8bit_18-07-2017.png'
    image3 = 'zurich_000000_000019_leftImg8bit_20-08-2015.png'

    draw_boxes(current, path2, image1, create_dataset(labels, 'berlin'))
    draw_boxes(current, path2, image2, create_dataset(labels, 'bonn'))
    draw_boxes(current, path2, image3, create_dataset(labels, 'zurich'))


    ##  Ejercicio 4.1
    path3 = r'\dataset_cities\\'
    file2 = 'class_name.txt'
    regex = '(?:(?<=^\d)|(?<=^\d{2}))\s'
    errors = []
    dataset = dataset_filtered(current, path, check_yolo(current, path))
    print("EJERCICIO 4.1 : Los Top Categorias de objetos mas vistos son : ")
    histogram(path3, file2, dataset)



    ##Ejercicio 4.2
    print("EJERCICIO 4.2 : Los Top Categorias de objetos por ciudad  : ")
    test = labels[labels['confidence'] >= 0.4].copy()
    test['id'] = test['id'].astype(int)
    top = test[test['id'].isin([0, 1, 2, 7, 9])].copy()
    graphs(top)


    ##Ejercicio 4.3
    print("EJERCICIO 4.3 : El promedio de objetos por imagen  : ")
    images = test.set_index(['city', 'image_id']).groupby(level='image_id').count()['id']
    promedio = sum(list(images)) / len(list(images))
    print('El promedio de objetos por imagen es de : {}'.format(promedio))

    ##  Ejercicio 4.4
    ## PENDIENTE


    ## Ejercicio 5
    filter = test['id'] == 2
    test['date'] = pd.to_datetime(test['date'], dayfirst=True)
    cars = test[filter]
    print("EJERCICIO 5 : Grafico de cantidad de Autos por ano  : ")
    car_graph(cars)

    ## Ejercicio 6
    print("EJERCICIO 6 : Identificar archivos de imagenes colados  : ")
    print("Margen de error alto si damos puntos por tipo de objeto, ya que pueden haber fotos con muchas personas, en un reciento cerrado")
    print("Segundo metodo, segun el tamano de imagen, si por defecto las imagenes del archivo todas son de 2048x1024 : ")
    print("Por tanto los imagenes coladas son :")
    validate_img_file(current, path2)


    ##  Ejercicio 7
    ##  PENDIENTE