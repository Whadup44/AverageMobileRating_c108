import pandas as pd
import plotly.figure_factory as ff
import csv
data = pd.read_csv("AverageMobileRating.csv")
fig = ff.create_distplot([data["Avg Rating"].tolist()], ["Average Rating"], show_hist = True)
fig.show()