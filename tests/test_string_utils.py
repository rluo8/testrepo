"""
Tests for string_utils module
"""

import pytest
from mypackage.string_utils import (
    reverse_string,
    count_words,
    capitalize_words,
    is_palindrome,
    truncate
)


class TestReverseString:
    def test_basic_reverse(self):
        assert reverse_string("hello") == "olleh"
    
    def test_empty_string(self):
        assert reverse_string("") == ""
    
    def test_single_char(self):
        assert reverse_string("a") == "a"
    
    def test_with_spaces(self):
        assert reverse_string("hello world") == "dlrow olleh"
    
    def test_invalid_input(self):
        with pytest.raises(TypeError):
            reverse_string(123)


class TestCountWords:
    def test_single_word(self):
        assert count_words("hello") == 1
    
    def test_multiple_words(self):
        assert count_words("hello world") == 2
    
    def test_extra_spaces(self):
        assert count_words("hello  world  test") == 3
    
    def test_empty_string(self):
        assert count_words("") == 0
    
    def test_invalid_input(self):
        with pytest.raises(TypeError):
            count_words(None)


class TestCapitalizeWords:
    def test_basic_capitalize(self):
        assert capitalize_words("hello world") == "Hello World"
    
    def test_already_capitalized(self):
        assert capitalize_words("Hello World") == "Hello World"
    
    def test_all_caps(self):
        assert capitalize_words("HELLO WORLD") == "Hello World"
    
    def test_single_word(self):
        assert capitalize_words("hello") == "Hello"
    
    def test_empty_string(self):
        assert capitalize_words("") == ""


class TestIsPalindrome:
    def test_simple_palindrome(self):
        assert is_palindrome("racecar") is True
    
    def test_palindrome_with_spaces(self):
        assert is_palindrome("race car") is True
    
    def test_not_palindrome(self):
        assert is_palindrome("hello") is False
    
    def test_case_insensitive(self):
        assert is_palindrome("RaceCar") is True
    
    def test_single_char(self):
        assert is_palindrome("a") is True
    
    def test_empty_string(self):
        assert is_palindrome("") is True


class TestTruncate:
    def test_no_truncation_needed(self):
        assert truncate("hello", 10) == "hello"
    
    def test_basic_truncation(self):
        assert truncate("hello world", 8) == "hello..."
    
    def test_custom_suffix(self):
        assert truncate("hello world", 8, suffix=">>") == "hello >>"
    
    def test_exact_length(self):
        assert truncate("hello", 5) == "hello"
    
    def test_very_short_max_length(self):
        assert truncate("hello world", 5) == "he..."
    
    def test_negative_max_length(self):
        with pytest.raises(ValueError):
            truncate("hello", -1)
    
    def test_invalid_input(self):
        with pytest.raises(TypeError):
            truncate(12345, 3)
