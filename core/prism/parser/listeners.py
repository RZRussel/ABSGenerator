from antlr4.error.ErrorListener import ErrorListener
from .PrismTemplateListener import PrismTemplateListener
from .PrismTemplateParser import PrismTemplateParser


class PrismReplacementsGatherer(PrismTemplateListener):
    replacements = []

    def exitReplacement(self, ctx: PrismTemplateParser.ReplacementContext):
        self.replacements.append(ctx.identifier().getText())


class PrismErrorListener(ErrorListener):
    _msg_list = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self._msg_list.append(msg)

    @property
    def msg_list(self):
        return self._msg_list
