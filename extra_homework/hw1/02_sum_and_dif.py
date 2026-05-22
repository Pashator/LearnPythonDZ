# ЮНУСОВ ПАВЕЛ ИИАД 1

def sum_of_digits(number):
    k = 0
    for char in str(number):
        k += int(char)
    return k

def count_of_digits(number):
    return len(str(number))

user_input = input("Введите число: ")

if user_input.isdigit():
    n = int(user_input)
    s = sum_of_digits(n)
    c = count_of_digits(n)
    diff = s - c

    print("Сумма чисел:", s)
    print("Количество цифр в числе:", c)
    print("Разность суммы и количества цифр:", diff)
else:
    print("Ошибка: нужно ввести целое положительное число.")
