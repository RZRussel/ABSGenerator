# Generated from PrismTemplate.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PrismTemplateParser import PrismTemplateParser
else:
    from PrismTemplateParser import PrismTemplateParser

# This class defines a complete generic visitor for a parse tree produced by PrismTemplateParser.

class PrismTemplateVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PrismTemplateParser#expression.
    def visitExpression(self, ctx:PrismTemplateParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismTemplateParser#identifier.
    def visitIdentifier(self, ctx:PrismTemplateParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismTemplateParser#identifier_prime.
    def visitIdentifier_prime(self, ctx:PrismTemplateParser.Identifier_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismTemplateParser#native_type.
    def visitNative_type(self, ctx:PrismTemplateParser.Native_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismTemplateParser#program.
    def visitProgram(self, ctx:PrismTemplateParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismTemplateParser#statements.
    def visitStatements(self, ctx:PrismTemplateParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismTemplateParser#model_type.
    def visitModel_type(self, ctx:PrismTemplateParser.Model_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismTemplateParser#common_declarations.
    def visitCommon_declarations(self, ctx:PrismTemplateParser.Common_declarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismTemplateParser#common_declaration.
    def visitCommon_declaration(self, ctx:PrismTemplateParser.Common_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismTemplateParser#constant_declaration.
    def visitConstant_declaration(self, ctx:PrismTemplateParser.Constant_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismTemplateParser#formula_declaration.
    def visitFormula_declaration(self, ctx:PrismTemplateParser.Formula_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismTemplateParser#expr_or_replacement.
    def visitExpr_or_replacement(self, ctx:PrismTemplateParser.Expr_or_replacementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismTemplateParser#global_declaration.
    def visitGlobal_declaration(self, ctx:PrismTemplateParser.Global_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismTemplateParser#init_declaration.
    def visitInit_declaration(self, ctx:PrismTemplateParser.Init_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismTemplateParser#module_declarations.
    def visitModule_declarations(self, ctx:PrismTemplateParser.Module_declarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismTemplateParser#module_declaration.
    def visitModule_declaration(self, ctx:PrismTemplateParser.Module_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismTemplateParser#module_content.
    def visitModule_content(self, ctx:PrismTemplateParser.Module_contentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismTemplateParser#module_rename.
    def visitModule_rename(self, ctx:PrismTemplateParser.Module_renameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismTemplateParser#id_assign.
    def visitId_assign(self, ctx:PrismTemplateParser.Id_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismTemplateParser#id_assign_block.
    def visitId_assign_block(self, ctx:PrismTemplateParser.Id_assign_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismTemplateParser#module_desc.
    def visitModule_desc(self, ctx:PrismTemplateParser.Module_descContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismTemplateParser#var_declarations.
    def visitVar_declarations(self, ctx:PrismTemplateParser.Var_declarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismTemplateParser#var_declaration.
    def visitVar_declaration(self, ctx:PrismTemplateParser.Var_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismTemplateParser#range_declaration.
    def visitRange_declaration(self, ctx:PrismTemplateParser.Range_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismTemplateParser#guard_declarations.
    def visitGuard_declarations(self, ctx:PrismTemplateParser.Guard_declarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismTemplateParser#guard_declaration.
    def visitGuard_declaration(self, ctx:PrismTemplateParser.Guard_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismTemplateParser#guard_updates.
    def visitGuard_updates(self, ctx:PrismTemplateParser.Guard_updatesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismTemplateParser#guard_update.
    def visitGuard_update(self, ctx:PrismTemplateParser.Guard_updateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismTemplateParser#state_updates.
    def visitState_updates(self, ctx:PrismTemplateParser.State_updatesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismTemplateParser#state_update.
    def visitState_update(self, ctx:PrismTemplateParser.State_updateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismTemplateParser#no_change.
    def visitNo_change(self, ctx:PrismTemplateParser.No_changeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrismTemplateParser#replacement.
    def visitReplacement(self, ctx:PrismTemplateParser.ReplacementContext):
        return self.visitChildren(ctx)



del PrismTemplateParser