# Generated from .\pythonparser.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .pythonparserParser import pythonparserParser
else:
    from pythonparserParser import pythonparserParser

# This class defines a complete listener for a parse tree produced by pythonparserParser.
class pythonparserListener(ParseTreeListener):

    # Enter a parse tree produced by pythonparserParser#start.
    def enterStart(self, ctx:pythonparserParser.StartContext):
        pass

    # Exit a parse tree produced by pythonparserParser#start.
    def exitStart(self, ctx:pythonparserParser.StartContext):
        pass


    # Enter a parse tree produced by pythonparserParser#variable.
    def enterVariable(self, ctx:pythonparserParser.VariableContext):
        pass

    # Exit a parse tree produced by pythonparserParser#variable.
    def exitVariable(self, ctx:pythonparserParser.VariableContext):
        pass


    # Enter a parse tree produced by pythonparserParser#conditional.
    def enterConditional(self, ctx:pythonparserParser.ConditionalContext):
        pass

    # Exit a parse tree produced by pythonparserParser#conditional.
    def exitConditional(self, ctx:pythonparserParser.ConditionalContext):
        pass


    # Enter a parse tree produced by pythonparserParser#ifblocks.
    def enterIfblocks(self, ctx:pythonparserParser.IfblocksContext):
        pass

    # Exit a parse tree produced by pythonparserParser#ifblocks.
    def exitIfblocks(self, ctx:pythonparserParser.IfblocksContext):
        pass


    # Enter a parse tree produced by pythonparserParser#block.
    def enterBlock(self, ctx:pythonparserParser.BlockContext):
        pass

    # Exit a parse tree produced by pythonparserParser#block.
    def exitBlock(self, ctx:pythonparserParser.BlockContext):
        pass



del pythonparserParser