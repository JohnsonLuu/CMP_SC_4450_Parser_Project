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
        4,1,27,124,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,1,0,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,0,1,
        0,1,1,1,1,1,1,1,1,3,1,33,8,1,1,2,1,2,1,2,1,2,1,2,3,2,40,8,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,51,8,2,10,2,12,2,54,9,2,1,3,
        1,3,3,3,58,8,3,1,3,1,3,3,3,62,8,3,1,3,1,3,1,3,1,3,1,3,3,3,69,8,3,
        1,3,1,3,3,3,73,8,3,1,3,1,3,1,3,5,3,78,8,3,10,3,12,3,81,9,3,1,3,1,
        3,1,3,3,3,86,8,3,1,4,1,4,4,4,90,8,4,11,4,12,4,91,1,4,3,4,95,8,4,
        1,5,1,5,1,5,1,5,1,5,1,6,1,6,5,6,104,8,6,10,6,12,6,107,9,6,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,119,8,7,1,7,1,7,1,7,1,7,0,
        1,4,8,0,2,4,6,8,10,12,14,0,4,2,0,17,19,24,24,1,0,1,3,1,0,12,12,2,
        0,17,18,24,24,138,0,23,1,0,0,0,2,28,1,0,0,0,4,39,1,0,0,0,6,55,1,
        0,0,0,8,89,1,0,0,0,10,96,1,0,0,0,12,101,1,0,0,0,14,108,1,0,0,0,16,
        22,3,2,1,0,17,22,3,6,3,0,18,22,3,10,5,0,19,22,3,12,6,0,20,22,3,14,
        7,0,21,16,1,0,0,0,21,17,1,0,0,0,21,18,1,0,0,0,21,19,1,0,0,0,21,20,
        1,0,0,0,22,25,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,26,1,0,0,0,
        25,23,1,0,0,0,26,27,5,0,0,1,27,1,1,0,0,0,28,29,5,17,0,0,29,30,5,
        22,0,0,30,32,7,0,0,0,31,33,5,25,0,0,32,31,1,0,0,0,32,33,1,0,0,0,
        33,3,1,0,0,0,34,35,6,2,-1,0,35,40,5,17,0,0,36,40,5,18,0,0,37,40,
        5,19,0,0,38,40,5,24,0,0,39,34,1,0,0,0,39,36,1,0,0,0,39,37,1,0,0,
        0,39,38,1,0,0,0,40,52,1,0,0,0,41,42,10,3,0,0,42,43,7,1,0,0,43,51,
        3,4,2,4,44,45,10,2,0,0,45,46,5,27,0,0,46,51,3,4,2,3,47,48,10,1,0,
        0,48,49,5,23,0,0,49,51,3,4,2,2,50,41,1,0,0,0,50,44,1,0,0,0,50,47,
        1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,5,1,0,0,0,54,
        52,1,0,0,0,55,57,5,4,0,0,56,58,5,5,0,0,57,56,1,0,0,0,57,58,1,0,0,
        0,58,59,1,0,0,0,59,61,3,4,2,0,60,62,5,6,0,0,61,60,1,0,0,0,61,62,
        1,0,0,0,62,63,1,0,0,0,63,64,5,7,0,0,64,65,3,8,4,0,65,79,1,0,0,0,
        66,68,5,8,0,0,67,69,5,5,0,0,68,67,1,0,0,0,68,69,1,0,0,0,69,70,1,
        0,0,0,70,72,3,4,2,0,71,73,5,6,0,0,72,71,1,0,0,0,72,73,1,0,0,0,73,
        74,1,0,0,0,74,75,5,7,0,0,75,76,3,8,4,0,76,78,1,0,0,0,77,66,1,0,0,
        0,78,81,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,85,1,0,0,0,81,79,
        1,0,0,0,82,83,5,9,0,0,83,84,5,7,0,0,84,86,3,8,4,0,85,82,1,0,0,0,
        85,86,1,0,0,0,86,7,1,0,0,0,87,90,3,2,1,0,88,90,3,6,3,0,89,87,1,0,
        0,0,89,88,1,0,0,0,90,91,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,94,
        1,0,0,0,93,95,5,25,0,0,94,93,1,0,0,0,94,95,1,0,0,0,95,9,1,0,0,0,
        96,97,5,10,0,0,97,98,3,4,2,0,98,99,5,7,0,0,99,100,3,8,4,0,100,11,
        1,0,0,0,101,105,5,11,0,0,102,104,8,2,0,0,103,102,1,0,0,0,104,107,
        1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,13,1,0,0,0,107,105,1,
        0,0,0,108,109,5,13,0,0,109,110,5,17,0,0,110,118,5,14,0,0,111,119,
        5,17,0,0,112,113,5,15,0,0,113,114,7,3,0,0,114,115,5,16,0,0,115,116,
        7,3,0,0,116,117,1,0,0,0,117,119,5,6,0,0,118,111,1,0,0,0,118,112,
        1,0,0,0,119,120,1,0,0,0,120,121,5,7,0,0,121,122,3,8,4,0,122,15,1,
        0,0,0,17,21,23,32,39,50,52,57,61,68,72,79,85,89,91,94,105,118
    ]

