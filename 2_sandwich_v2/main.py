# ЮНУСОВ ПАВЕЛ ИИАД 1

import functools

def bun(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        x = func(*args, **kwargs)
        return 'Хлеб верх\n' + x + 'Хлеб низ\n'
    return wrapper

def sauce(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        x = func(*args, **kwargs)
        return 'Соус\n'+ x + 'Соус\n'
    return wrapper

def salad(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        x = func(*args, **kwargs)
        return  x + 'Салат\n'
    return wrapper

def sausage(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        x = func(*args, **kwargs)
        return x + 'Колбаса\n'
    return wrapper

@bun
@sauce
@salad
@sausage

def makebuter():
    return ''
print(makebuter())
