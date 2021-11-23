#!/usr/bin/env python
# coding: utf-8

# In[1]:


nomes_cidades = ['São Paulo', 'Londres', 'Tóquio', 'Paris']
for nome in nomes_cidades:
    print(nome)


# In[2]:


cidade = {
    'nome': 'São Paulo',
    'estado': 'São Paulo',
    'população_milhoes': 12.2
}
for chave in cidade:
    print(f'{chave}:{cidade[chave]}')


# In[3]:


nomes_cidades = ['São Paulo', 'Londres', 'Tóquio', 'Paris']
for nome in nomes_cidades:
    nome = 'Rio de Janeiro'
    print(nomes_cidades)


# In[4]:


for posicao in range(len(nomes_cidades)):
    print(posicao)


# In[5]:


print(list(range(10)))
print(list(range(2,10)))
print(list(range(2,10,2)))


# In[ ]:




