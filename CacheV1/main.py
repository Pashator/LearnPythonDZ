# ЮНУСОВ ПАВЕЛ ИИАД 1

def cache(func):
    cache_storage = {}

    def wrapper(*args):
        if args in cache_storage:
            print(f"Возвращаем из кеша для аргументов {args}")
            return cache_storage[args]

        result = func(*args)
        cache_storage[args] = result
        print(f"Вычисляем новое значение для аргументов {args}")
        return result
    return wrapper

@cache
def my_sum(a, b):
    print(f"Выполняем my_sum({a}, {b})")
    return a + b

print(my_sum(2, 3))
print(my_sum(2, 3))
print(my_sum(4, 5))
print(my_sum(2, 3))
