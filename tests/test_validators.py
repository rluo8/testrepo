"""
Tests for validators module
"""

import pytest
from mypackage.validators import (
    is_valid_email,
    is_valid_phone,
    is_strong_password,
    validate_range,
    is_valid_url
)


class TestIsValidEmail:
    def test_valid_emails(self):
        assert is_valid_email("user@example.com") is True
        assert is_valid_email("test.user@example.com") is True
        assert is_valid_email("user+tag@example.co.uk") is True
    
    def test_invalid_emails(self):
        assert is_valid_email("invalid") is False
        assert is_valid_email("@example.com") is False
        assert is_valid_email("user@") is False
        assert is_valid_email("user @example.com") is False
    
    def test_empty_string(self):
        assert is_valid_email("") is False
    
    def test_non_string_input(self):
        assert is_valid_email(123) is False
        assert is_valid_email(None) is False
    
    def test_too_long(self):
        long_email = "a" * 250 + "@example.com"
        assert is_valid_email(long_email) is False


class TestIsValidPhone:
    def test_valid_us_phones(self):
        assert is_valid_phone("2025551234") is True
        assert is_valid_phone("(202) 555-1234") is True
        assert is_valid_phone("202-555-1234") is True
        assert is_valid_phone("+1-202-555-1234") is True
    
    def test_invalid_us_phones(self):
        assert is_valid_phone("123456") is False
        assert is_valid_phone("1234567890") is False  # starts with 1
        assert is_valid_phone("0123456789") is False  # starts with 0
    
    def test_generic_country(self):
        assert is_valid_phone("1234567", country_code='UK') is True
        assert is_valid_phone("123456789012345", country_code='UK') is True
    
    def test_empty_string(self):
        assert is_valid_phone("") is False
    
    def test_non_string_input(self):
        assert is_valid_phone(1234567890) is False


class TestIsStrongPassword:
    def test_strong_passwords(self):
        assert is_strong_password("Test123!") is True
        assert is_strong_password("MyP@ssw0rd") is True
        assert is_strong_password("Abcd1234!@#$") is True
    
    def test_weak_passwords(self):
        assert is_strong_password("test") is False  # too short
        assert is_strong_password("testtest") is False  # no upper, digit, special
        assert is_strong_password("TESTTEST") is False  # no lower, digit, special
        assert is_strong_password("Test1234") is False  # no special
        assert is_strong_password("Test!@#$") is False  # no digit
    
    def test_minimum_length(self):
        assert is_strong_password("Aa1!") is False  # only 4 chars
        assert is_strong_password("Aa1!xyz") is False  # 7 chars
        assert is_strong_password("Aa1!xyzz") is True  # 8 chars
    
    def test_non_string_input(self):
        assert is_strong_password(12345678) is False
        assert is_strong_password(None) is False


class TestValidateRange:
    def test_within_range(self):
        assert validate_range(5, min_val=0, max_val=10) is True
    
    def test_at_boundaries(self):
        assert validate_range(0, min_val=0, max_val=10) is True
        assert validate_range(10, min_val=0, max_val=10) is True
    
    def test_outside_range(self):
        assert validate_range(-1, min_val=0, max_val=10) is False
        assert validate_range(11, min_val=0, max_val=10) is False
    
    def test_only_min(self):
        assert validate_range(5, min_val=0) is True
        assert validate_range(-1, min_val=0) is False
    
    def test_only_max(self):
        assert validate_range(5, max_val=10) is True
        assert validate_range(11, max_val=10) is False
    
    def test_no_bounds(self):
        assert validate_range(999) is True
    
    def test_float_values(self):
        assert validate_range(5.5, min_val=5.0, max_val=6.0) is True
    
    def test_non_numeric_input(self):
        assert validate_range("5", min_val=0, max_val=10) is False


class TestIsValidUrl:
    def test_valid_urls(self):
        assert is_valid_url("http://example.com") is True
        assert is_valid_url("https://example.com") is True
        assert is_valid_url("https://www.example.com") is True
        assert is_valid_url("https://example.com/path") is True
        assert is_valid_url("https://example.com/path?query=value") is True
    
    def test_invalid_urls(self):
        assert is_valid_url("not-a-url") is False
        assert is_valid_url("ftp://example.com") is False
        assert is_valid_url("http://") is False
        assert is_valid_url("http://.com") is False
    
    def test_empty_string(self):
        assert is_valid_url("") is False
    
    def test_non_string_input(self):
        assert is_valid_url(123) is False
        assert is_valid_url(None) is False
    
    def test_with_port(self):
        assert is_valid_url("http://example.com:8080") is True