class pythonparserParser ( Parser ):

    grammarFileName = "pythonparser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'and'", "'or'", "'not'", "'if'", "'('", 
                     "')'", "':'", "'elif'", "'else'", "'while'", "'#'", 
                     "'\\n'", "'for'", "'in'", "'range('", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
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
    RULE_forloop = 7

    ruleNames =  [ "start", "variable", "conditional", "ifblocks", "block", 
                   "whileloop", "comment", "forloop" ]

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
    VAR=17
    NUMBER=18
    STRING=19
    DIGIT=20
    LETTER=21
    ASSIGNMENT_OPERATORS=22
    ARITHMETIC_OPERATORS=23
    ARITHMETIC_FUNCTIONS=24
    NEWLINE=25
    WHITE_SPACE=26
    CONDITIONAL_OPERATORS=27

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


        def forloop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pythonparserParser.ForloopContext)
            else:
                return self.getTypedRuleContext(pythonparserParser.ForloopContext,i)


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
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 142352) != 0:
                self.state = 21
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [17]:
                    self.state = 16
                    self.variable()
                    pass
                elif token in [4]:
                    self.state = 17
                    self.ifblocks()
                    pass
                elif token in [10]:
                    self.state = 18
                    self.whileloop()
                    pass
                elif token in [11]:
                    self.state = 19
                    self.comment()
                    pass
                elif token in [13]:
                    self.state = 20
                    self.forloop()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
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
            self.state = 28
            self.match(pythonparserParser.VAR)
            self.state = 29
            self.match(pythonparserParser.ASSIGNMENT_OPERATORS)
            self.state = 30
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 17694720) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 32
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 31
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
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.state = 35
                self.match(pythonparserParser.VAR)
                pass
            elif token in [18]:
                self.state = 36
                self.match(pythonparserParser.NUMBER)
                pass
            elif token in [19]:
                self.state = 37
                self.match(pythonparserParser.STRING)
                pass
            elif token in [24]:
                self.state = 38
                self.match(pythonparserParser.ARITHMETIC_FUNCTIONS)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 52
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 50
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = pythonparserParser.ConditionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional)
                        self.state = 41
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 42
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 43
                        self.conditional(4)
                        pass

                    elif la_ == 2:
                        localctx = pythonparserParser.ConditionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional)
                        self.state = 44
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 45
                        self.match(pythonparserParser.CONDITIONAL_OPERATORS)
                        self.state = 46
                        self.conditional(3)
                        pass

                    elif la_ == 3:
                        localctx = pythonparserParser.ConditionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional)
                        self.state = 47
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 48
                        self.match(pythonparserParser.ARITHMETIC_OPERATORS)
                        self.state = 49
                        self.conditional(2)
                        pass

             
                self.state = 54
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
            self.state = 55
            self.match(pythonparserParser.T__3)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 56
                self.match(pythonparserParser.T__4)


            self.state = 59
            self.conditional(0)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 60
                self.match(pythonparserParser.T__5)


            self.state = 63
            self.match(pythonparserParser.T__6)
            self.state = 64
            self.block()
            self.state = 79
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 66
                    self.match(pythonparserParser.T__7)
                    self.state = 68
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==5:
                        self.state = 67
                        self.match(pythonparserParser.T__4)


                    self.state = 70
                    self.conditional(0)
                    self.state = 72
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==6:
                        self.state = 71
                        self.match(pythonparserParser.T__5)


                    self.state = 74
                    self.match(pythonparserParser.T__6)
                    self.state = 75
                    self.block() 
                self.state = 81
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 82
                self.match(pythonparserParser.T__8)
                self.state = 83
                self.match(pythonparserParser.T__6)
                self.state = 84
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
            self.state = 89 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 89
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [17]:
                        self.state = 87
                        self.variable()
                        pass
                    elif token in [4]:
                        self.state = 88
                        self.ifblocks()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 91 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 93
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
            self.state = 96
            self.match(pythonparserParser.T__9)
            self.state = 97
            self.conditional(0)
            self.state = 98
            self.match(pythonparserParser.T__6)
            self.state = 99
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
            self.state = 101
            self.match(pythonparserParser.T__10)
            self.state = 105
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 102
                    _la = self._input.LA(1)
                    if _la <= 0 or _la==12:
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 107
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
        self.enterRule(localctx, 14, self.RULE_forloop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(pythonparserParser.T__12)
            self.state = 109
            self.match(pythonparserParser.VAR)
            self.state = 110
            self.match(pythonparserParser.T__13)
            self.state = 118
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.state = 111
                self.match(pythonparserParser.VAR)
                pass
            elif token in [15]:
                self.state = 112
                self.match(pythonparserParser.T__14)

                self.state = 113
                _la = self._input.LA(1)
                if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 17170432) != 0):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 114
                self.match(pythonparserParser.T__15)
                self.state = 115
                _la = self._input.LA(1)
                if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 17170432) != 0):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 117
                self.match(pythonparserParser.T__5)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 120
            self.match(pythonparserParser.T__6)
            self.state = 121
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
         




