import seaborn as sns
import pandas as pd
import os
import pathlib
import matplotlib.pyplot as plt
from pec4_modulo1 import create_dataframe, new_columns

current = os.getcwd()
path3 = r'\dataset_cities\\'
file2 = 'class_name.txt'
regex = '(?:(?<=^\d)|(?<=^\d{2}))\s'


def ParseFile_noerror(current: str, path: str, exclude: set):
    global labels

    directory = pathlib.Path(current + path)
    for file in directory.iterdir():
        if os.path.isfile(file):
            filename = str(file).split('\\')[-1]
            if filename not in exclude:
                temp = create_dataframe(current + path + filename)
            else:
                temp = pd.DataFrame()
            new_columns(filename, temp)
            labels = pd.concat([labels, temp])
    return labels


def dataset_filtered(current, path, errors):
    global labels
    labels = pd.DataFrame()
    labels = ParseFile_noerror(current, path, errors)
    df = labels[labels['confidence'] >= 0.4]
    return df


def map_ids(path: str, file: str, df: pd.DataFrame):
    class_name = pd.read_csv(current + path3 + file2, sep=regex, header=None, engine='python')
    class_name.columns = ['object_id', 'object_name']
    objects = {k: v for (k, v) in zip(class_name['object_id'], class_name['object_name'])}
    df['object_id'] = df['object_id'].map(objects)
    return


def histogram(path: str, file: str, df: pd.DataFrame):
    histogram = df['id'].value_counts()
    data = pd.DataFrame(histogram)
    data.columns = ['frequency']
    data.reset_index(inplace=True)
    data.columns = ['object_id', 'frequency']
    data['object_id'] = data['object_id'].astype(int)
    map_ids(path, file, data)
    fig, ax = plt.subplots(figsize=(9, 6))
    sns.barplot(x="object_id", y="frequency", data=data.head(5), ax = ax)
    plt.xlabel("Top 5 Objects", fontsize=15)
    plt.ylabel("Count", fontsize=15)
    plt.show()
    print(data.head(5))
    return