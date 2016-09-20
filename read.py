from write import read, read_scores
import string

a = read()
b = read_scores()

home = a.keys()
away = a.values()
scores = map(lambda s: s.strip(), b.values())

for i in scores:
    print i
