#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Soma
4 + 4


# In[2]:


# Subtração
4 - 3


# In[4]:


# Multiplicação
3 * 3


# In[6]:


# Divisão
3 / 2


# In[7]:


# Modulo
10 % 3


# ### Função Type

# In[8]:


type(5)


# In[10]:


type(5.2)


# In[11]:


a = 'Eu Sou uma String'
type(a)


# ### Operações Com numeros float

# In[12]:


3.1 + 6.4


# In[14]:


4 + 4.0


# In[15]:


# Resultado é um numero float
4 / 2


# In[17]:


# Resultado é um numero inteiro, pois usei duas barras
4 // 2


# In[18]:


# Sem utilizar as duas barras ele retornou o numero por completo
4 / 3.0


# In[19]:


# Ele aredondou o valor ao utilizar as duas barras
4 // 3.0


# ### Conversão

# In[22]:


float(9)


# In[25]:


int (6.0)


# In[27]:


#Ele arredonda
int (6.5)


# ### Hexadecimal e Binário

# In[31]:


hex(394)


# In[32]:


hex(217)


# In[33]:


bin(286)


# In[34]:


bin(390)


# ### Funções Abs, round e pow

# In[37]:


abs(-8)


# In[38]:


abs(8)


# In[43]:


round(3.14151922,3)


# In[40]:


pow(4,2)


# In[41]:


pow(5,3)


# ### Variaveis

# In[2]:


pessoa1, pessoa2, pessoa3 = "wuldson","Laura", "jeannyne"


# In[3]:


pessoa2


# In[4]:


type(pessoa2)


# In[1]:


#Não começar variavel com numeros, da erro
1x = 85


# In[2]:


#Não pode usar palavra reservada como nome de variavel - CONSULTAR DOCUMENTAÇÃO
except = 2


# ### Variaies atribuidas a outras variaveis e ordem dos operadores

# In[22]:


largura = 0.6


# In[23]:


comprimento = 7.5


# In[24]:


metro_quadrado = largura * comprimento


# In[26]:


metro_quadrado


# ### Concatenação de variaiveis

# In[28]:


nome = "Woody"


# In[29]:


sobrenome = "Pride"


# In[30]:


fullname = nome + " " + sobrenome


# In[31]:


fullname


# In[ ]:




