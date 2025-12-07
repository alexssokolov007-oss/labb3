import functools

from src.constants import (
    FACTORIAL_MAX_ITERATIVE,
    FACTORIAL_MAX_RECURSIVE,
    FIBO_MAX_ITERATIVE,
    FIBO_MAX_RECURSIVE,
)


def _ensure_int(n):
    if not isinstance(n, int):
        raise TypeError('Ожидалось целое число')
    return n


class Sequences:
    """Факториал и числа Фибоначчи в двух вариантах — итеративно и рекурсивно."""

    def __init__(self):
        self.factorial_recursive.cache_clear()
        self.fibo_recursive.cache_clear()

    def factorial(self, n: int) -> int:
        _ensure_int(n)
        if n < 0:
            raise ValueError('Факториал определён только для неотрицательных чисел')
        if n > FACTORIAL_MAX_ITERATIVE:
            raise ValueError('Слишком большое n для итеративного подсчёта факториала')

        result = 1
        for i in range(1, n + 1):
            result *= i
            if result < 0:
                raise OverflowError('Переполнение при вычислении факториала')
        return result

    @functools.lru_cache(maxsize=1000)
    def factorial_recursive(self, n: int) -> int:
        _ensure_int(n)
        if n < 0:
            raise ValueError('Факториал определён только для неотрицательных чисел')
        if n > FACTORIAL_MAX_RECURSIVE:
            raise RecursionError('Слишком глубокая рекурсия для факториала')
        if n in (0, 1):
            return 1

        result = n * self.factorial_recursive(n - 1)
        if result < 0:
            raise OverflowError('Переполнение при вычислении факториала')
        return result

    def fibo(self, n: int) -> int:
        _ensure_int(n)
        if n < 0:
            raise ValueError('Фибоначчи определён только для неотрицательных индексов')
        if n > FIBO_MAX_ITERATIVE:
            raise ValueError('Слишком большое n для итеративного подсчёта Фибоначчи')
        if n == 0:
            return 0
        if n == 1:
            return 1

        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
            if b < 0:
                raise OverflowError('Переполнение при вычислении Фибоначчи')
        return b

    @functools.lru_cache(maxsize=1000)
    def fibo_recursive(self, n: int) -> int:
        _ensure_int(n)
        if n < 0:
            raise ValueError('Фибоначчи определён только для неотрицательных индексов')
        if n > FIBO_MAX_RECURSIVE:
            raise RecursionError('Слишком глубокая рекурсия для Фибоначчи')
        if n in (0, 1):
            return n

        result = self.fibo_recursive(n - 1) + self.fibo_recursive(n - 2)
        if result < 0:
            raise OverflowError('Переполнение при вычислении Фибоначчи')
        return result
