# Generated from pythonparser.g4 by ANTLR 4.11.1
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
        4,1,21,96,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,0,5,0,16,8,0,10,0,12,0,19,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,27,
        8,1,1,2,1,2,1,2,1,2,1,2,3,2,34,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,5,2,45,8,2,10,2,12,2,48,9,2,1,3,1,3,3,3,52,8,3,1,3,1,3,3,3,
        56,8,3,1,3,1,3,1,3,1,3,1,3,3,3,63,8,3,1,3,1,3,3,3,67,8,3,1,3,1,3,
        1,3,5,3,72,8,3,10,3,12,3,75,9,3,1,3,1,3,1,3,3,3,80,8,3,1,4,1,4,4,
        4,84,8,4,11,4,12,4,85,1,4,3,4,89,8,4,1,5,1,5,1,5,1,5,1,5,1,5,0,1,
        4,6,0,2,4,6,8,10,0,2,2,0,11,13,18,18,1,0,1,3,108,0,17,1,0,0,0,2,
        22,1,0,0,0,4,33,1,0,0,0,6,49,1,0,0,0,8,83,1,0,0,0,10,90,1,0,0,0,
        12,16,3,2,1,0,13,16,3,6,3,0,14,16,3,10,5,0,15,12,1,0,0,0,15,13,1,
        0,0,0,15,14,1,0,0,0,16,19,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,
        20,1,0,0,0,19,17,1,0,0,0,20,21,5,0,0,1,21,1,1,0,0,0,22,23,5,11,0,
        0,23,24,5,16,0,0,24,26,7,0,0,0,25,27,5,19,0,0,26,25,1,0,0,0,26,27,
        1,0,0,0,27,3,1,0,0,0,28,29,6,2,-1,0,29,34,5,11,0,0,30,34,5,12,0,
        0,31,34,5,13,0,0,32,34,5,18,0,0,33,28,1,0,0,0,33,30,1,0,0,0,33,31,
        1,0,0,0,33,32,1,0,0,0,34,46,1,0,0,0,35,36,10,3,0,0,36,37,7,1,0,0,
        37,45,3,4,2,4,38,39,10,2,0,0,39,40,5,21,0,0,40,45,3,4,2,3,41,42,
        10,1,0,0,42,43,5,17,0,0,43,45,3,4,2,2,44,35,1,0,0,0,44,38,1,0,0,
        0,44,41,1,0,0,0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,5,1,
        0,0,0,48,46,1,0,0,0,49,51,5,4,0,0,50,52,5,5,0,0,51,50,1,0,0,0,51,
        52,1,0,0,0,52,53,1,0,0,0,53,55,3,4,2,0,54,56,5,6,0,0,55,54,1,0,0,
        0,55,56,1,0,0,0,56,57,1,0,0,0,57,58,5,7,0,0,58,59,3,8,4,0,59,73,
        1,0,0,0,60,62,5,8,0,0,61,63,5,5,0,0,62,61,1,0,0,0,62,63,1,0,0,0,
        63,64,1,0,0,0,64,66,3,4,2,0,65,67,5,6,0,0,66,65,1,0,0,0,66,67,1,
        0,0,0,67,68,1,0,0,0,68,69,5,7,0,0,69,70,3,8,4,0,70,72,1,0,0,0,71,
        60,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,79,1,0,0,
        0,75,73,1,0,0,0,76,77,5,9,0,0,77,78,5,7,0,0,78,80,3,8,4,0,79,76,
        1,0,0,0,79,80,1,0,0,0,80,7,1,0,0,0,81,84,3,2,1,0,82,84,3,6,3,0,83,
        81,1,0,0,0,83,82,1,0,0,0,84,85,1,0,0,0,85,83,1,0,0,0,85,86,1,0,0,
        0,86,88,1,0,0,0,87,89,5,19,0,0,88,87,1,0,0,0,88,89,1,0,0,0,89,9,
        1,0,0,0,90,91,5,10,0,0,91,92,3,4,2,0,92,93,5,7,0,0,93,94,3,8,4,0,
        94,11,1,0,0,0,15,15,17,26,33,44,46,51,55,62,66,73,79,83,85,88
    ]

