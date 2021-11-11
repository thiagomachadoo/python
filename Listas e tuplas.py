#!/usr/bin/env python
# coding: utf-8

# In[3]:


nomes_paises = ['Brasil', 'Argentina', 'China','Canadá','Japão']
print(nomes_paises)


# In[4]:


print('Tamanho da lista: ', len(nomes_paises))


# In[5]:


print('País: ', nomes_paises[4])


# In[7]:


print('País', nomes_paises[-2])


# In[8]:


nomes_paises[4] = 'Uruguai'
print('País: ', nomes_paises[4])


# In[9]:


nomes_paises[5] = 'Uruguai'


# In[10]:


print(nomes_paises[1:3])


# In[11]:


print(nomes_paises[1:-1])


# In[12]:


print(nomes_paises[2:])


# In[16]:


print(nomes_paises[:1])


# In[17]:


#pular conforme o numero proposto
print(nomes_paises[::2])


# In[18]:


#Retorna um resultado booleano
print("Brasil" in nomes_paises)


# In[19]:


print("China" not in nomes_paises)


# In[20]:


lista_capitais = []


# In[21]:


#Metodo é executado a partir do valor da variavel
lista_capitais.append('Brasilia')
lista_capitais.append('Manaus')
lista_capitais.append('Rio Grande')
lista_capitais.append('Gramado')

print(lista_capitais)


# In[22]:


lista_capitais.insert(2, 'Fartura')
print(lista_capitais)


# In[23]:


lista_capitais.remove('Brasilia')
print(lista_capitais)


# In[24]:


removido = lista_capitais.pop(2)
print(lista_capitais, removido)


# In[25]:


#Tuplas uma vez definida nao pode ser alterada
nomes_paises = 'Brasil', 'Argentina', 'China', 'Canadá', 'Japão'
print(nomes_paises, type(nomes_paises))


# In[26]:


nome_estado = 'São Paulo',
print(nome_estado, type(nome_estado))


# In[27]:


nomes_paises[0]


# In[28]:


#Pegar todos os valores de uma tupla so e colocar em uma variavel diferente
b, a, c, ca, j = nomes_paises


# In[30]:


print(b,a,c)


# In[31]:


print(*nomes_paises)


# In[ ]:




