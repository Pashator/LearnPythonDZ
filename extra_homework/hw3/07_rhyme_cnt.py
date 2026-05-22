# ЮНУСОВ ПАВЕЛ ИИАД 1

N = int(input("Кол-во человек: "))
K = int(input("Какое число в считалке? "))
print(f"Значит, выбывает каждый {K}-й человек\n")

people = list(range(1, N + 1))
start = 0

print("Текущий круг людей:", people)
print("Начало счёта с номера", people[start])

while len(people) > 1:
    remove_idx = (start + K - 1) % len(people)
    removed = people.pop(remove_idx)
    print("Выбывает человек под номером", removed)

    start = remove_idx

    if len(people) > 1:
        current_start = start % len(people)
        print("\nТекущий круг людей:", people)
        print("Начало счёта с номера", people[current_start])

print("\nОстался человек под номером", people[0])
