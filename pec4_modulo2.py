import pandas as pd
import os
import pathlib


def check_image_file(current : str, path : str, file : str, errors: list):
    with open(current+path+file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            items = line.split(' ')
            if len(items) == 6:
                if items[0].isdigit():
                    if int(items[0]) < 80:
                        for n in range(1,6):
                            if float(items[n]) < 1 and float(items[n]) > 0:
                                if n == 5 :
                                    pass
                            else :
                                print('False1 - Error dato no numerico o negativo', file , items[n])
                                errors.append(file)
                                break
                    else:
                        print('False2 - Error objeto no registrado ', file)
                        errors.append(file)
                        break
                else:
                    print('False3 - Error dato no entero en tipo de imagen ', file)
                    errors.append(file)
                    break
            else:
                print('False4 - Error archivo con menos columnas ', file)
                errors.append(file)
                break
            #print(line)
        #print('todas las lineas de archivo {} estan bien'.format(file))
    return errors

def check_yolo (current : str, path : str):
    errors =[]
    directory = pathlib.Path(current+path)
    for file in directory.iterdir():
        if os.path.isfile(file):
            filename = str(file).split('\\')[-1]
            list_errors=check_image_file(current,path,filename, errors)
    list_errors = set(list_errors)
    return list_errors
