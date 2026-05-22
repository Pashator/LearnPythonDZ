# ЮНУСОВ ПАВЕЛ ИИАД 1

LOWER = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
UPPER = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

message = input("Введите сообщение: ")
shift = int(input("Введите сдвиг: "))

encrypted = ""

for char in message:
    if char in LOWER:
        idx = LOWER.index(char)
        new_idx = (idx + shift) % len(LOWER)
        encrypted += LOWER[new_idx]
    elif char in UPPER:
        idx = UPPER.index(char)
        new_idx = (idx + shift) % len(UPPER)
        encrypted += UPPER[new_idx]
    else:
        encrypted += char

print("Зашифрованное сообщение:", encrypted)
