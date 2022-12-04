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
        4,1,23,106,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,0,5,0,19,8,0,10,0,12,0,22,9,0,1,0,1,0,1,1,1,1,1,
        1,1,1,3,1,30,8,1,1,2,1,2,1,2,1,2,1,2,3,2,37,8,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,5,2,48,8,2,10,2,12,2,51,9,2,1,3,1,3,3,3,55,8,
        3,1,3,1,3,3,3,59,8,3,1,3,1,3,1,3,1,3,1,3,3,3,66,8,3,1,3,1,3,3,3,
        70,8,3,1,3,1,3,1,3,5,3,75,8,3,10,3,12,3,78,9,3,1,3,1,3,1,3,3,3,83,
        8,3,1,4,1,4,4,4,87,8,4,11,4,12,4,88,1,4,3,4,92,8,4,1,5,1,5,1,5,1,
        5,1,5,1,6,1,6,5,6,101,8,6,10,6,12,6,104,9,6,1,6,0,1,4,7,0,2,4,6,
        8,10,12,0,3,2,0,13,15,20,20,1,0,1,3,1,0,12,12,119,0,20,1,0,0,0,2,
        25,1,0,0,0,4,36,1,0,0,0,6,52,1,0,0,0,8,86,1,0,0,0,10,93,1,0,0,0,
        12,98,1,0,0,0,14,19,3,2,1,0,15,19,3,6,3,0,16,19,3,10,5,0,17,19,3,
        12,6,0,18,14,1,0,0,0,18,15,1,0,0,0,18,16,1,0,0,0,18,17,1,0,0,0,19,
        22,1,0,0,0,20,18,1,0,0,0,20,21,1,0,0,0,21,23,1,0,0,0,22,20,1,0,0,
        0,23,24,5,0,0,1,24,1,1,0,0,0,25,26,5,13,0,0,26,27,5,18,0,0,27,29,
        7,0,0,0,28,30,5,21,0,0,29,28,1,0,0,0,29,30,1,0,0,0,30,3,1,0,0,0,
        31,32,6,2,-1,0,32,37,5,13,0,0,33,37,5,14,0,0,34,37,5,15,0,0,35,37,
        5,20,0,0,36,31,1,0,0,0,36,33,1,0,0,0,36,34,1,0,0,0,36,35,1,0,0,0,
        37,49,1,0,0,0,38,39,10,3,0,0,39,40,7,1,0,0,40,48,3,4,2,4,41,42,10,
        2,0,0,42,43,5,23,0,0,43,48,3,4,2,3,44,45,10,1,0,0,45,46,5,19,0,0,
        46,48,3,4,2,2,47,38,1,0,0,0,47,41,1,0,0,0,47,44,1,0,0,0,48,51,1,
        0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,5,1,0,0,0,51,49,1,0,0,0,52,
        54,5,4,0,0,53,55,5,5,0,0,54,53,1,0,0,0,54,55,1,0,0,0,55,56,1,0,0,
        0,56,58,3,4,2,0,57,59,5,6,0,0,58,57,1,0,0,0,58,59,1,0,0,0,59,60,
        1,0,0,0,60,61,5,7,0,0,61,62,3,8,4,0,62,76,1,0,0,0,63,65,5,8,0,0,
        64,66,5,5,0,0,65,64,1,0,0,0,65,66,1,0,0,0,66,67,1,0,0,0,67,69,3,
        4,2,0,68,70,5,6,0,0,69,68,1,0,0,0,69,70,1,0,0,0,70,71,1,0,0,0,71,
        72,5,7,0,0,72,73,3,8,4,0,73,75,1,0,0,0,74,63,1,0,0,0,75,78,1,0,0,
        0,76,74,1,0,0,0,76,77,1,0,0,0,77,82,1,0,0,0,78,76,1,0,0,0,79,80,
        5,9,0,0,80,81,5,7,0,0,81,83,3,8,4,0,82,79,1,0,0,0,82,83,1,0,0,0,
        83,7,1,0,0,0,84,87,3,2,1,0,85,87,3,6,3,0,86,84,1,0,0,0,86,85,1,0,
        0,0,87,88,1,0,0,0,88,86,1,0,0,0,88,89,1,0,0,0,89,91,1,0,0,0,90,92,
        5,21,0,0,91,90,1,0,0,0,91,92,1,0,0,0,92,9,1,0,0,0,93,94,5,10,0,0,
        94,95,3,4,2,0,95,96,5,7,0,0,96,97,3,8,4,0,97,11,1,0,0,0,98,102,5,
        11,0,0,99,101,8,2,0,0,100,99,1,0,0,0,101,104,1,0,0,0,102,100,1,0,
        0,0,102,103,1,0,0,0,103,13,1,0,0,0,104,102,1,0,0,0,16,18,20,29,36,
        47,49,54,58,65,69,76,82,86,88,91,102
    ]

