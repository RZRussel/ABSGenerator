from unittest import TestCase
from ..base_expression import *

class TestBaseExpression(TestCase):

    def test_integer(self):
        result = "10"

        self.assertEqual(str(Integer(10)), result)

    def test_identifier(self):
        result = "_identifier10"

        self.assertEqual(str(Identifier("_identifier10")), result)

    def test_unary_operation(self):
        result = "!x"

        unary = UnaryOperation("!", Identifier("x"))

        self.assertEqual(str(unary), result)

    def test_binary_operation(self):
        result = "x + y"

        binary_operation = BinaryOperation("+", Identifier("x"), Identifier("y"))

        self.assertEqual(str(binary_operation), result)

    def test_function(self):
        result = "func(x, y)"

        func = Function("func", Identifier("x"), Identifier("y"))

        self.assertEqual(str(func), result)

    def test_paranthesis(self):
        result = "(x + y)"

        paranthesis = Paranthesis(Identifier("x + y"))

        self.assertEqual(str(paranthesis), result)

    def test_bracket(self):
        result = "[label]"

        brackets = Brackets(Identifier("label"))

        self.assertEqual(str(brackets), result)

    def test_newline(self):
        result = "some_id\n"

        newline = Newline(Identifier("some_id"))

        self.assertEqual(str(newline), result)