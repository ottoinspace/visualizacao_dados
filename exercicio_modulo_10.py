import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('ecommerce_preparados.csv')
print(df.head())


# Grafico de dispersao
plt.hexbin(
    df['Nota'],
    df['Preço'],
    gridsize=40,
    cmap='Blues'
)
plt.colorbar(label='Contagem dentro do bin')
plt.xlabel('Nota')
plt.ylabel('Preço')
plt.title("Dispersão de Nota e Preço")
plt.show()

# Mapa de calor
plt.figure(figsize=(10, 6))
corr = df[['Nota', 'Preço']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlação Nota e Preço')
plt.show()

x = df['Marca_Cod'].value_counts().index
y = df['Marca_Cod'].value_counts().values

# Gráfico de barra
plt.figure(figsize=(10, 6))
plt.bar(x, y, color='#60aa65')
plt.title('Divisao de Marca - 2')
plt.xlabel('Marca')
plt.ylabel('Quantidade')
plt.show()

# Grafico de pizza
plt.figure(figsize=(10, 6))
plt.pie(y, labels=x, autopct='%.1f%%', startangle=90)
plt.title('Distribuicao de Marca')
plt.show()

# Gráfico de densidade
plt.figure(figsize=(10, 6))
sns.kdeplot(
    df['Preço'],
    fill=True,
    color="#863e9c"
)
plt.title('Densidade de Preços')
plt.xlabel("Preço")
plt.show()
