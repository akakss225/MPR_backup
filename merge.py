import pandas as pd

gyeonggi = pd.read_csv("data/gyeonggi.csv")
incheon = pd.read_csv("data/incheon.csv")
seoul = pd.read_csv("data/seoul.csv")

result = pd.concat([gyeonggi, incheon, seoul])


result.to_csv("data/result.csv")
print("success")