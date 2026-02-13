"""
Input validation utilities
"""

import re


def is_valid_email(email):
    """Check if a string is a valid email address
    
    Args:
        email: String to validate
        
    Returns:
        True if valid email, False otherwise
    """
    if not isinstance(email, str):
        return False
    
    if not email or len(email) > 254:
        return False
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def is_valid_phone(phone, country_code='US'):
    """Check if a string is a valid phone number
    
    Args:
        phone: String to validate
        country_code: Country code (default: 'US')
        
    Returns:
        True if valid phone, False otherwise
    """
    if not isinstance(phone, str):
        return False
    
    # Remove common separators
    cleaned = re.sub(r'[\s\-\(\)\.]', '', phone)
    
    if country_code == 'US':
        # US: 10 digits, optionally starting with +1 or 1
        pattern = r'^(\+?1)?[2-9]\d{9}$'
        return bool(re.match(pattern, cleaned))
    
    # Generic: 7-15 digits
    return cleaned.isdigit() and 7 <= len(cleaned) <= 15


def is_strong_password(password):
    """Check if a password meets strength requirements
    
    Requirements:
    - At least 8 characters
    - Contains uppercase letter
    - Contains lowercase letter
    - Contains digit
    - Contains special character
    
    Args:
        password: String to validate
        
    Returns:
        True if strong password, False otherwise
    """
    if not isinstance(password, str):
        return False
    
    if len(password) < 8:
        return False
    
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    return all([has_upper, has_lower, has_digit, has_special])


def validate_range(value, min_val=None, max_val=None):
    """Validate that a value is within a range
    
    Args:
        value: Value to validate
        min_val: Minimum allowed value (optional)
        max_val: Maximum allowed value (optional)
        
    Returns:
        True if within range, False otherwise
    """
    if not isinstance(value, (int, float)):
        return False
    
    if min_val is not None and value < min_val:
        return False
    
    if max_val is not None and value > max_val:
        return False
    
    return True


def is_valid_url(url):
    """Check if a string is a valid URL
    
    Args:
        url: String to validate
        
    Returns:
        True if valid URL, False otherwise
    """
    if not isinstance(url, str):
        return False
    
    if not url:
        return False
    
    pattern = r'^https?://[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*(/.*)?$'
    return bool(re.match(pattern, url))
