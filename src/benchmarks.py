import time
from typing import Callable, Dict, Iterable

from src.output import COLORAMA_AVAILABLE, Fore, format_output


def _color(color):
    return color if COLORAMA_AVAILABLE else None


def timeit_once(func: Callable, *args, **kwargs) -> float:
    """Измерить время единственного вызова функции."""
    start_time = time.perf_counter()
    func(*args, **kwargs)
    end_time = time.perf_counter()
    return end_time - start_time


def benchmark_sorts(arrays: Dict[str, Iterable], algos: Dict[str, Callable]) -> Dict[str, Dict[str, float | None]]:
    """Запустить каждый алгоритм на каждом массиве, вернуть времена в секундах."""
    results: Dict[str, Dict[str, float | None]] = {}
    for algo_name, algo_func in algos.items():
        results[algo_name] = {}
        print(format_output(f'Тестируем {algo_name}...'))
        for array_name, array in arrays.items():
            test_array = list(array)
            try:
                time_taken = timeit_once(algo_func, test_array)
                results[algo_name][array_name] = time_taken
                color = Fore.GREEN if time_taken < 0.001 else Fore.YELLOW if time_taken < 0.01 else Fore.RED
                print(format_output(f'  {array_name}: {time_taken:.6f} с', _color(color)))
            except RecursionError:
                print(format_output(f'  {array_name}: ошибка рекурсии', _color(Fore.RED)))
                results[algo_name][array_name] = None
            except MemoryError:
                print(format_output(f'  {array_name}: недостаточно памяти', _color(Fore.RED)))
                results[algo_name][array_name] = None
            except ValueError as e:
                print(format_output(f'  {array_name}: предупреждение — {e}', _color(Fore.YELLOW)))
                results[algo_name][array_name] = None
            except Exception as e:
                print(format_output(f'  {array_name}: ошибка — {e}', _color(Fore.RED)))
                results[algo_name][array_name] = None
    return results


def print_benchmark_results(results: Dict[str, Dict[str, float | None]]) -> None:
    """Печатает таблицу результатов бенчмарков."""
    print(format_output('\n' + '=' * 80))
    print(format_output('Результаты бенчмарков'))
    print(format_output('=' * 80))

    array_names = sorted({name for algo_results in results.values() for name in algo_results.keys()})
    header = 'Алгоритм'.ljust(16) + ''.join(f' {name[:10]:>10}' for name in array_names)
    print(header)
    print('-' * len(header))

    for algo_name, algo_results in results.items():
        row = algo_name.ljust(16)
        for array_name in array_names:
            time_val = algo_results.get(array_name)
            if time_val is None:
                row += format_output(f' {"N/A":>10}', _color(Fore.RED))
            else:
                color = Fore.GREEN if time_val < 0.001 else Fore.YELLOW if time_val < 0.01 else Fore.RED
                row += format_output(f' {time_val:>10.6f}', _color(color))
        print(row)


def run_comprehensive_benchmark():
    """Интеграционный бенчмарк на наборах целых и вещественных чисел."""
    from src.generator_tests import many_duplicates, nearly_sorted, rand_float_array, rand_int_array, reverse_sorted
    from src.sorting import bucket_sort, bubble_sort, counting_sort, heap_sort, quick_sort, radix_sort

    int_arrays = {
        'Случайные 100': rand_int_array(100, 1, 1000),
        'Случайные 1000': rand_int_array(1000, 1, 10000),
        'Почти отсортированные 100': nearly_sorted(100, 10),
        'Почти отсортированные 1000': nearly_sorted(1000, 50),
        'Много повторов 1000': many_duplicates(1000, 10),
        'Обратный порядок 100': reverse_sorted(100),
        'Обратный порядок 1000': reverse_sorted(1000),
    }

    float_arrays = {
        'Float 100': rand_float_array(100, 0.0, 1.0),
        'Float 1000': rand_float_array(1000, 0.0, 1.0),
        'Float почти отсорт. 100': [x / 100 for x in nearly_sorted(100, 10)],
        'Float почти отсорт. 1000': [x / 1000 for x in nearly_sorted(1000, 50)],
    }

    algos = {
        'Пузырьковая': bubble_sort,
        'Быстрая': quick_sort,
        'Подсчетом': counting_sort,
        'По разрядам': radix_sort,
        'Кучей': heap_sort,
        'По корзинам': bucket_sort,
    }

    all_arrays = {**int_arrays, **float_arrays}
    print(format_output('Стартуем бенчмарк'))
    print(format_output('=' * 50))
    results = benchmark_sorts(all_arrays, algos)
    print_benchmark_results(results)
    return results
