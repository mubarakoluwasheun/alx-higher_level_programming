#!/usr/bin/python3
# test_base.py
"""Defines unittests for base.py."""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Unittests for class Base instantiation."""

    def test_default_id(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)

    def test_three_bases(self):
        base1 = Base()
        base2 = Base()
        base3 = Base()
        self.assertEqual(base1.id, base3.id - 2)

    def test_None_id(self):
        base1 = Base(None)
        base2 = Base(None)
        self.assertEqual(base1.id, base2.id - 1)

    def test_public_id(self):
        base1 = Base(6)
        base1.id = 25
        self.assertEqual(25, base1.id)

    def test_private_nb_instances(self):
        with self.assertRaises(AttributeError):
            print(Base(16).__nb_instances)

    def test_str_id(self):
        self.assertEqual("Goody", Base("Goody").id)

    def test_float_id(self):
        self.assertEqual(2.5, Base(2.5).id)

    def test_bool_id(self):
        self.assertEqual(False, Base(False).id)

    def test_dict_id(self):
        self.assertEqual({"x": 1, "y": 2}, Base({"x": 1, "y": 2}).id)

    def test_list_id(self):
        self.assertEqual([2, 4, 6], Base([2, 4, 6]).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_binary_id(self):
        self.assertEqual(b'Image', Base(b'Image').id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(10, 25)


class TestBase_to_json_string(unittest.TestCase):
    """Unittests for testing to_json_string method of class Base."""

    def test_to_json_string_rect_type(self):
        r = Rectangle(2, 4, 6, 8, 10)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_square_type(self):
        s = Square(5, 10, 15, 20)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()


class TestBase_save_to_file(unittest.TestCase):
    """Unittests for testing save_to_file method of class Base."""

    @classmethod
    def tearDown(self):
        """Delete any created .json files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()


class TestBase_from_json_string(unittest.TestCase):
    """Unittests for testing from_json_string method of class Base."""

    def test_from_json_string_type(self):
        list_input = [{"id": 25, "width": 5, "height": 10}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_one_rectangle(self):
        list_input = [{"id": 8, "width": 4, "height": 2, "x": 9}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_rectangles(self):
        list_input = [
            {"id": 5, "width": 13, "height": 6, "x": 1, "y": 3},
            {"id": 9, "width": 8, "height": 11, "x": 2, "y": 6},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_one_square(self):
        list_input = [{"id": 25, "size": 15, "height": 8}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_squares(self):
        list_input = [
            {"id": 25, "size": 15, "height": 8},
            {"id": 2, "size": 11, "height": 3}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class TestBase_create(unittest.TestCase):
    """Unittests for testing create method of class Base."""

    def test_create_rectangle_original(self):
        r1 = Rectangle(13, 15, 3, 5, 10)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (10) 3/5 - 13/15", str(r1))

    def test_create_rectangle_new(self):
        r1 = Rectangle(13, 15, 3, 5, 10)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (10) 3/5 - 13/15", str(r2))

    def test_create_rectangle_is(self):
        r1 = Rectangle(13, 15, 3, 5, 10)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_create_rectangle_equals(self):
        r1 = Rectangle(13, 15, 3, 5, 10)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_create_square_original(self):
        s1 = Square(13, 15, 3, 5)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (5) 15/3 - 13", str(s1))

    def test_create_square_new(self):
        s1 = Square(13, 15, 3, 5)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (5) 15/3 - 13", str(s2))

    def test_create_square_is(self):
        s1 = Square(13, 15, 3, 5)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

    def test_create_square_equals(self):
        s1 = Square(13, 15, 3, 5)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)


class TestBase_load_from_file(unittest.TestCase):
    """Unittests for testing load_from_file_method of class Base."""

    @classmethod
    def tearDown(self):
        """Delete any created .json files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_first_rectangle(self):
        r1 = Rectangle(2, 4, 6, 8, 10)
        r2 = Rectangle(10, 8, 6, 4, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_second_rectangle(self):
        r1 = Rectangle(2, 4, 6, 8, 10)
        r2 = Rectangle(10, 8, 6, 4, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_rectangle_types(self):
        r1 = Rectangle(2, 4, 6, 8, 10)
        r2 = Rectangle(10, 8, 6, 4, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_first_square(self):
        s1 = Square(5, 10, 15, 3)
        s2 = Square(19, 7, 4, 2)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_second_square(self):
        s1 = Square(5, 10, 15, 3)
        s2 = Square(19, 7, 4, 2)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_square_types(self):
        s1 = Square(5, 10, 15, 3)
        s2 = Square(19, 7, 4, 2)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


class TestBase_save_to_file_csv(unittest.TestCase):
    """Unittests for testing save_to_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created .csv files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_save_to_file_csv_one_rectangle(self):
        r = Rectangle(10, 3, 2, 6, 5)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv") as f:
            self.assertTrue("10,3,2,6,5", f.read())

    def test_save_to_file_csv_two_rectangles(self):
        r1 = Rectangle(10, 3, 2, 6, 5)
        r2 = Rectangle(7, 5, 3, 2, 4)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv") as f:
            self.assertTrue("10,3,2,6,5\n7,5,3,2,4", f.read())

    def test_save_to_file_csv_one_square(self):
        s = Square(10, 17, 4, 2)
        Square.save_to_file_csv([s])
        with open("Square.csv") as f:
            self.assertTrue("4,10,17,2", f.read())

    def test_save_to_file_csv_two_squares(self):
        s1 = Square(10, 17, 4, 2)
        s2 = Square(2, 4, 6, 8)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv") as f:
            self.assertTrue("4,10,17,2\n2,8,4,6", f.read())

    def test_save_to_file__csv_cls_name(self):
        s = Square(10, 17, 4, 2)
        Base.save_to_file_csv([s])
        with open("Base.csv") as f:
            self.assertTrue("4,10,17,2", f.read())

    def test_save_to_file_csv_overwrite(self):
        s = Square(6, 25, 39, 12)
        Square.save_to_file_csv([s])
        s = Square(9, 5, 13, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv") as f:
            self.assertTrue("8,9,5,13", f.read())

    def test_save_to_file__csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)


class TestBase_load_from_file_csv(unittest.TestCase):
    """Unittests for testing load_from_file_csv method of class Base."""

    @classmethod
    def tearDown(self):
        """Delete any created .csv files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_load_from_file_csv_first_rectangle(self):
        r1 = Rectangle(2, 4, 6, 8, 10)
        r2 = Rectangle(10, 8, 6, 4, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_csv_second_rectangle(self):
        r1 = Rectangle(2, 4, 6, 8, 10)
        r2 = Rectangle(10, 8, 6, 4, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_rectangle_types(self):
        r1 = Rectangle(10, 8, 6, 4, 2)
        r2 = Rectangle(2, 4, 6, 8, 10)
        Rectangle.save_to_file_csv([r1, r2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_csv_first_square(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square(9, 3, 6, 11)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_csv_second_square(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square(9, 3, 6, 11)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_csv_square_types(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square(9, 3, 6, 11)
        Square.save_to_file_csv([s1, s2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_csv_no_file(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_from_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)