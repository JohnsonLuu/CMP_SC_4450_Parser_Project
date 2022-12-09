// Generated from c:\Users\johns\Downloads\CMP_SC_4450_Parser_Project\pythonparser.g4 by ANTLR 4.9.2
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
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		VAR=18, NUMBER=19, STRING=20, DIGIT=21, LETTER=22, ASSIGN_OP=23, ARITH_OP=24, 
		ARITH_FUNC=25, NEWLINE=26, WHITE_SPACE=27, COND_OP=28, COMMENT=29;
	public static final int
		RULE_start = 0, RULE_definitions = 1, RULE_function = 2, RULE_functioncall = 3, 
		RULE_variable = 4, RULE_conditional = 5, RULE_ifblocks = 6, RULE_block = 7, 
		RULE_whileloop = 8, RULE_comment = 9, RULE_forloop = 10;
	private static String[] makeRuleNames() {
		return new String[] {
			"start", "definitions", "function", "functioncall", "variable", "conditional", 
			"ifblocks", "block", "whileloop", "comment", "forloop"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'def'", "'('", "','", "'):'", "')'", "'and'", "'or'", "'not'", 
			"'if'", "':'", "'elif'", "'else'", "'break'", "'while'", "'for'", "'in'", 
			"'range('"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, "VAR", "NUMBER", "STRING", "DIGIT", 
			"LETTER", "ASSIGN_OP", "ARITH_OP", "ARITH_FUNC", "NEWLINE", "WHITE_SPACE", 
			"COND_OP", "COMMENT"
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
			setState(25);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__8) | (1L << T__13) | (1L << T__14) | (1L << VAR) | (1L << COMMENT))) != 0)) {
				{
				{
				setState(22);
				definitions();
				}
				}
				setState(27);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(28);
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
		public FunctionContext function() {
			return getRuleContext(FunctionContext.class,0);
		}
		public FunctioncallContext functioncall() {
			return getRuleContext(FunctioncallContext.class,0);
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
			setState(37);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(30);
				variable();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(31);
				ifblocks();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(32);
				whileloop();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(33);
				comment();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(34);
				forloop();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(35);
				function();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(36);
				functioncall();
				}
				break;
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

	public static class FunctionContext extends ParserRuleContext {
		public List<TerminalNode> VAR() { return getTokens(pythonparserParser.VAR); }
		public TerminalNode VAR(int i) {
			return getToken(pythonparserParser.VAR, i);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public FunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function; }
	}

	public final FunctionContext function() throws RecognitionException {
		FunctionContext _localctx = new FunctionContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_function);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(39);
			match(T__0);
			setState(40);
			match(VAR);
			setState(41);
			match(T__1);
			setState(48);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VAR) {
				{
				{
				{
				setState(42);
				match(VAR);
				}
				setState(44);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__2) {
					{
					setState(43);
					match(T__2);
					}
				}

				}
				}
				setState(50);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(51);
			match(T__3);
			setState(52);
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

	public static class FunctioncallContext extends ParserRuleContext {
		public List<TerminalNode> VAR() { return getTokens(pythonparserParser.VAR); }
		public TerminalNode VAR(int i) {
			return getToken(pythonparserParser.VAR, i);
		}
		public List<TerminalNode> NUMBER() { return getTokens(pythonparserParser.NUMBER); }
		public TerminalNode NUMBER(int i) {
			return getToken(pythonparserParser.NUMBER, i);
		}
		public List<TerminalNode> ARITH_FUNC() { return getTokens(pythonparserParser.ARITH_FUNC); }
		public TerminalNode ARITH_FUNC(int i) {
			return getToken(pythonparserParser.ARITH_FUNC, i);
		}
		public List<FunctioncallContext> functioncall() {
			return getRuleContexts(FunctioncallContext.class);
		}
		public FunctioncallContext functioncall(int i) {
			return getRuleContext(FunctioncallContext.class,i);
		}
		public FunctioncallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functioncall; }
	}

	public final FunctioncallContext functioncall() throws RecognitionException {
		FunctioncallContext _localctx = new FunctioncallContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_functioncall);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(54);
			match(VAR);
			setState(55);
			match(T__1);
			setState(67);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << VAR) | (1L << NUMBER) | (1L << ARITH_FUNC))) != 0)) {
				{
				{
				setState(60);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
				case 1:
					{
					setState(56);
					match(VAR);
					}
					break;
				case 2:
					{
					setState(57);
					match(NUMBER);
					}
					break;
				case 3:
					{
					setState(58);
					match(ARITH_FUNC);
					}
					break;
				case 4:
					{
					setState(59);
					functioncall();
					}
					break;
				}
				setState(63);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__2) {
					{
					setState(62);
					match(T__2);
					}
				}

				}
				}
				setState(69);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(70);
			match(T__4);
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

	public static class VariableContext extends ParserRuleContext {
		public List<TerminalNode> VAR() { return getTokens(pythonparserParser.VAR); }
		public TerminalNode VAR(int i) {
			return getToken(pythonparserParser.VAR, i);
		}
		public TerminalNode ASSIGN_OP() { return getToken(pythonparserParser.ASSIGN_OP, 0); }
		public TerminalNode STRING() { return getToken(pythonparserParser.STRING, 0); }
		public TerminalNode NUMBER() { return getToken(pythonparserParser.NUMBER, 0); }
		public TerminalNode ARITH_FUNC() { return getToken(pythonparserParser.ARITH_FUNC, 0); }
		public TerminalNode NEWLINE() { return getToken(pythonparserParser.NEWLINE, 0); }
		public VariableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable; }
	}

	public final VariableContext variable() throws RecognitionException {
		VariableContext _localctx = new VariableContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_variable);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(72);
			match(VAR);
			setState(73);
			match(ASSIGN_OP);
			setState(74);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << VAR) | (1L << NUMBER) | (1L << STRING) | (1L << ARITH_FUNC))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(76);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				{
				setState(75);
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
		public TerminalNode ARITH_FUNC() { return getToken(pythonparserParser.ARITH_FUNC, 0); }
		public List<ConditionalContext> conditional() {
			return getRuleContexts(ConditionalContext.class);
		}
		public ConditionalContext conditional(int i) {
			return getRuleContext(ConditionalContext.class,i);
		}
		public TerminalNode COND_OP() { return getToken(pythonparserParser.COND_OP, 0); }
		public TerminalNode ARITH_OP() { return getToken(pythonparserParser.ARITH_OP, 0); }
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
		int _startState = 10;
		enterRecursionRule(_localctx, 10, RULE_conditional, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(83);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VAR:
				{
				setState(79);
				match(VAR);
				}
				break;
			case NUMBER:
				{
				setState(80);
				match(NUMBER);
				}
				break;
			case STRING:
				{
				setState(81);
				match(STRING);
				}
				break;
			case ARITH_FUNC:
				{
				setState(82);
				match(ARITH_FUNC);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(96);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(94);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
					case 1:
						{
						_localctx = new ConditionalContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditional);
						setState(85);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(86);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__5) | (1L << T__6) | (1L << T__7))) != 0)) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(87);
						conditional(4);
						}
						break;
					case 2:
						{
						_localctx = new ConditionalContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditional);
						setState(88);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(89);
						match(COND_OP);
						setState(90);
						conditional(3);
						}
						break;
					case 3:
						{
						_localctx = new ConditionalContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_conditional);
						setState(91);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(92);
						match(ARITH_OP);
						setState(93);
						conditional(2);
						}
						break;
					}
					} 
				}
				setState(98);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
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
		enterRule(_localctx, 12, RULE_ifblocks);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(99);
			match(T__8);
			setState(101);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__1) {
				{
				setState(100);
				match(T__1);
				}
			}

			setState(103);
			conditional(0);
			setState(105);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__4) {
				{
				setState(104);
				match(T__4);
				}
			}

			setState(107);
			match(T__9);
			setState(108);
			block();
			}
			setState(123);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(110);
					match(T__10);
					setState(112);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==T__1) {
						{
						setState(111);
						match(T__1);
						}
					}

					setState(114);
					conditional(0);
					setState(116);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==T__4) {
						{
						setState(115);
						match(T__4);
						}
					}

					setState(118);
					match(T__9);
					setState(119);
					block();
					}
					} 
				}
				setState(125);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			}
			setState(129);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				{
				setState(126);
				match(T__11);
				setState(127);
				match(T__9);
				setState(128);
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
		enterRule(_localctx, 14, RULE_block);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(140);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
			case T__8:
			case T__13:
			case T__14:
			case VAR:
			case COMMENT:
				{
				setState(132); 
				_errHandler.sync(this);
				_alt = 1;
				do {
					switch (_alt) {
					case 1:
						{
						{
						setState(131);
						definitions();
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(134); 
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
				} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
				setState(137);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
				case 1:
					{
					setState(136);
					match(T__12);
					}
					break;
				}
				}
				break;
			case T__12:
				{
				setState(139);
				match(T__12);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(143);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
			case 1:
				{
				setState(142);
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
		enterRule(_localctx, 16, RULE_whileloop);
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(145);
			match(T__13);
			setState(146);
			conditional(0);
			setState(147);
			match(T__9);
			setState(148);
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
		enterRule(_localctx, 18, RULE_comment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(150);
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
		public List<TerminalNode> ARITH_FUNC() { return getTokens(pythonparserParser.ARITH_FUNC); }
		public TerminalNode ARITH_FUNC(int i) {
			return getToken(pythonparserParser.ARITH_FUNC, i);
		}
		public ForloopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forloop; }
	}

	public final ForloopContext forloop() throws RecognitionException {
		ForloopContext _localctx = new ForloopContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_forloop);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(152);
			match(T__14);
			setState(153);
			match(VAR);
			setState(154);
			match(T__15);
			setState(163);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VAR:
				{
				setState(155);
				match(VAR);
				}
				break;
			case T__16:
				{
				setState(156);
				match(T__16);
				setState(161);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
				case 1:
					{
					setState(157);
					match(NUMBER);
					}
					break;
				case 2:
					{
					{
					setState(158);
					_la = _input.LA(1);
					if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << VAR) | (1L << NUMBER) | (1L << ARITH_FUNC))) != 0)) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(159);
					match(T__2);
					setState(160);
					_la = _input.LA(1);
					if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << VAR) | (1L << NUMBER) | (1L << ARITH_FUNC))) != 0)) ) {
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
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(165);
			match(T__3);
			setState(166);
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
		case 5:
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\37\u00ab\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\3\2\7\2\32\n\2\f\2\16\2\35\13\2\3\2\3\2\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\5\3(\n\3\3\4\3\4\3\4\3\4\3\4\5\4/\n\4\7\4\61\n\4\f\4\16\4"+
		"\64\13\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5?\n\5\3\5\5\5B\n\5\7\5"+
		"D\n\5\f\5\16\5G\13\5\3\5\3\5\3\6\3\6\3\6\3\6\5\6O\n\6\3\7\3\7\3\7\3\7"+
		"\3\7\5\7V\n\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\7\7a\n\7\f\7\16\7d\13"+
		"\7\3\b\3\b\5\bh\n\b\3\b\3\b\5\bl\n\b\3\b\3\b\3\b\3\b\3\b\5\bs\n\b\3\b"+
		"\3\b\5\bw\n\b\3\b\3\b\3\b\7\b|\n\b\f\b\16\b\177\13\b\3\b\3\b\3\b\5\b\u0084"+
		"\n\b\3\t\6\t\u0087\n\t\r\t\16\t\u0088\3\t\5\t\u008c\n\t\3\t\5\t\u008f"+
		"\n\t\3\t\5\t\u0092\n\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\3"+
		"\f\3\f\3\f\3\f\3\f\5\f\u00a4\n\f\5\f\u00a6\n\f\3\f\3\f\3\f\3\f\2\3\f\r"+
		"\2\4\6\b\n\f\16\20\22\24\26\2\5\4\2\24\26\33\33\3\2\b\n\4\2\24\25\33\33"+
		"\2\u00c0\2\33\3\2\2\2\4\'\3\2\2\2\6)\3\2\2\2\b8\3\2\2\2\nJ\3\2\2\2\fU"+
		"\3\2\2\2\16e\3\2\2\2\20\u008e\3\2\2\2\22\u0093\3\2\2\2\24\u0098\3\2\2"+
		"\2\26\u009a\3\2\2\2\30\32\5\4\3\2\31\30\3\2\2\2\32\35\3\2\2\2\33\31\3"+
		"\2\2\2\33\34\3\2\2\2\34\36\3\2\2\2\35\33\3\2\2\2\36\37\7\2\2\3\37\3\3"+
		"\2\2\2 (\5\n\6\2!(\5\16\b\2\"(\5\22\n\2#(\5\24\13\2$(\5\26\f\2%(\5\6\4"+
		"\2&(\5\b\5\2\' \3\2\2\2\'!\3\2\2\2\'\"\3\2\2\2\'#\3\2\2\2\'$\3\2\2\2\'"+
		"%\3\2\2\2\'&\3\2\2\2(\5\3\2\2\2)*\7\3\2\2*+\7\24\2\2+\62\7\4\2\2,.\7\24"+
		"\2\2-/\7\5\2\2.-\3\2\2\2./\3\2\2\2/\61\3\2\2\2\60,\3\2\2\2\61\64\3\2\2"+
		"\2\62\60\3\2\2\2\62\63\3\2\2\2\63\65\3\2\2\2\64\62\3\2\2\2\65\66\7\6\2"+
		"\2\66\67\5\20\t\2\67\7\3\2\2\289\7\24\2\29E\7\4\2\2:?\7\24\2\2;?\7\25"+
		"\2\2<?\7\33\2\2=?\5\b\5\2>:\3\2\2\2>;\3\2\2\2><\3\2\2\2>=\3\2\2\2?A\3"+
		"\2\2\2@B\7\5\2\2A@\3\2\2\2AB\3\2\2\2BD\3\2\2\2C>\3\2\2\2DG\3\2\2\2EC\3"+
		"\2\2\2EF\3\2\2\2FH\3\2\2\2GE\3\2\2\2HI\7\7\2\2I\t\3\2\2\2JK\7\24\2\2K"+
		"L\7\31\2\2LN\t\2\2\2MO\7\34\2\2NM\3\2\2\2NO\3\2\2\2O\13\3\2\2\2PQ\b\7"+
		"\1\2QV\7\24\2\2RV\7\25\2\2SV\7\26\2\2TV\7\33\2\2UP\3\2\2\2UR\3\2\2\2U"+
		"S\3\2\2\2UT\3\2\2\2Vb\3\2\2\2WX\f\5\2\2XY\t\3\2\2Ya\5\f\7\6Z[\f\4\2\2"+
		"[\\\7\36\2\2\\a\5\f\7\5]^\f\3\2\2^_\7\32\2\2_a\5\f\7\4`W\3\2\2\2`Z\3\2"+
		"\2\2`]\3\2\2\2ad\3\2\2\2b`\3\2\2\2bc\3\2\2\2c\r\3\2\2\2db\3\2\2\2eg\7"+
		"\13\2\2fh\7\4\2\2gf\3\2\2\2gh\3\2\2\2hi\3\2\2\2ik\5\f\7\2jl\7\7\2\2kj"+
		"\3\2\2\2kl\3\2\2\2lm\3\2\2\2mn\7\f\2\2no\5\20\t\2o}\3\2\2\2pr\7\r\2\2"+
		"qs\7\4\2\2rq\3\2\2\2rs\3\2\2\2st\3\2\2\2tv\5\f\7\2uw\7\7\2\2vu\3\2\2\2"+
		"vw\3\2\2\2wx\3\2\2\2xy\7\f\2\2yz\5\20\t\2z|\3\2\2\2{p\3\2\2\2|\177\3\2"+
		"\2\2}{\3\2\2\2}~\3\2\2\2~\u0083\3\2\2\2\177}\3\2\2\2\u0080\u0081\7\16"+
		"\2\2\u0081\u0082\7\f\2\2\u0082\u0084\5\20\t\2\u0083\u0080\3\2\2\2\u0083"+
		"\u0084\3\2\2\2\u0084\17\3\2\2\2\u0085\u0087\5\4\3\2\u0086\u0085\3\2\2"+
		"\2\u0087\u0088\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008b"+
		"\3\2\2\2\u008a\u008c\7\17\2\2\u008b\u008a\3\2\2\2\u008b\u008c\3\2\2\2"+
		"\u008c\u008f\3\2\2\2\u008d\u008f\7\17\2\2\u008e\u0086\3\2\2\2\u008e\u008d"+
		"\3\2\2\2\u008f\u0091\3\2\2\2\u0090\u0092\7\34\2\2\u0091\u0090\3\2\2\2"+
		"\u0091\u0092\3\2\2\2\u0092\21\3\2\2\2\u0093\u0094\7\20\2\2\u0094\u0095"+
		"\5\f\7\2\u0095\u0096\7\f\2\2\u0096\u0097\5\20\t\2\u0097\23\3\2\2\2\u0098"+
		"\u0099\7\37\2\2\u0099\25\3\2\2\2\u009a\u009b\7\21\2\2\u009b\u009c\7\24"+
		"\2\2\u009c\u00a5\7\22\2\2\u009d\u00a6\7\24\2\2\u009e\u00a3\7\23\2\2\u009f"+
		"\u00a4\7\25\2\2\u00a0\u00a1\t\4\2\2\u00a1\u00a2\7\5\2\2\u00a2\u00a4\t"+
		"\4\2\2\u00a3\u009f\3\2\2\2\u00a3\u00a0\3\2\2\2\u00a4\u00a6\3\2\2\2\u00a5"+
		"\u009d\3\2\2\2\u00a5\u009e\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a8\7\6"+
		"\2\2\u00a8\u00a9\5\20\t\2\u00a9\27\3\2\2\2\31\33\'.\62>AENU`bgkrv}\u0083"+
		"\u0088\u008b\u008e\u0091\u00a3\u00a5";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}