import pandas as pd
from preswald import connect, get_df, query, table, text, plotly
import plotly.express as px

connect()

df = get_df("my_dataset")

sql = """SELECT * FROM my_dataset WHERE firmness >= 30"""

filtered_df = query(sql, "my_dataset")

text("# My Data Analysis App")
table(filtered_df, title="Rows where firmness >= 30")


fig = px.scatter(df, x="firmness", y="weight_g", color="color_category")

plotly(fig)
