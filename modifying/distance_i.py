from haversine import haversine as hs
import numpy as np
import pandas as pd

# 역정보
stations = pd.read_csv("subwayLocation1.csv")

# seoul 음식점 정보
restaurants = pd.read_csv("modified_data_incheon.csv")

restaurants.insert(6, "station", "역")
restaurants.insert(7, "distance", 9999)


for r_rowIndex, r_row in restaurants.iterrows():
    r_location = (r_row.loc['lon'], r_row.loc['lat'])
    
    for rowIndex, row in stations.iterrows():
        st = row.loc['subwayLocation'] # 지하철 역
        st_location = (row.loc['lon'], row.loc['lat'])
        
        distance = round(hs(st_location, r_location), 3)
        
        if distance <= 2:
            if r_row.loc['distance'] > distance:
                restaurants.loc[r_rowIndex, 'station'] = st
                restaurants.loc[r_rowIndex, 'distance'] = distance

delete = restaurants[restaurants['distance'] == 9999].index
restaurants.drop(delete, inplace=True)

restaurants.to_csv('/Users/sumin/Desktop/sumin/SideProject/MPR_backup/incheon_data.csv')
print("success")