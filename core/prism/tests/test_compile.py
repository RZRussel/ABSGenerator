from unittest import TestCase
from ..compile import TaxiCompiler
from antlr4 import CommonTokenStream, InputStream
from io import StringIO
from ..parser.PrismTemplateLexer import PrismTemplateLexer
from ..parser.PrismTemplateParser import PrismTemplateParser
from ..parser.listeners import PrismErrorListener


class TestCompiler(TestCase):
    def test_compiler(self):
        pass
