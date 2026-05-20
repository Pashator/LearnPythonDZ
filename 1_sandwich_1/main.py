# ЮНУСОВ ПАВЕЛ ИИАД 1

def bread(func):
    def wrapper():
        print("Хлеб верх")
        func()
        print("Хлеб низ")
    return wrapper

def salat(func):
    def wrapper():
        print("Салат")
        func()
    return wrapper

def tomato(func):
    def wrapper():
        print("Помидор")
        func()
    return wrapper

def meat(func):
    def wrapper():
        print("Котлета")
        func()
    return wrapper

@bread
@salat
@tomato
@meat

def make_sandwich():
    pass

def main():
    make_sandwich()

if __name__ == '__main__':
    main()
