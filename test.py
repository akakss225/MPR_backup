from haversine import haversine as hs
import numpy as np
import pandas as pd

restaurants = pd.read_csv("data/seoul.csv")

df = pd.DataFrame()

for i, r in restaurants.iterrows():
    if r.loc['station'][-1] != "역":
        r.loc['station'] += "역"
    df = df.append(r.loc['name':])

df.to_csv('data/seoul2.csv')
print("success")