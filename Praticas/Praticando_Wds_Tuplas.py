#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Tuplas</font>
# 
# ## 

# In[ ]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Tuplas

# In[1]:


# Criando uma tupla
tupla1 = ("Geografia", 23, "Elefantes")


# In[2]:


# Imprimindo a tupla
tupla1


# In[3]:


# Tuplas não suportam append()
tupla1.append("Chocolate")   


# In[4]:


# Tuplas não suportam delete de um item específico
del tupla1["Gatos"]  


# In[5]:


# Tuplas podem ter um único item
tupla1 = ("Chocolate")


# In[6]:


tupla1


# In[7]:


tupla1 = ("Geografia", 23, "Elefantes")


# In[8]:


tupla1[0]


# In[9]:


# Verificando o comprimento da tupla
len(tupla1)


# In[10]:


# Slicing, da mesma forma que se faz com listas
tupla1[1:]


# In[11]:


tupla1.index('Elefantes')


# In[12]:


# Tuplas não suportam atribuição de item
tupla1[1] = 21


# In[13]:


# Deletando a tupla
del tupla1


# In[14]:


tupla1


# In[15]:


# Criando uma tupla
t2 = ('A', 'B', 'C')


# In[16]:


t2


# In[17]:


# Tuplas não suportam atribuição de item
t2[0] = 'D'


# In[18]:


# Usando a função list() para converter uma tupla para lista
lista_t2 = list(t2)


# In[19]:


lista_t2


# In[20]:


lista_t2.append('D')


# In[21]:


# Usando a função tuple() para converter uma lista para tupla
t2 = tuple(lista_t2)


# In[22]:


t2


# # Fim

# ### Obrigado
# 
# ### Visite o Blog da Data Science Academy - <a href="http://blog.dsacademy.com.br">Blog DSA</a>
