#!/usr/bin/env python
# coding: utf-8

# In[1]:


dados_cidade = {
    'nome': 'São Paulo',
    'estado': 'São Paulo',
    'area_km2': 1521,
    'populacao_milhoes': 12.18
}


# In[2]:


print(type(dados_cidade))


# In[3]:


dados_cidade['pais'] = 'Brasil'


# In[4]:


print(dados_cidade)


# In[5]:


print(dados_cidade['area_km2'])


# In[6]:


dados_cidade_2 = dados_cidade


# In[7]:


dados_cidade_2['nome'] = 'Santos'


# In[8]:


print(dados_cidade)


# In[10]:


novos_dados = {
    'populacao_milhoes': 15,
    'fundacao': '25/01/1554'
}
dados_cidade.update(novos_dados)
print(dados_cidade)


# In[11]:


print(dados_cidade.keys()) #retorna uma lista de chaves de um dicionário
print('----')
print(dados_cidade.values())#retorna uma lista de valores de um dicionário
print('----')
print(dados_cidade.items())#retorna uma lista de tuplas (chave,valor) de um dicionario


# In[ ]:




