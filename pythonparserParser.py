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
        4,1,20,74,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,5,0,11,8,0,10,
        0,12,0,14,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,22,8,1,1,2,1,2,1,2,1,2,
        1,2,3,2,29,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,40,8,2,10,
        2,12,2,43,9,2,1,3,1,3,3,3,47,8,3,1,3,1,3,3,3,51,8,3,1,3,1,3,1,3,
        1,3,3,3,57,8,3,1,3,1,3,3,3,61,8,3,1,3,1,3,5,3,65,8,3,10,3,12,3,68,
        9,3,1,3,1,3,3,3,72,8,3,1,3,0,1,4,4,0,2,4,6,0,2,2,0,10,12,17,17,1,
        0,1,3,84,0,12,1,0,0,0,2,17,1,0,0,0,4,28,1,0,0,0,6,44,1,0,0,0,8,11,
        3,2,1,0,9,11,3,6,3,0,10,8,1,0,0,0,10,9,1,0,0,0,11,14,1,0,0,0,12,
        10,1,0,0,0,12,13,1,0,0,0,13,15,1,0,0,0,14,12,1,0,0,0,15,16,5,0,0,
        1,16,1,1,0,0,0,17,18,5,10,0,0,18,19,5,15,0,0,19,21,7,0,0,0,20,22,
        5,18,0,0,21,20,1,0,0,0,21,22,1,0,0,0,22,3,1,0,0,0,23,24,6,2,-1,0,
        24,29,5,10,0,0,25,29,5,11,0,0,26,29,5,12,0,0,27,29,5,17,0,0,28,23,
        1,0,0,0,28,25,1,0,0,0,28,26,1,0,0,0,28,27,1,0,0,0,29,41,1,0,0,0,
        30,31,10,3,0,0,31,32,7,1,0,0,32,40,3,4,2,4,33,34,10,2,0,0,34,35,
        5,20,0,0,35,40,3,4,2,3,36,37,10,1,0,0,37,38,5,16,0,0,38,40,3,4,2,
        2,39,30,1,0,0,0,39,33,1,0,0,0,39,36,1,0,0,0,40,43,1,0,0,0,41,39,
        1,0,0,0,41,42,1,0,0,0,42,5,1,0,0,0,43,41,1,0,0,0,44,46,5,4,0,0,45,
        47,5,5,0,0,46,45,1,0,0,0,46,47,1,0,0,0,47,48,1,0,0,0,48,50,3,4,2,
        0,49,51,5,6,0,0,50,49,1,0,0,0,50,51,1,0,0,0,51,52,1,0,0,0,52,53,
        5,7,0,0,53,66,1,0,0,0,54,56,5,8,0,0,55,57,5,5,0,0,56,55,1,0,0,0,
        56,57,1,0,0,0,57,58,1,0,0,0,58,60,3,4,2,0,59,61,5,6,0,0,60,59,1,
        0,0,0,60,61,1,0,0,0,61,62,1,0,0,0,62,63,5,7,0,0,63,65,1,0,0,0,64,
        54,1,0,0,0,65,68,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,71,1,0,0,
        0,68,66,1,0,0,0,69,70,5,9,0,0,70,72,5,7,0,0,71,69,1,0,0,0,71,72,
        1,0,0,0,72,7,1,0,0,0,12,10,12,21,28,39,41,46,50,56,60,66,71
    ]

class pythonparserParser ( Parser ):

    grammarFileName = "pythonparser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'and'", "'or'", "'not'", "'if'", "'('", 
                     "')'", "':'", "'elif'", "'else'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "VAR", "NUMBER", "STRING", 
                      "DIGIT", "LETTER", "ASSIGNMENT_OPERATORS", "ARITHMETIC_OPERATORS", 
                      "ARITHMETIC_FUNCTIONS", "NEWLINE", "WHITE_SPACE", 
                      "CONDITIONAL_OPERATORS" ]

    RULE_start = 0
    RULE_variable = 1
    RULE_conditional = 2
    RULE_if = 3

    ruleNames =  [ "start", "variable", "conditional", "if" ]

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
    VAR=10
    NUMBER=11
    STRING=12
    DIGIT=13
    LETTER=14
    ASSIGNMENT_OPERATORS=15
    ARITHMETIC_OPERATORS=16
    ARITHMETIC_FUNCTIONS=17
    NEWLINE=18
    WHITE_SPACE=19
    CONDITIONAL_OPERATORS=20

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


        def if_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pythonparserParser.IfContext)
            else:
                return self.getTypedRuleContext(pythonparserParser.IfContext,i)


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
            self.state = 12
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4 or _la==10:
                self.state = 10
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [10]:
                    self.state = 8
                    self.variable()
                    pass
                elif token in [4]:
                    self.state = 9
                    self.if_()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 14
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 15
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
            self.state = 17
            self.match(pythonparserParser.VAR)
            self.state = 18
            self.match(pythonparserParser.ASSIGNMENT_OPERATORS)
            self.state = 19
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 138240) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 20
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
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.state = 24
                self.match(pythonparserParser.VAR)
                pass
            elif token in [11]:
                self.state = 25
                self.match(pythonparserParser.NUMBER)
                pass
            elif token in [12]:
                self.state = 26
                self.match(pythonparserParser.STRING)
                pass
            elif token in [17]:
                self.state = 27
                self.match(pythonparserParser.ARITHMETIC_FUNCTIONS)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 41
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 39
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = pythonparserParser.ConditionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional)
                        self.state = 30
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 31
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 32
                        self.conditional(4)
                        pass

                    elif la_ == 2:
                        localctx = pythonparserParser.ConditionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional)
                        self.state = 33
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 34
                        self.match(pythonparserParser.CONDITIONAL_OPERATORS)
                        self.state = 35
                        self.conditional(3)
                        pass

                    elif la_ == 3:
                        localctx = pythonparserParser.ConditionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional)
                        self.state = 36
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 37
                        self.match(pythonparserParser.ARITHMETIC_OPERATORS)
                        self.state = 38
                        self.conditional(2)
                        pass

             
                self.state = 43
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class IfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditional(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pythonparserParser.ConditionalContext)
            else:
                return self.getTypedRuleContext(pythonparserParser.ConditionalContext,i)


        def getRuleIndex(self):
            return pythonparserParser.RULE_if

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)




    def if_(self):

        localctx = pythonparserParser.IfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(pythonparserParser.T__3)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 45
                self.match(pythonparserParser.T__4)


            self.state = 48
            self.conditional(0)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 49
                self.match(pythonparserParser.T__5)


            self.state = 52
            self.match(pythonparserParser.T__6)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 54
                self.match(pythonparserParser.T__7)
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 55
                    self.match(pythonparserParser.T__4)


                self.state = 58
                self.conditional(0)
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==6:
                    self.state = 59
                    self.match(pythonparserParser.T__5)


                self.state = 62
                self.match(pythonparserParser.T__6)
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 69
                self.match(pythonparserParser.T__8)
                self.state = 70
                self.match(pythonparserParser.T__6)


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
         




