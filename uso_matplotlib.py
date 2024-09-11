import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('../dados/clientes-v2-tratados.csv')
print(df.head(20).to_string())

plt.figure(figsize=(10, 6))
df['nivel_educacao'].value_counts().plot(kind='bar', color='#90ee70')
plt.title('Divisiao de Escolaridade - 1')
plt.xlabel('Nivel de Educacao')
plt.ylabel('Quantidade')
plt.xticks(rotation=0)
plt.show()

x = df['nivel_educacao'].value_counts().index
y = df['nivel_educacao'].value_counts().values

plt.figure(figsize=(10, 6))
plt.bar(x, y, color='#60aa65')
plt.title('Divisao de Escolaridade - 2')
plt.xlabel('Nivel de Educacao')
plt.ylabel('Quantidade')
plt.show()

# Grafico de pizza
plt.figure(figsize=(10, 6))
plt.pie(y, labels=x, autopct='%.1f%%', startangle=90)
plt.title('Distribuicao de Nivel de Educacao')
plt.show()

# Grafico de dispersao
plt.hexbin(
    df['idade'],
    df['salario'],
    gridsize=40,
    cmap='Blues'
)
plt.colorbar(label='Contagem dentro do bin')
plt.xlabel('Idade')
plt.ylabel('Salario')
plt.title("Dispersao de Idade e Salario")
plt.show()

# Criar grafico de Pizza
plt.figure(figsize=(8, 8))
