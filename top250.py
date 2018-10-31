from imdb import IMDb
import pickle

with open('top250.dat', 'rb') as file:
    TOP250 = pickle.loads(file.read())

IA = IMDb()

DIR = 'movies/'

# mov = TOP250[0]

m = IA.get_movie('0057012')

print(m.key2infoset)
# IA.update(mov)
# print(mov.infoset2keys)
# print(mov['cast'])

# for movie in TOP250:
#     IA.update(movie)
#     with open(DIR + movie.movieID + '.dat', 'wb') as file:
#         file.write(pickle.dumps(movie))
#     print(movie['title'])

