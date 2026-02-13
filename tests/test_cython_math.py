"""
Tests for Cython math module
"""
import pytest
import numpy as np
from mypackage import fast_multiply, fast_power, cython_math


class TestFastMultiply:
    """Test fast_multiply function"""
    
    def test_positive_numbers(self):
        assert fast_multiply(2.0, 3.0) == 6.0
        assert fast_multiply(10.0, 5.0) == 50.0
    
    def test_negative_numbers(self):
        assert fast_multiply(-2.0, 3.0) == -6.0
        assert fast_multiply(-2.0, -3.0) == 6.0
    
    def test_zero(self):
        assert fast_multiply(0.0, 100.0) == 0.0
        assert fast_multiply(100.0, 0.0) == 0.0
    
    def test_decimals(self):
        result = fast_multiply(2.5, 4.0)
        assert abs(result - 10.0) < 1e-10


class TestFastPower:
    """Test fast_power function"""
    
    def test_power_zero(self):
        assert fast_power(5.0, 0) == 1.0
        assert fast_power(0.0, 0) == 1.0
    
    def test_power_one(self):
        assert fast_power(5.0, 1) == 5.0
        assert fast_power(2.5, 1) == 2.5
    
    def test_power_positive(self):
        assert fast_power(2.0, 3) == 8.0
        assert fast_power(3.0, 2) == 9.0
        assert fast_power(10.0, 2) == 100.0
    
    def test_power_negative_base(self):
        assert fast_power(-2.0, 2) == 4.0
        assert fast_power(-2.0, 3) == -8.0
    
    def test_power_negative_exponent(self):
        with pytest.raises(ValueError, match="must be non-negative"):
            fast_power(2.0, -1)


class TestSumArray:
    """Test sum_array function"""
    
    def test_sum_simple_array(self):
        arr = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
        assert cython_math.sum_array(arr) == 15.0
    
    def test_sum_empty_array(self):
        arr = np.array([])
        assert cython_math.sum_array(arr) == 0.0
    
    def test_sum_single_element(self):
        arr = np.array([42.0])
        assert cython_math.sum_array(arr) == 42.0
    
    def test_sum_negative_numbers(self):
        arr = np.array([-1.0, -2.0, -3.0])
        assert cython_math.sum_array(arr) == -6.0
    
    def test_sum_mixed_numbers(self):
        arr = np.array([10.0, -5.0, 3.0, -2.0])
        assert cython_math.sum_array(arr) == 6.0
