#Below code is used to get the table 
from io import StringIO
import pandas as pd
from plotly.io import to_json
import plotly.graph_objects as go
from azure.storage.blob import BlockBlobService
sas_token = '?sv=2021-04-10&st=2022-12-22T08%3A12%3A47Z&se=2023-12-30T08%3A12%3A00Z&sr=c&sp=racwl&sig=fMeYkXsCvwK%2F0qVrCmj2j3NiMricQjOPWOkAEXekIPA%3D'
account_name = 'willbedeletedsoon'
container_name = 'codx-pede-s02'
blob_name = 'diabetes.csv'

block_blob_service = BlockBlobService(account_name=account_name, sas_token= sas_token)
from_blob = block_blob_service.get_blob_to_text(container_name = container_name, blob_name=blob_name)
df=pd.read_csv(StringIO(from_blob.content))


fig = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns),
                line_color='darkslategray',
                fill_color='lightskyblue',
                align='left'),
    cells=dict(values=[df.Pregnancies, df.Glucose, df.BloodPressure, df.SkinThickness,df.Insulin,df.DiabetesPedigreeFunction,df.BMI,df.Age,df.Outcome],
                line_color='darkslategray',
                fill_color='lightcyan',
                align='left'))


])

container_dict = fig
dynamic_outputs = to_json(container_dict)