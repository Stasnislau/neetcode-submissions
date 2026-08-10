class MyQueue:

    def __init__(self):
        self.s1 = [] # Стек для входа
        self.s2 = [] # Стек для выхода

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        self.peek() # Хак: peek сам перекинет элементы, если нужно!
        return self.s2.pop()

    def peek(self) -> int:
        # Если стек на выход пуст, переливаем в него всё из s1
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        # Очередь пуста, только если ОБА стека пустые
        return not self.s1 and not self.s2