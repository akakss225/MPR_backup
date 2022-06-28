from haversine import haversine as hs
import numpy as np
import pandas as pd

# 역정보
stations = pd.read_csv("stations.csv")

# seoul 음식점 정보
restaurants = pd.read_csv("seoul_data.csv")

for i, r in restaurants.iterrows():
    r.loc['cate_1'] = '주점'
    print(r)
    break

for i, r in restaurants.iterrows():
    print(r.loc['name':])
    break
