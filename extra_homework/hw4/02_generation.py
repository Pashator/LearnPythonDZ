# ЮНУСОВ ПАВЕЛ ИИАД 1

N = int(input("Введите длину списка: "))

result = []
for i in range(N):
    if i % 2 == 0:
        result.append(1)
    else:
        result.append(i % 5)

print("Результат:", result)
