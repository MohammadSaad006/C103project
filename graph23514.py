import pandas as pd
import plotly.express as px

df=pd.read_csv("Copydata.csv")
fig=px.scatter(df,x="date",y="cases",color="country",title="per capita income",size_max=60)
fig.show()