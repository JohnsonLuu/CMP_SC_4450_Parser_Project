# Generated from .\pythonparser.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,29,169,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,38,8,1,1,2,1,2,1,2,1,
        2,1,2,3,2,45,8,2,5,2,47,8,2,10,2,12,2,50,9,2,1,2,1,2,1,2,1,3,1,3,
        1,3,1,3,1,3,1,3,3,3,61,8,3,1,3,3,3,64,8,3,5,3,66,8,3,10,3,12,3,69,
        9,3,1,3,1,3,1,4,1,4,1,4,1,4,3,4,77,8,4,1,5,1,5,1,5,1,5,1,5,3,5,84,
        8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,95,8,5,10,5,12,5,98,
        9,5,1,6,1,6,3,6,102,8,6,1,6,1,6,3,6,106,8,6,1,6,1,6,1,6,1,6,1,6,
        3,6,113,8,6,1,6,1,6,3,6,117,8,6,1,6,1,6,1,6,5,6,122,8,6,10,6,12,
        6,125,9,6,1,6,1,6,1,6,3,6,130,8,6,1,7,4,7,133,8,7,11,7,12,7,134,
        1,7,3,7,138,8,7,1,7,3,7,141,8,7,1,7,3,7,144,8,7,1,8,1,8,1,8,1,8,
        1,8,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,162,
        8,10,3,10,164,8,10,1,10,1,10,1,10,1,10,0,1,10,11,0,2,4,6,8,10,12,
        14,16,18,20,0,3,2,0,18,20,25,25,1,0,6,8,2,0,18,19,25,25,190,0,25,
        1,0,0,0,2,37,1,0,0,0,4,39,1,0,0,0,6,54,1,0,0,0,8,72,1,0,0,0,10,83,
        1,0,0,0,12,99,1,0,0,0,14,140,1,0,0,0,16,145,1,0,0,0,18,150,1,0,0,
        0,20,152,1,0,0,0,22,24,3,2,1,0,23,22,1,0,0,0,24,27,1,0,0,0,25,23,
        1,0,0,0,25,26,1,0,0,0,26,28,1,0,0,0,27,25,1,0,0,0,28,29,5,0,0,1,
        29,1,1,0,0,0,30,38,3,8,4,0,31,38,3,12,6,0,32,38,3,16,8,0,33,38,3,
        18,9,0,34,38,3,20,10,0,35,38,3,4,2,0,36,38,3,6,3,0,37,30,1,0,0,0,
        37,31,1,0,0,0,37,32,1,0,0,0,37,33,1,0,0,0,37,34,1,0,0,0,37,35,1,
        0,0,0,37,36,1,0,0,0,38,3,1,0,0,0,39,40,5,1,0,0,40,41,5,18,0,0,41,
        48,5,2,0,0,42,44,5,18,0,0,43,45,5,3,0,0,44,43,1,0,0,0,44,45,1,0,
        0,0,45,47,1,0,0,0,46,42,1,0,0,0,47,50,1,0,0,0,48,46,1,0,0,0,48,49,
        1,0,0,0,49,51,1,0,0,0,50,48,1,0,0,0,51,52,5,4,0,0,52,53,3,14,7,0,
        53,5,1,0,0,0,54,55,5,18,0,0,55,67,5,2,0,0,56,61,5,18,0,0,57,61,5,
        19,0,0,58,61,5,25,0,0,59,61,3,6,3,0,60,56,1,0,0,0,60,57,1,0,0,0,
        60,58,1,0,0,0,60,59,1,0,0,0,61,63,1,0,0,0,62,64,5,3,0,0,63,62,1,
        0,0,0,63,64,1,0,0,0,64,66,1,0,0,0,65,60,1,0,0,0,66,69,1,0,0,0,67,
        65,1,0,0,0,67,68,1,0,0,0,68,70,1,0,0,0,69,67,1,0,0,0,70,71,5,5,0,
        0,71,7,1,0,0,0,72,73,5,18,0,0,73,74,5,23,0,0,74,76,7,0,0,0,75,77,
        5,26,0,0,76,75,1,0,0,0,76,77,1,0,0,0,77,9,1,0,0,0,78,79,6,5,-1,0,
        79,84,5,18,0,0,80,84,5,19,0,0,81,84,5,20,0,0,82,84,5,25,0,0,83,78,
        1,0,0,0,83,80,1,0,0,0,83,81,1,0,0,0,83,82,1,0,0,0,84,96,1,0,0,0,
        85,86,10,3,0,0,86,87,7,1,0,0,87,95,3,10,5,4,88,89,10,2,0,0,89,90,
        5,28,0,0,90,95,3,10,5,3,91,92,10,1,0,0,92,93,5,24,0,0,93,95,3,10,
        5,2,94,85,1,0,0,0,94,88,1,0,0,0,94,91,1,0,0,0,95,98,1,0,0,0,96,94,
        1,0,0,0,96,97,1,0,0,0,97,11,1,0,0,0,98,96,1,0,0,0,99,101,5,9,0,0,
        100,102,5,2,0,0,101,100,1,0,0,0,101,102,1,0,0,0,102,103,1,0,0,0,
        103,105,3,10,5,0,104,106,5,5,0,0,105,104,1,0,0,0,105,106,1,0,0,0,
        106,107,1,0,0,0,107,108,5,10,0,0,108,109,3,14,7,0,109,123,1,0,0,
        0,110,112,5,11,0,0,111,113,5,2,0,0,112,111,1,0,0,0,112,113,1,0,0,
        0,113,114,1,0,0,0,114,116,3,10,5,0,115,117,5,5,0,0,116,115,1,0,0,
        0,116,117,1,0,0,0,117,118,1,0,0,0,118,119,5,10,0,0,119,120,3,14,
        7,0,120,122,1,0,0,0,121,110,1,0,0,0,122,125,1,0,0,0,123,121,1,0,
        0,0,123,124,1,0,0,0,124,129,1,0,0,0,125,123,1,0,0,0,126,127,5,12,
        0,0,127,128,5,10,0,0,128,130,3,14,7,0,129,126,1,0,0,0,129,130,1,
        0,0,0,130,13,1,0,0,0,131,133,3,2,1,0,132,131,1,0,0,0,133,134,1,0,
        0,0,134,132,1,0,0,0,134,135,1,0,0,0,135,137,1,0,0,0,136,138,5,13,
        0,0,137,136,1,0,0,0,137,138,1,0,0,0,138,141,1,0,0,0,139,141,5,13,
        0,0,140,132,1,0,0,0,140,139,1,0,0,0,141,143,1,0,0,0,142,144,5,26,
        0,0,143,142,1,0,0,0,143,144,1,0,0,0,144,15,1,0,0,0,145,146,5,14,
        0,0,146,147,3,10,5,0,147,148,5,10,0,0,148,149,3,14,7,0,149,17,1,
        0,0,0,150,151,5,29,0,0,151,19,1,0,0,0,152,153,5,15,0,0,153,154,5,
        18,0,0,154,163,5,16,0,0,155,164,5,18,0,0,156,161,5,17,0,0,157,162,
        5,19,0,0,158,159,7,2,0,0,159,160,5,3,0,0,160,162,7,2,0,0,161,157,
        1,0,0,0,161,158,1,0,0,0,162,164,1,0,0,0,163,155,1,0,0,0,163,156,
        1,0,0,0,164,165,1,0,0,0,165,166,5,4,0,0,166,167,3,14,7,0,167,21,
        1,0,0,0,23,25,37,44,48,60,63,67,76,83,94,96,101,105,112,116,123,
        129,134,137,140,143,161,163
    ]

