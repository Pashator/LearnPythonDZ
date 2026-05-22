#ЮНУСОВ ПАВЕЛ ИИАД 1

text = input("Введите текст: ")
vowels = "ауоыиэяюёе"

vowel_list = []
for char in text:
    if char.lower() in vowels:
        vowel_list.append(char)

print("Список гласных букв:", vowel_list)
print("Длина списка:", len(vowel_list))
