from unittest import TestCase
from ..expression import *
from ...base_expression import *


class TestRangeExpression(TestCase):

    def test_expression_range(self):
        range_expr = Range(Integer(0), Integer(10))
        self.assertEqual(str(range_expr), "[0..10]")

    def test_built_in_range(self):
        range_expr = Range.from_range(range(0, 11))
        self.assertEqual(str(range_expr), "[0..10]")


class TestBoolExpression(TestCase):

    def test_true(self):
        bool_expr = Bool(True)
        self.assertEqual(str(bool_expr), "true")

    def test_false(self):
        bool_expr = Bool(False)
        self.assertEqual(str(bool_expr), "false")