class pythonparserParser ( Parser ):

    grammarFileName = "pythonparser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'def'", "'('", "','", "'):'", "')'", 
                     "'and'", "'or'", "'not'", "'if'", "':'", "'elif'", 
                     "'else'", "'break'", "'while'", "'for'", "'in'", "'range('" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "VAR", "NUMBER", "STRING", 
                      "DIGIT", "LETTER", "ASSIGN_OP", "ARITH_OP", "ARITH_FUNC", 
                      "NEWLINE", "WHITE_SPACE", "COND_OP", "COMMENT" ]

    RULE_start = 0
    RULE_definitions = 1
    RULE_function = 2
    RULE_functioncall = 3
    RULE_variable = 4
    RULE_conditional = 5
    RULE_ifblocks = 6
    RULE_block = 7
    RULE_whileloop = 8
    RULE_comment = 9
    RULE_forloop = 10

    ruleNames =  [ "start", "definitions", "function", "functioncall", "variable", 
                   "conditional", "ifblocks", "block", "whileloop", "comment", 
                   "forloop" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    VAR=18
    NUMBER=19
    STRING=20
    DIGIT=21
    LETTER=22
    ASSIGN_OP=23
    ARITH_OP=24
    ARITH_FUNC=25
    NEWLINE=26
    WHITE_SPACE=27
    COND_OP=28
    COMMENT=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(pythonparserParser.EOF, 0)

        def definitions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pythonparserParser.DefinitionsContext)
            else:
                return self.getTypedRuleContext(pythonparserParser.DefinitionsContext,i)


        def getRuleIndex(self):
            return pythonparserParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = pythonparserParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 537182722) != 0:
                self.state = 22
                self.definitions()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
            self.match(pythonparserParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefinitionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(pythonparserParser.VariableContext,0)


        def ifblocks(self):
            return self.getTypedRuleContext(pythonparserParser.IfblocksContext,0)


        def whileloop(self):
            return self.getTypedRuleContext(pythonparserParser.WhileloopContext,0)


        def comment(self):
            return self.getTypedRuleContext(pythonparserParser.CommentContext,0)


        def forloop(self):
            return self.getTypedRuleContext(pythonparserParser.ForloopContext,0)


        def function(self):
            return self.getTypedRuleContext(pythonparserParser.FunctionContext,0)


        def functioncall(self):
            return self.getTypedRuleContext(pythonparserParser.FunctioncallContext,0)


        def getRuleIndex(self):
            return pythonparserParser.RULE_definitions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinitions" ):
                listener.enterDefinitions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinitions" ):
                listener.exitDefinitions(self)




    def definitions(self):

        localctx = pythonparserParser.DefinitionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_definitions)
        try:
            self.state = 37
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.ifblocks()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 32
                self.whileloop()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 33
                self.comment()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 34
                self.forloop()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 35
                self.function()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 36
                self.functioncall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self, i:int=None):
            if i is None:
                return self.getTokens(pythonparserParser.VAR)
            else:
                return self.getToken(pythonparserParser.VAR, i)

        def block(self):
            return self.getTypedRuleContext(pythonparserParser.BlockContext,0)


        def getRuleIndex(self):
            return pythonparserParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = pythonparserParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(pythonparserParser.T__0)
            self.state = 40
            self.match(pythonparserParser.VAR)
            self.state = 41
            self.match(pythonparserParser.T__1)
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 42
                self.match(pythonparserParser.VAR)
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==3:
                    self.state = 43
                    self.match(pythonparserParser.T__2)


                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 51
            self.match(pythonparserParser.T__3)
            self.state = 52
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctioncallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self, i:int=None):
            if i is None:
                return self.getTokens(pythonparserParser.VAR)
            else:
                return self.getToken(pythonparserParser.VAR, i)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(pythonparserParser.NUMBER)
            else:
                return self.getToken(pythonparserParser.NUMBER, i)

        def ARITH_FUNC(self, i:int=None):
            if i is None:
                return self.getTokens(pythonparserParser.ARITH_FUNC)
            else:
                return self.getToken(pythonparserParser.ARITH_FUNC, i)

        def functioncall(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pythonparserParser.FunctioncallContext)
            else:
                return self.getTypedRuleContext(pythonparserParser.FunctioncallContext,i)


        def getRuleIndex(self):
            return pythonparserParser.RULE_functioncall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctioncall" ):
                listener.enterFunctioncall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctioncall" ):
                listener.exitFunctioncall(self)




    def functioncall(self):

        localctx = pythonparserParser.FunctioncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_functioncall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(pythonparserParser.VAR)
            self.state = 55
            self.match(pythonparserParser.T__1)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 34340864) != 0:
                self.state = 60
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 56
                    self.match(pythonparserParser.VAR)
                    pass

                elif la_ == 2:
                    self.state = 57
                    self.match(pythonparserParser.NUMBER)
                    pass

                elif la_ == 3:
                    self.state = 58
                    self.match(pythonparserParser.ARITH_FUNC)
                    pass

                elif la_ == 4:
                    self.state = 59
                    self.functioncall()
                    pass


                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==3:
                    self.state = 62
                    self.match(pythonparserParser.T__2)


                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 70
            self.match(pythonparserParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self, i:int=None):
            if i is None:
                return self.getTokens(pythonparserParser.VAR)
            else:
                return self.getToken(pythonparserParser.VAR, i)

        def ASSIGN_OP(self):
            return self.getToken(pythonparserParser.ASSIGN_OP, 0)

        def STRING(self):
            return self.getToken(pythonparserParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(pythonparserParser.NUMBER, 0)

        def ARITH_FUNC(self):
            return self.getToken(pythonparserParser.ARITH_FUNC, 0)

        def NEWLINE(self):
            return self.getToken(pythonparserParser.NEWLINE, 0)

        def getRuleIndex(self):
            return pythonparserParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)




    def variable(self):

        localctx = pythonparserParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(pythonparserParser.VAR)
            self.state = 73
            self.match(pythonparserParser.ASSIGN_OP)
            self.state = 74
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 35389440) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 75
                self.match(pythonparserParser.NEWLINE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(pythonparserParser.VAR, 0)

        def NUMBER(self):
            return self.getToken(pythonparserParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(pythonparserParser.STRING, 0)

        def ARITH_FUNC(self):
            return self.getToken(pythonparserParser.ARITH_FUNC, 0)

        def conditional(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pythonparserParser.ConditionalContext)
            else:
                return self.getTypedRuleContext(pythonparserParser.ConditionalContext,i)


        def COND_OP(self):
            return self.getToken(pythonparserParser.COND_OP, 0)

        def ARITH_OP(self):
            return self.getToken(pythonparserParser.ARITH_OP, 0)

        def getRuleIndex(self):
            return pythonparserParser.RULE_conditional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)



    def conditional(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = pythonparserParser.ConditionalContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_conditional, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.state = 79
                self.match(pythonparserParser.VAR)
                pass
            elif token in [19]:
                self.state = 80
                self.match(pythonparserParser.NUMBER)
                pass
            elif token in [20]:
                self.state = 81
                self.match(pythonparserParser.STRING)
                pass
            elif token in [25]:
                self.state = 82
                self.match(pythonparserParser.ARITH_FUNC)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 96
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 94
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = pythonparserParser.ConditionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional)
                        self.state = 85
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 86
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 448) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 87
                        self.conditional(4)
                        pass

                    elif la_ == 2:
                        localctx = pythonparserParser.ConditionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional)
                        self.state = 88
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 89
                        self.match(pythonparserParser.COND_OP)
                        self.state = 90
                        self.conditional(3)
                        pass

                    elif la_ == 3:
                        localctx = pythonparserParser.ConditionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional)
                        self.state = 91
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 92
                        self.match(pythonparserParser.ARITH_OP)
                        self.state = 93
                        self.conditional(2)
                        pass

             
                self.state = 98
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class IfblocksContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditional(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pythonparserParser.ConditionalContext)
            else:
                return self.getTypedRuleContext(pythonparserParser.ConditionalContext,i)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pythonparserParser.BlockContext)
            else:
                return self.getTypedRuleContext(pythonparserParser.BlockContext,i)


        def getRuleIndex(self):
            return pythonparserParser.RULE_ifblocks

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfblocks" ):
                listener.enterIfblocks(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfblocks" ):
                listener.exitIfblocks(self)




    def ifblocks(self):

        localctx = pythonparserParser.IfblocksContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ifblocks)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(pythonparserParser.T__8)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 100
                self.match(pythonparserParser.T__1)


            self.state = 103
            self.conditional(0)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 104
                self.match(pythonparserParser.T__4)


            self.state = 107
            self.match(pythonparserParser.T__9)
            self.state = 108
            self.block()
            self.state = 123
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 110
                    self.match(pythonparserParser.T__10)
                    self.state = 112
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==2:
                        self.state = 111
                        self.match(pythonparserParser.T__1)


                    self.state = 114
                    self.conditional(0)
                    self.state = 116
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==5:
                        self.state = 115
                        self.match(pythonparserParser.T__4)


                    self.state = 118
                    self.match(pythonparserParser.T__9)
                    self.state = 119
                    self.block() 
                self.state = 125
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 126
                self.match(pythonparserParser.T__11)
                self.state = 127
                self.match(pythonparserParser.T__9)
                self.state = 128
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(pythonparserParser.NEWLINE, 0)

        def definitions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pythonparserParser.DefinitionsContext)
            else:
                return self.getTypedRuleContext(pythonparserParser.DefinitionsContext,i)


        def getRuleIndex(self):
            return pythonparserParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = pythonparserParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 9, 14, 15, 18, 29]:
                self.state = 132 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 131
                        self.definitions()

                    else:
                        raise NoViableAltException(self)
                    self.state = 134 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

                self.state = 137
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 136
                    self.match(pythonparserParser.T__12)


                pass
            elif token in [13]:
                self.state = 139
                self.match(pythonparserParser.T__12)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 142
                self.match(pythonparserParser.NEWLINE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileloopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditional(self):
            return self.getTypedRuleContext(pythonparserParser.ConditionalContext,0)


        def block(self):
            return self.getTypedRuleContext(pythonparserParser.BlockContext,0)


        def getRuleIndex(self):
            return pythonparserParser.RULE_whileloop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileloop" ):
                listener.enterWhileloop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileloop" ):
                listener.exitWhileloop(self)




    def whileloop(self):

        localctx = pythonparserParser.WhileloopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_whileloop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(pythonparserParser.T__13)
            self.state = 146
            self.conditional(0)
            self.state = 147
            self.match(pythonparserParser.T__9)
            self.state = 148
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(pythonparserParser.COMMENT, 0)

        def getRuleIndex(self):
            return pythonparserParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)




    def comment(self):

        localctx = pythonparserParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(pythonparserParser.COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForloopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self, i:int=None):
            if i is None:
                return self.getTokens(pythonparserParser.VAR)
            else:
                return self.getToken(pythonparserParser.VAR, i)

        def block(self):
            return self.getTypedRuleContext(pythonparserParser.BlockContext,0)


        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(pythonparserParser.NUMBER)
            else:
                return self.getToken(pythonparserParser.NUMBER, i)

        def ARITH_FUNC(self, i:int=None):
            if i is None:
                return self.getTokens(pythonparserParser.ARITH_FUNC)
            else:
                return self.getToken(pythonparserParser.ARITH_FUNC, i)

        def getRuleIndex(self):
            return pythonparserParser.RULE_forloop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForloop" ):
                listener.enterForloop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForloop" ):
                listener.exitForloop(self)




    def forloop(self):

        localctx = pythonparserParser.ForloopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_forloop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(pythonparserParser.T__14)
            self.state = 153
            self.match(pythonparserParser.VAR)
            self.state = 154
            self.match(pythonparserParser.T__15)
            self.state = 163
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.state = 155
                self.match(pythonparserParser.VAR)
                pass
            elif token in [17]:
                self.state = 156
                self.match(pythonparserParser.T__16)
                self.state = 161
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                if la_ == 1:
                    self.state = 157
                    self.match(pythonparserParser.NUMBER)
                    pass

                elif la_ == 2:
                    self.state = 158
                    _la = self._input.LA(1)
                    if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 34340864) != 0):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 159
                    self.match(pythonparserParser.T__2)
                    self.state = 160
                    _la = self._input.LA(1)
                    if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 34340864) != 0):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    pass


                pass
            else:
                raise NoViableAltException(self)

            self.state = 165
            self.match(pythonparserParser.T__3)
            self.state = 166
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.conditional_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def conditional_sempred(self, localctx:ConditionalContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         




