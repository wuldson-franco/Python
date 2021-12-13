#!/usr/bin/env python
# coding: utf-8

# # Dicionarios
# 
# 

# In[ ]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Dicionários

# In[1]:


# Isso é uma lista
estudantes_lst = ["Mateus", 24, "Fernanda", 22, "Tamires", 26, "Cristiano", 25]   


# In[2]:


estudantes_lst


# In[12]:


# Isso é um dicionário
estudantes_dict = {"Mateus":24, "Fernanda":22, "Tamires":26, "Cristiano":25}


# In[16]:


estudantes_dict 


# In[5]:


estudantes_dict["Mateus"]


# In[14]:


estudantes_dict["Pedro"] = 23


# In[15]:


estudantes_dict["Pedro"]


# In[9]:


estudantes_dict["Tamires"]


# In[17]:


estudantes_dict.clear()


# In[18]:


estudantes_dict


# In[19]:


del estudantes_dict


# In[20]:


estudantes_dict


# In[21]:


estudantes = {"Mateus":24, "Fernanda":22, "Tamires":26, "Cristiano":25}


# In[22]:


estudantes


# In[23]:


len(estudantes)


# In[24]:


estudantes.keys()


# In[25]:


estudantes.values()


# In[26]:


estudantes.items()


# In[27]:


estudantes2 = {"Maria":27, "Erika":28, "Milton":26}


# In[28]:


estudantes2


# In[29]:


estudantes.update(estudantes2)


# In[30]:


estudantes


# In[31]:


dic1 = {}


# In[32]:


dic1


# In[33]:


dic1["key_one"] = 2


# In[34]:


print(dic1)


# In[35]:


dic1[10] = 5


# In[36]:


dic1


# In[37]:


dic1[8.2] = "Python"


# In[38]:


dic1


# In[39]:


dic1["teste"] = 5


# In[40]:


dic1


# In[42]:


dict1 = {}


# In[43]:


dict1


# In[44]:


dict1["teste"] = 10


# In[45]:


dict1["key"] = "teste"


# In[46]:


# Atenção, pois chave e valor podem ser iguais, mas representam coisas diferentes.
dict1


# In[47]:


dict2 = {}


# In[48]:


dict2["key1"] = "Big Data"


# In[49]:


dict2["key2"] = 10


# In[50]:


dict2["key3"] = 5.6


# In[51]:


dict2


# In[52]:


a = dict2["key1"]


# In[53]:


b = dict2["key2"]


# In[54]:


c = dict2["key3"]


# In[55]:


a, b, c


# In[56]:


# Dicionário de listas
dict3 = {'key1':1230,'key2':[22,453,73.4],'key3':['leite','maça','batata']}


# In[57]:


dict3


# In[58]:


dict3['key2']


# In[59]:


# Acessando um item da lista, dentro do dicionário
dict3['key3'][0].upper()


# In[60]:


# Operações com itens da lista, dentro do dicionário
var1 = dict3['key2'][0] - 2


# In[61]:


var1


# In[62]:


# Duas operações no mesmo comando, para atualizar um item dentro da lista
dict3['key2'][0] -= 2


# In[63]:


dict3


# ### Criando dicionários aninhados

# In[64]:


# Criando dicionários aninhados
dict_aninhado = {'key1':{'key2_aninhada':{'key3_aninhada':'Dict aninhado em Python'}}}


# In[65]:


dict_aninhado


# In[66]:


dict_aninhado['key1']['key2_aninhada']['key3_aninhada']


# # Fim

# ### Obrigado
# 
# ### Visite o Blog da Data Science Academy - <a href="http://blog.dsacademy.com.br">Blog DSA</a>
