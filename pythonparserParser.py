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
        2,3,2,44,8,2,1,3,1,3,1,3,1,3,1,3,3,3,51,8,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,5,3,62,8,3,10,3,12,3,65,9,3,1,4,1,4,3,4,69,8,4,1,
        4,1,4,3,4,73,8,4,1,4,1,4,1,4,1,4,1,4,3,4,80,8,4,1,4,1,4,3,4,84,8,
        4,1,4,1,4,1,4,5,4,89,8,4,10,4,12,4,92,9,4,1,4,1,4,1,4,3,4,97,8,4,
        1,5,4,5,100,8,5,11,5,12,5,101,1,5,3,5,105,8,5,1,5,3,5,108,8,5,1,
        5,3,5,111,8,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,3,8,129,8,8,3,8,131,8,8,1,8,1,8,1,8,1,9,1,9,1,9,1,
        9,1,9,3,9,141,8,9,5,9,143,8,9,10,9,12,9,146,9,9,1,9,1,9,1,9,1,10,
        1,10,1,10,1,10,1,10,1,10,3,10,157,8,10,1,10,3,10,160,8,10,5,10,162,
        8,10,10,10,12,10,165,9,10,1,10,1,10,1,10,0,1,6,11,0,2,4,6,8,10,12,
        14,16,18,20,0,4,2,0,18,20,25,25,1,0,1,3,2,0,18,19,25,25,1,0,18,19,
        190,0,25,1,0,0,0,2,37,1,0,0,0,4,39,1,0,0,0,6,50,1,0,0,0,8,66,1,0,
        0,0,10,107,1,0,0,0,12,112,1,0,0,0,14,117,1,0,0,0,16,119,1,0,0,0,
        18,135,1,0,0,0,20,150,1,0,0,0,22,24,3,2,1,0,23,22,1,0,0,0,24,27,
        1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,28,1,0,0,0,27,25,1,0,0,0,
        28,29,5,0,0,1,29,1,1,0,0,0,30,38,3,4,2,0,31,38,3,8,4,0,32,38,3,12,
        6,0,33,38,3,14,7,0,34,38,3,16,8,0,35,38,3,18,9,0,36,38,3,20,10,0,
        37,30,1,0,0,0,37,31,1,0,0,0,37,32,1,0,0,0,37,33,1,0,0,0,37,34,1,
        0,0,0,37,35,1,0,0,0,37,36,1,0,0,0,38,3,1,0,0,0,39,40,5,18,0,0,40,
        41,5,23,0,0,41,43,7,0,0,0,42,44,5,26,0,0,43,42,1,0,0,0,43,44,1,0,
        0,0,44,5,1,0,0,0,45,46,6,3,-1,0,46,51,5,18,0,0,47,51,5,19,0,0,48,
        51,5,20,0,0,49,51,5,25,0,0,50,45,1,0,0,0,50,47,1,0,0,0,50,48,1,0,
        0,0,50,49,1,0,0,0,51,63,1,0,0,0,52,53,10,3,0,0,53,54,7,1,0,0,54,
        62,3,6,3,4,55,56,10,2,0,0,56,57,5,28,0,0,57,62,3,6,3,3,58,59,10,
        1,0,0,59,60,5,24,0,0,60,62,3,6,3,2,61,52,1,0,0,0,61,55,1,0,0,0,61,
        58,1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,7,1,0,0,
        0,65,63,1,0,0,0,66,68,5,4,0,0,67,69,5,5,0,0,68,67,1,0,0,0,68,69,
        1,0,0,0,69,70,1,0,0,0,70,72,3,6,3,0,71,73,5,6,0,0,72,71,1,0,0,0,
        72,73,1,0,0,0,73,74,1,0,0,0,74,75,5,7,0,0,75,76,3,10,5,0,76,90,1,
        0,0,0,77,79,5,8,0,0,78,80,5,5,0,0,79,78,1,0,0,0,79,80,1,0,0,0,80,
        81,1,0,0,0,81,83,3,6,3,0,82,84,5,6,0,0,83,82,1,0,0,0,83,84,1,0,0,
        0,84,85,1,0,0,0,85,86,5,7,0,0,86,87,3,10,5,0,87,89,1,0,0,0,88,77,
        1,0,0,0,89,92,1,0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,96,1,0,0,0,
        92,90,1,0,0,0,93,94,5,9,0,0,94,95,5,7,0,0,95,97,3,10,5,0,96,93,1,
        0,0,0,96,97,1,0,0,0,97,9,1,0,0,0,98,100,3,2,1,0,99,98,1,0,0,0,100,
        101,1,0,0,0,101,99,1,0,0,0,101,102,1,0,0,0,102,104,1,0,0,0,103,105,
        5,10,0,0,104,103,1,0,0,0,104,105,1,0,0,0,105,108,1,0,0,0,106,108,
        5,10,0,0,107,99,1,0,0,0,107,106,1,0,0,0,108,110,1,0,0,0,109,111,
        5,26,0,0,110,109,1,0,0,0,110,111,1,0,0,0,111,11,1,0,0,0,112,113,
        5,11,0,0,113,114,3,6,3,0,114,115,5,7,0,0,115,116,3,10,5,0,116,13,
        1,0,0,0,117,118,5,29,0,0,118,15,1,0,0,0,119,120,5,12,0,0,120,121,
        5,18,0,0,121,130,5,13,0,0,122,131,5,18,0,0,123,128,5,14,0,0,124,
        129,5,19,0,0,125,126,7,2,0,0,126,127,5,15,0,0,127,129,7,2,0,0,128,
        124,1,0,0,0,128,125,1,0,0,0,129,131,1,0,0,0,130,122,1,0,0,0,130,
        123,1,0,0,0,131,132,1,0,0,0,132,133,5,16,0,0,133,134,3,10,5,0,134,
        17,1,0,0,0,135,136,5,17,0,0,136,137,5,18,0,0,137,144,5,5,0,0,138,
        140,7,3,0,0,139,141,5,15,0,0,140,139,1,0,0,0,140,141,1,0,0,0,141,
        143,1,0,0,0,142,138,1,0,0,0,143,146,1,0,0,0,144,142,1,0,0,0,144,
        145,1,0,0,0,145,147,1,0,0,0,146,144,1,0,0,0,147,148,5,16,0,0,148,
        149,3,10,5,0,149,19,1,0,0,0,150,151,5,18,0,0,151,163,5,5,0,0,152,
        157,5,18,0,0,153,157,5,19,0,0,154,157,5,25,0,0,155,157,3,20,10,0,
        156,152,1,0,0,0,156,153,1,0,0,0,156,154,1,0,0,0,156,155,1,0,0,0,
        157,159,1,0,0,0,158,160,5,15,0,0,159,158,1,0,0,0,159,160,1,0,0,0,
        160,162,1,0,0,0,161,156,1,0,0,0,162,165,1,0,0,0,163,161,1,0,0,0,
        163,164,1,0,0,0,164,166,1,0,0,0,165,163,1,0,0,0,166,167,5,6,0,0,
        167,21,1,0,0,0,23,25,37,43,50,61,63,68,72,79,83,90,96,101,104,107,
        110,128,130,140,144,156,159,163
    ]

