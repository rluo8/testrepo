"""
Tests for calculator module
"""
import pytest
from mypackage import Calculator, fibonacci


class TestCalculator:
    """Test Calculator class"""
    
    def test_add(self):
        calc = Calculator()
        assert calc.add(2, 3) == 5
        assert calc.add(-1, 1) == 0
        assert calc.add(0, 0) == 0
    
    def test_subtract(self):
        calc = Calculator()
        assert calc.subtract(5, 3) == 2
        assert calc.subtract(1, 1) == 0
        assert calc.subtract(0, 5) == -5
    
    def test_multiply(self):
        calc = Calculator()
        assert calc.multiply(2, 3) == 6
        assert calc.multiply(-2, 3) == -6
        assert calc.multiply(0, 100) == 0
    
    def test_divide(self):
        calc = Calculator()
        assert calc.divide(6, 2) == 3
        assert calc.divide(5, 2) == 2.5
        
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(5, 0)
    
    def test_history(self):
        calc = Calculator()
        calc.add(1, 2)
        calc.multiply(3, 4)
        
        history = calc.get_history()
        assert len(history) == 2
        assert "1 + 2 = 3" in history[0]
        assert "3 * 4 = 12" in history[1]
        
        calc.clear_history()
        assert len(calc.get_history()) == 0


class TestFibonacci:
    """Test Fibonacci function"""
    
    def test_fibonacci_base_cases(self):
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1
    
    def test_fibonacci_sequence(self):
        assert fibonacci(2) == 1
        assert fibonacci(3) == 2
        assert fibonacci(4) == 3
        assert fibonacci(5) == 5
        assert fibonacci(10) == 55
    
    def test_fibonacci_negative(self):
        with pytest.raises(ValueError, match="must be non-negative"):
            fibonacci(-1)
