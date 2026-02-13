"""
Data processing utilities
"""


def filter_positive(numbers):
    """Filter positive numbers from a list
    
    Args:
        numbers: List of numbers
        
    Returns:
        List of positive numbers
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    return [n for n in numbers if isinstance(n, (int, float)) and n > 0]


def calculate_statistics(numbers):
    """Calculate basic statistics for a list of numbers
    
    Args:
        numbers: List of numbers
        
    Returns:
        Dictionary with mean, median, min, max
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    if not numbers:
        raise ValueError("List cannot be empty")
    
    if not all(isinstance(n, (int, float)) for n in numbers):
        raise TypeError("All elements must be numbers")
    
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    
    mean = sum(numbers) / n
    
    if n % 2 == 0:
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        median = sorted_numbers[n // 2]
    
    return {
        'mean': mean,
        'median': median,
        'min': min(numbers),
        'max': max(numbers),
        'count': n
    }


def group_by_range(numbers, step=10):
    """Group numbers into ranges
    
    Args:
        numbers: List of numbers
        step: Range step size (default: 10)
        
    Returns:
        Dictionary with ranges as keys and counts as values
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    if step <= 0:
        raise ValueError("Step must be positive")
    
    if not numbers:
        return {}
    
    groups = {}
    for num in numbers:
        if not isinstance(num, (int, float)):
            continue
        
        range_start = (int(num) // step) * step
        range_key = f"{range_start}-{range_start + step}"
        
        if range_key not in groups:
            groups[range_key] = 0
        groups[range_key] += 1
    
    return groups


def normalize(numbers, target_min=0, target_max=1):
    """Normalize numbers to a target range
    
    Args:
        numbers: List of numbers
        target_min: Target minimum value (default: 0)
        target_max: Target maximum value (default: 1)
        
    Returns:
        List of normalized numbers
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    if not numbers:
        return []
    
    if not all(isinstance(n, (int, float)) for n in numbers):
        raise TypeError("All elements must be numbers")
    
    min_val = min(numbers)
    max_val = max(numbers)
    
    if min_val == max_val:
        # All numbers are the same, return middle of target range
        mid = (target_min + target_max) / 2
        return [mid] * len(numbers)
    
    range_val = max_val - min_val
    target_range = target_max - target_min
    
    return [
        target_min + ((n - min_val) / range_val) * target_range
        for n in numbers
    ]
