"""
Classes are responsible for storing expression data and expression strings generation
"""


class Integer:
    def __init__(self, value):
        if type(value) != int:
            raise TypeError("Integer value expected")

        self.value = value

    def __str__(self):
        return str(self.value)


class Identifier:
    def __init__(self, identifier):
        if type(identifier) != str:
            raise TypeError("String identifier expected")

        if len(identifier) == 0:
            raise Exception("Identifier string must not be empty")

        self.identifier = identifier

    def __str__(self):
        return self.identifier


class UnaryOperation:
    def __init__(self, symbol, argument):
        if type(symbol) != str:
            raise TypeError("String unary operation symbol expected")

        if len(symbol) == 0:
            raise Exception("Unary operation symbol string must not be empty")

        self.symbol = symbol
        self.argument = argument

    def __str__(self):
        return self.symbol + str(self.argument)


class BinaryOperation:
    def __init__(self, symbol, left, right):
        if type(symbol) != str:
            raise TypeError("String binary operation symbol expected")

        if len(symbol) == 0:
            raise Exception("Binary operation symbol string must not be empty")

        self.symbol = symbol
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.left) + ' ' + self.symbol + ' ' + str(self.right)


class Function:
    def __init__(self, name, *arguments):
        if type(name) != str:
            raise TypeError("String function name expected")

        if len(name) == 0:
            raise Exception("Function name must not be empty")

        self.name = name
        self.arguments = arguments

    def __str__(self):
        return self.name + '(' + ', '.join(list(map(lambda exp: str(exp), list(self.arguments)))) + ')'


class Paranthesis:
    def __init__(self, expression):
        if expression is None:
            raise TypeError("Unexpected none expression inside paranthesis")

        self.expression = expression

    def __str__(self):
        return '('+str(self.expression)+')'


class Brackets:
    def __init__(self, expression):
        if expression is None:
            raise TypeError("Unexpected none expression inside paranthesis")

        self.expression = expression

    def __str__(self):
        return '['+str(self.expression)+']'


class Newline:
    def __init__(self, expression):
        self.expression = expression

    def __str__(self):
        return str(self.expression) + "\n"
