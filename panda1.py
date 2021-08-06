import numpy as np
import pandas as pd

dict1 ={
    "name":["harry","rohan","shubh"],
    "marks":[98,76,88],
    "city":["Siliguri","kolkata","chennai"]
}
df = pd.DataFrame(dict1)
# print(df)
# print(df.tail()) 
# print(df.describe())
df.to_csv("sample1.csv")
n = pd.read_csv("carsample.csv")
print(n)
print()
