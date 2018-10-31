from imdb import IMDb
import pickle

IA = IMDb()

## getting top 250 movies
top250 = IA.get_top250_movies()
dump = pickle.dumps(top250)

with open('top250.dat', 'wb') as file:
    file.write(dump)