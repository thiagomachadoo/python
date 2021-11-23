#!/usr/bin/env python
# coding: utf-8

# In[1]:


def calcula_media(valor1, valor2, valor3):
        soma = valor1 + valor2 + valor3
        media = soma / 3
        return media


# In[8]:


def calcula_media(*args, margem):
        soma = sum(args)
        media = soma / len(args)
        return media + margem


# In[9]:


calcula_media(10,8,9, margem = 0.3)


# In[11]:


def print_info(**qualquer):
    print(qualquer, type(qualquer))


# In[12]:


print_info(nome = 'Thiago', sobrenome = 'Rico')


# In[ ]:




