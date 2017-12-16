from unittest import TestCase
from copy import deepcopy
from ..expression import *
from ..expression_builder import *
from ...base_expression import *


class TestExpressionBuilder(TestCase):
    def test_ariphmetic_expression(self):
        result = "(a + b - c) * 77 / d"

        builder = ExpressionBuilder(Identifier("a"))
        builder.append_add(Identifier("b"))
        builder.append_subtract(Identifier("c"))
        builder.wrap_paranthesis()
        builder.append_multiply(Integer(77))
        builder.append_divide(Identifier("d"))

        self.assertEqual(builder.build(), result)

    def test_logic_expression_with_deep_copy(self):
        result = "((true & x | y) => !z) & false"

        builder = ExpressionBuilder(Bool.true())
        builder.append_and(Identifier("x"))
        builder.append_or(Identifier("y"))
        builder.wrap_paranthesis()

        z_builder = ExpressionBuilder(Identifier("z"))
        z_builder.append_not()

        builder.append_imply(deepcopy(z_builder.expression))
        builder.wrap_paranthesis()
        builder.append_and(Bool.false())

        self.assertEqual(builder.build(), result)

    def test_comparison_expression(self):
        result = "((a = b) < c > d) <= a >= b"

        builder = ExpressionBuilder(Identifier("a"))
        builder.append_eq(Identifier("b"))
        builder.wrap_paranthesis()
        builder.append_lt(Identifier("c"))
        builder.append_gt(Identifier("d"))
        builder.wrap_paranthesis()
        builder.append_le(Identifier("a"))
        builder.append_ge(Identifier("b"))

        self.assertEqual(builder.build(), result)

    def test_next(self):
        result = "(a + b)'"

        builder = ExpressionBuilder(Identifier("a"))
        builder.append_add(Identifier("b"))
        builder.wrap_paranthesis()
        builder.wrap_next()

        self.assertEqual(builder.build(), result)

    def test_multiline_expression(self):
        result = "x => y\n | z"

        builder = ExpressionBuilder(Identifier("x"))
        builder.append_imply(Identifier("y"))
        builder.append_newline()
        builder.append_or(Identifier("z"))

        self.assertEqual(builder.build(), result)

    def test_temporal_logic_expression(self):
        result = "x = 5 & y = 5 & E[G(x > y => A[F(x = y)])]"

        builder = ExpressionBuilder(Identifier("x"))
        builder.append_eq(Integer(5))
        y_builder = ExpressionBuilder(Identifier("y"))
        y_builder.append_eq(Integer(5))
        builder.append_and(y_builder.expression)
        af_builder = ExpressionBuilder(Identifier("x"))
        af_builder.append_eq(Identifier("y"))
        af_builder.wrap_tl_eventually()
        af_builder.wrap_tl_always()
        eg_builder = ExpressionBuilder(Identifier("x"))
        eg_builder.append_gt(Identifier("y"))
        eg_builder.append_imply(af_builder.expression)
        eg_builder.wrap_tl_globally()
        eg_builder.wrap_tl_exist()
        builder.append_and(eg_builder.expression)

        self.assertEqual(builder.build(), result)


class TestUpdateBuilder(TestCase):

    def test_single_update(self):
        result = "(x' = x + y)"

        builder = ExpressionBuilder(Identifier("x"))
        builder.append_add(Identifier("y"))
        update = UpdateBuilder(Identifier("x"), builder.expression)

        self.assertEqual(update.build(), result)

    def test_multiple_update(self):
        result = "(x' = x + y) & (y' = x * x + z * z) & (z' = x / y)"

        builder1 = ExpressionBuilder(Identifier("x"))
        builder1.append_add(Identifier("y"))

        update = UpdateBuilder(Identifier("x"), builder1.expression)

        builder2 = ExpressionBuilder(Identifier("x"))
        builder2.append_multiply(Identifier("x"))
        z_builder = ExpressionBuilder(Identifier("z"))
        z_builder.append_multiply(Identifier("z"))
        builder2.append_add(z_builder.expression)

        update.add_update(Identifier("y"), builder2.expression)

        builder3 = ExpressionBuilder(Identifier("x"))
        builder3.append_divide(Identifier("y"))

        update.add_update(Identifier("z"), builder3.expression)

        self.assertEqual(update.build(), result)


class TestGuardBuilder(TestCase):

    def test_empty_label(self):
        result = "[] x > y -> (x' = x + 1);"

        guard_builder = GuardBuilder("")

        condition_builder = ExpressionBuilder(Identifier("x"))
        condition_builder.append_gt(Identifier("y"))

        x_builder = ExpressionBuilder(Identifier("x"))
        x_builder.append_add(Integer(1))
        update_builder = UpdateBuilder(Identifier("x"), x_builder.expression)

        guard_builder.add_guard(condition_builder.expression, update_builder.expression)

        self.assertEqual(guard_builder.build(), result)

    def test_nonempty_label(self):
        result = "[move] (x > y) & (z < x + y) -> (x' = y + z) & (z' = x * z) & (y' = x - y);"

        guard_builder = GuardBuilder("move")

        condition_builder = ExpressionBuilder(Identifier("x"))
        condition_builder.append_gt(Identifier("y"))
        condition_builder.wrap_paranthesis()
        x_builder = ExpressionBuilder(Identifier("x"))
        x_builder.append_add(Identifier("y"))
        z_builder = ExpressionBuilder(Identifier("z"))
        z_builder.append_lt(x_builder.expression)
        z_builder.wrap_paranthesis()
        condition_builder.append_and(z_builder.expression)

        x_builder = ExpressionBuilder(Identifier("y"))
        x_builder.append_add(Identifier("z"))

        update_builder = UpdateBuilder(Identifier("x"), x_builder.expression)

        z_builder = ExpressionBuilder(Identifier("x"))
        z_builder.append_multiply(Identifier("z"))

        update_builder.add_update(Identifier("z"), z_builder.expression)

        y_builder = ExpressionBuilder(Identifier("x"))
        y_builder.append_subtract(Identifier("y"))

        update_builder.add_update(Identifier("y"), y_builder.expression)

        guard_builder.add_guard(condition_builder.expression, update_builder.expression)

        self.assertEqual(guard_builder.build(), result)

    def test_update_without_changes(self):
        result = "[no_change] y < z -> true;"

        guard_builder = GuardBuilder("no_change")

        condition_builder = ExpressionBuilder(Identifier("y"))
        condition_builder.append_lt(Identifier("z"))

        guard_builder.add_guard(condition_builder.expression, Bool(True))

        self.assertEqual(guard_builder.build(), result)

    def test_multiline_guard(self):
        result = "[] x > y -> (x' = x + 1);\n[] y < z -> true;"

        guard_builder = GuardBuilder("")

        condition_builder = ExpressionBuilder(Identifier("x"))
        condition_builder.append_gt(Identifier("y"))

        x_builder = ExpressionBuilder(Identifier("x"))
        x_builder.append_add(Integer(1))
        update_builder = UpdateBuilder(Identifier("x"), x_builder.expression)

        guard_builder.add_guard(condition_builder.expression, update_builder.expression)

        condition_builder = ExpressionBuilder(Identifier("y"))
        condition_builder.append_lt(Identifier("z"))

        guard_builder.add_guard(condition_builder.expression, Bool(True))

        self.assertEqual(guard_builder.build(), result)
