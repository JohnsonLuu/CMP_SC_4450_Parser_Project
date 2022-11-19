// Generated from c:\Users\johns\Downloads\git\CMP_SC_4450_Parser_Project\pythonparser.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class pythonparserParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		VAR=10, NUMBER=11, STRING=12, DIGIT=13, LETTER=14, ASSIGNMENT_OPERATORS=15, 
		ARITHMETIC_OPERATORS=16, ARITHMETIC_FUNCTIONS=17, NEWLINE=18, WHITE_SPACE=19, 
		CONDITIONAL_OPERATORS=20;
	public static final int
		RULE_start = 0, RULE_variable = 1, RULE_conditional = 2, RULE_ifblocks = 3, 
		RULE_block = 4;
	private static String[] makeRuleNames() {
		return new String[] {
			"start", "variable", "conditional", "ifblocks", "block"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'and'", "'or'", "'not'", "'if'", "'('", "')'", "':'", "'elif'", 
			"'else'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, "VAR", "NUMBER", 
			"STRING", "DIGIT", "LETTER", "ASSIGNMENT_OPERATORS", "ARITHMETIC_OPERATORS", 
			"ARITHMETIC_FUNCTIONS", "NEWLINE", "WHITE_SPACE", "CONDITIONAL_OPERATORS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "pythonparser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public pythonparserParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class StartContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(pythonparserParser.EOF, 0); }
		public List<VariableContext> variable() {
			return getRuleContexts(VariableContext.class);
		}
		public VariableContext variable(int i) {
			return getRuleContext(VariableContext.class,i);
		}
		public List<IfblocksContext> ifblocks() {
			return getRuleContexts(IfblocksContext.class);
		}
		public IfblocksContext ifblocks(int i) {
			return getRuleContext(IfblocksContext.class,i);
		}
		public StartContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_start; }
	}

	public final StartContext start() throws RecognitionException {
		StartContext _localctx = new StartContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_start);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(14);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__3 || _la==VAR) {
				{
				setState(12);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case VAR:
					{
					setState(10);
					variable();
					}
					break;
				case T__3:
					{
					setState(11);
					ifblocks();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(16);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(17);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VariableContext extends ParserRuleContext {
		public List<TerminalNode> VAR() { return getTokens(pythonparserParser.VAR); }
		public TerminalNode VAR(int i) {
			return getToken(pythonparserParser.VAR, i);
		}
		public TerminalNode ASSIGNMENT_OPERATORS() { return getToken(pythonparserParser.ASSIGNMENT_OPERATORS, 0); }
		public TerminalNode STRING() { return getToken(pythonparserParser.STRING, 0); }
		public TerminalNode NUMBER() { return getToken(pythonparserParser.NUMBER, 0); }
		public TerminalNode ARITHMETIC_FUNCTIONS() { return getToken(pythonparserParser.ARITHMETIC_FUNCTIONS, 0); }
		public TerminalNode NEWLINE() { return getToken(pythonparserParser.NEWLINE, 0); }
		public VariableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable; }
	}

	public final VariableContext variable() throws RecognitionException {
		VariableContext _localctx = new VariableContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_variable);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(19);
			match(VAR);
			setState(20);
			match(ASSIGNMENT_OPERATORS);
			setState(21);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << VAR) | (1L << NUMBER) | (1L << STRING) | (1L << ARITHMETIC_FUNCTIONS))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(23);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				{
				setState(22);
				match(NEWLINE);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ConditionalContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(pythonparserParser.VAR, 0); }
		public TerminalNode NUMBER() { return getToken(pythonparserParser.NUMBER, 0); }
		public TerminalNode STRING() { return getToken(pythonparserParser.STRING, 0); }
		public TerminalNode ARITHMETIC_FUNCTIONS() { return getToken(pythonparserParser.ARITHMETIC_FUNCTIONS, 0); }
		public List<ConditionalContext> conditional() {
			return getRuleContexts(ConditionalContext.class);
		}
		public ConditionalContext conditional(int i) {
			return getRuleContext(ConditionalContext.class,i);
		}
		public TerminalNode CONDITIONAL_OPERATORS() { return getToken(pythonparserParser.CONDITIONAL_OPERATORS, 0); }
		public TerminalNode ARITHMETIC_OPERATORS() { return getToken(pythonparserParser.ARITHMETIC_OPERATORS, 0); }
		public ConditionalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_conditional; }
	}

	public final ConditionalContext conditional() throws RecognitionException {
		return conditional(0);
	}

	private ConditionalContext conditional(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ConditionalContext _localctx = new ConditionalContext(_ctx, _parentState);
		ConditionalContext _prevctx = _localctx;
		int _startState = 4;
		enterRecursionRule(_localctx, 4, RULE_conditional, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(30);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VAR:
				{
				setState(26);
				match(VAR);
				}
				break;
			case NUMBER:
				{
				setState(27);
				match(NUMBER);
				}
				break;
			case STRING:
				{
				setState(28);
				match(STRING);
				}
				break;
			case ARITHMETIC_FUNCTIONS:
				{
				setState(29);
				match(ARITHMETIC_FUNCTIONS);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(43);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(41);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
					case 1:
						{
						_localctx = new ConditionalContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditional);
						setState(32);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(33);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__1) | (1L << T__2))) != 0)) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(34);
						conditional(4);
						}
						break;
					case 2:
						{
						_localctx = new ConditionalContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditional);
						setState(35);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(36);
						match(CONDITIONAL_OPERATORS);
						setState(37);
						conditional(3);
						}
						break;
					case 3:
						{
						_localctx = new ConditionalContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditional);
						setState(38);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(39);
						match(ARITHMETIC_OPERATORS);
						setState(40);
						conditional(2);
						}
						break;
					}
					} 
				}
				setState(45);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class IfblocksContext extends ParserRuleContext {
		public List<ConditionalContext> conditional() {
			return getRuleContexts(ConditionalContext.class);
		}
		public ConditionalContext conditional(int i) {
			return getRuleContext(ConditionalContext.class,i);
		}
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public IfblocksContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifblocks; }
	}

	public final IfblocksContext ifblocks() throws RecognitionException {
		IfblocksContext _localctx = new IfblocksContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_ifblocks);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(46);
			match(T__3);
			setState(48);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__4) {
				{
				setState(47);
				match(T__4);
				}
			}

			setState(50);
			conditional(0);
			setState(52);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__5) {
				{
				setState(51);
				match(T__5);
				}
			}

			setState(54);
			match(T__6);
			setState(55);
			block();
			}
			setState(70);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(57);
					match(T__7);
					setState(59);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==T__4) {
						{
						setState(58);
						match(T__4);
						}
					}

					setState(61);
					conditional(0);
					setState(63);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==T__5) {
						{
						setState(62);
						match(T__5);
						}
					}

					setState(65);
					match(T__6);
					setState(66);
					block();
					}
					} 
				}
				setState(72);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			}
			setState(76);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				{
				setState(73);
				match(T__8);
				setState(74);
				match(T__6);
				setState(75);
				block();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BlockContext extends ParserRuleContext {
		public List<VariableContext> variable() {
			return getRuleContexts(VariableContext.class);
		}
		public VariableContext variable(int i) {
			return getRuleContext(VariableContext.class,i);
		}
		public List<IfblocksContext> ifblocks() {
			return getRuleContexts(IfblocksContext.class);
		}
		public IfblocksContext ifblocks(int i) {
			return getRuleContext(IfblocksContext.class,i);
		}
		public TerminalNode NEWLINE() { return getToken(pythonparserParser.NEWLINE, 0); }
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_block);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(80); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					setState(80);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case VAR:
						{
						setState(78);
						variable();
						}
						break;
					case T__3:
						{
						setState(79);
						ifblocks();
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(82); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			setState(85);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				{
				setState(84);
				match(NEWLINE);
				}
				break;
			}
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 2:
			return conditional_sempred((ConditionalContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean conditional_sempred(ConditionalContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 3);
		case 1:
			return precpred(_ctx, 2);
		case 2:
			return precpred(_ctx, 1);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26Z\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\7\2\17\n\2\f\2\16\2\22\13\2\3\2\3\2"+
		"\3\3\3\3\3\3\3\3\5\3\32\n\3\3\4\3\4\3\4\3\4\3\4\5\4!\n\4\3\4\3\4\3\4\3"+
		"\4\3\4\3\4\3\4\3\4\3\4\7\4,\n\4\f\4\16\4/\13\4\3\5\3\5\5\5\63\n\5\3\5"+
		"\3\5\5\5\67\n\5\3\5\3\5\3\5\3\5\3\5\5\5>\n\5\3\5\3\5\5\5B\n\5\3\5\3\5"+
		"\3\5\7\5G\n\5\f\5\16\5J\13\5\3\5\3\5\3\5\5\5O\n\5\3\6\3\6\6\6S\n\6\r\6"+
		"\16\6T\3\6\5\6X\n\6\3\6\2\3\6\7\2\4\6\b\n\2\4\4\2\f\16\23\23\3\2\3\5\2"+
		"f\2\20\3\2\2\2\4\25\3\2\2\2\6 \3\2\2\2\b\60\3\2\2\2\nR\3\2\2\2\f\17\5"+
		"\4\3\2\r\17\5\b\5\2\16\f\3\2\2\2\16\r\3\2\2\2\17\22\3\2\2\2\20\16\3\2"+
		"\2\2\20\21\3\2\2\2\21\23\3\2\2\2\22\20\3\2\2\2\23\24\7\2\2\3\24\3\3\2"+
		"\2\2\25\26\7\f\2\2\26\27\7\21\2\2\27\31\t\2\2\2\30\32\7\24\2\2\31\30\3"+
		"\2\2\2\31\32\3\2\2\2\32\5\3\2\2\2\33\34\b\4\1\2\34!\7\f\2\2\35!\7\r\2"+
		"\2\36!\7\16\2\2\37!\7\23\2\2 \33\3\2\2\2 \35\3\2\2\2 \36\3\2\2\2 \37\3"+
		"\2\2\2!-\3\2\2\2\"#\f\5\2\2#$\t\3\2\2$,\5\6\4\6%&\f\4\2\2&\'\7\26\2\2"+
		"\',\5\6\4\5()\f\3\2\2)*\7\22\2\2*,\5\6\4\4+\"\3\2\2\2+%\3\2\2\2+(\3\2"+
		"\2\2,/\3\2\2\2-+\3\2\2\2-.\3\2\2\2.\7\3\2\2\2/-\3\2\2\2\60\62\7\6\2\2"+
		"\61\63\7\7\2\2\62\61\3\2\2\2\62\63\3\2\2\2\63\64\3\2\2\2\64\66\5\6\4\2"+
		"\65\67\7\b\2\2\66\65\3\2\2\2\66\67\3\2\2\2\678\3\2\2\289\7\t\2\29:\5\n"+
		"\6\2:H\3\2\2\2;=\7\n\2\2<>\7\7\2\2=<\3\2\2\2=>\3\2\2\2>?\3\2\2\2?A\5\6"+
		"\4\2@B\7\b\2\2A@\3\2\2\2AB\3\2\2\2BC\3\2\2\2CD\7\t\2\2DE\5\n\6\2EG\3\2"+
		"\2\2F;\3\2\2\2GJ\3\2\2\2HF\3\2\2\2HI\3\2\2\2IN\3\2\2\2JH\3\2\2\2KL\7\13"+
		"\2\2LM\7\t\2\2MO\5\n\6\2NK\3\2\2\2NO\3\2\2\2O\t\3\2\2\2PS\5\4\3\2QS\5"+
		"\b\5\2RP\3\2\2\2RQ\3\2\2\2ST\3\2\2\2TR\3\2\2\2TU\3\2\2\2UW\3\2\2\2VX\7"+
		"\24\2\2WV\3\2\2\2WX\3\2\2\2X\13\3\2\2\2\21\16\20\31 +-\62\66=AHNRTW";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}