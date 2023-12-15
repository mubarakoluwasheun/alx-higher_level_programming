#!/usr/bin/python3
# test_sqruare.py
"""Defines unittests for sqruare.py module."""
import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Square class."""

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_is_base(self):
        self.assertIsInstance(Square(6), Base)

    def test_is_rectangle(self):
        self.assertIsInstance(Square(19), Square)

    def test_one_arg(self):
        s1 = Square(15)
        s2 = Square(16)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_args(self):
        s1 = Square(15, 6)
        s2 = Square(20, 3)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        s1 = Square(2, 4, 6)
        s2 = Square(6, 4, 2)

    def test_more_than_three_args(self):
        with self.assertRaises(TypeError):
            Square(10, 2, 13, 41, 3)

    def test_size_private(self):
        with self.assertRaises(AttributeError):
            print(Square(2, 4, 6, 8).__size)

    def test_size_getter(self):
        self.assertEqual(11, Square(11, 5, 8, 3).size)

    def test_size_setter(self):
        s = Square(10, 1, 5, 12)
        s.size = 5
        self.assertEqual(5, s.size)

    def test_width_getter(self):
        s = Square(14, 3, 6, 12)
        s.size = 15
        self.assertEqual(15, s.width)

    def test_height_getter(self):
        s = Square(12, 6, 3, 1)
        s.size = 7
        self.assertEqual(7, s.height)

    def test_x_getter(self):
        self.assertEqual(0, Square(30).x)

    def test_y_getter(self):
        self.assertEqual(0, Square(32).y)


class TestSquare_size(unittest.TestCase):
    """Unittests for testing size initialization of the Square class."""

    def test_None_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_str_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("String")

    def test_float_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(2.5)

    def test_dict_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"x": 1, "y": 2}, 3)

    def test_bool_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(False, 17, 23)

    def test_list_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([2, 4, 6])

    def test_set_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({2, 4, 6}, 2)

    def test_negative_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-20, 1)

    def test_zero_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 6)


class TestSquare_x(unittest.TestCase):
    """Unittests for testing initialization of x attribute of class Square."""

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(4, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(8, "invalid")

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, 1.7)

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, {"age": 5, "num": 2}, 2)

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(6, False)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, [2, 4, 6])

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, {2, 4, 6})

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -8, 0)


class TestSquare_y(unittest.TestCase):
    """Unittests for testing initialization of y attribute of class Square."""

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 10, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 5, "meow")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 10, 7.3)

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 5, {"age": 18, "number": 2})

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 5, [2, 4, 6])

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 5, {2, 4, 6})

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(6, 0, -13)


class TestSquare_order_of_initialization(unittest.TestCase):
    """Unittests for testing order of Square attribute initialization."""

    def test_size_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("StringType", "x")

    def test_size_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("StringType", 5, "y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, "x", "y")


class TestSquare_area(unittest.TestCase):
    """Unittests for testing the area method of the Square class."""

    def test_area_small_int(self):
        self.assertEqual(36, Square(6, 1, 0, 12).area())

    def test_area_large_int(self):
        sqr = Square(77777777777777777, 3, 1, 10)
        self.assertEqual(6049382716049382595061728395061729, sqr.area())

    def test_area_one_arg(self):
        sqr = Square(2, 4, 6, 1)
        with self.assertRaises(TypeError):
            sqr.area(6)


class TestSquare_stdout(unittest.TestCase):
    """Unittests for testing __str__ and display methods of Square class."""

    @staticmethod
    def return_text(sqr, method):
        """Returns text printed to stdout.

        Args:
            sqr (Square): The Square to print to stdout.
            method (str): The method to run on the sqr.
        Return:
            The text printed to stdout.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(sqr)
        else:
            sqr.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_str_method_print_size(self):
        sqr = Square(4)
        capture = TestSquare_stdout.return_text(sqr, "print")
        correct = "[Square] ({}) 0/0 - 4\n".format(sqr.id)
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_size_x(self):
        sqr = Square(15, 3)
        correct = "[Square] ({}) 3/0 - 15".format(sqr.id)
        self.assertEqual(correct, sqr.__str__())

    def test_str_method_size_x_y(self):
        sqr = Square(5, 2, 10)
        correct = "[Square] ({}) 2/10 - 5".format(sqr.id)
        self.assertEqual(correct, str(sqr))

    def test_str_method_size_x_y_id(self):
        sqr = Square(6, 19, 5, 8)
        self.assertEqual("[Square] (8) 19/5 - 6", str(sqr))

    def test_str_method_one_arg(self):
        sqr = Square(11, 2, 4, 6)
        with self.assertRaises(TypeError):
            sqr.__str__(11)

    def test_display_size(self):
        sqr = Square(2, 0, 0, 3)
        capture = TestSquare_stdout.return_text(sqr, "display")
        self.assertEqual("##\n##\n", capture.getvalue())

    def test_display_size_x(self):
        sqr = Square(3, 1, 0, 9)
        capture = TestSquare_stdout.return_text(sqr, "display")
        self.assertEqual(" ###\n ###\n ###\n", capture.getvalue())

    def test_display_size_y(self):
        sqr = Square(4, 0, 1, 6)
        capture = TestSquare_stdout.return_text(sqr, "display")
        display = "\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_size_x_y(self):
        sqr = Square(2, 3, 2, 1)
        capture = TestSquare_stdout.return_text(sqr, "display")
        display = "\n\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_one_arg(self):
        sqr = Square(2, 4, 6, 8)
        with self.assertRaises(TypeError):
            sqr.display(8)


