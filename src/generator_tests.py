import random
from typing import List


def rand_int_array(n: int, lo: int, hi: int, distinct: bool = False) -> List[int]:
    """n случайных целых в диапазоне [lo, hi]. При distinct=True числа не повторяются."""
    if n <= 0:
        return []
    if lo > hi:
        raise ValueError('Нижняя граница больше верхней')

    if distinct:
        if hi - lo + 1 < n:
            raise ValueError(f'Нельзя выбрать {n} уникальных значений из диапазона [{lo}, {hi}]')
        return random.sample(range(lo, hi + 1), n)
    return [random.randint(lo, hi) for _ in range(n)]


def nearly_sorted(n: int, swaps: int) -> List[int]:
    """Почти отсортированный массив: берём range(n) и делаем несколько случайных обменов."""
    if n <= 0:
        return []
    if swaps < 0:
        raise ValueError('Количество обменов не может быть отрицательным')

    arr = list(range(n))
    if n == 1 or swaps == 0:
        return arr

    max_swaps = min(swaps, n * (n - 1) // 2)
    for _ in range(max_swaps):
        i, j = random.sample(range(n), 2)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


def many_duplicates(n: int, k_unique: int = 5) -> List[int]:
    """Массив длины n с максимум k_unique разными значениями (равномерный выбор)."""
    if n <= 0:
        return []
    if k_unique <= 0:
        raise ValueError('k_unique должно быть положительным')

    values = list(range(k_unique))
    return [random.choice(values) for _ in range(n)]


def reverse_sorted(n: int) -> List[int]:
    """Массив от n-1 до 0."""
    return list(range(n - 1, -1, -1)) if n > 0 else []


def rand_float_array(n: int, lo: float = 0.0, hi: float = 1.0) -> List[float]:
    """n случайных чисел с плавающей точкой в диапазоне [lo, hi]."""
    if n <= 0:
        return []
    if lo > hi:
        raise ValueError('Нижняя граница больше верхней')
    return [random.uniform(lo, hi) for _ in range(n)]
