from typing import Iterable, List

from src.constants import (
    BUCKET_SORT_MAX_VALUE,
    BUCKET_SORT_MIN_VALUE,
    COUNTING_SORT_MAX_RANGE_RATIO,
    COUNTING_SORT_MAX_VALUE,
    RADIX_DEFAULT_BASE,
)


def _copy(arr: Iterable[int]) -> List[int]:
    return list(arr)


def bubble_sort(arr: Iterable[int]) -> List[int]:
    """Простая пузырьковая сортировка. Возвращает новый отсортированный список."""
    a = _copy(arr)
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


def quick_sort(arr: Iterable[int]) -> List[int]:
    """Быстрая сортировка Hoare (in-place на копии, возвращает новый список)."""
    a = _copy(arr)
    if len(a) <= 1:
        return a

    def _quick_sort(left: int, right: int) -> None:
        if left >= right:
            return
        pivot = a[right]
        i = left - 1
        for j in range(left, right):
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
        pivot_index = i + 1
        a[pivot_index], a[right] = a[right], a[pivot_index]
        _quick_sort(left, pivot_index - 1)
        _quick_sort(pivot_index + 1, right)

    _quick_sort(0, len(a) - 1)
    return a


def counting_sort(arr: Iterable[int]) -> List[int]:
    """Сортировка подсчётом для неотрицательных целых."""
    a = _copy(arr)
    if not a:
        return []
    if min(a) < 0:
        raise ValueError('Counting sort работает только с неотрицательными числами')

    max_val = max(a)
    if max_val > COUNTING_SORT_MAX_VALUE:
        raise ValueError('Слишком большой диапазон для counting sort')
    if max_val > len(a) * COUNTING_SORT_MAX_RANGE_RATIO:
        raise ValueError('Диапазон значений слишком широк для counting sort')

    count = [0] * (max_val + 1)
    for num in a:
        count[num] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    result = [0] * len(a)
    for num in reversed(a):
        count[num] -= 1
        result[count[num]] = num
    return result


def radix_sort(arr: Iterable[int], base: int = RADIX_DEFAULT_BASE) -> List[int]:
    """Сортировка по разрядам (LSD) для неотрицательных целых."""
    a = _copy(arr)
    if not a:
        return []
    if min(a) < 0:
        raise ValueError('Radix sort работает только с неотрицательными числами')
    if base <= 1:
        raise ValueError('Основание должно быть больше 1')

    max_val = max(a)
    exp = 1
    while max_val // exp > 0:
        a = _counting_sort_for_radix(a, exp, base)
        exp *= base
    return a


def _counting_sort_for_radix(arr: List[int], exp: int, base: int) -> List[int]:
    n = len(arr)
    output = [0] * n
    count = [0] * base

    for num in arr:
        index = (num // exp) % base
        count[index] += 1

    for i in range(1, base):
        count[i] += count[i - 1]

    for num in reversed(arr):
        index = (num // exp) % base
        count[index] -= 1
        output[count[index]] = num

    return output


def bucket_sort(arr: Iterable[float], buckets: int | None = None) -> List[float]:
    """Сортировка по корзинам для чисел из диапазона [0, 1]."""
    a = list(arr)
    if not a:
        return []

    min_val, max_val = min(a), max(a)
    if min_val < BUCKET_SORT_MIN_VALUE or max_val > BUCKET_SORT_MAX_VALUE:
        raise ValueError('Bucket sort ожидает элементы в диапазоне [0, 1]')
    if min_val == max_val:
        return a

    buckets = buckets or len(a)
    bucket_list: list[list[float]] = [[] for _ in range(buckets)]
    for num in a:
        index = int(num * buckets)
        index = buckets - 1 if index == buckets else index
        bucket_list[index].append(num)

    result: list[float] = []
    for bucket in bucket_list:
        bucket.sort()
        result.extend(bucket)
    return result


def heap_sort(arr: Iterable[int]) -> List[int]:
    """Классический heapsort."""
    a = _copy(arr)
    n = len(a)

    def heapify(i: int, heap_size: int) -> None:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < heap_size and a[left] > a[largest]:
            largest = left
        if right < heap_size and a[right] > a[largest]:
            largest = right
        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            heapify(largest, heap_size)

    for i in range(n // 2 - 1, -1, -1):
        heapify(i, n)

    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        heapify(0, end)

    return a