class TestSquare_update_args(unittest.TestCase):
    """Unittests for testing update args method of the Square class."""

    def test_update_args_empty(self):
        sqr = Square(15, 15, 15, 15)
        sqr.update()
        self.assertEqual("[Square] (15) 15/15 - 15", str(sqr))

    def test_update_args_one(self):
        sqr = Square(15, 15, 15, 15)
        sqr.update(25)
        self.assertEqual("[Square] (25) 15/15 - 15", str(sqr))

    def test_update_args_two(self):
        sqr = Square(15, 15, 15, 15)
        sqr.update(25, 5)
        self.assertEqual("[Square] (25) 15/15 - 5", str(sqr))

    def test_update_args_three(self):
        sqr = Square(15, 15, 15, 15)
        sqr.update(25, 5, 1)
        self.assertEqual("[Square] (25) 1/15 - 5", str(sqr))

    def test_update_args_more_than_three(self):
        sqr = Square(15, 15, 15, 15)
        sqr.update(25, 5, 2, 3, 1)
        self.assertEqual("[Square] (25) 2/3 - 5", str(sqr))

    def test_update_args_width_setter(self):
        sqr = Square(15, 15, 15, 15)
        sqr.update(25, 5)
        self.assertEqual(5, sqr.width)

    def test_update_args_height_setter(self):
        sqr = Square(15, 15, 15, 15)
        sqr.update(25, 5)
        self.assertEqual(5, sqr.height)

    def test_update_args_None_id(self):
        sqr = Square(15, 15, 15, 15)
        sqr.update(None)
        expect = "[Square] ({}) 15/15 - 15".format(sqr.id)
        self.assertEqual(expect, str(sqr))

    def test_update_args_twice(self):
        sqr = Square(15, 15, 15, 15)
        sqr.update(25, 5, 1, 2)
        sqr.update(2, 4, 6, 10)
        self.assertEqual("[Square] (2) 6/10 - 4", str(sqr))

    def test_update_args_str_size_type(self):
        sqr = Square(15, 15, 15, 15)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sqr.update(25, "StringType")

    def test_update_args_size_zero(self):
        sqr = Square(15, 15, 15, 15)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sqr.update(25, 0)

    def test_update_args_size_negative(self):
        sqr = Square(15, 15, 15, 15)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sqr.update(25, -7)

    def test_update_args_str_x(self):
        sqr = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sqr.update(25, 6, "5")

    def test_update_args_negative_x(self):
        sqr = Square(15, 15, 15, 15)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            sqr.update(25, 5, -8)

    def test_update_args_invalid_y(self):
        sqr = Square(15, 15, 15, 15)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sqr.update(25, 5, 7, "Five")

    def test_update_args_y_negative(self):
        sqr = Square(15, 15, 15, 15)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            sqr.update(25, 5, 1, -2)

    def test_update_args_size_before_x(self):
        sqr = Square(15, 15, 15, 15)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sqr.update(25, "Three", "six")

    def test_update_args_x_before_y(self):
        sqr = Square(15, 15, 15, 15)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sqr.update(25, 5, "Nine", "Seven")


