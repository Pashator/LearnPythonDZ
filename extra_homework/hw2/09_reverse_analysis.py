# ЮНУСОВ ПАВЕЛ ИИАД 1

n = int(input("Количество элементов: "))
numbers = []

for i in range(n):
    num = int(input(f"Элемент {i+1}: "))
    numbers.append(num)

print("Изначальный список:", numbers)

print("Чётные числа в обратном порядке:")
for i in range(len(numbers)-1, -1, -1):
    if numbers[i] % 2 == 0:
        print(numbers[i], end=' ')
