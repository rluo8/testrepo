"""
Cython math functions for performance
"""


def fast_multiply(double a, double b):
    """
    Fast multiplication using Cython
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Product of a and b
    """
    return a * b


def fast_power(double base, int exponent):
    """
    Fast power calculation using Cython
    
    Args:
        base: Base number
        exponent: Exponent (must be non-negative)
    
    Returns:
        base raised to the power of exponent
    """
    if exponent < 0:
        raise ValueError("Exponent must be non-negative")
    
    if exponent == 0:
        return 1.0
    
    cdef double result = 1.0
    cdef int i
    
    for i in range(exponent):
        result *= base
    
    return result


cpdef double sum_array(double[:] arr):
    """
    Sum elements in an array using Cython
    
    Args:
        arr: Array of numbers
    
    Returns:
        Sum of all elements
    """
    cdef double total = 0.0
    cdef int i
    
    for i in range(arr.shape[0]):
        total += arr[i]
    
    return total
