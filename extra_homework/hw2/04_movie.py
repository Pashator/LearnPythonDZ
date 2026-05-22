# ЮНУСОВ ПАВЕЛ ИИАД 1

films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

count = int(input("Сколько фильмов хотите добавить? "))
favorites = []

for i in range(count):
    movie = input("Введите название фильма: ")
    if movie in films:
        favorites.append(movie)
    else:
        print(f"Ошибка: фильма {movie} у нас нет :(")

print("Ваш список любимых фильмов:", ", ".join(favorites))
