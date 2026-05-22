# ЮНУСОВ ПАВЕЛ ИИАД 1

n = int(input("Количество контейнеров: "))
weights = []

for x in range(n):
    while True:
        w = int(input("Введите вес контейнера: "))
        if w <= 200:
            weights.append(w)
            break
        else:
            print("Ошибка: вес должен быть не более 200. Попробуйте ещё раз.")

while True:
    new_weight = int(input("Введите вес нового контейнера: "))
    if new_weight <= 200:
        break
    else:
        print("Ошибка: вес должен быть не более 200. Попробуйте ещё раз.")

position = 1  
for w in weights:
    if w < new_weight:
        break
    position += 1

print("Номер, который получит новый контейнер:", position)
