import pandas as pd

url = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula1.2/ratings.csv"
dados = pd.read_csv(url)

filme_id_32 = dados[(dados['movieId'] == 32) & (dados['rating'] > 3)]

if filme_id_32.empty:
    print("Não há avaliações para o filme com ID=32 com nota maior que 3.")
else:
    nome_filme = filme_id_32.iloc[0]['title']
    print(f"O filme '{nome_filme}' é considerado um filme bom.")
