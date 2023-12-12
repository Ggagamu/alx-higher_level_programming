#!/usr/bin/python3
"""base.Base class unittest """


import unittest
import json
import inspect
from models import base


class TestBase_docstrings(unittest.TestCase):
    """base.Base class unit tests"""

    @classmethod
    def setUpClass(cls):
        """Prepare for the doc tests"""
        cls.base_functs = inspect.getmembers(base.Base, inspect.isfunction)

    def test_module_doc(self):
        """Test module documentation"""
        self.assertTrue(len(base.__doc__) > 0)

    def test_class_doc(self):
        """Test class documentation"""
        self.assertTrue(len(base.Base.__doc__) > 0)

    def test_instance_id(self):
        """Test ids for class instances"""
        test1 = base.Base()
        self.assertEqual(test1.id, 1)

        bast_test = base.Base()
        self.assertEqual(bast_test.id, 2)

        test10 = base.Base(10)
        self.assertEqual(test10.id, 10)

        test3 = base.Base(12)
        self.assertEqual(test3.id, 3)

    def test_func_docstrings(self):
        """Docstrings tests"""
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) > 0)


class TestBase(unittest.TestCase):
    """Tests for base.Base class usability """

    def test_excess_args(self):
        """ If more arguments passed"""
        with self.assertRaises(TypeError):
            base_test = base.Base(1, 1)

    def test_no_id(self):
        """ If no Id is passed """
        base_test = base.Base()
        self.assertEqual(base_test.id, 1)

    def test_specific_id(self):
        """If actual ID is passed """
        base_test = base.Base(50)
        self.assertEqual(base_test.id, 50)

    def test_none_after_id(self):
        """if no ID after not None"""
        bast_test = base.Base()
        self.assertEqual(bast_test.id, 2)

    def test_private_instance_att(self):
        """Private instances attribute"""
        base_test = base.Base(3)
        with self.assertRaises(AttributeError):
            print(base_test.__nb_objects)
        with self.assertRaises(AttributeError):
            print(base_test.nb_objects)

    def test_dumps(self):
        """Test 'dumps' """
        base.Base._Base__nb_objects = 0
        test_1 = {"id": 23, "width": 15, "height": 18, "x": 4, "y": 6}
        test_2 = {"id": 1, "width": 7, "height": 10, "x": 7, "y": 2}
        json_string = base.Base.to_json_string([test_1, test_2])
        self.assertTrue(type(json_string) is str)
        json_object = json.loads(json_string)
        self.assertEqual(json_object, [test_1, test_2])

    def test_to_json_string_empty(self):
        """If empty list s passed"""
        json_string = base.Base.to_json_string([])
        self.assertTrue(type(json_string) is str)
        self.assertEqual(json_string, "[]")

    def test_to_json_String_none(self):
        """ If none was passed"""
        json_string = base.Base.to_json_string(None)
        self.assertTrue(type(json_string) is str)
        self.assertEqual(json_string, "[]")

    def test_from_json_string(self):
        """if the from_json_string is as it should be"""
        json_string = '[{"id": 12, "width": 15, "height": 3, "x": 6, "y": 9}, \
{"id": 22, "width": 21, "height": 13, "x": 12, "y": 2}]'
        json_list = base.Base.from_json_string(json_string)
        self.assertTrue(type(json_list) is list)
        self.assertEqual(len(json_list), 2)
        self.assertTrue(type(json_list[0]) is dict)
        self.assertTrue(type(json_list[1]) is dict)
        self.assertEqual(json_list[0],
                         {"id": 12, "width": 15, "height": 3, "x": 6, "y": 9})
        self.assertEqual(json_list[1],
                         {"id": 22, "width": 21, "height": 13, "x": 12, "y": 2})

    def test_from_json_string_empty(self):
        """If JSON is empty"""
        self.assertEqual([], base.Base.from_json_string(""))

    def test_from_json_string_None(self):
        """ If JSON is None"""
        self.assertEqual([], base.Base.from_json_string(None))


if __name__ == '__main__':
    unittest.main()
