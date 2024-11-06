import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os arquivos CSV
resultados_df = pd.read_csv('Search_Heuristics/Results/resultados.csv')
resultados_amostras_df = pd.read_csv('Search_Heuristics/Results/resultados_amostras.csv')

# Configurações de estilo para os gráficos
plt.style.use('classic')
sns.set_palette('Set2')

# Gráfico 1: Gráfico de barras comparando 'q-medio' e '% do ótimo' para diferentes algoritmos
plt.figure(figsize=(10, 6))
ax = sns.barplot(data=resultados_df, x='algoritmo', y='q-medio', hue='instancia')
plt.title('Comparação de Qualidade Média (q-medio) entre Algoritmos e Instâncias')
plt.xlabel('Algoritmo')
plt.ylabel('Qualidade Média (q-medio)')
plt.xticks(rotation=45)
plt.legend(title='Instância')
plt.tight_layout()

# Exibir o gráfico 1
#plt.show()
plt.savefig('grafico/grafico1.png')


# Gráfico 2: Boxplot das amostras para visualizar a variação entre algoritmos
plt.figure(figsize=(12, 6))
samples_df = pd.melt(resultados_amostras_df, id_vars=['instancia', 'algoritmo'], 
                     value_vars=[f'Sample {i}' for i in range(1, 11)],
                     var_name='Amostras', value_name='Qualidade')

ax = sns.boxplot(data=samples_df, x='algoritmo', y='Qualidade', hue='instancia')
plt.title('Distribuição das Amostras de Qualidade por Algoritmo e Instância')
plt.xlabel('Algoritmo')
plt.ylabel('Qualidade')
plt.xticks(rotation=45)
plt.legend(title='Instância')
plt.tight_layout()

# Exibir o gráfico 2
#plt.show()
plt.savefig('grafico/grafico2.png')