class TestSquare_update_kwargs(unittest.TestCase):
    """Unittests for testing update kwargs method of Square class."""

    def test_update_kwargs_one(self):
        sqr = Square(15, 15, 15, 15)
        sqr.update(id=5)
        self.assertEqual("[Square] (5) 15/15 - 15", str(sqr))

    def test_update_kwargs_two(self):
        sqr = Square(15, 15, 15, 15)
        sqr.update(size=5, id=1)
        self.assertEqual("[Square] (1) 15/15 - 5", str(sqr))

    def test_update_kwargs_three(self):
        sqr = Square(15, 15, 15, 15)
        sqr.update(y=1, size=5, id=9)
        self.assertEqual("[Square] (9) 15/1 - 5", str(sqr))

    def test_update_kwargs_width_setter(self):
        sqr = Square(15, 15, 15, 15)
        sqr.update(id=9, size=5)
        self.assertEqual(5, sqr.width)

    def test_update_kwargs_height_setter(self):
        sqr = Square(15, 15, 15, 15)
        sqr.update(id=9, size=7)
        self.assertEqual(7, sqr.height)

    def test_update_kwargs_None_id(self):
        sqr = Square(15, 15, 15, 15)
        sqr.update(id=None)
        correct = "[Square] ({}) 15/15 - 15".format(sqr.id)
        self.assertEqual(correct, str(sqr))

    def test_update_kwargs_None_id_and_more(self):
        sqr = Square(15, 15, 15, 15)
        sqr.update(id=None, size=5, x=9)
        correct = "[Square] ({}) 9/15 - 5".format(sqr.id)
        self.assertEqual(correct, str(sqr))

    def test_update_kwargs_twice(self):
        sqr = Square(15, 15, 15, 15)
        sqr.update(id=9, x=3)
        sqr.update(y=2, x=6, size=4)
        self.assertEqual("[Square] (9) 6/2 - 4", str(sqr))

    def test_update_kwargs_str_size(self):
        sqr = Square(15, 15, 15, 15)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sqr.update(size="Six")

    def test_update_kwargs_size_zero(self):
        sqr = Square(15, 15, 15, 15)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sqr.update(size=0)

    def test_update_kwargs_size_negative(self):
        sqr = Square(15, 15, 15, 15)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sqr.update(size=-5)

    def test_update_kwargs_str_x(self):
        sqr = Square(15, 15, 15, 15)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sqr.update(x="twelve")

    def test_update_kwargs_x_negative(self):
        sqr = Square(15, 15, 15, 15)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            sqr.update(x=-3)

    def test_update_kwargs_str_y(self):
        sqr = Square(15, 15, 15, 15)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sqr.update(y="thirteen")

    def test_update_kwargs_y_negative(self):
        sqr = Square(15, 15, 15, 15)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            sqr.update(y=-12)

    def test_update_args_and_kwargs(self):
        sqr = Square(15, 15, 15, 15)
        sqr.update(9, 4, y=12)
        self.assertEqual("[Square] (9) 15/15 - 4", str(sqr))

    def test_update_kwargs_wrong_keys(self):
        sqr = Square(15, 15, 15, 15)
        sqr.update(a=3, b=6)
        self.assertEqual("[Square] (15) 15/15 - 15", str(sqr))


class TestSquare_to_dictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Square class."""

    def test_to_dictionary_output(self):
        sqr = Square(25, 2, 5, 3)
        expect = {'id': 3, 'x': 2, 'size': 25, 'y': 5}
        self.assertDictEqual(expect, sqr.to_dictionary())

    def test_to_dictionary_one_arg(self):
        sqr = Square(15, 15, 15, 15)
        with self.assertRaises(TypeError):
            sqr.to_dictionary(8)
