import os
import inspect
from unittest import TestCase
from antlr4 import ParseTreeWalker, CommonTokenStream, FileStream
from ..parser.PrismTemplateLexer import PrismTemplateLexer
from ..parser.PrismTemplateParser import PrismTemplateParser
from ..parser.listeners import PrismReplacementsGatherer, PrismErrorListener


class TestTemplateParser(TestCase):

    def test_create_tree(self):
        path = os.path.abspath(inspect.getsourcefile(lambda: 0))
        path = os.path.dirname(path)
        input_stream = FileStream("{}/resources/test_model.prism".format(path))
        lexer = PrismTemplateLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = PrismTemplateParser(stream)

        error_listener = PrismErrorListener()
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)

        parser.program()

        self.assertTrue(len(error_listener.msg_list) == 0)

    def test_replacements_parsing(self):
        path = os.path.abspath(inspect.getsourcefile(lambda: 0))
        path = os.path.dirname(path)
        input_stream = FileStream("{}/resources/test_template.prism".format(path))
        lexer = PrismTemplateLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = PrismTemplateParser(stream)
        tree = parser.program()

        listener = PrismReplacementsGatherer()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        self.assertTrue("move" in listener.replacements)
        self.assertTrue("max_x" in listener.replacements)
        self.assertTrue("max_y" in listener.replacements)
        self.assertTrue("max_direction" in listener.replacements)
