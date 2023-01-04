#Below code is used to make the Multi Trace plot
#Plot 1
from io import StringIO
import pandas as pd
from plotly.io import to_json
import plotly.express as px
from azure.storage.blob import BlockBlobService
sas_token = '?sv=2021-04-10&st=2022-12-22T08%3A12%3A47Z&se=2023-12-30T08%3A12%3A00Z&sr=c&sp=racwl&sig=fMeYkXsCvwK%2F0qVrCmj2j3NiMricQjOPWOkAEXekIPA%3D'
account_name = 'willbedeletedsoon'
container_name = 'codx-pede-s02'
blob_name = 'df_complete.csv'

block_blob_service = BlockBlobService(account_name=account_name, sas_token= sas_token)
from_blob = block_blob_service.get_blob_to_text(container_name = container_name, blob_name=blob_name)
df=pd.read_csv(StringIO(from_blob.content))
df=df.dropna()

fig = px.bar(df, x="artist", y=df.year, title="Famous Artist across years")

container_dict = fig
dynamic_outputs = to_json(container_dict)

#Plot2

from io import StringIO
import pandas as pd
from plotly.io import to_json
import plotly.express as px
from azure.storage.blob import BlockBlobService
sas_token = '?sv=2021-04-10&st=2022-12-22T08%3A12%3A47Z&se=2023-12-30T08%3A12%3A00Z&sr=c&sp=racwl&sig=fMeYkXsCvwK%2F0qVrCmj2j3NiMricQjOPWOkAEXekIPA%3D'
account_name = 'willbedeletedsoon'
container_name = 'codx-pede-s02'
blob_name = 'df_complete.csv'

block_blob_service = BlockBlobService(account_name=account_name, sas_token= sas_token)
from_blob = block_blob_service.get_blob_to_text(container_name = container_name, blob_name=blob_name)
df=pd.read_csv(StringIO(from_blob.content))
df=df.dropna()


fig = px.pie(df, values='danceability', names="year", title='Most Danceability Available songs across years')

container_dict = fig
dynamic_outputs = to_json(container_dict)

#Plot 3
from io import StringIO
import pandas as pd
from plotly.io import to_json
import plotly.express as px
from azure.storage.blob import BlockBlobService
sas_token = '?sv=2021-04-10&st=2022-12-22T08%3A12%3A47Z&se=2023-12-30T08%3A12%3A00Z&sr=c&sp=racwl&sig=fMeYkXsCvwK%2F0qVrCmj2j3NiMricQjOPWOkAEXekIPA%3D'
account_name = 'willbedeletedsoon'
container_name = 'codx-pede-s02'
blob_name = 'df_complete.csv'

block_blob_service = BlockBlobService(account_name=account_name, sas_token= sas_token)
from_blob = block_blob_service.get_blob_to_text(container_name = container_name, blob_name=blob_name)
df=pd.read_csv(StringIO(from_blob.content))
df=df.dropna()



fig = px.line(df.head(5), x="artist", y='followers',color="year",title="Arist based on most fan following")

container_dict = fig
dynamic_outputs = to_json(container_dict)

#Plot 4
from io import StringIO
import pandas as pd
from plotly.io import to_json
import plotly.express as px
from azure.storage.blob import BlockBlobService
sas_token = '?sv=2021-04-10&st=2022-12-22T08%3A12%3A47Z&se=2023-12-30T08%3A12%3A00Z&sr=c&sp=racwl&sig=fMeYkXsCvwK%2F0qVrCmj2j3NiMricQjOPWOkAEXekIPA%3D'
account_name = 'willbedeletedsoon'
container_name = 'codx-pede-s02'
blob_name = 'df_complete.csv'

block_blob_service = BlockBlobService(account_name=account_name, sas_token= sas_token)
from_blob = block_blob_service.get_blob_to_text(container_name = container_name, blob_name=blob_name)
df=pd.read_csv(StringIO(from_blob.content))
df=df.dropna()

fig = px.scatter(df, x="artist_popularity", y="energy" , color="artist")

container_dict = fig
dynamic_outputs = to_json(container_dict)