class Node:
    """Узел для связного стека."""

    def __init__(self, value: int, next_node=None):
        self.value = value
        self.next = next_node


class LinkedListStack:
    """Стек на односвязном списке с поддержкой O(1) минимума."""

    def __init__(self):
        self.top = None
        self._size = 0
        self._mins = []

    def push(self, x: int) -> None:
        self.top = Node(x, self.top)
        self._size += 1
        if not self._mins or x <= self._mins[-1]:
            self._mins.append(x)

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError('Pop from empty stack')
        value = self.top.value
        self.top = self.top.next
        self._size -= 1
        if value == self._mins[-1]:
            self._mins.pop()
        return value

    def is_empty(self) -> bool:
        return self.top is None

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError('Peek from empty stack')
        return self.top.value

    def __len__(self) -> int:
        return self._size

    def min(self) -> int:
        if self.is_empty():
            raise IndexError('Min from empty stack')
        return self._mins[-1]


class ListStack:
    """Стек на list, тоже хранит минимум в отдельном стеке."""

    def __init__(self):
        self._data: list[int] = []
        self._mins: list[int] = []

    def push(self, x: int) -> None:
        self._data.append(x)
        if not self._mins or x <= self._mins[-1]:
            self._mins.append(x)

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError('Pop from empty stack')
        value = self._data.pop()
        if value == self._mins[-1]:
            self._mins.pop()
        return value

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError('Peek from empty stack')
        return self._data[-1]

    def __len__(self) -> int:
        return len(self._data)

    def min(self) -> int:
        if self.is_empty():
            raise IndexError('Min from empty stack')
        return self._mins[-1]


class QueueStack:
    """Стек, реализованный через две очереди (списки)."""

    def __init__(self):
        self._main: list[int] = []
        self._tmp: list[int] = []
        self._min_value: int | None = None

    def push(self, x: int) -> None:
        self._main.append(x)
        if self._min_value is None or x < self._min_value:
            self._min_value = x

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError('Pop from empty stack')
        while len(self._main) > 1:
            self._tmp.append(self._main.pop(0))
        value = self._main.pop(0)
        self._main, self._tmp = self._tmp, []
        if value == self._min_value and self._main:
            self._min_value = min(self._main)
        elif not self._main:
            self._min_value = None
        return value

    def is_empty(self) -> bool:
        return len(self._main) == 0

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError('Peek from empty stack')
        while len(self._main) > 1:
            self._tmp.append(self._main.pop(0))
        value = self._main[0]
        self._tmp.append(self._main.pop(0))
        self._main, self._tmp = self._tmp, []
        return value

    def __len__(self) -> int:
        return len(self._main)

    def min(self) -> int:
        if self.is_empty():
            raise IndexError('Min from empty stack')
        return self._min_value  # type: ignore[return-value]
