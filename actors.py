from imdb import IMDb
import pickle
import os

DIR = 'movies/'

movie_files = os.listdir('movies')

for file in movie_files:
    with open(DIR + file, 'rb') as file:
        movie = pickle.loads(file.read())
        if(movie['title'] ==  'Whiplash'):
            for actor in movie['cast']:
                print(actor)