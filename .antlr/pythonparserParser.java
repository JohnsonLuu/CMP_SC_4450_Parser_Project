// Generated from c:\Users\johns\Downloads\new\CMP_SC_4450_Parser_Project\pythonparser.g4 by ANTLR 4.9.2
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
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, VAR=17, 
		NUMBER=18, STRING=19, DIGIT=20, LETTER=21, ASSIGNMENT_OPERATORS=22, ARITHMETIC_OPERATORS=23, 
		ARITHMETIC_FUNCTIONS=24, NEWLINE=25, WHITE_SPACE=26, CONDITIONAL_OPERATORS=27;
	public static final int
		RULE_start = 0, RULE_variable = 1, RULE_conditional = 2, RULE_ifblocks = 3, 
		RULE_block = 4, RULE_whileloop = 5, RULE_comment = 6, RULE_forloop = 7;
	private static String[] makeRuleNames() {
		return new String[] {
			"start", "variable", "conditional", "ifblocks", "block", "whileloop", 
			"comment", "forloop"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'and'", "'or'", "'not'", "'if'", "'('", "')'", "':'", "'elif'", 
			"'else'", "'while'", "'#'", "'\n'", "'for'", "'in'", "'range('", "','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, "VAR", "NUMBER", "STRING", "DIGIT", "LETTER", 
			"ASSIGNMENT_OPERATORS", "ARITHMETIC_OPERATORS", "ARITHMETIC_FUNCTIONS", 
			"NEWLINE", "WHITE_SPACE", "CONDITIONAL_OPERATORS"
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
		public List<WhileloopContext> whileloop() {
			return getRuleContexts(WhileloopContext.class);
		}
		public WhileloopContext whileloop(int i) {
			return getRuleContext(WhileloopContext.class,i);
		}
		public List<CommentContext> comment() {
			return getRuleContexts(CommentContext.class);
		}
		public CommentContext comment(int i) {
			return getRuleContext(CommentContext.class,i);
		}
		public List<ForloopContext> forloop() {
			return getRuleContexts(ForloopContext.class);
		}
		public ForloopContext forloop(int i) {
			return getRuleContext(ForloopContext.class,i);
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
			setState(23);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__3) | (1L << T__9) | (1L << T__10) | (1L << T__12) | (1L << VAR))) != 0)) {
				{
				setState(21);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case VAR:
					{
					setState(16);
					variable();
					}
					break;
				case T__3:
					{
					setState(17);
					ifblocks();
					}
					break;
				case T__9:
					{
					setState(18);
					whileloop();
					}
					break;
				case T__10:
					{
					setState(19);
					comment();
					}
					break;
				case T__12:
					{
					setState(20);
					forloop();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(25);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(26);
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
			setState(28);
			match(VAR);
			setState(29);
			match(ASSIGNMENT_OPERATORS);
			setState(30);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << VAR) | (1L << NUMBER) | (1L << STRING) | (1L << ARITHMETIC_FUNCTIONS))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(32);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				{
				setState(31);
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
			setState(39);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VAR:
				{
				setState(35);
				match(VAR);
				}
				break;
			case NUMBER:
				{
				setState(36);
				match(NUMBER);
				}
				break;
			case STRING:
				{
				setState(37);
				match(STRING);
				}
				break;
			case ARITHMETIC_FUNCTIONS:
				{
				setState(38);
				match(ARITHMETIC_FUNCTIONS);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(52);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(50);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
					case 1:
						{
						_localctx = new ConditionalContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditional);
						setState(41);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(42);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__1) | (1L << T__2))) != 0)) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(43);
						conditional(4);
						}
						break;
					case 2:
						{
						_localctx = new ConditionalContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditional);
						setState(44);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(45);
						match(CONDITIONAL_OPERATORS);
						setState(46);
						conditional(3);
						}
						break;
					case 3:
						{
						_localctx = new ConditionalContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditional);
						setState(47);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(48);
						match(ARITHMETIC_OPERATORS);
						setState(49);
						conditional(2);
						}
						break;
					}
					} 
				}
				setState(54);
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
			setState(55);
			match(T__3);
			setState(57);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__4) {
				{
				setState(56);
				match(T__4);
				}
			}

			setState(59);
			conditional(0);
			setState(61);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__5) {
				{
				setState(60);
				match(T__5);
				}
			}

			setState(63);
			match(T__6);
			setState(64);
			block();
			}
			setState(79);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(66);
					match(T__7);
					setState(68);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==T__4) {
						{
						setState(67);
						match(T__4);
						}
					}

					setState(70);
					conditional(0);
					setState(72);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==T__5) {
						{
						setState(71);
						match(T__5);
						}
					}

					setState(74);
					match(T__6);
					setState(75);
					block();
					}
					} 
				}
				setState(81);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			}
			setState(85);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				{
				setState(82);
				match(T__8);
				setState(83);
				match(T__6);
				setState(84);
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
			setState(89); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					setState(89);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case VAR:
						{
						setState(87);
						variable();
						}
						break;
					case T__3:
						{
						setState(88);
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
				setState(91); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			setState(94);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				{
				setState(93);
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

	public static class WhileloopContext extends ParserRuleContext {
		public ConditionalContext conditional() {
			return getRuleContext(ConditionalContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public WhileloopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileloop; }
	}

	public final WhileloopContext whileloop() throws RecognitionException {
		WhileloopContext _localctx = new WhileloopContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_whileloop);
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(96);
			match(T__9);
			setState(97);
			conditional(0);
			setState(98);
			match(T__6);
			setState(99);
			block();
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

	public static class CommentContext extends ParserRuleContext {
		public CommentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comment; }
	}

	public final CommentContext comment() throws RecognitionException {
		CommentContext _localctx = new CommentContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_comment);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(101);
			match(T__10);
			setState(105);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(102);
					_la = _input.LA(1);
					if ( _la <= 0 || (_la==T__11) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					}
					} 
				}
				setState(107);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
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

	public static class ForloopContext extends ParserRuleContext {
		public List<TerminalNode> VAR() { return getTokens(pythonparserParser.VAR); }
		public TerminalNode VAR(int i) {
			return getToken(pythonparserParser.VAR, i);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public List<TerminalNode> NUMBER() { return getTokens(pythonparserParser.NUMBER); }
		public TerminalNode NUMBER(int i) {
			return getToken(pythonparserParser.NUMBER, i);
		}
		public List<TerminalNode> ARITHMETIC_FUNCTIONS() { return getTokens(pythonparserParser.ARITHMETIC_FUNCTIONS); }
		public TerminalNode ARITHMETIC_FUNCTIONS(int i) {
			return getToken(pythonparserParser.ARITHMETIC_FUNCTIONS, i);
		}
		public ForloopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forloop; }
	}

	public final ForloopContext forloop() throws RecognitionException {
		ForloopContext _localctx = new ForloopContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_forloop);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(108);
			match(T__12);
			setState(109);
			match(VAR);
			setState(110);
			match(T__13);
			setState(118);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VAR:
				{
				setState(111);
				match(VAR);
				}
				break;
			case T__14:
				{
				setState(112);
				match(T__14);
				{
				setState(113);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << VAR) | (1L << NUMBER) | (1L << ARITHMETIC_FUNCTIONS))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(114);
				match(T__15);
				setState(115);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << VAR) | (1L << NUMBER) | (1L << ARITHMETIC_FUNCTIONS))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				setState(117);
				match(T__5);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(120);
			match(T__6);
			setState(121);
			block();
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\35~\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\3\2\3\2\3\2\3\2\3\2"+
		"\7\2\30\n\2\f\2\16\2\33\13\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3#\n\3\3\4\3\4"+
		"\3\4\3\4\3\4\5\4*\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4\65\n\4\f"+
		"\4\16\48\13\4\3\5\3\5\5\5<\n\5\3\5\3\5\5\5@\n\5\3\5\3\5\3\5\3\5\3\5\5"+
		"\5G\n\5\3\5\3\5\5\5K\n\5\3\5\3\5\3\5\7\5P\n\5\f\5\16\5S\13\5\3\5\3\5\3"+
		"\5\5\5X\n\5\3\6\3\6\6\6\\\n\6\r\6\16\6]\3\6\5\6a\n\6\3\7\3\7\3\7\3\7\3"+
		"\7\3\b\3\b\7\bj\n\b\f\b\16\bm\13\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t"+
		"\3\t\5\ty\n\t\3\t\3\t\3\t\3\t\2\3\6\n\2\4\6\b\n\f\16\20\2\6\4\2\23\25"+
		"\32\32\3\2\3\5\3\2\16\16\4\2\23\24\32\32\2\u008c\2\31\3\2\2\2\4\36\3\2"+
		"\2\2\6)\3\2\2\2\b9\3\2\2\2\n[\3\2\2\2\fb\3\2\2\2\16g\3\2\2\2\20n\3\2\2"+
		"\2\22\30\5\4\3\2\23\30\5\b\5\2\24\30\5\f\7\2\25\30\5\16\b\2\26\30\5\20"+
		"\t\2\27\22\3\2\2\2\27\23\3\2\2\2\27\24\3\2\2\2\27\25\3\2\2\2\27\26\3\2"+
		"\2\2\30\33\3\2\2\2\31\27\3\2\2\2\31\32\3\2\2\2\32\34\3\2\2\2\33\31\3\2"+
		"\2\2\34\35\7\2\2\3\35\3\3\2\2\2\36\37\7\23\2\2\37 \7\30\2\2 \"\t\2\2\2"+
		"!#\7\33\2\2\"!\3\2\2\2\"#\3\2\2\2#\5\3\2\2\2$%\b\4\1\2%*\7\23\2\2&*\7"+
		"\24\2\2\'*\7\25\2\2(*\7\32\2\2)$\3\2\2\2)&\3\2\2\2)\'\3\2\2\2)(\3\2\2"+
		"\2*\66\3\2\2\2+,\f\5\2\2,-\t\3\2\2-\65\5\6\4\6./\f\4\2\2/\60\7\35\2\2"+
		"\60\65\5\6\4\5\61\62\f\3\2\2\62\63\7\31\2\2\63\65\5\6\4\4\64+\3\2\2\2"+
		"\64.\3\2\2\2\64\61\3\2\2\2\658\3\2\2\2\66\64\3\2\2\2\66\67\3\2\2\2\67"+
		"\7\3\2\2\28\66\3\2\2\29;\7\6\2\2:<\7\7\2\2;:\3\2\2\2;<\3\2\2\2<=\3\2\2"+
		"\2=?\5\6\4\2>@\7\b\2\2?>\3\2\2\2?@\3\2\2\2@A\3\2\2\2AB\7\t\2\2BC\5\n\6"+
		"\2CQ\3\2\2\2DF\7\n\2\2EG\7\7\2\2FE\3\2\2\2FG\3\2\2\2GH\3\2\2\2HJ\5\6\4"+
		"\2IK\7\b\2\2JI\3\2\2\2JK\3\2\2\2KL\3\2\2\2LM\7\t\2\2MN\5\n\6\2NP\3\2\2"+
		"\2OD\3\2\2\2PS\3\2\2\2QO\3\2\2\2QR\3\2\2\2RW\3\2\2\2SQ\3\2\2\2TU\7\13"+
		"\2\2UV\7\t\2\2VX\5\n\6\2WT\3\2\2\2WX\3\2\2\2X\t\3\2\2\2Y\\\5\4\3\2Z\\"+
		"\5\b\5\2[Y\3\2\2\2[Z\3\2\2\2\\]\3\2\2\2][\3\2\2\2]^\3\2\2\2^`\3\2\2\2"+
		"_a\7\33\2\2`_\3\2\2\2`a\3\2\2\2a\13\3\2\2\2bc\7\f\2\2cd\5\6\4\2de\7\t"+
		"\2\2ef\5\n\6\2f\r\3\2\2\2gk\7\r\2\2hj\n\4\2\2ih\3\2\2\2jm\3\2\2\2ki\3"+
		"\2\2\2kl\3\2\2\2l\17\3\2\2\2mk\3\2\2\2no\7\17\2\2op\7\23\2\2px\7\20\2"+
		"\2qy\7\23\2\2rs\7\21\2\2st\t\5\2\2tu\7\22\2\2uv\t\5\2\2vw\3\2\2\2wy\7"+
		"\b\2\2xq\3\2\2\2xr\3\2\2\2yz\3\2\2\2z{\7\t\2\2{|\5\n\6\2|\21\3\2\2\2\23"+
		"\27\31\")\64\66;?FJQW[]`kx";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}