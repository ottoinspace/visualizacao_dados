import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('../dados/clientes-v2-tratados.csv')
print(df.head().to_string())


# Histograma
plt.hist(df['salario'])
plt.show()

# Histograma - Paramentros
plt.figure(figsize=(10, 6))
plt.hist(df['salario'], bins=100, color='green', alpha=0.8)
plt.title("Histograma - Distribuicao de Salarios")
plt.xlabel("Salario")
plt.xticks(ticks=range(0, int(df['salario'].max())+2000, 2000))
plt.ylabel("Frequencia")
plt.grid(True)
plt.show()


# Multiplos graficos
plt.figure(figsize=(10, 6))
plt.subplot(2, 2, 1)  # 2 linhas, 2 colunas, 1o grafico
# Grafico de dispersao
plt.scatter(
    df['salario'],
    df['salario']
)
plt.title('Dispersao - Salario a Salario')
plt.xlabel('Salario')
plt.ylabel('Salario')

plt.subplot(1, 2, 2)  # 1 linha, 2 colunas, 2o grafico
plt.scatter(
    df['salario'],
    df['anos_experiencia'],
    color='#5885a8',
    alpha=0.6,
    s=30
)
plt.title('Dispersao - Idade e Anos de Experiencia')
plt.xlabel('Salario')
plt.ylabel('Anos de Experiencia')

# Mapa de Calor
corr = df[['salario', 'anos_experiencia']].corr()
plt.subplot(2, 2, 3)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlacao Salario e Idade')

plt.tight_layout()
plt.show()
