import pytest
from src.generator_tests import *


class TestGenerators:
    def test_rand_int_array_basic(self):
        arr = rand_int_array(10, 0, 100)
        assert len(arr) == 10
        assert all(0 <= x <= 100 for x in arr)

    def test_rand_int_array_distinct(self):
        arr = rand_int_array(5, 1, 5, distinct=True)
        assert len(arr) == 5
        assert len(set(arr)) == 5
        assert all(1 <= x <= 5 for x in arr)

    def test_rand_int_array_distinct_error(self):
        with pytest.raises(ValueError):
            rand_int_array(10, 1, 5, distinct=True)

    def test_nearly_sorted(self):
        arr = nearly_sorted(10, 3)
        assert len(arr) == 10
        assert sorted(arr) == list(range(10))
        assert arr != list(range(10))

    def test_nearly_sorted_no_swaps(self):
        arr = nearly_sorted(5, 0)
        assert arr == [0, 1, 2, 3, 4]

    def test_many_duplicates(self):
        arr = many_duplicates(10, 3)
        assert len(arr) == 10
        assert len(set(arr)) <= 3
        assert all(0 <= x < 3 for x in arr)

    def test_many_duplicates_error(self):
        with pytest.raises(ValueError):
            many_duplicates(10, 0)

    def test_reverse_sorted(self):
        arr = reverse_sorted(5)
        assert arr == [4, 3, 2, 1, 0]

    def test_rand_float_array(self):
        arr = rand_float_array(10, 0.0, 1.0)
        assert len(arr) == 10
        assert all(0.0 <= x <= 1.0 for x in arr)
        assert all(isinstance(x, float) for x in arr)

    def test_edge_cases(self):
        assert rand_int_array(0, 1, 10) == []
        assert nearly_sorted(0, 5) == []
        assert many_duplicates(0, 5) == []
        assert reverse_sorted(0) == []
        assert rand_float_array(0, 0.0, 1.0) == []
        
        assert rand_int_array(1, 5, 5) == [5]
        assert nearly_sorted(1, 5) == [0]
        assert reverse_sorted(1) == [0]

    def test_generated_arrays_sortable(self):
        from src.sorting import bubble_sort
        
        arrays = [
            rand_int_array(20, 1, 100),
            nearly_sorted(20, 5),
            many_duplicates(20, 5),
            reverse_sorted(20)
        ]
        
        for arr in arrays:
            sorted_arr = bubble_sort(arr)
            assert sorted_arr == sorted(arr)
