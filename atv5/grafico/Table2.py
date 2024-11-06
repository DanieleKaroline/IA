import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
from matplotlib.table import Table

# Carregar os arquivos CSV
resultados_df = pd.read_csv('Search_Heuristics/Results/resultados.csv')
resultados_amostras_df = pd.read_csv('Search_Heuristics/Results/resultados_amostras.csv')

def save_table_as_png(dataframe, filename):
    fig, ax = plt.subplots(figsize=(10, len(dataframe) * 0.2))  # Ajuste o tamanho da figura conforme necessário
    ax.axis('tight')
    ax.axis('off')
    
    # Cria uma tabela com os dados do DataFrame
    table = Table(ax)
    n_rows, n_cols = dataframe.shape

    # Adiciona células à tabela
    for i in range(n_rows):
        for j in range(n_cols):
            table.add_cell(i, j, width=0.2, height=0.1, text=str(dataframe.iat[i, j]), loc='center')
    
    # Adiciona cabeçalhos
    for j, col in enumerate(dataframe.columns):
        table.add_cell(-1, j, width=0.2, height=0.1, text=col, loc='center', facecolor='lightgrey')

    ax.add_table(table)
    
    # Salva a figura como PNG
    plt.savefig(filename, bbox_inches='tight', dpi=300)
    plt.close()

# Salvar as tabelas como PNG
save_table_as_png(resultados_df, 'grafico/resultados.png')
save_table_as_png(resultados_amostras_df, 'grafico/resultados_amostras.png')

print("Tabelas salvas como PNG com sucesso!")
