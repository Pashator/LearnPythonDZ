# ЮНУСОВ ПАВЕЛ ИИАД 1

n = int(input("Количество видеокарт: "))
cards = []
for i in range(1, n + 1):
    card = int(input(f"{i} Видеокарта: "))
    cards.append(card)

print("Старый список видеокарт:", cards)

max_value = max(cards)

new_cards = []
for card in cards:
    if card != max_value:
        new_cards.append(card)

print("Новый список видеокарт:", new_cards)
