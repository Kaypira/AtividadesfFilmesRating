import pandas as pd

url = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula1.2/ratings.csv"
dados = pd.read_csv(url)

print("Os 12 primeiros registros:")
print(dados.head(12))

print("\nOs 6 últimos registros:")
print(dados.tail(6))

print("\nTamanho da massa de dados:", dados.shape)
