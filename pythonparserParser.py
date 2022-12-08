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
        4,1,29,148,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,0,1,
        0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,35,8,1,1,2,1,2,1,2,1,2,3,2,41,8,2,
        1,3,1,3,1,3,1,3,1,3,3,3,48,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,5,3,59,8,3,10,3,12,3,62,9,3,1,4,1,4,3,4,66,8,4,1,4,1,4,3,4,70,
        8,4,1,4,1,4,1,4,1,4,1,4,3,4,77,8,4,1,4,1,4,3,4,81,8,4,1,4,1,4,1,
        4,5,4,86,8,4,10,4,12,4,89,9,4,1,4,1,4,1,4,3,4,94,8,4,1,5,4,5,97,
        8,5,11,5,12,5,98,1,5,3,5,102,8,5,1,5,3,5,105,8,5,1,5,3,5,108,8,5,
        1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        3,8,126,8,8,3,8,128,8,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,3,9,138,
        8,9,5,9,140,8,9,10,9,12,9,143,9,9,1,9,1,9,1,9,1,9,0,1,6,10,0,2,4,
        6,8,10,12,14,16,18,0,4,2,0,18,20,25,25,1,0,1,3,2,0,18,19,25,25,1,
        0,18,19,164,0,23,1,0,0,0,2,34,1,0,0,0,4,36,1,0,0,0,6,47,1,0,0,0,
        8,63,1,0,0,0,10,104,1,0,0,0,12,109,1,0,0,0,14,114,1,0,0,0,16,116,
        1,0,0,0,18,132,1,0,0,0,20,22,3,2,1,0,21,20,1,0,0,0,22,25,1,0,0,0,
        23,21,1,0,0,0,23,24,1,0,0,0,24,26,1,0,0,0,25,23,1,0,0,0,26,27,5,
        0,0,1,27,1,1,0,0,0,28,35,3,4,2,0,29,35,3,8,4,0,30,35,3,12,6,0,31,
        35,3,14,7,0,32,35,3,16,8,0,33,35,3,18,9,0,34,28,1,0,0,0,34,29,1,
        0,0,0,34,30,1,0,0,0,34,31,1,0,0,0,34,32,1,0,0,0,34,33,1,0,0,0,35,
        3,1,0,0,0,36,37,5,18,0,0,37,38,5,23,0,0,38,40,7,0,0,0,39,41,5,26,
        0,0,40,39,1,0,0,0,40,41,1,0,0,0,41,5,1,0,0,0,42,43,6,3,-1,0,43,48,
        5,18,0,0,44,48,5,19,0,0,45,48,5,20,0,0,46,48,5,25,0,0,47,42,1,0,
        0,0,47,44,1,0,0,0,47,45,1,0,0,0,47,46,1,0,0,0,48,60,1,0,0,0,49,50,
        10,3,0,0,50,51,7,1,0,0,51,59,3,6,3,4,52,53,10,2,0,0,53,54,5,28,0,
        0,54,59,3,6,3,3,55,56,10,1,0,0,56,57,5,24,0,0,57,59,3,6,3,2,58,49,
        1,0,0,0,58,52,1,0,0,0,58,55,1,0,0,0,59,62,1,0,0,0,60,58,1,0,0,0,
        60,61,1,0,0,0,61,7,1,0,0,0,62,60,1,0,0,0,63,65,5,4,0,0,64,66,5,5,
        0,0,65,64,1,0,0,0,65,66,1,0,0,0,66,67,1,0,0,0,67,69,3,6,3,0,68,70,
        5,6,0,0,69,68,1,0,0,0,69,70,1,0,0,0,70,71,1,0,0,0,71,72,5,7,0,0,
        72,73,3,10,5,0,73,87,1,0,0,0,74,76,5,8,0,0,75,77,5,5,0,0,76,75,1,
        0,0,0,76,77,1,0,0,0,77,78,1,0,0,0,78,80,3,6,3,0,79,81,5,6,0,0,80,
        79,1,0,0,0,80,81,1,0,0,0,81,82,1,0,0,0,82,83,5,7,0,0,83,84,3,10,
        5,0,84,86,1,0,0,0,85,74,1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,87,88,
        1,0,0,0,88,93,1,0,0,0,89,87,1,0,0,0,90,91,5,9,0,0,91,92,5,7,0,0,
        92,94,3,10,5,0,93,90,1,0,0,0,93,94,1,0,0,0,94,9,1,0,0,0,95,97,3,
        2,1,0,96,95,1,0,0,0,97,98,1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,
        101,1,0,0,0,100,102,5,10,0,0,101,100,1,0,0,0,101,102,1,0,0,0,102,
        105,1,0,0,0,103,105,5,10,0,0,104,96,1,0,0,0,104,103,1,0,0,0,105,
        107,1,0,0,0,106,108,5,26,0,0,107,106,1,0,0,0,107,108,1,0,0,0,108,
        11,1,0,0,0,109,110,5,11,0,0,110,111,3,6,3,0,111,112,5,7,0,0,112,
        113,3,10,5,0,113,13,1,0,0,0,114,115,5,29,0,0,115,15,1,0,0,0,116,
        117,5,12,0,0,117,118,5,18,0,0,118,127,5,13,0,0,119,128,5,18,0,0,
        120,125,5,14,0,0,121,126,5,19,0,0,122,123,7,2,0,0,123,124,5,15,0,
        0,124,126,7,2,0,0,125,121,1,0,0,0,125,122,1,0,0,0,126,128,1,0,0,
        0,127,119,1,0,0,0,127,120,1,0,0,0,128,129,1,0,0,0,129,130,5,16,0,
        0,130,131,3,10,5,0,131,17,1,0,0,0,132,133,5,17,0,0,133,134,5,18,
        0,0,134,141,5,5,0,0,135,137,7,3,0,0,136,138,5,15,0,0,137,136,1,0,
        0,0,137,138,1,0,0,0,138,140,1,0,0,0,139,135,1,0,0,0,140,143,1,0,
        0,0,141,139,1,0,0,0,141,142,1,0,0,0,142,144,1,0,0,0,143,141,1,0,
        0,0,144,145,5,16,0,0,145,146,3,10,5,0,146,19,1,0,0,0,20,23,34,40,
        47,58,60,65,69,76,80,87,93,98,101,104,107,125,127,137,141
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

    ruleNames =  [ "start", "definitions", "variable", "conditional", "ifblocks", 
                   "block", "whileloop", "comment", "forloop", "function" ]

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
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 537270288) != 0:
                self.state = 20
                self.definitions()
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
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.variable()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.ifblocks()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.whileloop()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 4)
                self.state = 31
                self.comment()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 32
                self.forloop()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 6)
                self.state = 33
                self.function()
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
            self.state = 36
            self.match(pythonparserParser.VAR)
            self.state = 37
            self.match(pythonparserParser.ASSIGN_OP)
            self.state = 38
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 35389440) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 40
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 39
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
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.state = 43
                self.match(pythonparserParser.VAR)
                pass
            elif token in [19]:
                self.state = 44
                self.match(pythonparserParser.NUMBER)
                pass
            elif token in [20]:
                self.state = 45
                self.match(pythonparserParser.STRING)
                pass
            elif token in [25]:
                self.state = 46
                self.match(pythonparserParser.ARITH_FUNC)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 60
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 58
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = pythonparserParser.ConditionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional)
                        self.state = 49
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 50
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 51
                        self.conditional(4)
                        pass

                    elif la_ == 2:
                        localctx = pythonparserParser.ConditionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional)
                        self.state = 52
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 53
                        self.match(pythonparserParser.COND_OP)
                        self.state = 54
                        self.conditional(3)
                        pass

                    elif la_ == 3:
                        localctx = pythonparserParser.ConditionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional)
                        self.state = 55
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 56
                        self.match(pythonparserParser.ARITH_OP)
                        self.state = 57
                        self.conditional(2)
                        pass

             
                self.state = 62
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
            self.state = 63
            self.match(pythonparserParser.T__3)
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
            self.state = 87
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 74
                    self.match(pythonparserParser.T__7)
                    self.state = 76
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==5:
                        self.state = 75
                        self.match(pythonparserParser.T__4)


                    self.state = 78
                    self.conditional(0)
                    self.state = 80
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==6:
                        self.state = 79
                        self.match(pythonparserParser.T__5)


                    self.state = 82
                    self.match(pythonparserParser.T__6)
                    self.state = 83
                    self.block() 
                self.state = 89
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 90
                self.match(pythonparserParser.T__8)
                self.state = 91
                self.match(pythonparserParser.T__6)
                self.state = 92
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
            self.state = 104
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 11, 12, 17, 18, 29]:
                self.state = 96 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 95
                        self.definitions()

                    else:
                        raise NoViableAltException(self)
                    self.state = 98 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                self.state = 101
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 100
                    self.match(pythonparserParser.T__9)


                pass
            elif token in [10]:
                self.state = 103
                self.match(pythonparserParser.T__9)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 106
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
            self.state = 109
            self.match(pythonparserParser.T__10)
            self.state = 110
            self.conditional(0)
            self.state = 111
            self.match(pythonparserParser.T__6)
            self.state = 112
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
            self.state = 114
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
            self.state = 116
            self.match(pythonparserParser.T__11)
            self.state = 117
            self.match(pythonparserParser.VAR)
            self.state = 118
            self.match(pythonparserParser.T__12)
            self.state = 127
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.state = 119
                self.match(pythonparserParser.VAR)
                pass
            elif token in [14]:
                self.state = 120
                self.match(pythonparserParser.T__13)
                self.state = 125
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 121
                    self.match(pythonparserParser.NUMBER)
                    pass

                elif la_ == 2:
                    self.state = 122
                    _la = self._input.LA(1)
                    if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 34340864) != 0):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 123
                    self.match(pythonparserParser.T__14)
                    self.state = 124
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

            self.state = 129
            self.match(pythonparserParser.T__15)
            self.state = 130
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
            self.state = 132
            self.match(pythonparserParser.T__16)
            self.state = 133
            self.match(pythonparserParser.VAR)
            self.state = 134
            self.match(pythonparserParser.T__4)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18 or _la==19:
                self.state = 135
                _la = self._input.LA(1)
                if not(_la==18 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==15:
                    self.state = 136
                    self.match(pythonparserParser.T__14)


                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 144
            self.match(pythonparserParser.T__15)
            self.state = 145
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
         




