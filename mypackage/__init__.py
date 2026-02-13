"""
MyPackage - A simple package with Python and Cython code
"""

__version__ = "0.1.0"

from .calculator import Calculator, fibonacci
from .string_utils import (
    reverse_string,
    count_words,
    capitalize_words,
    is_palindrome,
    truncate
)
from .data_processor import (
    filter_positive,
    calculate_statistics,
    group_by_range,
    normalize
)
from .validators import (
    is_valid_email,
    is_valid_phone,
    is_strong_password,
    validate_range,
    is_valid_url
)

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

__all__ = [
    # Calculator
    "Calculator",
    "fibonacci",
    # Cython math
    "fast_multiply",
    "fast_power",
    "sum_array",
    # String utils
    "reverse_string",
    "count_words",
    "capitalize_words",
    "is_palindrome",
    "truncate",
    # Data processor
    "filter_positive",
    "calculate_statistics",
    "group_by_range",
    "normalize",
    # Validators
    "is_valid_email",
    "is_valid_phone",
    "is_strong_password",
    "validate_range",
    "is_valid_url",
]
