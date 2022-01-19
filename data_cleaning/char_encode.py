import pandas as pd
import numpy as np
import chardet

np.random.seed(0)

before = "This is the euro symbol: €"
print(type(before))

after = before.encode("utf-8", errors="replace")
print(type(after))
print(after.decode("utf-8"))

with open("../input/kickstarter-projects/ks-projects-201801.csv", 'rb') as rawdata:
    result = chardet.detect(rawdata.read(10000))
print(result)

kickstarter_2016 = pd.read_csv("../input/kickstarter-projects/ks-projects-201612.csv", encoding='Windows-1252')
print(kickstarter_2016.head())

kickstarter_2016.to_csv("ks-projects-201801-utf8.csv")