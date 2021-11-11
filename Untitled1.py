#!/usr/bin/env python
# coding: utf-8

# In[1]:


idade = input("Informe a sua idade: ")
print(idade,type(idade))


# In[2]:


idade = int(idade)
print(idade, type(idade))


# In[3]:


int('123abc')


# In[4]:


print(float('123.25'))
print(str(123.25))
print(bool('abc'))
print(bool(-2))


# In[10]:


salario_mensal = input("digite o valor do seu salário mensal: ")
salario_mensal = float(salario_mensal)

gasto_mensal = input("Gasto mensal em media: ")
gasto_mensal = float(gasto_mensal)

salario_total = salario_mensal * 12
gasto_total = gasto_mensal * 12

montante_economizado = salario_total - gasto_total
print('O montante que você pode economizar no fim do ano é de, ', montante_economizado)


# In[ ]:




