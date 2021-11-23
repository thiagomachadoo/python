#!/usr/bin/env python
# coding: utf-8

# In[1]:


def hello():
    print('Olá, mundo!')


# In[3]:


hello()


# In[4]:


def calcula_media(valor1, valor2, valor3):
    soma = valor1 + valor2 + valor3
    media = soma / 3
    return media


# In[6]:


resultado = calcula_media(10, 6, 3)
print(resultado)


# In[7]:


resultado2 = calcula_media(valor1= 5, valor2 = 10, valor3 = 8)
print(resultado2)


# In[9]:


print('Olá', end = ' ')
print(', Thiago')


# In[12]:


def calcula_media(valor1=0, valor2=0, valor3=0):
    soma = valor1 + valor2 + valor3
    media = soma / 3
    return media


# In[13]:


resultado = calcula_media()
print(resultado)


# In[ ]:




