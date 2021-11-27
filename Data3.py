import pandas as pd
import numpy as np
import plotly_express as px

df = pd.read_csv("Data3.csv")
x = df["Days Present"].tolist()
y = df["Marks In Percentage"].tolist()

correlation = np.corrcoef(x, y)
print(correlation[0][1])


scatterPlot = px.scatter(x= x, y= y)
scatterPlot.show()