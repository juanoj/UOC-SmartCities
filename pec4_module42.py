
import seaborn as sns
import pandas as pd
import os
import pathlib
import matplotlib.pyplot as plt
from pec4_modulo1 import create_dataframe, new_columns


def graphs(top: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(9, 6))
    sns.countplot (data= top, x="id", hue='city', ax=ax)
    plt.xlabel("Top 5 Objects per city",fontsize=15)
    plt.ylabel("Count",fontsize=15)
    plt.show()
    return
