#
# Carregamento de variaveis
#
import pandas as pd


# 
# Codigo principal
# 1. carregar o arquivo base.xlsx
# 2. exibir linhas do arquivo
print("Inicio do script de PIB x Percapta")
r = pd.ExcelFile("base.xlsx")
print(pd.read_excel(r, "UF_Regiao"))