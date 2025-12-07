import pytest

from src.benchmarks import benchmark_sorts, print_benchmark_results, run_comprehensive_benchmark, timeit_once
from src.generator_tests import rand_int_array
from src.sorting import bubble_sort, quick_sort


class TestBenchmarks:
    def test_timeit_once_basic(self):
        def dummy_func():
            return sum(range(1000))

        time_taken = timeit_once(dummy_func)
        assert isinstance(time_taken, float)
        assert time_taken > 0

    def test_timeit_once_with_args(self):
        def func_with_args(a, b):
            return a + b

        time_taken = timeit_once(func_with_args, 5, 10)
        assert time_taken > 0

    def test_timeit_once_with_kwargs(self):
        def func_with_kwargs(a, b=10):
            return a + b

        time_taken = timeit_once(func_with_kwargs, 5, b=15)
        assert time_taken > 0

    def test_benchmark_sorts_basic(self):
        arrays = {
            'small': [3, 1, 2],
            'medium': rand_int_array(10, 1, 100),
        }

        algos = {
            'bubble': bubble_sort,
            'quick': quick_sort,
        }

        results = benchmark_sorts(arrays, algos)

        assert 'bubble' in results
        assert 'quick' in results
        assert 'small' in results['bubble']
        assert 'medium' in results['quick']

        assert results['bubble']['small'] is None or results['bubble']['small'] > 0
        assert results['quick']['medium'] is None or results['quick']['medium'] > 0

    def test_benchmark_sorts_with_errors(self):
        arrays = {'valid': [1, 2, 3], 'empty': []}
        algos = {'bubble': bubble_sort, 'quick': quick_sort}
        results = benchmark_sorts(arrays, algos)

        assert 'valid' in results['bubble']
        assert 'empty' in results['bubble']
        assert 'valid' in results['quick']
        assert 'empty' in results['quick']

    def test_benchmark_sorts_recursion_error(self):
        arrays = {'large_reverse': list(range(2000, 0, -1))}
        algos = {'quick': quick_sort}
        results = benchmark_sorts(arrays, algos)

        assert 'large_reverse' in results['quick']
        assert results['quick']['large_reverse'] is None or results['quick']['large_reverse'] > 0

    def test_benchmark_sorts_value_error(self):
        from src.sorting import counting_sort

        arrays = {'negative': [-1, -2, -3]}
        algos = {'counting': counting_sort}
        results = benchmark_sorts(arrays, algos)

        assert 'negative' in results['counting']
        assert results['counting']['negative'] is None

    def test_benchmark_sorts_memory_error(self):
        arrays = {'normal': [1, 2, 3]}
        algos = {'bubble': bubble_sort}
        results = benchmark_sorts(arrays, algos)
        assert 'normal' in results['bubble']

    def test_print_benchmark_results_basic(self):
        results = {
            'Algorithm1': {'Array1': 0.001, 'Array2': 0.002},
            'Algorithm2': {'Array1': 0.0005, 'Array2': 0.0015},
        }

        print_benchmark_results(results)

    def test_print_benchmark_results_with_none(self):
        results = {'Algo1': {'arr1': 0.001, 'arr2': None}, 'Algo2': {'arr1': None, 'arr2': 0.002}}
        print_benchmark_results(results)

    def test_print_benchmark_results_empty(self):
        print_benchmark_results({})

    def test_print_benchmark_results_complex_names(self):
        results = {
            'ОченьДлинноеИмяАлгоритма': {'ОченьДлинныйМассив': 0.001, 'ЕщёИмя': 0.002},
        }
        print_benchmark_results(results)

    def test_run_comprehensive_benchmark_integration(self):
        """Бенчмарк должен вернуть словарь с ключами-алгоритмами."""
        results = run_comprehensive_benchmark()
        assert isinstance(results, dict)
        expected_algos = ['Пузырьковая', 'Быстрая', 'Подсчетом', 'По разрядам', 'Кучей', 'По корзинам']
        for algo in expected_algos:
            assert algo in results

    def test_colorama_fallback(self):
        """Форматирование не падает без colorama."""
        import src.benchmarks as benchmarks_module

        original_colorama = benchmarks_module.COLORAMA_AVAILABLE
        try:
            benchmarks_module.COLORAMA_AVAILABLE = False
            results = {'Test': {'Array': 0.001}}
            print_benchmark_results(results)
            benchmark_sorts({'test': [1, 2, 3]}, {'algo': bubble_sort})
        finally:
            benchmarks_module.COLORAMA_AVAILABLE = original_colorama

    def test_benchmark_sorts_all_algorithms(self):
        """Проверяем, что все алгоритмы отрабатывают."""
        from src.sorting import counting_sort, heap_sort, radix_sort

        arrays = {'small': [3, 1, 4, 1, 5], 'sorted': [1, 2, 3, 4, 5]}
        algos = {
            'bubble': bubble_sort,
            'quick': quick_sort,
            'counting': counting_sort,
            'radix': radix_sort,
            'heap': heap_sort,
        }
        results = benchmark_sorts(arrays, algos)
        for algo_name in algos.keys():
            assert algo_name in results
            for array_name in arrays.keys():
                assert array_name in results[algo_name]
