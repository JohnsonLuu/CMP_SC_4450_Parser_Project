// Generated from c:\Users\johns\Downloads\mostupdated\CMP_SC_4450_Parser_Project\pythonparser.g4 by ANTLR 4.9.2
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
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, VAR=16, NUMBER=17, 
		STRING=18, DIGIT=19, LETTER=20, ASSIGNMENT_OPERATORS=21, ARITHMETIC_OPERATORS=22, 
		ARITHMETIC_FUNCTIONS=23, NEWLINE=24, WHITE_SPACE=25, CONDITIONAL_OPERATORS=26, 
		COMMENT=27;
	public static final int
		RULE_start = 0, RULE_definitions = 1, RULE_variable = 2, RULE_conditional = 3, 
		RULE_ifblocks = 4, RULE_block = 5, RULE_whileloop = 6, RULE_comment = 7, 
		RULE_forloop = 8;
	private static String[] makeRuleNames() {
		return new String[] {
			"start", "definitions", "variable", "conditional", "ifblocks", "block", 
			"whileloop", "comment", "forloop"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'and'", "'or'", "'not'", "'if'", "'('", "')'", "':'", "'elif'", 
			"'else'", "'break'", "'while'", "'for'", "'in'", "'range('", "','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, "VAR", "NUMBER", "STRING", "DIGIT", "LETTER", 
			"ASSIGNMENT_OPERATORS", "ARITHMETIC_OPERATORS", "ARITHMETIC_FUNCTIONS", 
			"NEWLINE", "WHITE_SPACE", "CONDITIONAL_OPERATORS", "COMMENT"
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
		public List<DefinitionsContext> definitions() {
			return getRuleContexts(DefinitionsContext.class);
		}
		public DefinitionsContext definitions(int i) {
			return getRuleContext(DefinitionsContext.class,i);
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
			setState(21);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__3) | (1L << T__10) | (1L << T__11) | (1L << VAR) | (1L << COMMENT))) != 0)) {
				{
				{
				setState(18);
				definitions();
				}
				}
				setState(23);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(24);
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

	public static class DefinitionsContext extends ParserRuleContext {
		public VariableContext variable() {
			return getRuleContext(VariableContext.class,0);
		}
		public IfblocksContext ifblocks() {
			return getRuleContext(IfblocksContext.class,0);
		}
		public WhileloopContext whileloop() {
			return getRuleContext(WhileloopContext.class,0);
		}
		public CommentContext comment() {
			return getRuleContext(CommentContext.class,0);
		}
		public ForloopContext forloop() {
			return getRuleContext(ForloopContext.class,0);
		}
		public DefinitionsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_definitions; }
	}

	public final DefinitionsContext definitions() throws RecognitionException {
		DefinitionsContext _localctx = new DefinitionsContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_definitions);
		try {
			setState(31);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VAR:
				enterOuterAlt(_localctx, 1);
				{
				setState(26);
				variable();
				}
				break;
			case T__3:
				enterOuterAlt(_localctx, 2);
				{
				setState(27);
				ifblocks();
				}
				break;
			case T__10:
				enterOuterAlt(_localctx, 3);
				{
				setState(28);
				whileloop();
				}
				break;
			case COMMENT:
				enterOuterAlt(_localctx, 4);
				{
				setState(29);
				comment();
				}
				break;
			case T__11:
				enterOuterAlt(_localctx, 5);
				{
				setState(30);
				forloop();
				}
				break;
			default:
				throw new NoViableAltException(this);
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
		enterRule(_localctx, 4, RULE_variable);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(33);
			match(VAR);
			setState(34);
			match(ASSIGNMENT_OPERATORS);
			setState(35);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << VAR) | (1L << NUMBER) | (1L << STRING) | (1L << ARITHMETIC_FUNCTIONS))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(37);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				{
				setState(36);
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
		int _startState = 6;
		enterRecursionRule(_localctx, 6, RULE_conditional, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(44);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VAR:
				{
				setState(40);
				match(VAR);
				}
				break;
			case NUMBER:
				{
				setState(41);
				match(NUMBER);
				}
				break;
			case STRING:
				{
				setState(42);
				match(STRING);
				}
				break;
			case ARITHMETIC_FUNCTIONS:
				{
				setState(43);
				match(ARITHMETIC_FUNCTIONS);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(57);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(55);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
					case 1:
						{
						_localctx = new ConditionalContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditional);
						setState(46);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(47);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__1) | (1L << T__2))) != 0)) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(48);
						conditional(4);
						}
						break;
					case 2:
						{
						_localctx = new ConditionalContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditional);
						setState(49);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(50);
						match(CONDITIONAL_OPERATORS);
						setState(51);
						conditional(3);
						}
						break;
					case 3:
						{
						_localctx = new ConditionalContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditional);
						setState(52);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(53);
						match(ARITHMETIC_OPERATORS);
						setState(54);
						conditional(2);
						}
						break;
					}
					} 
				}
				setState(59);
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
		enterRule(_localctx, 8, RULE_ifblocks);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(60);
			match(T__3);
			setState(62);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__4) {
				{
				setState(61);
				match(T__4);
				}
			}

			setState(64);
			conditional(0);
			setState(66);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__5) {
				{
				setState(65);
				match(T__5);
				}
			}

			setState(68);
			match(T__6);
			setState(69);
			block();
			}
			setState(84);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(71);
					match(T__7);
					setState(73);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==T__4) {
						{
						setState(72);
						match(T__4);
						}
					}

					setState(75);
					conditional(0);
					setState(77);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==T__5) {
						{
						setState(76);
						match(T__5);
						}
					}

					setState(79);
					match(T__6);
					setState(80);
					block();
					}
					} 
				}
				setState(86);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			}
			setState(90);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				{
				setState(87);
				match(T__8);
				setState(88);
				match(T__6);
				setState(89);
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
		public TerminalNode NEWLINE() { return getToken(pythonparserParser.NEWLINE, 0); }
		public List<DefinitionsContext> definitions() {
			return getRuleContexts(DefinitionsContext.class);
		}
		public DefinitionsContext definitions(int i) {
			return getRuleContext(DefinitionsContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_block);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(101);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__3:
			case T__10:
			case T__11:
			case VAR:
			case COMMENT:
				{
				setState(93); 
				_errHandler.sync(this);
				_alt = 1;
				do {
					switch (_alt) {
					case 1:
						{
						{
						setState(92);
						definitions();
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(95); 
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
				} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
				setState(98);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
				case 1:
					{
					setState(97);
					match(T__9);
					}
					break;
				}
				}
				break;
			case T__9:
				{
				setState(100);
				match(T__9);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(104);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				{
				setState(103);
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
		enterRule(_localctx, 12, RULE_whileloop);
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(106);
			match(T__10);
			setState(107);
			conditional(0);
			setState(108);
			match(T__6);
			setState(109);
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
		public TerminalNode COMMENT() { return getToken(pythonparserParser.COMMENT, 0); }
		public CommentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comment; }
	}

	public final CommentContext comment() throws RecognitionException {
		CommentContext _localctx = new CommentContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_comment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(111);
			match(COMMENT);
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
		enterRule(_localctx, 16, RULE_forloop);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(113);
			match(T__11);
			setState(114);
			match(VAR);
			setState(115);
			match(T__12);
			setState(125);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VAR:
				{
				setState(116);
				match(VAR);
				}
				break;
			case T__13:
				{
				setState(117);
				match(T__13);
				setState(122);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
				case 1:
					{
					setState(118);
					match(NUMBER);
					}
					break;
				case 2:
					{
					{
					setState(119);
					_la = _input.LA(1);
					if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << VAR) | (1L << NUMBER) | (1L << ARITHMETIC_FUNCTIONS))) != 0)) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(120);
					match(T__14);
					setState(121);
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
					}
					break;
				}
				setState(124);
				match(T__5);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(127);
			match(T__6);
			setState(128);
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
		case 3:
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\35\u0085\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\3\2\7"+
		"\2\26\n\2\f\2\16\2\31\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5\3\"\n\3\3\4\3"+
		"\4\3\4\3\4\5\4(\n\4\3\5\3\5\3\5\3\5\3\5\5\5/\n\5\3\5\3\5\3\5\3\5\3\5\3"+
		"\5\3\5\3\5\3\5\7\5:\n\5\f\5\16\5=\13\5\3\6\3\6\5\6A\n\6\3\6\3\6\5\6E\n"+
		"\6\3\6\3\6\3\6\3\6\3\6\5\6L\n\6\3\6\3\6\5\6P\n\6\3\6\3\6\3\6\7\6U\n\6"+
		"\f\6\16\6X\13\6\3\6\3\6\3\6\5\6]\n\6\3\7\6\7`\n\7\r\7\16\7a\3\7\5\7e\n"+
		"\7\3\7\5\7h\n\7\3\7\5\7k\n\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3"+
		"\n\3\n\3\n\3\n\3\n\3\n\5\n}\n\n\3\n\5\n\u0080\n\n\3\n\3\n\3\n\3\n\2\3"+
		"\b\13\2\4\6\b\n\f\16\20\22\2\5\4\2\22\24\31\31\3\2\3\5\4\2\22\23\31\31"+
		"\2\u0093\2\27\3\2\2\2\4!\3\2\2\2\6#\3\2\2\2\b.\3\2\2\2\n>\3\2\2\2\fg\3"+
		"\2\2\2\16l\3\2\2\2\20q\3\2\2\2\22s\3\2\2\2\24\26\5\4\3\2\25\24\3\2\2\2"+
		"\26\31\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2\30\32\3\2\2\2\31\27\3\2\2\2"+
		"\32\33\7\2\2\3\33\3\3\2\2\2\34\"\5\6\4\2\35\"\5\n\6\2\36\"\5\16\b\2\37"+
		"\"\5\20\t\2 \"\5\22\n\2!\34\3\2\2\2!\35\3\2\2\2!\36\3\2\2\2!\37\3\2\2"+
		"\2! \3\2\2\2\"\5\3\2\2\2#$\7\22\2\2$%\7\27\2\2%\'\t\2\2\2&(\7\32\2\2\'"+
		"&\3\2\2\2\'(\3\2\2\2(\7\3\2\2\2)*\b\5\1\2*/\7\22\2\2+/\7\23\2\2,/\7\24"+
		"\2\2-/\7\31\2\2.)\3\2\2\2.+\3\2\2\2.,\3\2\2\2.-\3\2\2\2/;\3\2\2\2\60\61"+
		"\f\5\2\2\61\62\t\3\2\2\62:\5\b\5\6\63\64\f\4\2\2\64\65\7\34\2\2\65:\5"+
		"\b\5\5\66\67\f\3\2\2\678\7\30\2\28:\5\b\5\49\60\3\2\2\29\63\3\2\2\29\66"+
		"\3\2\2\2:=\3\2\2\2;9\3\2\2\2;<\3\2\2\2<\t\3\2\2\2=;\3\2\2\2>@\7\6\2\2"+
		"?A\7\7\2\2@?\3\2\2\2@A\3\2\2\2AB\3\2\2\2BD\5\b\5\2CE\7\b\2\2DC\3\2\2\2"+
		"DE\3\2\2\2EF\3\2\2\2FG\7\t\2\2GH\5\f\7\2HV\3\2\2\2IK\7\n\2\2JL\7\7\2\2"+
		"KJ\3\2\2\2KL\3\2\2\2LM\3\2\2\2MO\5\b\5\2NP\7\b\2\2ON\3\2\2\2OP\3\2\2\2"+
		"PQ\3\2\2\2QR\7\t\2\2RS\5\f\7\2SU\3\2\2\2TI\3\2\2\2UX\3\2\2\2VT\3\2\2\2"+
		"VW\3\2\2\2W\\\3\2\2\2XV\3\2\2\2YZ\7\13\2\2Z[\7\t\2\2[]\5\f\7\2\\Y\3\2"+
		"\2\2\\]\3\2\2\2]\13\3\2\2\2^`\5\4\3\2_^\3\2\2\2`a\3\2\2\2a_\3\2\2\2ab"+
		"\3\2\2\2bd\3\2\2\2ce\7\f\2\2dc\3\2\2\2de\3\2\2\2eh\3\2\2\2fh\7\f\2\2g"+
		"_\3\2\2\2gf\3\2\2\2hj\3\2\2\2ik\7\32\2\2ji\3\2\2\2jk\3\2\2\2k\r\3\2\2"+
		"\2lm\7\r\2\2mn\5\b\5\2no\7\t\2\2op\5\f\7\2p\17\3\2\2\2qr\7\35\2\2r\21"+
		"\3\2\2\2st\7\16\2\2tu\7\22\2\2u\177\7\17\2\2v\u0080\7\22\2\2w|\7\20\2"+
		"\2x}\7\23\2\2yz\t\4\2\2z{\7\21\2\2{}\t\4\2\2|x\3\2\2\2|y\3\2\2\2}~\3\2"+
		"\2\2~\u0080\7\b\2\2\177v\3\2\2\2\177w\3\2\2\2\u0080\u0081\3\2\2\2\u0081"+
		"\u0082\7\t\2\2\u0082\u0083\5\f\7\2\u0083\23\3\2\2\2\24\27!\'.9;@DKOV\\"+
		"adgj|\177";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}