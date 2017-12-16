# Generated from PrismTemplate.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PrismTemplateParser import PrismTemplateParser
else:
    from PrismTemplateParser import PrismTemplateParser

# This class defines a complete listener for a parse tree produced by PrismTemplateParser.
class PrismTemplateListener(ParseTreeListener):

    # Enter a parse tree produced by PrismTemplateParser#expression.
    def enterExpression(self, ctx:PrismTemplateParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PrismTemplateParser#expression.
    def exitExpression(self, ctx:PrismTemplateParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PrismTemplateParser#identifier.
    def enterIdentifier(self, ctx:PrismTemplateParser.IdentifierContext):
        pass

    # Exit a parse tree produced by PrismTemplateParser#identifier.
    def exitIdentifier(self, ctx:PrismTemplateParser.IdentifierContext):
        pass


    # Enter a parse tree produced by PrismTemplateParser#identifier_prime.
    def enterIdentifier_prime(self, ctx:PrismTemplateParser.Identifier_primeContext):
        pass

    # Exit a parse tree produced by PrismTemplateParser#identifier_prime.
    def exitIdentifier_prime(self, ctx:PrismTemplateParser.Identifier_primeContext):
        pass


    # Enter a parse tree produced by PrismTemplateParser#native_type.
    def enterNative_type(self, ctx:PrismTemplateParser.Native_typeContext):
        pass

    # Exit a parse tree produced by PrismTemplateParser#native_type.
    def exitNative_type(self, ctx:PrismTemplateParser.Native_typeContext):
        pass


    # Enter a parse tree produced by PrismTemplateParser#program.
    def enterProgram(self, ctx:PrismTemplateParser.ProgramContext):
        pass

    # Exit a parse tree produced by PrismTemplateParser#program.
    def exitProgram(self, ctx:PrismTemplateParser.ProgramContext):
        pass


    # Enter a parse tree produced by PrismTemplateParser#statements.
    def enterStatements(self, ctx:PrismTemplateParser.StatementsContext):
        pass

    # Exit a parse tree produced by PrismTemplateParser#statements.
    def exitStatements(self, ctx:PrismTemplateParser.StatementsContext):
        pass


    # Enter a parse tree produced by PrismTemplateParser#model_type.
    def enterModel_type(self, ctx:PrismTemplateParser.Model_typeContext):
        pass

    # Exit a parse tree produced by PrismTemplateParser#model_type.
    def exitModel_type(self, ctx:PrismTemplateParser.Model_typeContext):
        pass


    # Enter a parse tree produced by PrismTemplateParser#common_declarations.
    def enterCommon_declarations(self, ctx:PrismTemplateParser.Common_declarationsContext):
        pass

    # Exit a parse tree produced by PrismTemplateParser#common_declarations.
    def exitCommon_declarations(self, ctx:PrismTemplateParser.Common_declarationsContext):
        pass


    # Enter a parse tree produced by PrismTemplateParser#common_declaration.
    def enterCommon_declaration(self, ctx:PrismTemplateParser.Common_declarationContext):
        pass

    # Exit a parse tree produced by PrismTemplateParser#common_declaration.
    def exitCommon_declaration(self, ctx:PrismTemplateParser.Common_declarationContext):
        pass


    # Enter a parse tree produced by PrismTemplateParser#constant_declaration.
    def enterConstant_declaration(self, ctx:PrismTemplateParser.Constant_declarationContext):
        pass

    # Exit a parse tree produced by PrismTemplateParser#constant_declaration.
    def exitConstant_declaration(self, ctx:PrismTemplateParser.Constant_declarationContext):
        pass


    # Enter a parse tree produced by PrismTemplateParser#formula_declaration.
    def enterFormula_declaration(self, ctx:PrismTemplateParser.Formula_declarationContext):
        pass

    # Exit a parse tree produced by PrismTemplateParser#formula_declaration.
    def exitFormula_declaration(self, ctx:PrismTemplateParser.Formula_declarationContext):
        pass


    # Enter a parse tree produced by PrismTemplateParser#expr_or_replacement.
    def enterExpr_or_replacement(self, ctx:PrismTemplateParser.Expr_or_replacementContext):
        pass

    # Exit a parse tree produced by PrismTemplateParser#expr_or_replacement.
    def exitExpr_or_replacement(self, ctx:PrismTemplateParser.Expr_or_replacementContext):
        pass


    # Enter a parse tree produced by PrismTemplateParser#global_declaration.
    def enterGlobal_declaration(self, ctx:PrismTemplateParser.Global_declarationContext):
        pass

    # Exit a parse tree produced by PrismTemplateParser#global_declaration.
    def exitGlobal_declaration(self, ctx:PrismTemplateParser.Global_declarationContext):
        pass


    # Enter a parse tree produced by PrismTemplateParser#init_declaration.
    def enterInit_declaration(self, ctx:PrismTemplateParser.Init_declarationContext):
        pass

    # Exit a parse tree produced by PrismTemplateParser#init_declaration.
    def exitInit_declaration(self, ctx:PrismTemplateParser.Init_declarationContext):
        pass


    # Enter a parse tree produced by PrismTemplateParser#module_declarations.
    def enterModule_declarations(self, ctx:PrismTemplateParser.Module_declarationsContext):
        pass

    # Exit a parse tree produced by PrismTemplateParser#module_declarations.
    def exitModule_declarations(self, ctx:PrismTemplateParser.Module_declarationsContext):
        pass


    # Enter a parse tree produced by PrismTemplateParser#module_declaration.
    def enterModule_declaration(self, ctx:PrismTemplateParser.Module_declarationContext):
        pass

    # Exit a parse tree produced by PrismTemplateParser#module_declaration.
    def exitModule_declaration(self, ctx:PrismTemplateParser.Module_declarationContext):
        pass


    # Enter a parse tree produced by PrismTemplateParser#module_content.
    def enterModule_content(self, ctx:PrismTemplateParser.Module_contentContext):
        pass

    # Exit a parse tree produced by PrismTemplateParser#module_content.
    def exitModule_content(self, ctx:PrismTemplateParser.Module_contentContext):
        pass


    # Enter a parse tree produced by PrismTemplateParser#module_rename.
    def enterModule_rename(self, ctx:PrismTemplateParser.Module_renameContext):
        pass

    # Exit a parse tree produced by PrismTemplateParser#module_rename.
    def exitModule_rename(self, ctx:PrismTemplateParser.Module_renameContext):
        pass


    # Enter a parse tree produced by PrismTemplateParser#id_assign.
    def enterId_assign(self, ctx:PrismTemplateParser.Id_assignContext):
        pass

    # Exit a parse tree produced by PrismTemplateParser#id_assign.
    def exitId_assign(self, ctx:PrismTemplateParser.Id_assignContext):
        pass


    # Enter a parse tree produced by PrismTemplateParser#id_assign_block.
    def enterId_assign_block(self, ctx:PrismTemplateParser.Id_assign_blockContext):
        pass

    # Exit a parse tree produced by PrismTemplateParser#id_assign_block.
    def exitId_assign_block(self, ctx:PrismTemplateParser.Id_assign_blockContext):
        pass


    # Enter a parse tree produced by PrismTemplateParser#module_desc.
    def enterModule_desc(self, ctx:PrismTemplateParser.Module_descContext):
        pass

    # Exit a parse tree produced by PrismTemplateParser#module_desc.
    def exitModule_desc(self, ctx:PrismTemplateParser.Module_descContext):
        pass


    # Enter a parse tree produced by PrismTemplateParser#var_declarations.
    def enterVar_declarations(self, ctx:PrismTemplateParser.Var_declarationsContext):
        pass

    # Exit a parse tree produced by PrismTemplateParser#var_declarations.
    def exitVar_declarations(self, ctx:PrismTemplateParser.Var_declarationsContext):
        pass


    # Enter a parse tree produced by PrismTemplateParser#var_declaration.
    def enterVar_declaration(self, ctx:PrismTemplateParser.Var_declarationContext):
        pass

    # Exit a parse tree produced by PrismTemplateParser#var_declaration.
    def exitVar_declaration(self, ctx:PrismTemplateParser.Var_declarationContext):
        pass


    # Enter a parse tree produced by PrismTemplateParser#range_declaration.
    def enterRange_declaration(self, ctx:PrismTemplateParser.Range_declarationContext):
        pass

    # Exit a parse tree produced by PrismTemplateParser#range_declaration.
    def exitRange_declaration(self, ctx:PrismTemplateParser.Range_declarationContext):
        pass


    # Enter a parse tree produced by PrismTemplateParser#guard_declarations.
    def enterGuard_declarations(self, ctx:PrismTemplateParser.Guard_declarationsContext):
        pass

    # Exit a parse tree produced by PrismTemplateParser#guard_declarations.
    def exitGuard_declarations(self, ctx:PrismTemplateParser.Guard_declarationsContext):
        pass


    # Enter a parse tree produced by PrismTemplateParser#guard_declaration.
    def enterGuard_declaration(self, ctx:PrismTemplateParser.Guard_declarationContext):
        pass

    # Exit a parse tree produced by PrismTemplateParser#guard_declaration.
    def exitGuard_declaration(self, ctx:PrismTemplateParser.Guard_declarationContext):
        pass


    # Enter a parse tree produced by PrismTemplateParser#guard_updates.
    def enterGuard_updates(self, ctx:PrismTemplateParser.Guard_updatesContext):
        pass

    # Exit a parse tree produced by PrismTemplateParser#guard_updates.
    def exitGuard_updates(self, ctx:PrismTemplateParser.Guard_updatesContext):
        pass


    # Enter a parse tree produced by PrismTemplateParser#guard_update.
    def enterGuard_update(self, ctx:PrismTemplateParser.Guard_updateContext):
        pass

    # Exit a parse tree produced by PrismTemplateParser#guard_update.
    def exitGuard_update(self, ctx:PrismTemplateParser.Guard_updateContext):
        pass


    # Enter a parse tree produced by PrismTemplateParser#state_updates.
    def enterState_updates(self, ctx:PrismTemplateParser.State_updatesContext):
        pass

    # Exit a parse tree produced by PrismTemplateParser#state_updates.
    def exitState_updates(self, ctx:PrismTemplateParser.State_updatesContext):
        pass


    # Enter a parse tree produced by PrismTemplateParser#state_update.
    def enterState_update(self, ctx:PrismTemplateParser.State_updateContext):
        pass

    # Exit a parse tree produced by PrismTemplateParser#state_update.
    def exitState_update(self, ctx:PrismTemplateParser.State_updateContext):
        pass


    # Enter a parse tree produced by PrismTemplateParser#no_change.
    def enterNo_change(self, ctx:PrismTemplateParser.No_changeContext):
        pass

    # Exit a parse tree produced by PrismTemplateParser#no_change.
    def exitNo_change(self, ctx:PrismTemplateParser.No_changeContext):
        pass


    # Enter a parse tree produced by PrismTemplateParser#replacement.
    def enterReplacement(self, ctx:PrismTemplateParser.ReplacementContext):
        pass

    # Exit a parse tree produced by PrismTemplateParser#replacement.
    def exitReplacement(self, ctx:PrismTemplateParser.ReplacementContext):
        pass


