#Below code is used to make the plot 
import pandas as pd
from sklearn.datasets import *
import plotly.graph_objects as go
from plotly.io import to_json

fig_df = pd.DataFrame(data = load_diabetes().data, columns = load_diabetes().feature_names)
fig = go.Figure()
fig.add_trace(go.Histogram(x = fig_df['sex']))


container_dict = {}
container_dict = fig
dynamic_outputs = to_json(container_dict)