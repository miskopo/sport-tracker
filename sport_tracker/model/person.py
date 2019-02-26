from sport_tracker.common.exceptions import IllegalArgumentException


class Person:

    def __init__(self):
        self._name = None
        self._age = 0
        self._weight = 0
        self._height = 0
        self._activity_level = 1  # default value 1, range 1 - 5


    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def weight(self):
        return self._weight

    @property
    def height(self):
        return self._height

    @property
    def activity_level(self):
        return self._activity_level

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value.capitalize()
        else:
            raise TypeError("Name must be string.")

    @age.setter
    def age(self, value):
        if isinstance(value, int):
            if 0 < value < 150:
                self._age = value
            else:
                raise IllegalArgumentException("Your age must fall in interval 1 - 149.")
        else:
            raise TypeError("Age must be a number.")

    @weight.setter
    def weight(self, value):
        if isinstance(value, int):
            if 0 < value < 250:
                self._age = value
            else:
                raise IllegalArgumentException("Your weight must fall in interval 1 - 249.")
        else:
            raise TypeError("Weight must be a number.")

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if 70 < value < 250:
                self._height = value
            else:
                raise IllegalArgumentException("Your height must fall in interval 71 - 249.")
        else:
            raise TypeError("Height must be a number.")

    @activity_level.setter
    def activity_level(self, value):
        if isinstance(value, int):
            if 1 <= value <= 5:
                self._activity_level = value
            else:
                raise IllegalArgumentException("Your activity level must fall in interval 1 - 5.")
        else:
            raise TypeError("Activity level must be a number.")
