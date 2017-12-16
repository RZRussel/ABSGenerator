from ..base_expression import *


class ExpressionBuilder:
    def __init__(self, expression):
        self.expression = expression

    def append_add(self, expression):
        self.expression = BinaryOperation("+", self.expression, expression)

    def append_subtract(self, expression):
        self.expression = BinaryOperation("-", self.expression, expression)

    def append_multiply(self, expression):
        self.expression = BinaryOperation("*", self.expression, expression)

    def append_divide(self, expression):
        self.expression = BinaryOperation("/", self.expression, expression)

    def append_negate(self):
        self.expression = UnaryOperation("-", self.expression)

    def append_and(self, expression):
        self.expression = BinaryOperation("&", self.expression, expression)

    def append_or(self, expression):
        self.expression = BinaryOperation("|", self.expression, expression)

    def append_not(self):
        self.expression = UnaryOperation("!", self.expression)

    def append_imply(self, expression):
        self.expression = BinaryOperation("=>", self.expression, expression)

    def append_iff(self, expression):
        self.expression = BinaryOperation("<=>", self.expression, expression)

    def wrap_tl_always(self):
        self.wrap_brackets()
        self.expression = UnaryOperation("A", self.expression)

    def wrap_tl_exist(self):
        self.wrap_brackets()
        self.expression = UnaryOperation("E", self.expression)

    def wrap_tl_globally(self):
        self.wrap_paranthesis()
        self.expression = UnaryOperation("G", self.expression)

    def wrap_tl_eventually(self):
        self.wrap_paranthesis()
        self.expression = UnaryOperation("F", self.expression)

    def wrap_tl_next(self):
        self.wrap_paranthesis()
        self.expression = UnaryOperation("X", self.expression)

    def wrap_next(self):
        self.expression = Identifier("{}\'".format(str(self.expression)))

    def wrap_paranthesis(self):
        self.expression = Paranthesis(self.expression)

    def wrap_brackets(self):
        self.expression = Brackets(self.expression)

    def append_eq(self, expression):
        self.expression = BinaryOperation("=", self.expression, expression)

    def append_neq(self, expression):
        self.expression = BinaryOperation("!=", self.expression, expression)

    def append_lt(self, expression):
        self.expression = BinaryOperation("<", self.expression, expression)

    def append_le(self, expression):
        self.expression = BinaryOperation("<=", self.expression, expression)

    def append_gt(self, expression):
        self.expression = BinaryOperation(">", self.expression, expression)

    def append_ge(self, expression):
        self.expression = BinaryOperation(">=", self.expression, expression)

    def append_newline(self):
        self.expression = Newline(self.expression)

    def build(self):
        return str(self.expression)


class UpdateBuilder:
    def __init__(self, identifier, value):
        expression = self._create_update_expression(identifier, value)
        self._expression_builder = ExpressionBuilder(expression)

    @property
    def expression(self):
        return self._expression_builder.expression

    def add_update(self, identifier, value):
        expression = self._create_update_expression(identifier, value)
        self._expression_builder.append_and(expression)

    def build(self):
        return self._expression_builder.build()

    @staticmethod
    def _create_update_expression(identifier, value):
        expression_builder = ExpressionBuilder(identifier)
        expression_builder.wrap_next()
        expression_builder.append_eq(value)
        expression_builder.wrap_paranthesis()

        return expression_builder.expression


class GuardBuilder:

    class Guard:
        def __init__(self, condition, update):
            self._condition = condition
            self._update = update

        @property
        def condition(self):
            return self._condition

        @property
        def update(self):
            return self._update

        def __str__(self):
            return "{} -> {};".format(str(self._condition), str(self._update))

    def __init__(self, label: str):
        self._label = label
        self._guards = []

    @property
    def label(self):
        return self._label

    @property
    def guards(self):
        return self._guards

    def add_guard(self, condition, update):
        self.guards.append(self.Guard(condition, update))

    def build(self):
        flatten_guards = list(map(lambda guard: "[{}] {}".format(self._label, str(guard)), self.guards))
        return "\n".join(flatten_guards)
