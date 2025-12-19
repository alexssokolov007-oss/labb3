class Node:
    '''Узел связного списка.'''
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LinkedListStack:
    '''Реализация стека на связном списке.'''
    
    def __init__(self):
        self.top = None
        self._size = 0
        self.min_stack = []
    
    def push(self, x):
        new_node = Node(x, self.top)
        self.top = new_node
        self._size += 1

        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
    
    def pop(self):
        if self.is_empty():
            raise IndexError('Pop from empty stack')
        
        value = self.top.value
        self.top = self.top.next
        self._size -= 1

        if value == self.min_stack[-1]:
            self.min_stack.pop()
        
        return value
    
    def is_empty(self):
        return self.top is None
    
    def peek(self):
        if self.is_empty():
            raise IndexError('Peek from empty stack')
        return self.top.value
    
    def __len__(self):
        return self._size
    
    def min(self):
        if self.is_empty():
            raise IndexError('Min from empty stack')
        return self.min_stack[-1]


class ListStack:
    '''Реализация стека на встроенном списке.'''
    
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, x):
        self.stack.append(x)

        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
    
    def pop(self):
        if self.is_empty():
            raise IndexError('Pop from empty stack')
        
        value = self.stack.pop()

        if value == self.min_stack[-1]:
            self.min_stack.pop()
        
        return value
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def peek(self):
        if self.is_empty():
            raise IndexError('Peek from empty stack')
        return self.stack[-1]
    
    def __len__(self):
        return len(self.stack)
    
    def min(self):
        if self.is_empty():
            raise IndexError('Min from empty stack')
        return self.min_stack[-1]


class QueueStack:
    '''Реализация стека на двух очередях (списках).'''
    
    def __init__(self):
        self.main_queue = []
        self.temp_queue = []
        self._min_value = None
    
    def push(self, x):
        self.main_queue.append(x)

        if self._min_value is None or x < self._min_value:
            self._min_value = x
    
    def pop(self):
        if self.is_empty():
            raise IndexError('Pop from empty stack')

        while len(self.main_queue) > 1:
            element = self.main_queue.pop(0)
            self.temp_queue.append(element)
        
        value = self.main_queue.pop(0)

        self.main_queue, self.temp_queue = self.temp_queue, self.main_queue

        if value == self._min_value and not self.is_empty():
            self._min_value = min(self.main_queue) if self.main_queue else None
        elif self.is_empty():
            self._min_value = None
        
        return value
    
    def is_empty(self):
        return len(self.main_queue) == 0
    
    def peek(self):
        if self.is_empty():
            raise IndexError('Peek from empty stack')

        while len(self.main_queue) > 1:
            self.temp_queue.append(self.main_queue.pop(0))
        
        value = self.main_queue[0]
        self.temp_queue.append(self.main_queue.pop(0))

        self.main_queue, self.temp_queue = self.temp_queue, self.main_queue
        
        return value
    
    def __len__(self):
        return len(self.main_queue)
    
    def min(self):
        if self.is_empty():
            raise IndexError('Min from empty stack')
        return self._min_value
