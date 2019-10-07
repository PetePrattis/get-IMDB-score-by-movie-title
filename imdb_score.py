#!/usr/bin/python
# -*- coding: utf8 -*-

#Author Παναγιώτης Πράττης/Panagiotis Prattis

'''
Write a program which takes for input a title of a movie that the user choses and by using the link
http://www.omdbapi.com/ it returns the IMDB score and the awards that it may has.
'''

'''
These are all the fields that you can search for any movie, we search for title, imdbrating and awards
Example:
{"Title":"Inception","Year":"2010","Rated":"PG-13","Released":"16 Jul 2010","Runtime":"148 min","Genre":"Action, Adventure, Sci-Fi",
"Director":"Christopher Nolan","Writer":"Christopher Nolan","Actors":"Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page, Tom Hardy",
"Plot":"A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.",
"Language":"English, Japanese, French","Country":"USA, UK","Awards":"Won 4 Oscars. Another 143 wins & 198 nominations.",
"Poster":"http://ia.media-imdb.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SX300.jpg","Metascore":"74",
"imdbRating":"8.8","imdbVotes":"1,477,526","imdbID":"tt1375666","Type":"movie","Response":"True"}
'''

import json, requests
from imdb import IMDb
import omdb
import imdb
import urllib
from jabbapylib.web.web import get_page


BASE = 'http://www.omdbapi.com/?i=&'


class Movie(object):

    def __init__(self, keyword):
        self.keyword = keyword
        self.url = BASE + urllib.urlencode({'t' : keyword})
        self.d = self.get_info()


    def get_info(self):
        text = get_page(self.url)
        return json.loads(text)

    def __getitem__(self, key):
        return self.d[key]

    def __str__(self):
        li = []
        for key in self.d:
            li.append("{key}: {value}".format(key=key, value=self.d[key]))

        return '\n'.join(li)


def get_rating(title):
    m = Movie(title)

    return float(m['imdbRating'])


if __name__ == "__main__":

    m = Movie(raw_input('Enter movie title: '))
    while m['Response']=='False':
        m = Movie(raw_input('Please, re-enter movie title:'))

print 'Title: {title}'.format(title=m['Title'])
print 'Year: {year}'.format(year=m['Year'])
print 'Rating: {rating}'.format(rating=m['imdbRating'])
print 'Awards: {awards}'.format(awards=m['Awards'])