class pythonparserParser ( Parser ):

    grammarFileName = "pythonparser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'and'", "'or'", "'not'", "'if'", "'('", 
                     "')'", "':'", "'elif'", "'else'", "'while'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "VAR", "NUMBER", 
                      "STRING", "DIGIT", "LETTER", "ASSIGNMENT_OPERATORS", 
                      "ARITHMETIC_OPERATORS", "ARITHMETIC_FUNCTIONS", "NEWLINE", 
                      "WHITE_SPACE", "CONDITIONAL_OPERATORS" ]

    RULE_start = 0
    RULE_variable = 1
    RULE_conditional = 2
    RULE_ifblocks = 3
    RULE_block = 4
    RULE_whileloop = 5

    ruleNames =  [ "start", "variable", "conditional", "ifblocks", "block", 
                   "whileloop" ]

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
    VAR=11
    NUMBER=12
    STRING=13
    DIGIT=14
    LETTER=15
    ASSIGNMENT_OPERATORS=16
    ARITHMETIC_OPERATORS=17
    ARITHMETIC_FUNCTIONS=18
    NEWLINE=19
    WHITE_SPACE=20
    CONDITIONAL_OPERATORS=21

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

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pythonparserParser.VariableContext)
            else:
                return self.getTypedRuleContext(pythonparserParser.VariableContext,i)


        def ifblocks(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pythonparserParser.IfblocksContext)
            else:
                return self.getTypedRuleContext(pythonparserParser.IfblocksContext,i)


        def whileloop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pythonparserParser.WhileloopContext)
            else:
                return self.getTypedRuleContext(pythonparserParser.WhileloopContext,i)


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
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 3088) != 0:
                self.state = 15
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [11]:
                    self.state = 12
                    self.variable()
                    pass
                elif token in [4]:
                    self.state = 13
                    self.ifblocks()
                    pass
                elif token in [10]:
                    self.state = 14
                    self.whileloop()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 20
            self.match(pythonparserParser.EOF)
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
        self.enterRule(localctx, 2, self.RULE_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(pythonparserParser.VAR)
            self.state = 23
            self.match(pythonparserParser.ASSIGNMENT_OPERATORS)
            self.state = 24
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 276480) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 26
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 25
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
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_conditional, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.state = 29
                self.match(pythonparserParser.VAR)
                pass
            elif token in [12]:
                self.state = 30
                self.match(pythonparserParser.NUMBER)
                pass
            elif token in [13]:
                self.state = 31
                self.match(pythonparserParser.STRING)
                pass
            elif token in [18]:
                self.state = 32
                self.match(pythonparserParser.ARITHMETIC_FUNCTIONS)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 46
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 44
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = pythonparserParser.ConditionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional)
                        self.state = 35
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 36
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 37
                        self.conditional(4)
                        pass

                    elif la_ == 2:
                        localctx = pythonparserParser.ConditionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional)
                        self.state = 38
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 39
                        self.match(pythonparserParser.CONDITIONAL_OPERATORS)
                        self.state = 40
                        self.conditional(3)
                        pass

                    elif la_ == 3:
                        localctx = pythonparserParser.ConditionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional)
                        self.state = 41
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 42
                        self.match(pythonparserParser.ARITHMETIC_OPERATORS)
                        self.state = 43
                        self.conditional(2)
                        pass

             
                self.state = 48
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
        self.enterRule(localctx, 6, self.RULE_ifblocks)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(pythonparserParser.T__3)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 50
                self.match(pythonparserParser.T__4)


            self.state = 53
            self.conditional(0)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 54
                self.match(pythonparserParser.T__5)


            self.state = 57
            self.match(pythonparserParser.T__6)
            self.state = 58
            self.block()
            self.state = 73
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 60
                    self.match(pythonparserParser.T__7)
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
                self.state = 75
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 76
                self.match(pythonparserParser.T__8)
                self.state = 77
                self.match(pythonparserParser.T__6)
                self.state = 78
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

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pythonparserParser.VariableContext)
            else:
                return self.getTypedRuleContext(pythonparserParser.VariableContext,i)


        def ifblocks(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pythonparserParser.IfblocksContext)
            else:
                return self.getTypedRuleContext(pythonparserParser.IfblocksContext,i)


        def NEWLINE(self):
            return self.getToken(pythonparserParser.NEWLINE, 0)

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
        self.enterRule(localctx, 8, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 83
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [11]:
                        self.state = 81
                        self.variable()
                        pass
                    elif token in [4]:
                        self.state = 82
                        self.ifblocks()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 85 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 87
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
        self.enterRule(localctx, 10, self.RULE_whileloop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(pythonparserParser.T__9)
            self.state = 91
            self.conditional(0)
            self.state = 92
            self.match(pythonparserParser.T__6)
            self.state = 93
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
        self._predicates[2] = self.conditional_sempred
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
         




