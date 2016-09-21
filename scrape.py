import json
from bs4 import BeautifulSoup
import urllib

r = urllib.urlopen("http://www.goal.com/en/results").read()

soup = BeautifulSoup(r)

current_date = soup.find_all("div", class_="date-header")
team_away = soup.find_all("div", class_="module module-team simple away")
team_home = soup.find_all("div", class_="module module-team simple home")
goal = soup.find_all("td", class_="vs")
league = soup.find_all("tr", class_="subheader")


def away_team():
    teamsa = []
    for row in team_away:
        for cell in row("span"):
            teamsa.append(cell.text)
    return teamsa


def home_team():
    teamsb = []
    for i in team_home:
        for cell in i("span"):
            teamsb.append(cell.text)
    return teamsb


def match_scores():
    scores = []
    for j in goal:
        for cell in j("div"):
            scores.append(cell.text)

    return scores


def get_date():
    date = [row.text for row in current_date]
    formated = date[0][1: 27]
    return formated


home = dict(zip([i for i in range(1, len(team_home) + 1)], home_team()))
away = dict(zip([i for i in range(1, len(team_away) + 1)], away_team()))
scores = dict(zip([i for i in range(1, len(goal) + 1)], match_scores()))

