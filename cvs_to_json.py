import pandas as pd
import json

# Lee el archivo CSV
df = pd.read_csv("movies_initial.csv")

# Guarda el DataFrame como JSON
df.to_json('movies.json', orient='records')

# Abre el archivo JSON y carga los datos
with open('movies.json', 'r') as file:
    movies = json.load(file)

# Itera sobre las primeras 100 películas e imprime la primera
for i in range(100):
    movie = movies[i]
    print(movie)
    break