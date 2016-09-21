import json
from scrape import home, away, scores


def write_home_team():
    with open('home.json', 'wb') as f:
        json.dump(home, f)


def write_away_team():
    with open('away.json', 'wb') as g:
        json.dump(away, g)


def write_scores():
    with open('scores.json', 'wb') as h:
        json.dump(scores, h)


# def write_leagues():
#     with open('leagues.json', 'wb') as h:
#         json.dump(leagues, h)

write_home_team()
write_away_team()
write_scores()
# write_leagues()
