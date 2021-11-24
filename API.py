#!/usr/bin/env python
# coding: utf-8

# In[6]:


get_ipython().system('pip install requests')


# In[7]:


import requests

url = 'https://api.exchangerate-api.com/v6/latest'
req = requests.get(url)
print(req.status_code)
# In[9]:


url = 'https://api.exchangerate-api.com/v6/latest'
req = requests.get(url)
print(req.status_code)


# In[10]:


dados = req.json()

print(dados)


# In[13]:


valor_reais = float(input('informe em reais'))
cotacao = dados['rates']['BRL']
print(f'R${valor_reais} em dolar valem U${(valor_reais / cotacao):..2f}')


# In[ ]:





# In[ ]:




