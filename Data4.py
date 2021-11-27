import pandas as pd
import plotly_express as px
import numpy as np


df = pd.read_csv("Data4.csv")
x = df["Coffee in ml"].tolist()
y = df["sleep in hours"].tolist()

correlation = np.corrcoef(x, y)
print(correlation[0][1])


scatterPlot = px.scatter(x= x, y= y)
scatterPlot.show()


