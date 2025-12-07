import pytest
from src.sorting import *
from src.generator_tests import rand_int_array, nearly_sorted, many_duplicates, reverse_sorted


class TestSorting:
    test_arrays = {
        'empty': [],
        'single': [5],
        'sorted': [1, 2, 3, 4, 5],
        'reverse': [5, 4, 3, 2, 1],
        'random': [3, 1, 4, 1, 5, 9, 2, 6],
        'duplicates': [2, 2, 1, 1, 3, 3],
        'negative': [-3, -1, -4, -1],
        'mixed': [-5, 0, 3, -2, 1]
    }

    def test_bubble_sort(self):
        for name, arr in self.test_arrays.items():
            if name not in ['negative', 'mixed']:
                result = bubble_sort(arr)
                assert result == sorted(arr), f'Failed on {name}'

    def test_quick_sort(self):
        for name, arr in self.test_arrays.items():
            result = quick_sort(arr)
            assert result == sorted(arr), f'Failed on {name}'

    def test_counting_sort(self):
        positive_arrays = {k: v for k, v in self.test_arrays.items() 
                          if k not in ['negative', 'mixed'] and not any(x < 0 for x in v)}
        
        for name, arr in positive_arrays.items():
            result = counting_sort(arr)
            assert result == sorted(arr), f'Failed on {name}'

    def test_counting_sort_negative(self):
        with pytest.raises(ValueError):
            counting_sort([-1, 2, 3])
        
        with pytest.raises(ValueError):
            counting_sort([100001])

    def test_radix_sort(self):
        positive_arrays = {k: v for k, v in self.test_arrays.items() 
                          if k not in ['negative', 'mixed'] and not any(x < 0 for x in v)}
        
        for name, arr in positive_arrays.items():
            result = radix_sort(arr)
            assert result == sorted(arr), f'Failed on {name}'

    def test_radix_sort_different_bases(self):
        arr = [170, 45, 75, 90, 2, 802, 24, 66]
        assert radix_sort(arr, 2) == sorted(arr)
        assert radix_sort(arr, 10) == sorted(arr)
        assert radix_sort(arr, 16) == sorted(arr)

    def test_bucket_sort(self):
        float_arrays = {
            'simple': [0.1, 0.3, 0.2],
            'duplicates': [0.5, 0.5, 0.1, 0.1],
            'edges': [0.0, 1.0, 0.5]
        }
        
        for name, arr in float_arrays.items():
            result = bucket_sort(arr)
            assert result == sorted(arr), f'Failed on {name}'

    def test_bucket_sort_invalid_range(self):
        with pytest.raises(ValueError):
            bucket_sort([-0.1, 0.5])
        with pytest.raises(ValueError):
            bucket_sort([0.5, 1.1])

    def test_heap_sort(self):
        for name, arr in self.test_arrays.items():
            result = heap_sort(arr)
            assert result == sorted(arr), f'Failed on {name}'

    def test_immutability(self):
        original = [3, 1, 4, 1, 5]
        original_copy = original.copy()
        
        bubble_sort(original)
        quick_sort(original)
        heap_sort(original)
        
        assert original == original_copy

    def test_generated_arrays(self):
        arrays = {
            'random_100': rand_int_array(100, 1, 1000),
            'nearly_sorted': nearly_sorted(50, 10),
            'many_duplicates': many_duplicates(100, 5),
            'reverse': reverse_sorted(100)
        }
        
        for name, arr in arrays.items():
            assert bubble_sort(arr) == sorted(arr), f'Bubble failed on {name}'
            assert quick_sort(arr) == sorted(arr), f'Quick failed on {name}'
            assert heap_sort(arr) == sorted(arr), f'Heap failed on {name}'
            
            if min(arr) >= 0:
                assert counting_sort(arr) == sorted(arr), f'Counting failed on {name}'
                assert radix_sort(arr) == sorted(arr), f'Radix failed on {name}'
