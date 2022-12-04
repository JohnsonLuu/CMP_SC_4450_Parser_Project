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
        4,1,27,129,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,1,0,1,1,1,
        1,1,1,1,1,1,1,3,1,32,8,1,1,2,1,2,1,2,1,2,3,2,38,8,2,1,3,1,3,1,3,
        1,3,1,3,3,3,45,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,56,8,
        3,10,3,12,3,59,9,3,1,4,1,4,3,4,63,8,4,1,4,1,4,3,4,67,8,4,1,4,1,4,
        1,4,1,4,1,4,3,4,74,8,4,1,4,1,4,3,4,78,8,4,1,4,1,4,1,4,5,4,83,8,4,
        10,4,12,4,86,9,4,1,4,1,4,1,4,3,4,91,8,4,1,5,4,5,94,8,5,11,5,12,5,
        95,1,5,3,5,99,8,5,1,5,3,5,102,8,5,1,5,3,5,105,8,5,1,6,1,6,1,6,1,
        6,1,6,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,124,8,
        8,1,8,1,8,1,8,1,8,0,1,6,9,0,2,4,6,8,10,12,14,16,0,3,2,0,16,18,23,
        23,1,0,1,3,2,0,16,17,23,23,142,0,21,1,0,0,0,2,31,1,0,0,0,4,33,1,
        0,0,0,6,44,1,0,0,0,8,60,1,0,0,0,10,101,1,0,0,0,12,106,1,0,0,0,14,
        111,1,0,0,0,16,113,1,0,0,0,18,20,3,2,1,0,19,18,1,0,0,0,20,23,1,0,
        0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,24,1,0,0,0,23,21,1,0,0,0,24,25,
        5,0,0,1,25,1,1,0,0,0,26,32,3,4,2,0,27,32,3,8,4,0,28,32,3,12,6,0,
        29,32,3,14,7,0,30,32,3,16,8,0,31,26,1,0,0,0,31,27,1,0,0,0,31,28,
        1,0,0,0,31,29,1,0,0,0,31,30,1,0,0,0,32,3,1,0,0,0,33,34,5,16,0,0,
        34,35,5,21,0,0,35,37,7,0,0,0,36,38,5,24,0,0,37,36,1,0,0,0,37,38,
        1,0,0,0,38,5,1,0,0,0,39,40,6,3,-1,0,40,45,5,16,0,0,41,45,5,17,0,
        0,42,45,5,18,0,0,43,45,5,23,0,0,44,39,1,0,0,0,44,41,1,0,0,0,44,42,
        1,0,0,0,44,43,1,0,0,0,45,57,1,0,0,0,46,47,10,3,0,0,47,48,7,1,0,0,
        48,56,3,6,3,4,49,50,10,2,0,0,50,51,5,26,0,0,51,56,3,6,3,3,52,53,
        10,1,0,0,53,54,5,22,0,0,54,56,3,6,3,2,55,46,1,0,0,0,55,49,1,0,0,
        0,55,52,1,0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,58,7,1,
        0,0,0,59,57,1,0,0,0,60,62,5,4,0,0,61,63,5,5,0,0,62,61,1,0,0,0,62,
        63,1,0,0,0,63,64,1,0,0,0,64,66,3,6,3,0,65,67,5,6,0,0,66,65,1,0,0,
        0,66,67,1,0,0,0,67,68,1,0,0,0,68,69,5,7,0,0,69,70,3,10,5,0,70,84,
        1,0,0,0,71,73,5,8,0,0,72,74,5,5,0,0,73,72,1,0,0,0,73,74,1,0,0,0,
        74,75,1,0,0,0,75,77,3,6,3,0,76,78,5,6,0,0,77,76,1,0,0,0,77,78,1,
        0,0,0,78,79,1,0,0,0,79,80,5,7,0,0,80,81,3,10,5,0,81,83,1,0,0,0,82,
        71,1,0,0,0,83,86,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,90,1,0,0,
        0,86,84,1,0,0,0,87,88,5,9,0,0,88,89,5,7,0,0,89,91,3,10,5,0,90,87,
        1,0,0,0,90,91,1,0,0,0,91,9,1,0,0,0,92,94,3,2,1,0,93,92,1,0,0,0,94,
        95,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,98,1,0,0,0,97,99,5,10,
        0,0,98,97,1,0,0,0,98,99,1,0,0,0,99,102,1,0,0,0,100,102,5,10,0,0,
        101,93,1,0,0,0,101,100,1,0,0,0,102,104,1,0,0,0,103,105,5,24,0,0,
        104,103,1,0,0,0,104,105,1,0,0,0,105,11,1,0,0,0,106,107,5,11,0,0,
        107,108,3,6,3,0,108,109,5,7,0,0,109,110,3,10,5,0,110,13,1,0,0,0,
        111,112,5,27,0,0,112,15,1,0,0,0,113,114,5,12,0,0,114,115,5,16,0,
        0,115,123,5,13,0,0,116,124,5,16,0,0,117,118,5,14,0,0,118,119,7,2,
        0,0,119,120,5,15,0,0,120,121,7,2,0,0,121,122,1,0,0,0,122,124,5,6,
        0,0,123,116,1,0,0,0,123,117,1,0,0,0,124,125,1,0,0,0,125,126,5,7,
        0,0,126,127,3,10,5,0,127,17,1,0,0,0,17,21,31,37,44,55,57,62,66,73,
        77,84,90,95,98,101,104,123
    ]

