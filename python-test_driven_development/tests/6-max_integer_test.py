#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_ordered_list(self):
        """Test a list of ordered integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test a list of unordered integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test a list where the max value is at the beginning."""
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """Test a list with a single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_floats(self):
        """Test a list containing floats."""
        self.assertEqual(max_integer([1.5, 2.2, 0.9, 3.1]), 3.1)

    def test_ints_and_floats(self):
        """Test a list containing both integers and floats."""
        self.assertEqual(max_integer([1, 2.5, 3, 2.1]), 3)

    def test_negative_numbers(self):
        """Test a list of negative numbers."""
        self.assertEqual(max_integer([-1, -5, -3, -2]), -1)

    def test_none_argument(self):
        """Test passing None as the list argument raises TypeError."""
        with self.assertRaises(TypeError):
            max_integer(None)
