#!/usr/bin/env python
# coding: utf-8

# # Scraping data from a Real Website + Pandas

# In[4]:


from bs4 import BeautifulSoup
import requests


# In[5]:


url='https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text,'html')


# In[6]:


print(soup)


# In[7]:


soup.find_all('table')[1]


# In[8]:


soup.find('table', class_ ='wikitable sortable')


# In[9]:


table = soup.find_all('table')[1]
print(table)


# In[21]:


world_titles = table.find_all('th')


# In[22]:


world_titles


# In[23]:


world_table_titles=[title.text.strip() for title in world_titles]
print(world_table_titles)


# In[24]:


import pandas as pd


# In[32]:


df = pd.DataFrame(columns = world_table_titles)
df


# In[35]:


column_data = table.find_all('tr')


# In[40]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    lenght = len(df)
    df.loc[lenght] = individual_row_data
  


# In[41]:


df


# In[44]:


df.to_csv(r'C:\Users\zakv\Desktop\Data_analyst\companies.csv',  index = False)


# In[ ]:





# In[ ]:




