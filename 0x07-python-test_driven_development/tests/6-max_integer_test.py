#!/usr/bin/python3
"""Function unittest for max_integer(list=[])"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class for max_integer"""
    def test_module_docstring(self):
        """Test for module docsting"""
        m_doc = __import__('6-max_integer').__doc__
        self.assertTrue(len(m_doc) > 1)

    def test_function_docstring(self):
        """Test for funstion docstring"""
        f_doc = max_integer.__doc__
        self.assertTrue(len(f_doc) > 1)

    def test_empty_list(self):
        """Test for empty list []"""
        e_list = []
        self.assertIsNone(max_integer(e_list))

    def test_no_args(self):
        """Test for no arguments passed"""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """Test for only one number in the list"""
        one_el = [8]
        self.assertEqual(max_integer(one_el), 8)

    def test_positive_end(self):
        """Test for all positive with max at end"""
        pos_end = [6, 10, 8, 36, 84, 80]
        self.assertEqual(max_integer(pos_end), 80)

    def test_positive_middle(self):
        """Test for all positive with max in middle"""
        pos_mid = [27, 10, 8, 36, 14, 508]
        self.assertEqual(max_integer(pos_mid), 36)

    def test_positive_beginning(self):
        """Tests for all positive with max at beginning"""
        pos_begin = [20, 10, 8, 38, 18, 59]
        self.assertEqual(max_integer(pos_begin), 20)

    def test_one_negative(self):
        """Tests for list with one negative number"""
        one_neg = [20, 100, 9, -37, 1, 56]
        self.assertEqual(max_integer(one_neg), 20)

    def test_all_negative(self):
        """Tests for list with all negative numbers"""
        all_neg = [-3, -40, -55, -1, -101]
        self.assertEqual(max_integer(all_neg), -1)

    def test_none(self):
        """Tests for passing none as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_int_arg(self):
        """Tests for a non-int type in list"""
        string = [2, 4, "FizzBuzz", 8, 5]
        with self.assertRaises(TypeError):
            max_integer(string)

if __name__ == "__main__":
    unittest.main()
