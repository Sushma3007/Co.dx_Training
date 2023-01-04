#Below code is used to get the graph
import pandas as pd
import plotly.express as px
from plotly.io import to_json
 
# initialise data of lists.
data = {'X':[5,10,15,20,25,30,35,40]}

# Create DataFrame
df = pd.DataFrame(data)
df['Y'] = df['X'].pow(2)
fig = px.line(df, x="X", y="Y", title='Line Graph')


container_dict = fig
dynamic_outputs = to_json(container_dict)