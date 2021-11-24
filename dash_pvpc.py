# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 18:36:31 2021

@author: Rodrigo
"""

import pandas as pd
import requests
import json
import plotly.express as xp
import matplotlib.pyplot as plt
from datetime import datetime
url = "https://api.esios.ree.es/archives/70/download_json?locale=es&date=2021-11-01"

response = requests.get(url)
df = pd.DataFrame(response.json()["PVPC"])
#df["fecha"] = datetime.datetime(df["Dia"]+df["Hora"])

df2 = df[['Dia','PCB']]
df2['PCB'] = df2['PCB'].apply(lambda x: x.replace(',','.'))
df2['PCB'] = df2['PCB'].apply(lambda x: float(x))

df2.plot()
#%%

#%%
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 18:36:31 2021

@author: Rodrigo
"""

import pandas as pd
import requests
import json
import plotly.express as xp
import matplotlib.pyplot as plt
from datetime import datetime
url = "https://api.esios.ree.es/archives/70/download_json?locale=es&date=2021-11-01"

response = requests.get(url)
df = pd.DataFrame(response.json()["PVPC"])
#df["fecha"] = datetime.datetime(df["Dia"]+df["Hora"])
lista = list(df["PCB"])

nueva_PCB = [c.replace(',', '.') for c in lista]
l = [float(i) for i in nueva_PCB]

lista_dias = df["Hora"]
k = [i[0:2] for i in lista_dias]

df["PCB"] = l
df.index = df["Hora"]

x = k
y = df["PCB"]
fig, ax = plt.subplots()
ax.plot(x, y)
plt.xticks(k)
plt.show()


