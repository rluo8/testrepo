"""
String utilities module
"""


def reverse_string(text):
    """Reverse a string
    
    Args:
        text: The string to reverse
        
    Returns:
        The reversed string
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text[::-1]


def count_words(text):
    """Count the number of words in a string
    
    Args:
        text: The string to count words in
        
    Returns:
        The number of words
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return len(text.split())


def capitalize_words(text):
    """Capitalize the first letter of each word
    
    Args:
        text: The string to capitalize
        
    Returns:
        The capitalized string
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return ' '.join(word.capitalize() for word in text.split())


def is_palindrome(text):
    """Check if a string is a palindrome (ignoring spaces and case)
    
    Args:
        text: The string to check
        
    Returns:
        True if palindrome, False otherwise
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Remove spaces and convert to lowercase
    cleaned = text.replace(' ', '').lower()
    return cleaned == cleaned[::-1]


def truncate(text, max_length, suffix='...'):
    """Truncate a string to a maximum length
    
    Args:
        text: The string to truncate
        max_length: Maximum length of the result
        suffix: Suffix to add if truncated (default: '...')
        
    Returns:
        The truncated string
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    if max_length < 0:
        raise ValueError("max_length must be non-negative")
    
    if len(text) <= max_length:
        return text
    
    return text[:max_length - len(suffix)] + suffix
