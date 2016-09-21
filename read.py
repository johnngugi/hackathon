import json
from collections import OrderedDict


def read_home():
    with open('home.json', 'r') as i:
        homes = json.load(i)

    return homes


def read_away():
    with open('away.json', 'r') as j:
        aways = json.load(j)

    return aways


def read_scores():
    with open('scores.json', 'r') as k:
        score = json.load(k)

    return score


# def read_leagues():
#     with open('leagues.json', 'r') as k:
#         leagues = json.load(k)
#
#     return leagues


a = read_home()
b = read_away()
c = read_scores()

tuple1 = ([x for x in range(1, len(read_home()) + 1)])
tuple2 = ([y for y in range(1, len(read_away()) + 1)])
tuple3 = ([z for z in range(1, len(read_scores()) + 1)])

home = []
away = []
scores = []

for key in tuple1:
    home.append(a[unicode(str(key), 'utf-8')])

for key in tuple2:
    away.append(b[unicode(str(key), 'utf-8')])

for key in tuple3:
    scores.append(c[unicode(str(key), 'utf-8')])

