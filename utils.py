
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
import math
def PredictTheValue(ar,bd,ag):
    df=pd.read_csv("Book2.csv")
    df=df.dropna()
    med=math.floor(df.bedroom.median())
    df=df.fillna(value={"bedroom":med})
    reg=linear_model.LinearRegression()
    reg.fit(df[['area','bedroom','age']],df.price)
    if ar<1 or bd<1 or ag<1:
        print("Enter correct values")
    pr=reg.predict([[ar,bd,ag]])
    return int(pr)