class pythonparserParser ( Parser ):

    grammarFileName = "pythonparser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'and'", "'or'", "'not'", "'if'", "'('", 
                     "')'", "':'", "'elif'", "'else'", "'break'", "'while'", 
                     "'for'", "'in'", "'range('", "','", "'):'", "'def'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "VAR", "NUMBER", "STRING", 
                      "DIGIT", "LETTER", "ASSIGN_OP", "ARITH_OP", "ARITH_FUNC", 
                      "NEWLINE", "WHITE_SPACE", "COND_OP", "COMMENT" ]

    RULE_start = 0
    RULE_definitions = 1
    RULE_variable = 2
    RULE_conditional = 3
    RULE_ifblocks = 4
    RULE_block = 5
    RULE_whileloop = 6
    RULE_comment = 7
    RULE_forloop = 8
    RULE_function = 9
    RULE_functioncall = 10

    ruleNames =  [ "start", "definitions", "variable", "conditional", "ifblocks", 
                   "block", "whileloop", "comment", "forloop", "function", 
                   "functioncall" ]

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
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 537270288) != 0:
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
        self.enterRule(localctx, 4, self.RULE_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(pythonparserParser.VAR)
            self.state = 40
            self.match(pythonparserParser.ASSIGN_OP)
            self.state = 41
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 35389440) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 43
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 42
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
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_conditional, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.state = 46
                self.match(pythonparserParser.VAR)
                pass
            elif token in [19]:
                self.state = 47
                self.match(pythonparserParser.NUMBER)
                pass
            elif token in [20]:
                self.state = 48
                self.match(pythonparserParser.STRING)
                pass
            elif token in [25]:
                self.state = 49
                self.match(pythonparserParser.ARITH_FUNC)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 63
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 61
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = pythonparserParser.ConditionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional)
                        self.state = 52
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 53
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 54
                        self.conditional(4)
                        pass

                    elif la_ == 2:
                        localctx = pythonparserParser.ConditionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional)
                        self.state = 55
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 56
                        self.match(pythonparserParser.COND_OP)
                        self.state = 57
                        self.conditional(3)
                        pass

                    elif la_ == 3:
                        localctx = pythonparserParser.ConditionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional)
                        self.state = 58
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 59
                        self.match(pythonparserParser.ARITH_OP)
                        self.state = 60
                        self.conditional(2)
                        pass

             
                self.state = 65
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
            self.state = 66
            self.match(pythonparserParser.T__3)
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
            self.state = 90
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 77
                    self.match(pythonparserParser.T__7)
                    self.state = 79
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==5:
                        self.state = 78
                        self.match(pythonparserParser.T__4)


                    self.state = 81
                    self.conditional(0)
                    self.state = 83
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==6:
                        self.state = 82
                        self.match(pythonparserParser.T__5)


                    self.state = 85
                    self.match(pythonparserParser.T__6)
                    self.state = 86
                    self.block() 
                self.state = 92
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 93
                self.match(pythonparserParser.T__8)
                self.state = 94
                self.match(pythonparserParser.T__6)
                self.state = 95
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
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 11, 12, 17, 18, 29]:
                self.state = 99 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 98
                        self.definitions()

                    else:
                        raise NoViableAltException(self)
                    self.state = 101 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                self.state = 104
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 103
                    self.match(pythonparserParser.T__9)


                pass
            elif token in [10]:
                self.state = 106
                self.match(pythonparserParser.T__9)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 110
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 109
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
            self.state = 112
            self.match(pythonparserParser.T__10)
            self.state = 113
            self.conditional(0)
            self.state = 114
            self.match(pythonparserParser.T__6)
            self.state = 115
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
            self.state = 117
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
        self.enterRule(localctx, 16, self.RULE_forloop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(pythonparserParser.T__11)
            self.state = 120
            self.match(pythonparserParser.VAR)
            self.state = 121
            self.match(pythonparserParser.T__12)
            self.state = 130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.state = 122
                self.match(pythonparserParser.VAR)
                pass
            elif token in [14]:
                self.state = 123
                self.match(pythonparserParser.T__13)
                self.state = 128
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 124
                    self.match(pythonparserParser.NUMBER)
                    pass

                elif la_ == 2:
                    self.state = 125
                    _la = self._input.LA(1)
                    if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 34340864) != 0):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 126
                    self.match(pythonparserParser.T__14)
                    self.state = 127
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

            self.state = 132
            self.match(pythonparserParser.T__15)
            self.state = 133
            self.block()
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


        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(pythonparserParser.NUMBER)
            else:
                return self.getToken(pythonparserParser.NUMBER, i)

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
        self.enterRule(localctx, 18, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(pythonparserParser.T__16)
            self.state = 136
            self.match(pythonparserParser.VAR)
            self.state = 137
            self.match(pythonparserParser.T__4)
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18 or _la==19:
                self.state = 138
                _la = self._input.LA(1)
                if not(_la==18 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==15:
                    self.state = 139
                    self.match(pythonparserParser.T__14)


                self.state = 146
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 147
            self.match(pythonparserParser.T__15)
            self.state = 148
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
        self.enterRule(localctx, 20, self.RULE_functioncall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(pythonparserParser.VAR)
            self.state = 151
            self.match(pythonparserParser.T__4)
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 34340864) != 0:
                self.state = 156
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                if la_ == 1:
                    self.state = 152
                    self.match(pythonparserParser.VAR)
                    pass

                elif la_ == 2:
                    self.state = 153
                    self.match(pythonparserParser.NUMBER)
                    pass

                elif la_ == 3:
                    self.state = 154
                    self.match(pythonparserParser.ARITH_FUNC)
                    pass

                elif la_ == 4:
                    self.state = 155
                    self.functioncall()
                    pass


                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==15:
                    self.state = 158
                    self.match(pythonparserParser.T__14)


                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 166
            self.match(pythonparserParser.T__5)
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
         




