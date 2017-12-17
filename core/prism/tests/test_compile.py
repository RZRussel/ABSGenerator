import os
import inspect
from unittest import TestCase
from ..compile import Compiler
from ..expression_builder import *
from ..expression import *
from antlr4 import CommonTokenStream, InputStream
from io import StringIO
from ..parser.PrismTemplateLexer import PrismTemplateLexer
from ..parser.PrismTemplateParser import PrismTemplateParser
from ..parser.listeners import PrismErrorListener


class TestCompiler(TestCase):
    class TestGenerator:
        @staticmethod
        def max_x() -> int:
            return 10

        @staticmethod
        def max_y() -> int:
            return 20

        @staticmethod
        def max_direction() -> int:
            return 360

        @staticmethod
        def move() -> str:
            condition = ExpressionBuilder(Identifier("x"))
            condition.append_gt(Integer(0))
            y_builder = ExpressionBuilder(Identifier("y"))
            y_builder.append_gt(Integer(0))
            condition.append_and(y_builder.expression)

            guard_builder = GuardBuilder("")
            guard_builder.add_guard(condition.expression, Bool(True))

            return guard_builder.build()

    def test_compiler(self):
        path = os.path.abspath(inspect.getsourcefile(lambda: 0))
        path = os.path.dirname(path)

        compiler = Compiler(self.TestGenerator(), "{}/resources/test_template.prism".format(path))

        input_stream = InputStream(str(compiler.compile()))
        output_stream = StringIO()
        lexer = PrismTemplateLexer(input_stream, output=output_stream)
        stream = CommonTokenStream(lexer)
        parser = PrismTemplateParser(stream)

        error_listener = PrismErrorListener()
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)

        parser.program()

        self.assertTrue(len(error_listener.msg_list) == 0)
