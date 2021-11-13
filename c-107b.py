import csv
from numpy import double
import pandas as pd
import plotly.graph_objects as go
df=pd.read_csv("data.csv")
studentdf=df.loc[df["student_id"]=="TRL_987"]
mean=studentdf.groupby("level")["attempt"].mean()
print(mean)
fig=go.Figure(go.Bar(
    x=mean,
    y=["level 1","level 2","level 3","level 4"],
    orientation="h"
))
fig.show()