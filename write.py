import json
from scrape import store, scores, leagues


def write_home():
    with open('data.json', 'wb') as f:
        json.dump(store, f)


def write_away():
    with open('scores.json', 'wb') as g:
        json.dump(scores, g)


def write_leagues():
    with open('leagues.json', 'wb') as h:
        json.dump(leagues, h)

write_home()
write_away()
write_leagues()
