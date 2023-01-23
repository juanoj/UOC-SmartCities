import datetime
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def car_graph(cars: pd.DataFrame):
    cars_per_years= cars.groupby(['city',cars['date'].dt.year]).count()[['id']]
    cars_per_years = pd.DataFrame(cars_per_years)
    cars_per_years.reset_index(inplace = True)
    cars_per_years
    fig, ax = plt.subplots(figsize=(9, 6))
    sns.barplot (data=cars_per_years, x="date", y='id', hue = 'city', ax=ax)
    plt.xlabel("Cars images captured per city",fontsize= 15)
    plt.ylabel("Number of cars",fontsize= 15)
    plt.show()
    return