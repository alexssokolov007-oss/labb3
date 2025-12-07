import pytest
from src.sequences import Sequences


class TestSequences:
    def setup_method(self):
        self.seq = Sequences()

    def test_factorial_zero(self):
        assert self.seq.factorial(0) == 1
        assert self.seq.factorial_recursive(0) == 1

    def test_factorial_one(self):
        assert self.seq.factorial(1) == 1
        assert self.seq.factorial_recursive(1) == 1

    def test_factorial_positive(self):
        assert self.seq.factorial(5) == 120
        assert self.seq.factorial_recursive(5) == 120
        assert self.seq.factorial(10) == 3628800
        assert self.seq.factorial_recursive(10) == 3628800

    def test_factorial_negative(self):
        with pytest.raises(ValueError):
            self.seq.factorial(-1)
        with pytest.raises(ValueError):
            self.seq.factorial_recursive(-1)

    def test_factorial_large_numbers(self):
        with pytest.raises(ValueError):
            self.seq.factorial(1001)
        with pytest.raises(RecursionError):
            self.seq.factorial_recursive(501)

    def test_factorial_invalid_type(self):
        with pytest.raises(TypeError):
            self.seq.factorial('5')
        with pytest.raises(TypeError):
            self.seq.factorial_recursive(5.5)

    def test_fibo_zero(self):
        assert self.seq.fibo(0) == 0
        assert self.seq.fibo_recursive(0) == 0

    def test_fibo_one(self):
        assert self.seq.fibo(1) == 1
        assert self.seq.fibo_recursive(1) == 1

    def test_fibo_positive(self):
        assert self.seq.fibo(6) == 8
        assert self.seq.fibo_recursive(6) == 8
        assert self.seq.fibo(10) == 55
        assert self.seq.fibo_recursive(10) == 55

    def test_fibo_sequence(self):
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i, val in enumerate(expected):
            assert self.seq.fibo(i) == val
            assert self.seq.fibo_recursive(i) == val

    def test_fibo_large_numbers(self):
        assert self.seq.fibo(50) == 12586269025
        assert self.seq.fibo_recursive(50) == 12586269025

    def test_fibo_negative(self):
        with pytest.raises(ValueError):
            self.seq.fibo(-1)
        with pytest.raises(ValueError):
            self.seq.fibo_recursive(-1)

    def test_fibo_invalid_type(self):
        with pytest.raises(TypeError):
            self.seq.fibo('10')
        with pytest.raises(TypeError):
            self.seq.fibo_recursive([5])

    def test_fibo_overflow_protection(self):
        with pytest.raises(ValueError):
            self.seq.fibo(100001)
