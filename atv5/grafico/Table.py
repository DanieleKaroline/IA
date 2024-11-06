import pandas as pd
from tabulate import tabulate

# Carregar os arquivos CSV
resultados_df = pd.read_csv('Search_Heuristics/Results/resultados.csv')
resultados_amostras_df = pd.read_csv('Search_Heuristics/Results/resultados_amostras.csv')

# Exibir o conteúdo dos arquivos como tabelas bonitas
print("Tabela de Resultados:")
print(tabulate(resultados_df, headers='keys', tablefmt='fancy_grid'))

print("\nTabela de Resultados Amostras:")
print(tabulate(resultados_amostras_df, headers='keys', tablefmt='fancy_grid'))
