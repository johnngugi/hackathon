import json


def read():
    with open('data.json', 'r') as i:
        homes = json.load(i)

    return homes


def read_scores():
    with open('scores.json', 'r') as j:
        score = json.load(j)

    return score


def read_leagues():
    with open('leagues.json', 'r') as k:
        leagues = json.load(k)

    return leagues


a = read()
b = read_scores()
c = read_leagues()

home = a.keys()
away = a.values()
scores = map(lambda s: s.strip(), b.values())
scores.sort(reverse=True)
leagues = map(lambda t: t.strip(), c.values())
