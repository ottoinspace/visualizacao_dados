import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('../dados/clientes-v2-tratados.csv')
print(df.head(20).to_string)

# Grafico de dispersao
sns.jointplot(
    x='idade',
    y='salario',
    data=df,
    kind='scatter'
)
plt.show()

# Grafico de densidade
plt.figure(figsize=(10,6))
sns.kdeplot(
    df['salario'],
    fill=True,
    color="#863e9c"
)
plt.title('Densidade de Salarios')
plt.xlabel("Salario")
plt.show()

# Grafico de Pairplot - Dispersao e Histograma
sns.pairplot(df[[
    'idade',
    'salario',
    'nivel_educacao'
]])
plt.show()

# Grafico de Regressao
sns.regplot(
    x='idade',
    y='salario',
    data=df,
    color='#278f65',
    scatter_kws={
        'alpha': 0.5,
        'color': '#34c389'
    }
)
plt.title("Regressao de Salario por Idade")
plt.xlabel('Idade')
plt.ylabel('Salario')
plt.show()

# Grafico countplot com hue
sns.countplot(
    x='estado_civil',
    hue='nivel_educacao',
    data=df,
    palette='pastel'
)
plt.xlabel('Estado Civil')
plt.ylabel('Nivel de Educacao')
plt.legend(title='Nivel de Educacao')
plt.show()
