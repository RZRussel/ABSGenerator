from typing import List
from .parser.PrismTemplateLexer import PrismTemplateLexer


class BaseCode:
    @staticmethod
    def token_at(index: int):
        token = PrismTemplateLexer.literalNames[index]
        return token[1:len(token)-1]


class Program(BaseCode):
    def __init__(self, model, common_declarations, modules, init):
        self._model = model
        self._common_declarations = common_declarations
        self._modules = modules
        self._init_declaration = init

    @property
    def model(self):
        return self._model

    @property
    def common_declarations(self):
        return self._common_declarations

    @property
    def modules(self):
        return self._modules

    @property
    def init_declaration(self):
        return self._init_declaration

    def __str__(self):
        result = ""

        if self._model is not None:
            result = str(self._model)

        if self._common_declarations is not None:
            if len(result) > 0:
                result = "{}\n".format(result)

            for common_declaration in self._common_declarations:
                if len(result) > 0:
                    result = "{}\n{}".format(result, str(common_declaration))
                else:
                    result = str(common_declaration)

        if self._modules is not None:
            for module_declaration in self._modules:
                if len(result) > 0:
                    result = "{}\n\n{}".format(result, str(module_declaration))
                else:
                    result = str(module_declaration)

        if self._init_declaration is not None:
            result = "{}\n\n{}".format(result, str(self._init_declaration))

        return result


class Model(BaseCode):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def __str__(self):
        return str(self._name)


class ModuleDesc(BaseCode):
    def __init__(self, name, var_declarations, guard_declarations):
        self._name = name
        self._var_declarations = var_declarations
        self._guard_declarations = guard_declarations

    @property
    def name(self):
        return self._name

    @property
    def var_declarations(self):
        return self._var_declarations

    @property
    def guard_declarations(self):
        return self._guard_declarations

    def __str__(self):
        module_token = self.token_at(PrismTemplateLexer.MODULE)
        endmodule_token = self.token_at(PrismTemplateLexer.ENDMODULE)

        result = "{} {}".format(module_token, str(self._name))

        if self._var_declarations is not None:
            for var_declaration in self._var_declarations:
                result = "{}\n  {}".format(result, str(var_declaration))

        if self._guard_declarations is not None:
            result = "{}\n".format(result)
            for guard_declaration in self._guard_declarations:
                result = "{}\n  {}".format(result, str(guard_declaration))

        return "{}\n\n{}".format(result, endmodule_token)


class ModuleRename(BaseCode):
    def __init__(self, id_assigns: List):
        self._id_assigns = id_assigns

    @property
    def id_assigns(self):
        return self._id_assigns

    def __str__(self):
        module_token = self.token_at(PrismTemplateLexer.MODULE)
        endmodule_token = self.token_at(PrismTemplateLexer.ENDMODULE)

        result = "{} {}".format(module_token, str(self._id_assigns[0]))

        if len(self._id_assigns) > 1:
            str_assigns = list(map(lambda id_assign: str(id_assign), self._id_assigns[1:]))
            result = "{} [{}]".format(result, ", ".join(str_assigns))

        return "{}\n{}".format(result, endmodule_token)


class GlobalVarDeclaration(BaseCode):
    def __init__(self, var_declaration):
        self._var_declaration = var_declaration

    @property
    def var_declaration(self):
        return self._var_declaration

    def __str__(self):
        global_token = self.token_at(PrismTemplateLexer.GLOBAL)
        return "{} {}".format(global_token, str(self._var_declaration))


class VarDeclaration(BaseCode):
    def __init__(self, name, var_type):
        self._name = name
        self._var_type = var_type

    @property
    def name(self):
        return self._name

    @property
    def var_type(self):
        return self._var_type

    def __str__(self):
        colon_token = self.token_at(PrismTemplateLexer.COLON)
        semicolon_token = self.token_at(PrismTemplateLexer.SEMICOLON)
        return "{} {} {}{}".format(str(self._name), colon_token, str(self._var_type), semicolon_token)


class Formula(BaseCode):
    def __init__(self, name, expression):
        self._name = name
        self._expression = expression

    @property
    def name(self):
        return self._name

    @property
    def expression(self):
        return self._expression

    def __str__(self):
        eq_token = self.token_at(PrismTemplateLexer.EQ)
        semicolon_token = self.token_at(PrismTemplateLexer.SEMICOLON)
        formula_token = self.token_at(PrismTemplateLexer.FORMULA)

        return "{} {} {} {}{}".format(formula_token, str(self._name), eq_token, str(self._expression), semicolon_token)


class Constant(BaseCode):
    def __init__(self, const_type, name, expression):
        self._const_type = const_type
        self._name = name
        self._expression = expression

    @property
    def const_type(self):
        return self._const_type

    @property
    def name(self):
        return self._name

    @property
    def expression(self):
        return self._expression

    def __str__(self):
        const_token = self.token_at(PrismTemplateLexer.CONST)
        eq_token = self.token_at(PrismTemplateLexer.EQ)
        semicolon_token = self.token_at(PrismTemplateLexer.SEMICOLON)

        return "{} {} {} {} {}{}".format(const_token,
                                         str(self._const_type),
                                         str(self._name),
                                         eq_token,
                                         str(self._expression),
                                         semicolon_token)


class Init(BaseCode):
    def __init__(self, expression):
        self._expression = expression

    @property
    def expression(self):
        return self._expression

    def __str__(self):
        begin_init_token = self.token_at(PrismTemplateLexer.INIT)
        end_init_token = self.token_at(PrismTemplateLexer.ENDINIT)

        return "{}\n  {}\n{}".format(begin_init_token, str(self._expression), end_init_token)


class GuardDeclaration(BaseCode):
    def __init__(self, label, expression, updates):
        self._label = label
        self._expression = expression
        self._updates = updates

    @property
    def label(self):
        return self._label

    @property
    def expression(self):
        return self._expression

    @property
    def updates(self):
        return self._updates

    def __str__(self):
        rarrow_token = self.token_at(PrismTemplateLexer.RARROW)
        plus_token = self.token_at(PrismTemplateLexer.PLUS)
        semicolon_token = self.token_at(PrismTemplateLexer.SEMICOLON)

        if self._label is not None:
            result = "[{}]".format(str(self._label))
        else:
            result = "[]"

        result = "{} {} {}".format(result, str(self._expression), rarrow_token)

        result = "{} {}".format(result, str(self._updates[0]))
        for update in self._updates[1:]:
            result = "{} {} {}".format(result, plus_token, str(update))

        return "{}{}".format(result, semicolon_token)


class GuardUpdate(BaseCode):
    def __init__(self, expression, state_updates):
        self._expression = expression
        self._state_updates = state_updates

    @property
    def expression(self):
        return self._expression

    @property
    def state_updates(self):
        return self._state_updates

    def __str__(self):
        colon_token = self.token_at(PrismTemplateLexer.COLON)
        and_token = self.token_at(PrismTemplateLexer.AND)

        statements = list(map(lambda update: str(update), self._state_updates))
        return "{}{}{}".format(str(self._expression), colon_token, and_token.join(statements))


class StateUpdate(BaseCode):
    def __init__(self, identifier, expression):
        self._identifier = identifier
        self._expression = expression

    @property
    def identifier(self):
        return self._identifier

    @property
    def expression(self):
        return self._expression

    def __str__(self):
        eq_token = self.token_at(PrismTemplateLexer.EQ)

        return "{} {} {}".format(str(self._identifier), eq_token, str(self._expression))
