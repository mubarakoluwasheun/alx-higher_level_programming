#!/usr/bin/python3
# base.py
"""Defines a base model class."""
import json
import csv
import turtle


class Base:
    """Represent the base class.

    Represents the 'base' for all other classes in the project.

    Attributes:
        __nb_objects (int): The nu,mber of instantiated Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the class Base...

        Args:
            id (int): The identity of the Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file:.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                jsonfile.wrie(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation.

        Args:
            json_string (str): A string representing a list of dictionaries.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - return the list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set.

        Args:
            **dictionary (dict): key/value pairs of attributes to initialize.
        """
        if dictionary != {}:
            if cls.__name__ == "Rectangle":
                instance = cls(1, 1)
            if cls.__name__ == "Square":
                instance = cls(1)
            instance.update(**dictionary)
            return instance

    @classmethod
    def load_from_file(cls):
        """Return a list of instances.

        Reads from `<cls.__name__>.json`.

        Return:
            If the file does not exit - an empty list.
            Otherwise - a list of instances..
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**dic) for dic in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV seralization of a list of objects to a file.

        Args:
            list_objs (list): A list of objcets.
         """
        filename = cls.__name + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldname = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize a list of classes instantiated from a CSV file.

        Read from `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of objects.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in dic.items())
                              for dic in list_dicts]
                return [cls.create(**dic) for dic in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to drwa.
            list_squares (list): A list of Square objects to draw.
            """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()
        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.width)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turt.exitonclick()
