from haversine import haversine as hs
import numpy as np
import pandas as pd

stations = pd.read_csv("modifying/stations.csv")

df = pd.DataFrame()

for i, r in stations.iterrows():
    if r.loc['subwayLocation'][-1] != "역":
        r.loc['subwayLocation'] += "역"
    df = df.append(r.loc['subwayLocation':])

df.to_csv('data/stations.csv')
print("success")