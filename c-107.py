import csv
import pandas as pd
import plotly.graph_objects as go
df = pd.read_csv("data.csv")
mean=df.groupby("level")["attempt"].mean()
print(mean)
fig=go.Figure(go.Bar(
    y=mean,
    x=["level 1","level 2","level 3","level 4"],
    orientation="v"
))
fig.show()