# ЮНУСОВ ПАВЕЛ ИИАД 1

import pickle # нужен, чтобы превращать почти любые объекты Python в поток байтов и обратно
import os

def cache(file_name='cache.txt', key_type='positional'): # фабрика декораторов
    def decorator(func):
        cache_dict = {}
        if os.path.exists(file_name):
            with open(file_name, 'rb') as f:
                old_cache = pickle.load(f)
                cache_dict.update(old_cache)

        def wrapper(*args, **kwargs):
            if key_type == 'positional':
                key = args
            elif key_type == 'named':
                key = tuple(kwargs.items())
            else:
                key = (args, tuple(kwargs.items()))

            if key in cache_dict:
                return cache_dict[key]

            result = func(*args, **kwargs)
            cache_dict[key] = result

            with open(file_name, 'wb') as f:
                pickle.dump(cache_dict, f)

            return result

        return wrapper

    return decorator

@cache('my_cache.txt', 'positional')
def my_sum(a, b):
    print("Вычисляю...")
    return a + b

print(my_sum(10, 3))
print(my_sum(2, 3))
print(my_sum(4, 5))
print(my_sum(11, 6))
