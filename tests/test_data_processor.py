"""
Tests for data_processor module
"""

import pytest
from mypackage.data_processor import (
    filter_positive,
    calculate_statistics,
    group_by_range,
    normalize
)


class TestFilterPositive:
    def test_filter_positive_numbers(self):
        assert filter_positive([1, -2, 3, -4, 5]) == [1, 3, 5]
    
    def test_all_positive(self):
        assert filter_positive([1, 2, 3]) == [1, 2, 3]
    
    def test_all_negative(self):
        assert filter_positive([-1, -2, -3]) == []
    
    def test_with_zero(self):
        assert filter_positive([0, 1, -1]) == [1]
    
    def test_with_floats(self):
        assert filter_positive([1.5, -2.5, 3.5]) == [1.5, 3.5]
    
    def test_empty_list(self):
        assert filter_positive([]) == []
    
    def test_invalid_input(self):
        with pytest.raises(TypeError):
            filter_positive("not a list")


class TestCalculateStatistics:
    def test_basic_statistics(self):
        stats = calculate_statistics([1, 2, 3, 4, 5])
        assert stats['mean'] == 3.0
        assert stats['median'] == 3
        assert stats['min'] == 1
        assert stats['max'] == 5
        assert stats['count'] == 5
    
    def test_even_count_median(self):
        stats = calculate_statistics([1, 2, 3, 4])
        assert stats['median'] == 2.5
    
    def test_single_number(self):
        stats = calculate_statistics([5])
        assert stats['mean'] == 5
        assert stats['median'] == 5
    
    def test_negative_numbers(self):
        stats = calculate_statistics([-5, -3, -1])
        assert stats['mean'] == -3.0
        assert stats['min'] == -5
        assert stats['max'] == -1
    
    def test_empty_list(self):
        with pytest.raises(ValueError):
            calculate_statistics([])
    
    def test_invalid_input(self):
        with pytest.raises(TypeError):
            calculate_statistics("not a list")
    
    def test_non_numeric_elements(self):
        with pytest.raises(TypeError):
            calculate_statistics([1, 'two', 3])


class TestGroupByRange:
    def test_basic_grouping(self):
        groups = group_by_range([5, 15, 25, 35])
        assert groups == {'0-10': 1, '10-20': 1, '20-30': 1, '30-40': 1}
    
    def test_custom_step(self):
        groups = group_by_range([5, 10, 15], step=5)
        assert groups == {'5-10': 1, '10-15': 1, '15-20': 1}
    
    def test_multiple_in_range(self):
        groups = group_by_range([1, 2, 3, 4, 5])
        assert groups == {'0-10': 5}
    
    def test_empty_list(self):
        assert group_by_range([]) == {}
    
    def test_negative_numbers(self):
        groups = group_by_range([-5, 5, 15])
        assert '-10-0' in groups
        assert '0-10' in groups
    
    def test_invalid_step(self):
        with pytest.raises(ValueError):
            group_by_range([1, 2, 3], step=0)
    
    def test_invalid_input(self):
        with pytest.raises(TypeError):
            group_by_range("not a list")


class TestNormalize:
    def test_basic_normalization(self):
        result = normalize([0, 5, 10])
        assert result[0] == 0.0
        assert result[1] == 0.5
        assert result[2] == 1.0
    
    def test_custom_range(self):
        result = normalize([0, 5, 10], target_min=-1, target_max=1)
        assert result[0] == -1.0
        assert result[1] == 0.0
        assert result[2] == 1.0
    
    def test_single_value(self):
        result = normalize([5, 5, 5])
        assert all(v == 0.5 for v in result)
    
    def test_negative_numbers(self):
        result = normalize([-10, 0, 10])
        assert result[0] == 0.0
        assert result[1] == 0.5
        assert result[2] == 1.0
    
    def test_empty_list(self):
        assert normalize([]) == []
    
    def test_invalid_input(self):
        with pytest.raises(TypeError):
            normalize("not a list")
    
    def test_non_numeric_elements(self):
        with pytest.raises(TypeError):
            normalize([1, 'two', 3])
