# %% [markdown]
# # Python Insights - Analisando Dados com Python
# 
# ### Case - Cancelamento de Clientes
# 
# Você foi contratado por uma empresa com mais de 800 mil clientes para um projeto de Dados. Recentemente a empresa percebeu que da sua base total de clientes, a maioria são clientes inativos, ou seja, que já cancelaram o serviço.
# 
# Precisando melhorar seus resultados ela quer conseguir entender os principais motivos desses cancelamentos e quais as ações mais eficientes para reduzir esse número.
# 
# Base de dados e arquivos: https://drive.google.com/drive/folders/1uDesZePdkhiraJmiyeZ-w5tfc8XsNYFZ?usp=drive_link

# %%
!pip install pandas
!pip install plotly

# %%
import pandas as pd
import plotly.express as px

tabela = pd.read_csv("cancelamentos.csv")
tabela = tabela.drop(columns="CustomerID")

display(tabela)

# %%
display(tabela.info())


# %%
tabela = tabela.dropna()
display(tabela.info())

# %%
tabela["cancelou"].value_counts(normalize=True) #conta a porcentagem de cancelamentos

# %%
#analise da causa de cancelamentos

grafico = px.histogram(tabela, x = "duracao_contrato", color = "cancelou", text_auto= True)

grafico.show()

# %%
#analise causas de cancelamento:
#todos os clientes mensais cancelaram

#para cada coluna da tabela eu quero exibir o grafico para analisar o efeito no cancelamento

for coluna in tabela.columns:

    grafico = px.histogram(tabela, x = coluna, color = "cancelou", text_auto= True)
    grafico.show()

# %%
# clientes do contrato mensal TODOS cancelam
    # ofercer desconto nos planos anuais e trimestrais
# clientes que ligam mais do que 4 vezes para o call center, cancelam
    # criar um processo para resolver o problema do cliente em no máximo 3 ligações
# clientes que atrasaram mais de 20 dias, cancelaram
    # política de resolver atrasos em até 10 dias (equipe financeira)

tabela = tabela[tabela["duracao_contrato"]!="Monthly"]
tabela = tabela[tabela["ligacoes_callcenter"]<=4]
tabela = tabela[tabela["dias_atraso"]<=20]

display(tabela["cancelou"].value_counts())
# em percentual
display(tabela["cancelou"].value_counts(normalize=True))

#resultado reducao de 56% para 18% de cancelamentos


