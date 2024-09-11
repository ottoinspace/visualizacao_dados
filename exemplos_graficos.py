import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("../dados/clientes-v2-tratados.csv")

df_corr = df[['salario', 'idade', 'numero_filhos', 'nivel_educacao', 'estado']].corr()
# Heatmap de correlacao
plt.figure(figsize=(10, 8))
sns.heatmap(df_corr, annot=True, fmt=".2f")
plt.title('Mapa de Calor de Correlacao entre Variaveis')
plt.show()

#
