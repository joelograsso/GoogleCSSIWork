#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

inside_movie = {
    "title": "Inside Out",
    "id": "tt2096673",
    "year_released": 2012,
    "rating": "PG",
    "score": 7.5,
    "out_of": 10,
    "reviews": 463787,
    "genre": "Disney"
}
inside_movie["year_released"] = 2015
inside_movie['score'] = 8.2
inside_movie.pop('out_of')
inside_movie['reviews'] = 541183


endGame = {
    "title": "Avenger's: End Game",
    "id": "tt4154796",
    "year_released": 2019,
    "rating": "PG-13",
    "score": 8.7,
    "out_of": 10,
    "reviews": 475906,
    "genre": 'Marvel'

}
spiderMan = {
    "title": "Spiderman: Far From Home",
    "id": "tt6320628",
    "year_released": 2019,
    "rating": "PG-13",
    "score": 8.0,
    "out_of": 10,
    "reviews": 104071,
    'genre': 'Marvel'
}

movies = [inside_movie, endGame, spiderMan]

genre = raw_input('Marvel or Disney? ')
def getMovie(genre):
    if genre == "Disney":
        print(str(movies[inside_movie]))
    if genre == "Marvel":
        print(movies[endGame])
        print(movies[spiderMan])

getMovie(genre)






# Do not edit the code above!

# Write your code below to update the information in accordance with its
# IMDB page: http://www.imdb.com/title/tt2096673/
