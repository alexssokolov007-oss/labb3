import pytest
from src.stack import LinkedListStack, ListStack, QueueStack


class TestLinkedListStack:
    def setup_method(self):
        self.stack = LinkedListStack()

    def test_push_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        assert self.stack.pop() == 2
        assert self.stack.pop() == 1

    def test_peek(self):
        self.stack.push(1)
        self.stack.push(2)
        assert self.stack.peek() == 2
        assert self.stack.peek() == 2

    def test_is_empty(self):
        assert self.stack.is_empty() == True
        self.stack.push(1)
        assert self.stack.is_empty() == False
        self.stack.pop()
        assert self.stack.is_empty() == True

    def test_len(self):
        assert len(self.stack) == 0
        self.stack.push(1)
        assert len(self.stack) == 1
        self.stack.push(2)
        assert len(self.stack) == 2
        self.stack.pop()
        assert len(self.stack) == 1

    def test_min(self):
        self.stack.push(3)
        assert self.stack.min() == 3
        self.stack.push(2)
        assert self.stack.min() == 2
        self.stack.push(4)
        assert self.stack.min() == 2
        self.stack.push(1)
        assert self.stack.min() == 1
        self.stack.pop()
        assert self.stack.min() == 2

    def test_pop_empty(self):
        with pytest.raises(IndexError):
            self.stack.pop()

    def test_peek_empty(self):
        with pytest.raises(IndexError):
            self.stack.peek()

    def test_min_empty(self):
        with pytest.raises(IndexError):
            self.stack.min()


class TestListStack:
    def setup_method(self):
        self.stack = ListStack()

    def test_push_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        assert self.stack.pop() == 2
        assert self.stack.pop() == 1

    def test_peek(self):
        self.stack.push(1)
        self.stack.push(2)
        assert self.stack.peek() == 2
        assert self.stack.peek() == 2

    def test_is_empty(self):
        assert self.stack.is_empty() == True
        self.stack.push(1)
        assert self.stack.is_empty() == False
        self.stack.pop()
        assert self.stack.is_empty() == True

    def test_len(self):
        assert len(self.stack) == 0
        self.stack.push(1)
        assert len(self.stack) == 1
        self.stack.push(2)
        assert len(self.stack) == 2

    def test_min(self):
        self.stack.push(3)
        assert self.stack.min() == 3
        self.stack.push(2)
        assert self.stack.min() == 2
        self.stack.push(4)
        assert self.stack.min() == 2
        self.stack.push(1)
        assert self.stack.min() == 1

    def test_pop_empty(self):
        with pytest.raises(IndexError):
            self.stack.pop()

    def test_peek_empty(self):
        with pytest.raises(IndexError):
            self.stack.peek()

    def test_min_empty(self):
        with pytest.raises(IndexError):
            self.stack.min()


class TestQueueStack:
    def setup_method(self):
        self.stack = QueueStack()

    def test_push_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        assert self.stack.pop() == 2
        assert self.stack.pop() == 1

    def test_peek(self):
        self.stack.push(1)
        self.stack.push(2)
        assert self.stack.peek() == 2
        assert self.stack.peek() == 2

    def test_is_empty(self):
        assert self.stack.is_empty() == True
        self.stack.push(1)
        assert self.stack.is_empty() == False
        self.stack.pop()
        assert self.stack.is_empty() == True

    def test_len(self):
        assert len(self.stack) == 0
        self.stack.push(1)
        assert len(self.stack) == 1
        self.stack.push(2)
        assert len(self.stack) == 2

    def test_min(self):
        self.stack.push(3)
        assert self.stack.min() == 3
        self.stack.push(2)
        assert self.stack.min() == 2
        self.stack.push(4)
        assert self.stack.min() == 2
        self.stack.push(1)
        assert self.stack.min() == 1

    def test_pop_empty(self):
        with pytest.raises(IndexError):
            self.stack.pop()

    def test_peek_empty(self):
        with pytest.raises(IndexError):
            self.stack.peek()

    def test_min_empty(self):
        with pytest.raises(IndexError):
            self.stack.min()


def test_all_implementations_consistency():
    '''Тестируем что все реализации стека работают одинаково'''
    implementations = [LinkedListStack(), ListStack(), QueueStack()]
    
    for stack in implementations:
        assert stack.is_empty() == True
        assert len(stack) == 0
        
        stack.push(10)
        stack.push(20)
        stack.push(5)
        
        assert stack.is_empty() == False
        assert len(stack) == 3
        assert stack.peek() == 5
        assert stack.min() == 5
        
        assert stack.pop() == 5
        assert stack.pop() == 20
        assert stack.pop() == 10
        
        assert stack.is_empty() == True
        assert len(stack) == 0
