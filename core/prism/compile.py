from typing import Any
from antlr4 import CommonTokenStream, FileStream
from .parser.PrismTemplateParser import PrismTemplateParser
from .parser.PrismTemplateVisitor import PrismTemplateVisitor
from .program import *
from .expression import *
from .expression_builder import *


class Compiler(PrismTemplateVisitor):
    def __init__(self, generator: Any, template_path: str):
        self._generator = generator
        self._template_path = template_path

    def compile(self) -> Program:

        input_stream = FileStream(self._template_path)
        lexer = PrismTemplateLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = PrismTemplateParser(stream)

        return self.visit(parser.program())

    def visitProgram(self, ctx: PrismTemplateParser.ProgramContext):
        return self.visit(ctx.statements())

    def visitStatements(self, ctx: PrismTemplateParser.StatementsContext):
        model_node = ctx.model_type()
        common_node = ctx.common_declarations()
        modules_node = ctx.module_declarations()
        init_node = ctx.init_declaration()

        model = None
        common_declarations = None
        init_declaration = None

        if model_node is not None:
            model = self.visit(model_node)

        if common_node is not None:
            common_declarations = self.visit(common_node)

        module_declarations = self.visit(modules_node)

        if init_node is not None:
            init_declaration = self.visit(init_node)

        return Program(model, common_declarations, module_declarations, init_declaration)

    def visitModel_type(self, ctx: PrismTemplateParser.Model_typeContext):
        return Model(ctx.getText())

    def visitCommon_declarations(self, ctx: PrismTemplateParser.Common_declarationsContext):
        common_declaration = self.visit(ctx.common_declaration())

        common_declarations_node = ctx.common_declarations()
        if common_declarations_node is not None:
            return [common_declaration] + self.visit(common_declarations_node)
        else:
            return [common_declaration]

    def visitCommon_declaration(self, ctx: PrismTemplateParser.Common_declarationContext):
        global_node = ctx.global_declaration()
        const_node = ctx.constant_declaration()
        formula_node = ctx.formula_declaration()

        if global_node is not None:
            return self.visit(global_node)
        elif const_node is not None:
            return self.visit(const_node)
        else:
            return self.visit(formula_node)

    def visitGlobal_declaration(self, ctx: PrismTemplateParser.Global_declarationContext):
        var = self.visit(ctx.var_declaration())
        return GlobalVarDeclaration(var)

    def visitConstant_declaration(self, ctx: PrismTemplateParser.Constant_declarationContext):
        const_type = self.visit(ctx.native_type())
        name = self.visit(ctx.identifier())
        expr = self.visit(ctx.expr_or_replacement())

        return Constant(const_type, name, expr)

    def visitExpr_or_replacement(self, ctx: PrismTemplateParser.Expr_or_replacementContext):
        replacement_node = ctx.replacement()
        expr_node = ctx.expression()

        if replacement_node is not None:
            return self.visit(replacement_node)
        else:
            return self.visit(expr_node)

    def visitFormula_declaration(self, ctx: PrismTemplateParser.Formula_declarationContext):
        name = self.visit(ctx.identifier())
        expr = self.visit(ctx.expr_or_replacement())

        return Formula(name, expr)

    def visitInit_declaration(self, ctx: PrismTemplateParser.Init_declarationContext):
        expr = self.visit(ctx.expression())

        return Init(expr)

    def visitModule_declarations(self, ctx: PrismTemplateParser.Module_declarationsContext):
        module_declaration = self.visit(ctx.module_declaration())
        module_declarations_node = ctx.module_declarations()

        if module_declarations_node is not None:
            return [module_declaration] + self.visit(module_declarations_node)
        else:
            return [module_declaration]

    def visitModule_declaration(self, ctx: PrismTemplateParser.Module_declarationContext):
        return self.visit(ctx.module_content())

    def visitModule_content(self, ctx: PrismTemplateParser.Module_contentContext):
        rename_node = ctx.module_rename()

        if rename_node is not None:
            return self.visit(rename_node)
        else:
            name = self.visit(ctx.identifier())
            vars_list, guards_list = self.visit(ctx.module_desc())

            return ModuleDesc(name, vars_list, guards_list)

    def visitModule_rename(self, ctx: PrismTemplateParser.Module_renameContext):
        rename_assign = self.visit(ctx.id_assign())
        assign_block_node = ctx.id_assign_block()

        if assign_block_node is not None:
            assigns = [rename_assign] + self.visit(assign_block_node)
            return ModuleRename(assigns)
        else:
            return ModuleRename([rename_assign])

    def visitModule_desc(self, ctx: PrismTemplateParser.Module_descContext):
        vars_node = ctx.var_declarations()
        guards_node = ctx.guard_declarations()

        vars_list = []
        guards_list = []

        if vars_node is not None:
            vars_list = self.visit(vars_node)

        if guards_node is not None:
            guards_list = self.visit(guards_node)

        return vars_list, guards_list

    def visitId_assign(self, ctx: PrismTemplateParser.Id_assignContext):
        return Identifier(ctx.getText())

    def visitId_assign_block(self, ctx: PrismTemplateParser.Id_assign_blockContext):
        assigns = []
        for child in ctx.children:
            if isinstance(child, PrismTemplateParser.Id_assignContext):
                assigns.append(self.visit(child))

        return assigns

    def visitVar_declarations(self, ctx: PrismTemplateParser.Var_declarationsContext):
        var_declaration = self.visit(ctx.var_declaration())
        var_declarations_node = ctx.var_declarations()

        if var_declarations_node is not None:
            return [var_declaration] + self.visit(var_declarations_node)
        else:
            return [var_declaration]

    def visitVar_declaration(self, ctx: PrismTemplateParser.Var_declarationContext):
        name = self.visit(ctx.identifier())
        native_type_node = ctx.native_type()

        if native_type_node is not None:
            native_type = self.visit(native_type_node)
            return VarDeclaration(name, native_type)
        else:
            range_type = self.visit(ctx.range_declaration())
            return VarDeclaration(name, range_type)

    def visitNative_type(self, ctx: PrismTemplateParser.Native_typeContext):
        return Identifier(ctx.getText())

    def visitRange_declaration(self, ctx: PrismTemplateParser.Range_declarationContext):
        left_expr = self.visit(ctx.expression(0))
        right_expr = self.visit(ctx.expression(1))

        return Range(left_expr, right_expr)

    def visitGuard_declarations(self, ctx: PrismTemplateParser.Guard_declarationsContext):
        guard_node = ctx.guard_declaration()
        replacement_node = ctx.replacement()

        if guard_node is not None:
            guard = self.visit(guard_node)
        else:
            guard = self.visit(replacement_node)

        guards_node = ctx.guard_declarations()

        if guards_node is not None:
            return [guard] + self.visit(guards_node)
        else:
            return [guard]

    def visitGuard_declaration(self, ctx: PrismTemplateParser.Guard_declarationContext):
        label_node = ctx.identifier()

        if label_node is not None:
            label = self.visit(label_node)
        else:
            label = None

        condition = self.visit(ctx.expression())

        state_updates_node = ctx.state_updates()
        guard_updates_node = ctx.guard_updates()
        no_change_node = ctx.no_change()

        if state_updates_node is not None:
            updates = self.visit(state_updates_node)
        elif guard_updates_node is not None:
            updates = self.visit(guard_updates_node)
        else:
            updates = [self.visit(no_change_node)]

        return GuardDeclaration(label, condition, updates)

    def visitGuard_updates(self, ctx: PrismTemplateParser.Guard_updatesContext):
        guard_update = self.visit(ctx.guard_update())
        guard_updates_node = ctx.guard_updates()

        if guard_updates_node is not None:
            return [guard_update] + guard_updates_node
        else:
            return [guard_update]

    def visitGuard_update(self, ctx: PrismTemplateParser.Guard_updateContext):
        expr = self.visit(ctx.expression())
        state_updates = self.visit(ctx.state_updates())

        return GuardUpdate(expr, state_updates)

    def visitState_updates(self, ctx: PrismTemplateParser.State_updatesContext):
        state_update = self.visit(ctx.state_update())
        state_updates = ctx.state_updates()

        if state_updates is not None:
            return [state_update] + self.visit(state_updates)
        else:
            return [state_update]

    def visitState_update(self, ctx: PrismTemplateParser.State_updateContext):
        identifier = self.visit(ctx.identifier_prime())
        expr = self.visit(ctx.expression())

        return StateUpdate(identifier, expr)

    def visitNo_change(self, ctx: PrismTemplateParser.No_changeContext):
        return Bool(True)

    def visitReplacement(self, ctx: PrismTemplateParser.ReplacementContext):
        method = ctx.identifier().getText()
        code = getattr(self._generator, method)()

        return Identifier(str(code))

    def visitIdentifier(self, ctx: PrismTemplateParser.IdentifierContext):
        return Identifier(ctx.getText())

    def visitIdentifier_prime(self, ctx: PrismTemplateParser.Identifier_primeContext):
        return Identifier(ctx.getText())

    def visitExpression(self, ctx: PrismTemplateParser.ExpressionContext):

        if ctx.LPARENTH() is not None and ctx.RPARENTH() is not None:
            expr = self.visit(ctx.expression(0))
            builder = ExpressionBuilder(expr)
            builder.wrap_paranthesis()
            return builder.expression
        elif ctx.IMPLIES() is not None:
            expr1 = self.visit(ctx.expression(0))
            expr2 = self.visit(ctx.expression(1))

            builder = ExpressionBuilder(expr1)
            builder.append_imply(expr2)
            return builder.expression

        elif ctx.IFF() is not None:
            expr1 = self.visit(ctx.expression(0))
            expr2 = self.visit(ctx.expression(1))

            builder = ExpressionBuilder(expr1)
            builder.append_iff(expr2)
            return builder.expression

        elif ctx.OR() is not None:
            expr1 = self.visit(ctx.expression(0))
            expr2 = self.visit(ctx.expression(1))

            builder = ExpressionBuilder(expr1)
            builder.append_or(expr2)
            return builder.expression

        elif ctx.AND() is not None:
            expr1 = self.visit(ctx.expression(0))
            expr2 = self.visit(ctx.expression(1))

            builder = ExpressionBuilder(expr1)
            builder.append_and(expr2)
            return builder.expression

        elif ctx.NOT() is not None:
            expr = self.visit(ctx.expression(0))

            builder = ExpressionBuilder(expr)
            builder.append_not()
            return builder.expression

        elif ctx.EQ() is not None:
            expr1 = self.visit(ctx.expression(0))
            expr2 = self.visit(ctx.expression(1))

            builder = ExpressionBuilder(expr1)
            builder.append_eq(expr2)
            return builder.expression

        elif ctx.NE() is not None:
            expr1 = self.visit(ctx.expression(0))
            expr2 = self.visit(ctx.expression(1))

            builder = ExpressionBuilder(expr1)
            builder.append_neq(expr2)
            return builder.expression

        elif ctx.LT() is not None:
            expr1 = self.visit(ctx.expression(0))
            expr2 = self.visit(ctx.expression(1))

            builder = ExpressionBuilder(expr1)
            builder.append_lt(expr2)
            return builder.expression

        elif ctx.LE() is not None:
            expr1 = self.visit(ctx.expression(0))
            expr2 = self.visit(ctx.expression(1))

            builder = ExpressionBuilder(expr1)
            builder.append_le(expr2)
            return builder.expression

        elif ctx.GT() is not None:
            expr1 = self.visit(ctx.expression(0))
            expr2 = self.visit(ctx.expression(1))

            builder = ExpressionBuilder(expr1)
            builder.append_gt(expr2)
            return builder.expression

        elif ctx.GE() is not None:
            expr1 = self.visit(ctx.expression(0))
            expr2 = self.visit(ctx.expression(1))

            builder = ExpressionBuilder(expr1)
            builder.append_ge(expr2)
            return builder.expression

        elif ctx.PLUS() is not None:
            expr1 = self.visit(ctx.expression(0))
            expr2 = self.visit(ctx.expression(1))

            builder = ExpressionBuilder(expr1)
            builder.append_add(expr2)
            return builder.expression

        elif ctx.MINUS() is not None and ctx.getChildCount() == 3:
            expr1 = self.visit(ctx.expression(0))
            expr2 = self.visit(ctx.expression(1))

            builder = ExpressionBuilder(expr1)
            builder.append_subtract(expr2)
            return builder.expression

        elif ctx.TIMES() is not None:
            expr1 = self.visit(ctx.expression(0))
            expr2 = self.visit(ctx.expression(1))

            builder = ExpressionBuilder(expr1)
            builder.append_multiply(expr2)
            return builder.expression

        elif ctx.DIVIDE() is not None:
            expr1 = self.visit(ctx.expression(0))
            expr2 = self.visit(ctx.expression(1))

            builder = ExpressionBuilder(expr1)
            builder.append_divide(expr2)
            return builder.expression

        elif ctx.MINUS() is not None:
            expr = self.visit(ctx.expression(0))

            builder = ExpressionBuilder(expr)
            builder.append_negate()
            return builder.expression

        elif ctx.getChildCount() == 1:
            return Identifier(ctx.getText())

        raise ValueError("Unexpected expression")
