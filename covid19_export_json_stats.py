#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""

LICENSE MIT
2020
Guillaume Rozier
Website : http://www.covidtracker.fr
Mail : guillaume.rozier@telecomnancy.net

README:
This file contains scripts that download data from data.gouv.fr and then process it to build many graphes.
I'm currently cleaning the code, please ask me if something is not clear enough.

The charts are exported to 'charts/images/france'.
Data is download to/imported from 'data/france'.
Requirements: please see the imports below (use pip3 to install them).

"""


# In[15]:


from multiprocessing import Pool
import requests
import pandas as pd
import math

from datetime import datetime
from datetime import timedelta

import json
import locale
import france_data_management as data
import numpy as np

locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
colors = px.colors.qualitative.D3 + plotly.colors.DEFAULT_PLOTLY_COLORS + px.colors.qualitative.Plotly + px.colors.qualitative.Dark24 + px.colors.qualitative.Alphabet
show_charts = False
now = datetime.now()
PATH = "/Users/guillaumerozier/Documents/Education/Covid-19/data/france/stats/"


# In[3]:


df, df_confirmed, dates, df_new, df_tests, df_deconf, df_sursaud, df_incid, df_tests_viros = data.import_data()


# In[28]:


df_france = df.groupby(["jour"]).sum().reset_index()

data_json = {}

#rea et hosp
for val in ["rea", "hosp", "dc_new"]:
    rea_json = {}
    date = df_france["jour"].max()
    rea_json["date"] = date[-2:] + "/" + date[-5:-3]
    rea_json["valeur"] = str(df_france[val].values[-1].astype(int))
    data_json[val] = rea_json
    
with open(PATH + 'stats.json', 'w') as outfile:
    json.dump(data_json, outfile)


# In[31]:





# In[19]:


df