class pythonparserParser ( Parser ):

    grammarFileName = "pythonparser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'and'", "'or'", "'not'", "'if'", "'('", 
                     "')'", "':'", "'elif'", "'else'", "'while'", "'#'", 
                     "'\\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "VAR", "NUMBER", "STRING", "DIGIT", "LETTER", 
                      "ASSIGNMENT_OPERATORS", "ARITHMETIC_OPERATORS", "ARITHMETIC_FUNCTIONS", 
                      "NEWLINE", "WHITE_SPACE", "CONDITIONAL_OPERATORS" ]

    RULE_start = 0
    RULE_variable = 1
    RULE_conditional = 2
    RULE_ifblocks = 3
    RULE_block = 4
    RULE_whileloop = 5
    RULE_comment = 6

    ruleNames =  [ "start", "variable", "conditional", "ifblocks", "block", 
                   "whileloop", "comment" ]

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
    VAR=13
    NUMBER=14
    STRING=15
    DIGIT=16
    LETTER=17
    ASSIGNMENT_OPERATORS=18
    ARITHMETIC_OPERATORS=19
    ARITHMETIC_FUNCTIONS=20
    NEWLINE=21
    WHITE_SPACE=22
    CONDITIONAL_OPERATORS=23

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


        def comment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pythonparserParser.CommentContext)
            else:
                return self.getTypedRuleContext(pythonparserParser.CommentContext,i)


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
            self.state = 20
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 11280) != 0:
                self.state = 18
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [13]:
                    self.state = 14
                    self.variable()
                    pass
                elif token in [4]:
                    self.state = 15
                    self.ifblocks()
                    pass
                elif token in [10]:
                    self.state = 16
                    self.whileloop()
                    pass
                elif token in [11]:
                    self.state = 17
                    self.comment()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 23
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
            self.state = 25
            self.match(pythonparserParser.VAR)
            self.state = 26
            self.match(pythonparserParser.ASSIGNMENT_OPERATORS)
            self.state = 27
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 1105920) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 29
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 28
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
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.state = 32
                self.match(pythonparserParser.VAR)
                pass
            elif token in [14]:
                self.state = 33
                self.match(pythonparserParser.NUMBER)
                pass
            elif token in [15]:
                self.state = 34
                self.match(pythonparserParser.STRING)
                pass
            elif token in [20]:
                self.state = 35
                self.match(pythonparserParser.ARITHMETIC_FUNCTIONS)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 49
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 47
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = pythonparserParser.ConditionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional)
                        self.state = 38
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 39
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 40
                        self.conditional(4)
                        pass

                    elif la_ == 2:
                        localctx = pythonparserParser.ConditionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional)
                        self.state = 41
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 42
                        self.match(pythonparserParser.CONDITIONAL_OPERATORS)
                        self.state = 43
                        self.conditional(3)
                        pass

                    elif la_ == 3:
                        localctx = pythonparserParser.ConditionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional)
                        self.state = 44
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 45
                        self.match(pythonparserParser.ARITHMETIC_OPERATORS)
                        self.state = 46
                        self.conditional(2)
                        pass

             
                self.state = 51
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
            self.state = 52
            self.match(pythonparserParser.T__3)
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 53
                self.match(pythonparserParser.T__4)


            self.state = 56
            self.conditional(0)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 57
                self.match(pythonparserParser.T__5)


            self.state = 60
            self.match(pythonparserParser.T__6)
            self.state = 61
            self.block()
            self.state = 76
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 63
                    self.match(pythonparserParser.T__7)
                    self.state = 65
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==5:
                        self.state = 64
                        self.match(pythonparserParser.T__4)


                    self.state = 67
                    self.conditional(0)
                    self.state = 69
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==6:
                        self.state = 68
                        self.match(pythonparserParser.T__5)


                    self.state = 71
                    self.match(pythonparserParser.T__6)
                    self.state = 72
                    self.block() 
                self.state = 78
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 79
                self.match(pythonparserParser.T__8)
                self.state = 80
                self.match(pythonparserParser.T__6)
                self.state = 81
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
            self.state = 86 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 86
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [13]:
                        self.state = 84
                        self.variable()
                        pass
                    elif token in [4]:
                        self.state = 85
                        self.ifblocks()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 88 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 90
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
            self.state = 93
            self.match(pythonparserParser.T__9)
            self.state = 94
            self.conditional(0)
            self.state = 95
            self.match(pythonparserParser.T__6)
            self.state = 96
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
        self.enterRule(localctx, 12, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(pythonparserParser.T__10)
            self.state = 102
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 99
                    _la = self._input.LA(1)
                    if _la <= 0 or _la==12:
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 104
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
         




