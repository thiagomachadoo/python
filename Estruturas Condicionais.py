#!/usr/bin/env python
# coding: utf-8

# In[5]:


valor_passagem = 4.30

valor_corrida = input('Qual o valor da corrida? ')

if float(valor_corrida) <= valor_passagem * 5:
    print('Pague a corrida')
if float(valor_corrida) > valor_passagem * 5:
    print('Pegue o ônibus')


# In[6]:


valor_passagem = 4.30

valor_corrida = input('Qual o valor da corrida? ')

if float(valor_corrida) <= valor_passagem * 5:
    print('Pague a corrida')
else:
    print('Pegue o ônibus')


# In[11]:


valor_passagem = 4.30

valor_corrida = input('Qual o valor da corrida? ')

if float(valor_corrida) <= valor_passagem * 5:
    print('Pague a corrida')
else:
    if float(valor_corrida) <= valor_passagem * 6:
        print('Aguarde um momento, o valor pode abaixar')
    else:
        print('Pegue o ônibus')


# In[14]:


valor_passagem = 4.30

valor_corrida = input('Qual o valor da corrida? ')

if float(valor_corrida) <= valor_passagem * 5:
    print('Pague a corrida')
elif float(valor_corrida) <= valor_passagem * 6:
        print('Aguarde um momento, o valor pode abaixar')
else:
        print('Pegue o ônibus')


# In[ ]:





# In[ ]:




