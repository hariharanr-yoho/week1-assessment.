#!/usr/bin/env python
# coding: utf-8

# # Chennai Weather Analysis
# 
# ## Introduction
# 
# This notebook analyzes temperature and rainfall
# data from Chennai and nearby cities.
# 
# ## Objectives
# 
# - Calculate average temperature.
# - Calculate average rainfall.
# - Filter Chennai records.
# - Compare city temperatures.
# 

# In[7]:


import pandas as pd
import matplotlib.pyplot as plt


# In[8]:


df = pd.read_csv("../data/chennai_data.csv")

print(df)


# In[9]:


chennai = df[df["City"] == "Chennai"]

print("Chennai Records:")
print(chennai)

print("Average Temperature:")
print(chennai["Temperature"].mean())

print("Average Rainfall:")
print(chennai["Rainfall"].mean())


# In[10]:


city_summary = df.groupby("City").agg({
    "Temperature": "mean",
    "Rainfall": "mean"
})

print(city_summary)


# In[11]:


city_summary["Temperature"].plot(
    kind="bar",
    color="skyblue"
)

plt.title("Average Temperature by City")
plt.xlabel("City")
plt.ylabel("Temperature")
plt.show()


# In[12]:


get_ipython().run_line_magic('timeit', 'df["Temperature"].mean()')


# ## Findings
# 
# 1. Chennai has three observations.
# 2. Chennai's average temperature is 35°C.
# 3. Chennai's average rainfall is 110 mm.
# 4. Chennai has a higher average temperature than Coimbatore and Madurai.
# 5. Chennai has the highest average temperature in this sample.
# 
# ## Conclusion
# 
# The dataset shows that Chennai has relatively
# high temperatures compared with the other cities.
