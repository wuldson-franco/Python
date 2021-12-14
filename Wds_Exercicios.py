#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Praticando</font>
# 

# In[ ]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Exercícios Cap02

# In[70]:


# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.
Lista_Num = [1,2,3,4,5,6,7,8,9,10]
print(Lista_Num)


# In[71]:


# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
Lista_Obj = ['Cadeira', 'Celular','Mesa', 'Teclado', 'Mouse']
print(Lista_Obj)


# In[7]:


# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
Str1 = 'Formula'


# In[11]:


Str2 = ' 1'


# In[13]:


Str3 = Str1 + Str2


# In[14]:


Str3


# In[15]:


# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla
Tupla_Num = (1, 2, 2, 3, 4, 4, 4, 5)


# In[20]:


Tupla_Num.count(4)


# In[21]:


# Exercício 5 - Crie um dicionário vazio e imprima na tela
Dic_Vazio = {}


# In[22]:


Dic_Vazio


# In[27]:


# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
Dic_Familia = {"Mae": 31, "Pai": 32, "Filha": 9}


# In[28]:


Dic_Familia


# In[29]:


# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
Dic_Familia["Woody"] = 1


# In[30]:


Dic_Familia


# In[31]:


# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.
Dic_Familia = {'Mae':[29,31] , 'Pai': 32, 'Filha': 9}


# In[32]:


Dic_Familia


# In[56]:


# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.
List_Doida = ['Elemento1']


# In[67]:


List_Doida


# In[66]:


List_Doida.append(55.5)


# In[64]:


List_Doida.pop(2)


# In[34]:


# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'


# In[72]:


frase[0:18]


# # Fim

# ### Obrigado
# 
# ### Visite o Blog da Data Science Academy - <a href="http://blog.dsacademy.com.br">Blog DSA</a>

# Parabéns se você chegou até aqui. Use o voucher PYTHONDSA9642 para comprar qualquer curso ou Formação da DSA com 5% de desconto.
