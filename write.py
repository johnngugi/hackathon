import json
from scrape import store, scores

with open('data.json', 'wb') as f:
    json.dump(store, f)

with open('scores.json', 'wb') as g:
    json.dump(scores, g)


def read():
    with open('data.json', 'r') as h:
        a = json.load(h)

    return a


def read_scores():
    with open('scores.json', 'r') as i:
        b = json.load(i)

    return b
