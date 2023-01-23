import pandas as pd
import os
import pathlib

global labels

current = os.getcwd()
path = r"\dataset_cities\labels\\"


def parsename(filename: str):
    row = filename.strip().split('_')
    city = row[0]
    image_id = row[1]
    date = row[-1].split('.')[0]
    return city, image_id, date


def new_columns(file: str, df: pd.DataFrame):
    name = parsename(file)
    df.insert(0, 'city', name[0])
    df.insert(0, 'image_id', name[1])
    df.insert(0, 'date', name[2])
    return


def create_dataframe(route: str):
    df = pd.DataFrame()
    df = pd.read_csv(route, sep=' ', low_memory=False)
    df.columns = ['id', 'x_c', 'y_c', 'witdh', 'height', 'confidence']
    df.reset_index(drop=True, inplace=True)
    return df


def parsefile(current: str, path: str):
    global labels

    directory = pathlib.Path(current + path)
    for file in directory.iterdir():
        if os.path.isfile(file):
            filename = str(file).split('\\')[-1]
            temp = create_dataframe(current + path + filename)
            new_columns(filename, temp)
            labels = pd.concat([labels, temp])
    return labels


if __name__ == '__main__':
    labels = pd.DataFrame()
    parsefile(current, path)
    labels.info()
