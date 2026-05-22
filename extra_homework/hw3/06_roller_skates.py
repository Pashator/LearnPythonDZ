# ЮНУСОВ ПАВЕЛ ИИАД 1

n_skates = int(input("Кол-во коньков: "))
skates = []
for i in range(1, n_skates + 1):
    size = int(input(f"Размер {i}-й пары: "))
    skates.append(size)

n_people = int(input("\nКол-во людей: "))
people = []
for i in range(1, n_people + 1):
    size = int(input(f"Размер ноги {i}-го человека: "))
    people.append(size)

skates.sort()
people.sort()

count = 0
i = 0
j = 0

while i < n_people and j < n_skates:
    if skates[j] < people[i]:
        j += 1
    elif skates[j] == people[i]:
        count += 1
        i += 1
        j += 1
    else:  # skates[j] > people[i]
        i += 1

print(f"\nНаибольшее кол-во людей, которые могут взять ролики: {count}")
