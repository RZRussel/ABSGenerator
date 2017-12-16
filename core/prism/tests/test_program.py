from unittest import TestCase
from ..program import *
from ..expression_builder import *
from ..expression import *


class TestProgram(TestCase):

    def test_base_token_at(self):
        self.assertEqual(BaseCode.token_at(PrismTemplateLexer.COLON), ":")

    def test_model(self):
        result = "mdp"

        model = Model("mdp")

        self.assertEqual(model.name, "mdp")
        self.assertEqual(str(model), result)

    def test_init(self):
        result = "init\n  x = 1 & y = 1\nendinit"

        builder = ExpressionBuilder(Identifier("x"))
        builder.append_eq(Integer(1))

        y_builder = ExpressionBuilder(Identifier("y"))
        y_builder.append_eq(Integer(1))

        builder.append_and(y_builder.expression)

        init = Init(builder.expression)

        self.assertEqual(str(init), result)

    def test_constant(self):
        result = "const int x = 1;"

        constant = Constant(BaseCode.token_at(PrismTemplateLexer.INT), Identifier("x"), Integer(1))

        self.assertEqual(str(constant), result)

    def test_formula(self):
        result = "formula my_tag = @tag@;"

        formula = Formula("my_tag", Identifier("@tag@"))

        self.assertEqual(str(formula), result)

    def test_var_declaration(self):
        result = "x : [0..10];"

        var_declaration = VarDeclaration(Identifier("x"), Range(0, 10))

        self.assertEqual(str(var_declaration), result)

    def test_global_declaration(self):
        result = "global x : int;"

        global_declaration = GlobalVarDeclaration(VarDeclaration(Identifier("x"),
                                                                 BaseCode.token_at(PrismTemplateLexer.INT)))

        self.assertEqual(str(global_declaration), result)

    def test_module_rename(self):
        result = "module Module1 = Module2 [x1 = x2, y1 = y2, z1 = z2]\nendmodule"

        assign1 = ExpressionBuilder(Identifier("Module1"))
        assign1.append_eq(Identifier("Module2"))

        assign2 = ExpressionBuilder(Identifier("x1"))
        assign2.append_eq(Identifier("x2"))

        assign3 = ExpressionBuilder(Identifier("y1"))
        assign3.append_eq(Identifier("y2"))

        assign4 = ExpressionBuilder(Identifier("z1"))
        assign4.append_eq(Identifier("z2"))

        module_rename = ModuleRename([assign1.expression, assign2.expression, assign3.expression, assign4.expression])

        self.assertEqual(str(module_rename), result)

    def test_state_update(self):
        result = "x' = z + y"

        new_x = ExpressionBuilder(Identifier("x"))
        new_x.wrap_next()

        expr = ExpressionBuilder(Identifier("z"))
        expr.append_add(Identifier("y"))

        state_update = StateUpdate(new_x.expression, expr.expression)

        self.assertEqual(str(state_update), result)

    def test_guard_update(self):
        result = "0.95:(x' = z * y)&(z' = x / y)"

        state_builder1 = ExpressionBuilder(Identifier("x"))
        state_builder1.wrap_next()
        z_builder = ExpressionBuilder(Identifier("z"))
        z_builder.append_multiply(Identifier("y"))
        state_builder1.append_eq(z_builder.expression)
        state_builder1.wrap_paranthesis()

        state_builder2 = ExpressionBuilder(Identifier("z"))
        state_builder2.wrap_next()
        x_builder = ExpressionBuilder(Identifier("x"))
        x_builder.append_divide(Identifier("y"))
        state_builder2.append_eq(x_builder.expression)
        state_builder2.wrap_paranthesis()

        guard_update = GuardUpdate(Identifier("0.95"), [state_builder1.expression, state_builder2.expression])

        self.assertEqual(str(guard_update), result)

    def test_guard_declaration(self):
        result = "[label] x < y -> 0.6:(x' = z * y) + 0.4:(z' = x + y);"

        condition = ExpressionBuilder(Identifier("x"))
        condition.append_lt(Identifier("y"))

        state_builder1 = ExpressionBuilder(Identifier("x"))
        state_builder1.wrap_next()
        z_builder = ExpressionBuilder(Identifier("z"))
        z_builder.append_multiply(Identifier("y"))
        state_builder1.append_eq(z_builder.expression)
        state_builder1.wrap_paranthesis()

        update_builder1 = GuardUpdate(Identifier("0.6"), [state_builder1.expression])

        state_builder2 = ExpressionBuilder(Identifier("z"))
        state_builder2.wrap_next()
        x_builder = ExpressionBuilder(Identifier("x"))
        x_builder.append_add(Identifier("y"))
        state_builder2.append_eq(x_builder.expression)
        state_builder2.wrap_paranthesis()

        update_builder2 = GuardUpdate(Identifier("0.4"), [state_builder2.expression])

        guard_declaration = GuardDeclaration(Identifier("label"),
                                             condition.expression,
                                             [update_builder1, update_builder2])

        self.assertEqual(str(guard_declaration), result)

    def test_module_desc(self):
        result = "module Module\n  v : int;\n\n  [label] x > y -> true;\n\nendmodule"

        var_declaration = VarDeclaration(Identifier("v"), BaseCode.token_at(PrismTemplateLexer.INT))

        condition = ExpressionBuilder(Identifier("x"))
        condition.append_gt(Identifier("y"))

        guard_declaration = GuardDeclaration(Identifier("label"), condition.expression, [Bool(True)])

        module_desc = ModuleDesc("Module", [var_declaration], [guard_declaration])

        self.assertEqual(str(module_desc), result)

    def test_program(self):
        result = "mdp\n\n\nmodule Module\n  v : [1..5];\n\n  [] x = y -> true;\n\nendmodule\n\ninit\n  v = 1\nendinit"

        model = Model(Identifier("mdp"))

        var_declaration = VarDeclaration(Identifier("v"), Range(1, 5))

        condition = ExpressionBuilder(Identifier("x"))
        condition.append_eq(Identifier("y"))

        guard_declaration = GuardDeclaration("", condition.expression, [Bool(True)])

        module_desc = ModuleDesc("Module", [var_declaration], [guard_declaration])

        x_builder = ExpressionBuilder(Identifier("v"))
        x_builder.append_eq(Integer(1))

        init = Init(x_builder.expression)

        program = Program(model, [], [module_desc], init)

        self.assertEqual(str(program), result)
