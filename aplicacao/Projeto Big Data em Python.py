#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = 'formulario_clientes.csv'
analise = pd.read_csv(file)
analise


# In[47]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
file = 'formulario_clientes.csv'
analise = pd.read_csv(file)

# Excluir as colunas especificadas
analise = analise.drop(['Carimbo de data/hora', 'Qual a sua avaliação sobre o atendimento do professor?', 'Sugestão para melhorar a academia?'], axis=1)
analise


# In[8]:


# Gerar o gráfico de pizza com porcentagem
grafico1 = analise['Você é:'].value_counts().plot(kind='pie', autopct='%1.1f%%')

# Configurar o título do gráfico
plt.title('Quantidade de visitantes')

# Remover o rótulo do eixo y
grafico1.set_ylabel('')

# Exibir o gráfico
plt.show()



# In[17]:


# Definir as cores desejadas
cores = ['blue', 'green', 'red', 'yellow', 'purple']

# Gerar o gráfico de barras com cores
analise['Qual instrutor lhe atendeu?'].value_counts().plot(kind='bar', color=cores)

# Configurar título do gráfico
plt.title('Atendimento por instrutor')

# Configurar rotação do x no gráfico
plt.xticks(rotation=45, ha='right')

# Incluir rótulo do eixo y
plt.ylabel('Quantidade de atendimentos')

# Exibir o gráfico
plt.show()


# In[16]:


# Gerar o gráfico com porcentagem
grafico3 = analise['O que você achou do atendimento?'].value_counts().plot(kind='pie', autopct='%1.1f%%')

# Configurar o título do gráfico
plt.title('O que você achou do atendimento?')

# Remover o rótulo do eixo y
grafico3.set_ylabel('')

# Exibir o gráfico
plt.show()


# In[12]:


# Gerar o gráfico com porcentagem
grafico4 = analise['O que você achou da estrutura?'].value_counts().plot(kind='pie', autopct='%1.1f%%')

# Configurar o título do gráfico
plt.title('O que você achou da estrutura?')

# Remover o rótulo do eixo y
grafico4.set_ylabel('')

# Exibir o gráfico
plt.show()


# In[48]:


# Gerar o gráfico com porcentagem
grafico5 = analise['O que você achou dos aparelhos?'].value_counts().plot(kind='pie', autopct='%1.1f%%')

# Configurar o título do gráfico
plt.title('O que você achou dos aparelhos?')

# Remover o rótulo do eixo y
grafico5.set_ylabel('')

# Exibir o gráfico
plt.show()


# In[ ]:




