# ЮНУСОВ ПАВЕЛ ИИАД 1

n = int(input("Введите количество элементов: "))
original = []
for i in range(n):
    num = int(input(f"Введите {i+1}-й элемент: "))
    original.append(num)

k = int(input("Сдвиг: "))

if original:
    k %= len(original)
    shifted = original[-k:] + original[:-k] if k != 0 else original[:]
else:
    shifted = []

print("Сдвиг:", k)
print("Изначальный список:", original)
print("Сдвинутый список:", shifted)
