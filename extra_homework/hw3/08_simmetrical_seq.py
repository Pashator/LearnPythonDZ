# ЮНУСОВ ПАВЕЛ ИИАД 1

N = int(input("Кол-во чисел: "))
nums = []
for i in range(N):
    num = int(input("Число: "))
    nums.append(num)

print("Последовательность:", nums)

k = 0
for i in range(N):
    sub = nums[i:]
    if sub == sub[::-1]:
        break
to_add = nums[:k][::-1]

print("Нужно приписать чисел:", k)
if k > 0:
    print("Сами числа:", to_add)
