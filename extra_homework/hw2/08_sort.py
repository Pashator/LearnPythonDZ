# ЮНУСОВ ПАВЕЛ ИИАД 1

n = int(input("Введите количество элементов: "))

arr = []
for i in range(n):
    num = int(input(f"Введите {i+1}-й элемент: "))
    arr.append(num)

print("Изначальный список:", arr)
# Сортировка вставками
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

print("Отсортированный список:", arr)
