class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Попытка извлечь элемент из пустого стека")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Попытка просмотреть элемент в пустом стеке")

    def size(self):
        return len(self.items)

# Пример использования стека
stack = Stack()

# Добавляем три элемента
stack.push(1)
stack.push(2)
stack.push(3)

# Удаляем один элемент
removed_element = stack.pop()
print(f"Удалённый элемент: {removed_element}")

# Просматриваем верхний элемент
top_element = stack.peek()
print(f"Верхний элемент: {top_element}")