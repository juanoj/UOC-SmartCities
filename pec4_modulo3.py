import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import os
import pandas as pd
from functools import reduce

image1 = 'berlin_000001_000019_leftImg8bit_15-01-2018.png'
image2 = 'bonn_000000_000019_leftImg8bit_18-07-2017.png'
image3 = 'zurich_000000_000019_leftImg8bit_20-08-2015.png'

current = os.getcwd()
path2 = r'/dataset_cities/images/'
path = r'/dataset_cities/labels/'


def create_dataset(df: pd.DataFrame, city: str):
    temp = df[(df['city'] == city)].sort_values(by=['image_id'])
    temp.reset_index(drop=True, inplace=True)
    first = temp.loc[0, 'image_id']
    city_df = temp[temp['image_id'] == first].copy()
    #a = list(city_df.loc[:, 'x_c']*2028)
    #b = list(city_df.loc[:, 'witdh'] *1024)
    #c = [x-y for x,y in zip(a,b)]
    #print(c)
    city_df.loc[:, 'x_r'] = (city_df.loc[:, 'x_c'] - city_df.loc[:, 'witdh'] / 2) * 2048
    #city_df['x_r'] = c
    city_df.loc[:, 'y_r'] = (city_df.loc[:, 'y_c'] - city_df.loc[:, 'height'] / 2) * 1024
    return city_df


def draw_boxes(current: str, path: str, image: str, df: pd.DataFrame):
    img = plt.imread(current + path + image)
    figure, ax = plt.subplots(1)
    ax.imshow(img)
    for n in df.index:
        x, y, w, h = df.loc[n, 'y_r'], df.loc[n, 'x_r'], df.loc[n, 'witdh'] * 2048, df.loc[n, 'height'] * 1024
        rect = Rectangle((y, x), w, h, edgecolor='r', facecolor="none")
        ax.add_patch(rect)
    print('Imagen  '+image +'  impresa')
    return