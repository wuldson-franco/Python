#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Data Science Academy - Python Fundamentos - Capítulo 2</font>
# 
# ## Download: http://github.com/dsacademybr

# In[ ]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Listas

# In[6]:


# Criando uma lista
listadomercado = ['ovos, farinha, leite, maças']


# In[7]:


# Imprimindo a lista
print(listadomercado)


# In[8]:


# Criando outra lista
listadomercado2 = ["ovos", "farinha", "leite", "maças"]


# In[9]:


# Imprimindo a lista
print(listadomercado2)


# In[ ]:


# Criando lista
lista3 = [12, 100, "Universidade"]


# In[10]:


# Exemplo da lista 1 com todos os itens no mesmo campo(Uma String Só)
listadomercado[0]


# In[12]:


# Exemplo da Lista 2 com os itens separados, pois os mesmos estão divididos pelas ""
listadomercado2[0]


# In[15]:


# Imprimindo
print(lista3)


# In[14]:


lista3 = [12, 100, "Universidade"]


# In[16]:


# Atribuindo cada valor da lista a uma variável.
item1 = lista3[0]
item2 = lista3[1]
item3 = lista3[2]


# In[17]:


# Imprimindo as variáveis
print(item1, item2, item3)


# ### Atualizando um item da lista

# In[18]:


# Imprimindo um item da lista
listadomercado2[2]


# In[19]:


# Atualizando um item da lista
listadomercado2[2] = "chocolate"


# In[20]:


# Imprimindo lista alterada
listadomercado2


# ### Deletando um item da lista

# In[22]:


# Out of index. Não é possível deletar um item que não existe na lista
del listadomercado2[4]   


# In[23]:


# Deletando um item específico da lista
del listadomercado2[3]


# In[24]:


# Imprimindo o item com a lista alterada
listadomercado2


# ### Listas de listas (Listas aninhadas)
# Listas de listas são matrizes em Python

# In[25]:


# Criando uma lista de listas - 3 listas dentro de uma lista 
listas = [[1,2,3], [10,15,14], [10.1,8.7,2.3]]


# In[26]:


# Imprimindo a lista
listas


# In[27]:


# Atribuindo um item da lista a uma variável
a = listas[0]


# In[28]:


a


# In[35]:


b = a[2]


# In[36]:


b


# In[37]:


list1 = listas[1]


# In[38]:


list1


# In[39]:


valor_1_0 = list1[0]


# In[40]:


valor_1_0


# In[41]:


valor_1_2 = list1[2]


# In[42]:


valor_1_2


# In[43]:


list2 = listas[2]


# In[44]:


list2


# In[45]:


valor_2_0 = list2[0]


# In[46]:


valor_2_0


# ### Operações com listas

# In[47]:


# Criando uma lista aninhada (lista de listas)
listas = [[1,2,3], [10,15,14], [10.1,8.7,2.3]]


# In[48]:


listas


# In[49]:


# Atribuindo à variável a, o primeiro valor da primeira lista
a = listas[0][0]


# In[50]:


a


# In[51]:


b = listas[1][2]


# In[52]:


b


# In[53]:


c = listas[0][2] + 10


# In[54]:


c


# In[55]:


d = 10


# In[56]:


d


# In[57]:


e = d * listas[2][0]


# In[58]:


e


# ### Concatenando listas

# In[59]:


lista_s1 = [34, 32, 56]


# In[60]:


lista_s1


# In[61]:


lista_s2 = [21, 90, 51]


# In[62]:


lista_s2


# In[63]:


# Concatenando listas
lista_total = lista_s1 + lista_s2


# In[64]:


lista_total


# ## Operador in

# In[65]:


# Criando uma lista
lista_teste_op = [100, 2, -5, 3.4]


# In[66]:


# Verificando se o valor 10 pertence a lista
print(10 in lista_teste_op)


# In[68]:


# Verificando se o valor 100 pertence a lista
print(-5 in lista_teste_op)


# ## Funções Built-in

# In[69]:


# Função len() retorna o comprimento da lista
len(lista_teste_op)


# In[70]:


# Função max() retorna o valor máximo da lista
max(lista_teste_op)


# In[71]:


# Função min() retorna o valor mínimo da lista
min(lista_teste_op)


# In[72]:


# Criando uma lista
listadomercado2 = ["ovos", "farinha", "leite", "maças"]


# In[73]:


# Adicionando um item à lista
listadomercado2.append("carne")


# In[74]:


listadomercado2


# In[78]:


listadomercado2.append("peixe")


# In[79]:


listadomercado2


# In[80]:


listadomercado2.count("carne")


# In[81]:


# Criando uma lista vazia
a = []


# In[82]:


print(a)


# In[83]:


type(a)


# In[84]:


a.append(10)


# In[85]:


a


# In[86]:


a.append(50)


# In[87]:


a


# In[88]:


old_list = [1,2,5,10]


# In[89]:


new_list = []


# In[90]:


# Copiando os itens de uma lista para outra
for item in old_list:
    new_list.append(item)


# In[91]:


new_list


# In[92]:


c = [20,30]


# In[93]:


c.append(60)


# In[94]:


c.append(70)


# In[95]:


c


# In[96]:


c.count(20)


# In[97]:


cidades = ['Recife', 'Manaus', 'Salvador']
cidades.extend(['Fortaleza', 'Palmas'])
print (cidades)


# In[98]:


cidades.index('Salvador')


# Lembre-se: em Python o índice começa por 0!

# In[99]:


cidades.index('Rio de Janeiro')


# In[100]:


cidades


# In[101]:


cidades.insert(2, 110)


# In[102]:


cidades


# In[103]:


# Remove um item da lista
cidades.remove(110)


# In[104]:


cidades


# In[105]:


# Reverte a lista
cidades.reverse()


# In[106]:


# Imprime a lista
cidades


# In[107]:


x = [3, 4, 2, 1]


# In[108]:


x


# In[109]:


# Ordena a lista
x.sort()


# In[110]:


x


# # Fim

# ### Obrigado
# 
# ### Visite o Blog da Data Science Academy - <a href="http://blog.dsacademy.com.br">Blog DSA</a>
