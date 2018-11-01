from imdb import IMDb
import pickle
import os

DIR = 'movies/'

movie_files = os.listdir('movies')

actors_list = list()

# for file in movie_files:
#         with open(DIR + file, 'rb') as file:
#             movie = pickle.loads(file.read())
#             with open(DIR + movie.movieID + "_actors.txt", "w", encoding='utf-8') as file:
#                 try:
#                     for actor in movie['cast']:
#                         actors_list.append(actor)
#                 except Exception as e:
#                     pass
#                 finally:
#                     pass

for file in movie_files:
    if file.endswith('.txt'):
        with open(DIR + file, 'r', encoding='utf-8') as file:
            for line in file:
                actors_list.append(line)

with open('all_actors.txt', 'w', encoding='utf-8') as file:
    for actor in list(sorted(set(actors_list))):
        file.write(actor)