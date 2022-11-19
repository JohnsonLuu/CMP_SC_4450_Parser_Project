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
        4,1,14,42,2,0,7,0,2,1,7,1,2,2,7,2,1,0,5,0,8,8,0,10,0,12,0,11,9,0,
        1,0,1,0,1,1,1,1,1,1,1,1,3,1,19,8,1,1,2,1,2,1,2,1,2,1,2,3,2,26,8,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,37,8,2,10,2,12,2,40,9,
        2,1,2,0,1,4,3,0,2,4,0,2,2,0,4,6,11,11,1,0,1,3,46,0,9,1,0,0,0,2,14,
        1,0,0,0,4,25,1,0,0,0,6,8,3,2,1,0,7,6,1,0,0,0,8,11,1,0,0,0,9,7,1,
        0,0,0,9,10,1,0,0,0,10,12,1,0,0,0,11,9,1,0,0,0,12,13,5,0,0,1,13,1,
        1,0,0,0,14,15,5,4,0,0,15,16,5,9,0,0,16,18,7,0,0,0,17,19,5,12,0,0,
        18,17,1,0,0,0,18,19,1,0,0,0,19,3,1,0,0,0,20,21,6,2,-1,0,21,26,5,
        4,0,0,22,26,5,5,0,0,23,26,5,6,0,0,24,26,5,11,0,0,25,20,1,0,0,0,25,
        22,1,0,0,0,25,23,1,0,0,0,25,24,1,0,0,0,26,38,1,0,0,0,27,28,10,3,
        0,0,28,29,7,1,0,0,29,37,3,4,2,4,30,31,10,2,0,0,31,32,5,14,0,0,32,
        37,3,4,2,3,33,34,10,1,0,0,34,35,5,10,0,0,35,37,3,4,2,2,36,27,1,0,
        0,0,36,30,1,0,0,0,36,33,1,0,0,0,37,40,1,0,0,0,38,36,1,0,0,0,38,39,
        1,0,0,0,39,5,1,0,0,0,40,38,1,0,0,0,5,9,18,25,36,38
    ]

class pythonparserParser ( Parser ):

    grammarFileName = "pythonparser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'and'", "'or'", "'not'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "VAR", "NUMBER", "STRING", "DIGIT", "LETTER", "ASSIGNMENT_OPERATORS", 
                      "ARITHMETIC_OPERATORS", "ARITHMETIC_FUNCTIONS", "NEWLINE", 
                      "WHITE_SPACE", "CONDITIONAL_OPERATORS" ]

    RULE_start = 0
    RULE_variable = 1
    RULE_conditional = 2

    ruleNames =  [ "start", "variable", "conditional" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    VAR=4
    NUMBER=5
    STRING=6
    DIGIT=7
    LETTER=8
    ASSIGNMENT_OPERATORS=9
    ARITHMETIC_OPERATORS=10
    ARITHMETIC_FUNCTIONS=11
    NEWLINE=12
    WHITE_SPACE=13
    CONDITIONAL_OPERATORS=14

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
            self.state = 9
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 6
                self.variable()
                self.state = 11
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 12
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
            self.state = 14
            self.match(pythonparserParser.VAR)
            self.state = 15
            self.match(pythonparserParser.ASSIGNMENT_OPERATORS)
            self.state = 16
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 2160) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 18
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 17
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
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.state = 21
                self.match(pythonparserParser.VAR)
                pass
            elif token in [5]:
                self.state = 22
                self.match(pythonparserParser.NUMBER)
                pass
            elif token in [6]:
                self.state = 23
                self.match(pythonparserParser.STRING)
                pass
            elif token in [11]:
                self.state = 24
                self.match(pythonparserParser.ARITHMETIC_FUNCTIONS)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 38
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 36
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = pythonparserParser.ConditionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional)
                        self.state = 27
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 28
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 29
                        self.conditional(4)
                        pass

                    elif la_ == 2:
                        localctx = pythonparserParser.ConditionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional)
                        self.state = 30
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 31
                        self.match(pythonparserParser.CONDITIONAL_OPERATORS)
                        self.state = 32
                        self.conditional(3)
                        pass

                    elif la_ == 3:
                        localctx = pythonparserParser.ConditionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional)
                        self.state = 33
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 34
                        self.match(pythonparserParser.ARITHMETIC_OPERATORS)
                        self.state = 35
                        self.conditional(2)
                        pass

             
                self.state = 40
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
         




