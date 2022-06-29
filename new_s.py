from haversine import haversine as hs
import numpy as np
import pandas as pd

# 역정보
stations = pd.read_csv("stations.csv")

# seoul 음식점 정보
restaurants = pd.read_csv("seoul_data.csv")

# new
df = pd.DataFrame()

for r_rowIndex, r_row in restaurants.iterrows():
    r_location = (r_row.loc['lon'], r_row.loc['lat'])
    
    for rowIndex, row in stations.iterrows():
        st = row.loc['subwayLocation'] + "역" # 지하철 역
        st_location = (row.loc['lon'], row.loc['lat'])
        
        distance = round(hs(r_location, st_location), 3)
        
        if r_row.loc['distance'] > distance:
            r_row.loc['station'] = st
            r_row.loc['distance'] = distance
        if r_row.loc['station'][-1] != "역":
            r_row.loc['station'] += "역"
    df = df.append(r_row.loc['name':])

df.to_csv('/Users/sumin/Desktop/sumin/SideProject/MPR_backup/seoul.csv')
print("success")