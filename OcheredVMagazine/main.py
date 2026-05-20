# ЮНУСОВ ПАВЕЛ ИИАД 1 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StoreQueue:
    def __init__(self):
        self.first = None
        self.last = None

    def join(self, name):
        #Добавить покупателя в конец очереди
        person = Node(name)
        if not self.last:
            self.first = self.last = person
            print(f"{name} — первый в очереди!")
        else:
            self.last.next = person
            self.last = person
            print(f"{name} занял место за {self._prev_name(person)}.")

    def serve(self):
        #Обслужить первого в очереди
        if not self.first:
            print("Очередь пуста — некому обслуживать.")
            return None

        customer = self.first.data
        self.first = self.first.next

        if not self.first:
            self.last = None
            print(f"Обслужен последний покупатель: {customer}.")
        else:
            print(f"Обслужен: {customer}. Следующий: {self.first.data}")
        return customer

    def next_in_line(self):
        return self.first.data if self.first else "Никого нет"

    def _prev_name(self, new_node):
        current = self.first
        while current and current.next != new_node:
            current = current.next
        return current.data if current else "?"


class Deque:
    #Двусторонняя очередь (можно добавлять/удалять с обоих концов)
    def __init__(self):
        self.head = None
        self.tail = None

    def push_first(self, value):
        #Добавить элемент в начало
        node = Node(value)
        node.next = self.head
        self.head = node
        if not self.tail:
            self.tail = node
        print(f"[В начало] +{value}")

    def push_last(self, value):
        #Добавить элемент в конец
        node = Node(value)
        if not self.tail:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        print(f"[В конец] +{value}")

    def pop_first(self):
        #Удалить и вернуть первый элемент
        if not self.head:
            print("Пусто — нечего удалять из начала.")
            return None

        item = self.head.data
        self.head = self.head.next

        if not self.head:
            self.tail = None

        print(f"[С начала] -{item}")
        return item

    def pop_last(self):
        #Удалить и вернуть последний элемент
        if not self.tail:
            print("Пусто — нечего удалять из конца.")
            return None

        # Если всего один элемент
        if self.head == self.tail:
            item = self.tail.data
            self.head = self.tail = None
            print(f"[С конца] -{item}")
            return item

        # Найти предпоследний элемент
        current = self.head
        while current.next != self.tail:
            current = current.next

        item = self.tail.data
        self.tail = current
        self.tail.next = None
        print(f"[С конца] -{item}")
        return item

    def peek_both(self):
        first = self.head.data if self.head else "—"
        last = self.tail.data if self.tail else "—"
        return f"Начало: {first} | Конец: {last}"


# Пример использования
if __name__ == "__main__":
    print("Очередь в магазине")
    q = StoreQueue()
    q.join("Анна")
    q.join("Борис")
    q.join("Виктор")
    print(f"Следующий: {q.next_in_line()}")
    q.serve()
    q.serve()
    q.serve()
    q.serve()  # Очередь пуста

    print("\nДвусторонняя очередь")
    dq = Deque()
    dq.push_first("A")
    dq.push_last("B")
    dq.push_first("X")
    print(dq.peek_both())
    dq.pop_first()
    dq.pop_last()
    print(dq.peek_both())
