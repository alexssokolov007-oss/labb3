from src.constants import *


def _ensure_integer_array(arr, algo_name):
    '''Проверяет, что массив состоит только из целых чисел.'''
    if any(not isinstance(x, int) for x in arr):
        raise TypeError(f'{algo_name} работает только с целыми числами')


def bubble_sort(arr):
    '''Сортировка пузырьком.'''
    if not arr:
        return []
    
    _ensure_integer_array(arr, 'Сортировка пузырьком')
    
    a = arr.copy()
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


def quick_sort(arr):
    '''Быстрая сортировка.'''
    _ensure_integer_array(arr, 'Быстрая сортировка')
    
    if len(arr) <= 1:
        return arr.copy()
    
    def _quick_sort(a, left, right):
        if left < right:
            pivot_index = partition(a, left, right)
            _quick_sort(a, left, pivot_index - 1)
            _quick_sort(a, pivot_index + 1, right)
    
    def partition(a, left, right):
        pivot = a[right]
        i = left - 1
        
        for j in range(left, right):
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
        
        a[i + 1], a[right] = a[right], a[i + 1]
        return i + 1
    
    a = arr.copy()
    _quick_sort(a, 0, len(a) - 1)
    return a


def counting_sort(arr, *, exp=None, base=None):
    '''
    Сортировка подсчетом.
    При передаче exp и base работает как вспомогательная для поразрядной сортировки.
    '''
    if not arr:
        return []
    
    _ensure_integer_array(arr, 'Сортировка подсчетом')

    if exp is None:
        if min(arr) < 0:
            raise ValueError('Counting sort работает только с неотрицательными числами')
        
        max_val = max(arr)
        
        if max_val > COUNTING_SORT_MAX_VALUE:
            raise ValueError('Слишком большие числа для сортировки подсчетом')
        
        if max_val > len(arr) * COUNTING_SORT_MAX_RANGE_RATIO:
            raise ValueError('Слишком большой разброс значений для сортировки подсчетом')
        
        count = [0] * (max_val + 1)
        
        for num in arr:
            count[num] += 1
        
        for i in range(1, len(count)):
            count[i] += count[i - 1]
        
        result = [0] * len(arr)
        
        for num in reversed(arr):
            count[num] -= 1
            result[count[num]] = num
        
        return result
    
    if min(arr) < 0:
        raise ValueError('Counting sort работает только с неотрицательными числами')
    
    if not isinstance(exp, int) or exp <= 0:
        raise ValueError('exp должен быть положительным целым числом')
    
    if not isinstance(base, int):
        raise TypeError('Основание системы счисления должно быть целым числом')
    
    if base < 2:
        raise ValueError('Основание системы счисления должно быть не меньше 2')
    
    n = len(arr)
    output = [0] * n
    count = [0] * base
    
    for i in range(n):
        index = (arr[i] // exp) % base
        count[index] += 1
    
    for i in range(1, base):
        count[i] += count[i - 1]
    
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % base
        count[index] -= 1
        output[count[index]] = arr[i]
    
    return output


def radix_sort(arr, base=RADIX_DEFAULT_BASE):
    '''Поразрядная сортировка.'''
    if not arr:
        return []
    
    _ensure_integer_array(arr, 'Поразрядная сортировка')
    
    if min(arr) < 0:
        raise ValueError('Radix sort работает только с неотрицательными числами')
    
    if not isinstance(base, int):
        raise TypeError('Основание системы счисления должно быть целым числом')
    
    if base < 2:
        raise ValueError('Основание системы счисления должно быть не меньше 2')
    
    a = arr.copy()
    max_val = max(a)
    
    exp = 1
    while max_val // exp > 0:
        a = counting_sort(a, exp=exp, base=base)
        exp *= base
    
    return a


def bucket_sort(arr, buckets=None):
    '''Ведерная (корзинная) сортировка.'''
    if not arr:
        return []
    
    min_val = min(arr)
    max_val = max(arr)
    
    if min_val == max_val:
        return arr.copy()
    
    a = arr.copy()
    n = len(a)
    
    if buckets is None:
        buckets = n
    
    bucket_list = [[] for _ in range(buckets)]
    
    def insertion_sort(lst):
        for i in range(1, len(lst)):
            key = lst[i]
            j = i - 1
            while j >= 0 and lst[j] > key:
                lst[j + 1] = lst[j]
                j -= 1
            lst[j + 1] = key

    range_val = max_val - min_val
    for num in a:
        normalized = (num - min_val) / range_val
        index = int(normalized * buckets)
        if index == buckets:
            index = buckets - 1
        bucket_list[index].append(num)
    
    for bucket in bucket_list:
        insertion_sort(bucket)
    
    result = []
    for bucket in bucket_list:
        result.extend(bucket)
    
    return result


def heap_sort(arr):
    '''Пирамидальная сортировка.'''
    if not arr:
        return []
    
    _ensure_integer_array(arr, 'Пирамидальная сортировка')
    
    a = arr.copy()
    n = len(a)
    
    def heapify(a, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and a[left] > a[largest]:
            largest = left
        
        if right < n and a[right] > a[largest]:
            largest = right
        
        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            heapify(a, n, largest)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)
    
    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapify(a, i, 0)
    
    return a
