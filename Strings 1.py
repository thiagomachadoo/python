#!/usr/bin/env python
# coding: utf-8

# In[5]:


frase = "Hoje é dia de estudar python \"e também é quase sexta feira\""
print(frase)


# In[6]:


empresa = 'Google'
print(empresa[0])


# In[7]:


print(empresa[:3])


# In[9]:


nomes_cidades = "São Paulo, Belo Horizonte, Rio de Janeiro, Brasília"
nomes_cidades = nomes_cidades.split(', ')
print(nomes_cidades)


# In[10]:


cabecalho = "              MENU PRINCIPAL                "
print(cabecalho.split())


# In[11]:


nome_cidade = 'RiO De JaNeIrO'

print(nome_cidade.title()) #Rio de Janeiro
print(nome_cidade.capitalize()) #Rio de janeiro
print(nome_cidade.lower()) #rio de janeiro
print(nome_cidade.upper()) #RIO DE JANEIRO


# In[12]:


nome_cidade = input('Que cidade do Brasil é conhecida como terra da garoa')
nome_cidade = nome_cidade.strip()
while nome_cidade.lower() != 'são paulo':
    print('Tenta de novo campeão')
    nome_cidade = input('Que cidade do Brasil é conhecida como terra da garoa')
print('Boa fio!')


# In[13]:


mensagem = 'Você ouviu o que o mano disse na sala ontem? '
fui_citado = 'mano' in mensagem
print(fui_citado)


# In[ ]:




