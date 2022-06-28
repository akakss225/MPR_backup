from haversine import haversine as hs
import numpy as np
import pandas as pd

restaurants = pd.read_csv("seoul.csv")

for i, r in restaurants.iterrows():
    if r.loc['station'][-1] != "역":
        r.loc['station'] += "역"