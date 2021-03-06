# -*- coding: utf-8 -*-
"""Section 4: Charts and APIs.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1k_mPGskGgZE-6TTp93tNDgi-I-gvQbHS
"""

# importing necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import requests
import plotly.express as px

url = "https://api.covid19api.com/country/singapore/status/confirmed"

payload={}
headers = {}

# extract the data from the covidapi
response = requests.request("GET", url, headers=headers, data=payload)

if response.status_code == 200:
  print(f"Extraction successfull")

print(f"Extraction Data: \n\n {response.text}")

# Convert the response text to list of dictionary to make it usable for pandas dataframe
singapore_covid_data = list(eval(response.text))

print(f"Singapore Covid Data over time: \n\n {singapore_covid_data}")

# Convert the singapore covid data to a pandas dataframe
singapore_covid_df = pd.DataFrame(singapore_covid_data)
singapore_covid_df.head()

# Plot the chart for confirmed cases over time
line_chart = singapore_covid_df.loc[:, ['Date', 'Cases']]

fig = px.line(line_chart, x='Date', y='Cases')
fig.update_layout(xaxis=dict(tickformat='%d-%m-%Y'))
fig.show()

