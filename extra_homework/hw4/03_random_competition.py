# ЮНУСОВ ПАВЕЛ ИИАД 1

import random

SIZE = 20

team1 = [round(random.uniform(5, 10), 2) for x in range(SIZE)]
team2 = [round(random.uniform(5, 10), 2) for z in range(SIZE)]

winners = [max(team1[i], team2[i]) for i in range(SIZE)]

print("Первая команда:", team1)
print("Вторая команда:", team2)
print("Победители тура:", winners)
