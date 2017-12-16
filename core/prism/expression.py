"""
Classes represents syntax for specific prism expressions
"""


class Range:
    def __init__(self, left, right):
        self._left = left
        self._right = right

    @staticmethod
    def from_range(init_range: range):
        range_list = list(init_range)
        return Range(range_list[0], range_list[-1])

    def __str__(self):
        return "[{}..{}]".format(str(self._left), str(self._right))


class Bool:
    def __init__(self, value: bool):
        self._value = value

    @property
    def value(self):
        return self._value

    @staticmethod
    def true():
        return Bool(True)

    @staticmethod
    def false():
        return Bool(False)

    def __str__(self):
        if self._value:
            return "true"
        else:
            return "false"