class pythonparserParser ( Parser ):

    grammarFileName = "pythonparser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'and'", "'or'", "'not'", "'if'", "'('", 
                     "')'", "':'", "'elif'", "'else'", "'break'", "'while'", 
                     "'for'", "'in'", "'range('", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "VAR", "NUMBER", "STRING", "DIGIT", "LETTER", "ASSIGNMENT_OPERATORS", 
                      "ARITHMETIC_OPERATORS", "ARITHMETIC_FUNCTIONS", "NEWLINE", 
                      "WHITE_SPACE", "CONDITIONAL_OPERATORS", "COMMENT" ]

    RULE_start = 0
    RULE_definitions = 1
    RULE_variable = 2
    RULE_conditional = 3
    RULE_ifblocks = 4
    RULE_block = 5
    RULE_whileloop = 6
    RULE_comment = 7
    RULE_forloop = 8

    ruleNames =  [ "start", "definitions", "variable", "conditional", "ifblocks", 
                   "block", "whileloop", "comment", "forloop" ]

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
    VAR=16
    NUMBER=17
    STRING=18
    DIGIT=19
    LETTER=20
    ASSIGNMENT_OPERATORS=21
    ARITHMETIC_OPERATORS=22
    ARITHMETIC_FUNCTIONS=23
    NEWLINE=24
    WHITE_SPACE=25
    CONDITIONAL_OPERATORS=26
    COMMENT=27

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
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 134289424) != 0:
                self.state = 18
                self.definitions()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
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
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.variable()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.ifblocks()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 28
                self.whileloop()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 4)
                self.state = 29
                self.comment()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 30
                self.forloop()
                pass
            else:
                raise NoViableAltException(self)

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

        def ASSIGNMENT_OPERATORS(self):
            return self.getToken(pythonparserParser.ASSIGNMENT_OPERATORS, 0)

        def STRING(self):
            return self.getToken(pythonparserParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(pythonparserParser.NUMBER, 0)

        def ARITHMETIC_FUNCTIONS(self):
            return self.getToken(pythonparserParser.ARITHMETIC_FUNCTIONS, 0)

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
        self.enterRule(localctx, 4, self.RULE_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(pythonparserParser.VAR)
            self.state = 34
            self.match(pythonparserParser.ASSIGNMENT_OPERATORS)
            self.state = 35
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 8847360) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 37
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 36
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

        def ARITHMETIC_FUNCTIONS(self):
            return self.getToken(pythonparserParser.ARITHMETIC_FUNCTIONS, 0)

        def conditional(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pythonparserParser.ConditionalContext)
            else:
                return self.getTypedRuleContext(pythonparserParser.ConditionalContext,i)


        def CONDITIONAL_OPERATORS(self):
            return self.getToken(pythonparserParser.CONDITIONAL_OPERATORS, 0)

        def ARITHMETIC_OPERATORS(self):
            return self.getToken(pythonparserParser.ARITHMETIC_OPERATORS, 0)

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
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_conditional, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.state = 40
                self.match(pythonparserParser.VAR)
                pass
            elif token in [17]:
                self.state = 41
                self.match(pythonparserParser.NUMBER)
                pass
            elif token in [18]:
                self.state = 42
                self.match(pythonparserParser.STRING)
                pass
            elif token in [23]:
                self.state = 43
                self.match(pythonparserParser.ARITHMETIC_FUNCTIONS)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 57
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 55
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = pythonparserParser.ConditionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional)
                        self.state = 46
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 47
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 48
                        self.conditional(4)
                        pass

                    elif la_ == 2:
                        localctx = pythonparserParser.ConditionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional)
                        self.state = 49
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 50
                        self.match(pythonparserParser.CONDITIONAL_OPERATORS)
                        self.state = 51
                        self.conditional(3)
                        pass

                    elif la_ == 3:
                        localctx = pythonparserParser.ConditionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional)
                        self.state = 52
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 53
                        self.match(pythonparserParser.ARITHMETIC_OPERATORS)
                        self.state = 54
                        self.conditional(2)
                        pass

             
                self.state = 59
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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
        self.enterRule(localctx, 8, self.RULE_ifblocks)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(pythonparserParser.T__3)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 61
                self.match(pythonparserParser.T__4)


            self.state = 64
            self.conditional(0)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 65
                self.match(pythonparserParser.T__5)


            self.state = 68
            self.match(pythonparserParser.T__6)
            self.state = 69
            self.block()
            self.state = 84
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 71
                    self.match(pythonparserParser.T__7)
                    self.state = 73
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==5:
                        self.state = 72
                        self.match(pythonparserParser.T__4)


                    self.state = 75
                    self.conditional(0)
                    self.state = 77
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==6:
                        self.state = 76
                        self.match(pythonparserParser.T__5)


                    self.state = 79
                    self.match(pythonparserParser.T__6)
                    self.state = 80
                    self.block() 
                self.state = 86
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 87
                self.match(pythonparserParser.T__8)
                self.state = 88
                self.match(pythonparserParser.T__6)
                self.state = 89
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
        self.enterRule(localctx, 10, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 11, 12, 16, 27]:
                self.state = 93 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 92
                        self.definitions()

                    else:
                        raise NoViableAltException(self)
                    self.state = 95 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                self.state = 98
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 97
                    self.match(pythonparserParser.T__9)


                pass
            elif token in [10]:
                self.state = 100
                self.match(pythonparserParser.T__9)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 103
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
        self.enterRule(localctx, 12, self.RULE_whileloop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(pythonparserParser.T__10)
            self.state = 107
            self.conditional(0)
            self.state = 108
            self.match(pythonparserParser.T__6)
            self.state = 109
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
        self.enterRule(localctx, 14, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
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

        def ARITHMETIC_FUNCTIONS(self, i:int=None):
            if i is None:
                return self.getTokens(pythonparserParser.ARITHMETIC_FUNCTIONS)
            else:
                return self.getToken(pythonparserParser.ARITHMETIC_FUNCTIONS, i)

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
        self.enterRule(localctx, 16, self.RULE_forloop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(pythonparserParser.T__11)
            self.state = 114
            self.match(pythonparserParser.VAR)
            self.state = 115
            self.match(pythonparserParser.T__12)
            self.state = 123
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.state = 116
                self.match(pythonparserParser.VAR)
                pass
            elif token in [14]:
                self.state = 117
                self.match(pythonparserParser.T__13)

                self.state = 118
                _la = self._input.LA(1)
                if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 8585216) != 0):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 119
                self.match(pythonparserParser.T__14)
                self.state = 120
                _la = self._input.LA(1)
                if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 8585216) != 0):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 122
                self.match(pythonparserParser.T__5)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 125
            self.match(pythonparserParser.T__6)
            self.state = 126
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
        self._predicates[3] = self.conditional_sempred
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
         




