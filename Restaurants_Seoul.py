# 서울, 인천, 경기 지역 음식점 주소 및 좌표 데이터 정제

import pandas as pd
import numpy as np

df = pd.read_csv('/Users/sumin/Desktop/sumin/SideProject/informations/Seoul.csv')
df = df.loc[df['상권업종대분류명'] == '음식']

wantedColumn = pd.DataFrame(df, columns=['상호명', '상권업종대분류명', '상권업종중분류명', '상권업종소분류명', '표준산업분류명', '행정동명', '위도', '경도'])

wantedColumn.columns = [
    'name', # 상호명
    'cate_1', # 상권업종대분류명
    'cate_2', # 상권업종중분류명
    'cate_3', # 상권업종소분류명
    'cate_4', # 표준산업분류명
    'dong', # 행정동명
    'lon', # 위도
    'lat' # 경도
]

wantedColumn.to_csv('/Users/sumin/Desktop/sumin/SideProject/MPR_backup/modified_data_seoul.csv')
print(wantedColumn)