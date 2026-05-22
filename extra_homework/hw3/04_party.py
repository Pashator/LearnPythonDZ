# ЮНУСОВ ПАВЕЛ ИИАД 1

guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
MAX_GUESTS = 6

while True:
    print(f"\nСейчас на вечеринке {len(guests)} человек: {guests}")
    action = input("Гость пришёл или ушёл? ")

    if action == "Пора спать":
        print("\nВечеринка закончилась, все легли спать.")
        break

    name = input("Имя гостя: ")

    if action == "пришёл":
        if len(guests) < MAX_GUESTS:
            guests.append(name)
            print(f"Привет, {name}!")
        else:
            print(f"Прости, {name}, но мест нет.")
    elif action == "ушёл":
        if name in guests:
            guests.remove(name)
            print(f"Пока, {name}!")
        else:
            print(f"{name} не на вечеринке.")
    else:
        print("Неизвестное действие. Введите 'пришёл' или 'ушёл'.")
