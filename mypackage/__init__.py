"""
MyPackage - A simple package with Python and Cython code
"""

__version__ = "0.1.0"

from .calculator import Calculator, fibonacci

try:
    from .cython_math import fast_multiply, fast_power, sum_array
except ImportError:
    # Fallback if Cython not built
    def fast_multiply(a, b):
        return a * b
    
    def fast_power(a, b):
        return a ** b
    
    def sum_array(arr):
        return sum(arr)

__all__ = ["Calculator", "fibonacci", "fast_multiply", "fast_power", "sum_array"]
