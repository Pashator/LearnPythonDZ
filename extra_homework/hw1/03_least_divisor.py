# ЮНУСОВ ПАВЕЛ ИИАД 1

def smallest_divisor(n):
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            return divisor
        divisor += 1

number = int(input("Введите число: "))
result = smallest_divisor(number)
print("Наименьший делитель, отличный от единицы:", result)
