import pandas as pd
import plotly.express as px

df = pd.read_csv("PixelMath.csv")

x = df.groupby(["student_id","level"],as_index=False)["attempt"].mean()

fig = px.scatter(x,x = "student_id",y = "level",color = "attempt",size = "attempt")
fig.show()