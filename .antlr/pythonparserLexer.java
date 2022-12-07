// Generated from c:\Users\johns\Downloads\CMP_SC_4450_Parser_Project\pythonparser.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class pythonparserLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, VAR=16, NUMBER=17, 
		STRING=18, DIGIT=19, LETTER=20, ASSIGN_OP=21, ARITH_OP=22, ARITH_FUNC=23, 
		NEWLINE=24, WHITE_SPACE=25, COND_OP=26, COMMENT=27;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"T__9", "T__10", "T__11", "T__12", "T__13", "T__14", "VAR", "NUMBER", 
			"STRING", "DIGIT", "LETTER", "ASSIGN_OP", "ARITH_OP", "ARITH_FUNC", "NEWLINE", 
			"WHITE_SPACE", "COND_OP", "COMMENT"
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
			"ASSIGN_OP", "ARITH_OP", "ARITH_FUNC", "NEWLINE", "WHITE_SPACE", "COND_OP", 
			"COMMENT"
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


	public pythonparserLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "pythonparser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\35\u00e3\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\4\32\t\32\4\33\t\33\4\34\t\34\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3"+
		"\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n"+
		"\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f"+
		"\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20"+
		"\3\20\3\21\3\21\5\21v\n\21\3\21\3\21\3\21\7\21{\n\21\f\21\16\21~\13\21"+
		"\3\22\5\22\u0081\n\22\3\22\6\22\u0084\n\22\r\22\16\22\u0085\3\23\3\23"+
		"\7\23\u008a\n\23\f\23\16\23\u008d\13\23\3\23\3\23\3\24\3\24\3\25\3\25"+
		"\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u009e\n\26\3\27\3\27"+
		"\3\30\3\30\5\30\u00a4\n\30\3\30\5\30\u00a7\n\30\3\30\3\30\5\30\u00ab\n"+
		"\30\3\30\3\30\5\30\u00af\n\30\3\30\5\30\u00b2\n\30\3\30\3\30\5\30\u00b6"+
		"\n\30\3\30\3\30\5\30\u00ba\n\30\7\30\u00bc\n\30\f\30\16\30\u00bf\13\30"+
		"\3\31\3\31\7\31\u00c3\n\31\f\31\16\31\u00c6\13\31\3\31\3\31\3\32\6\32"+
		"\u00cb\n\32\r\32\16\32\u00cc\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3"+
		"\33\3\33\3\33\3\33\5\33\u00db\n\33\3\34\3\34\7\34\u00df\n\34\f\34\16\34"+
		"\u00e2\13\34\2\2\35\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r"+
		"\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33"+
		"\65\34\67\35\3\2\b\3\2\f\f\3\2\62;\4\2C\\c|\6\2\'\',-//\61\61\5\2\13\f"+
		"\17\17\"\"\4\2\f\f\17\17\2\u00fd\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2"+
		"\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2"+
		"\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2"+
		"\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2"+
		"\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2"+
		"\2\2\67\3\2\2\2\39\3\2\2\2\5=\3\2\2\2\7@\3\2\2\2\tD\3\2\2\2\13G\3\2\2"+
		"\2\rI\3\2\2\2\17K\3\2\2\2\21M\3\2\2\2\23R\3\2\2\2\25W\3\2\2\2\27]\3\2"+
		"\2\2\31c\3\2\2\2\33g\3\2\2\2\35j\3\2\2\2\37q\3\2\2\2!u\3\2\2\2#\u0080"+
		"\3\2\2\2%\u0087\3\2\2\2\'\u0090\3\2\2\2)\u0092\3\2\2\2+\u009d\3\2\2\2"+
		"-\u009f\3\2\2\2/\u00a3\3\2\2\2\61\u00c0\3\2\2\2\63\u00ca\3\2\2\2\65\u00da"+
		"\3\2\2\2\67\u00dc\3\2\2\29:\7c\2\2:;\7p\2\2;<\7f\2\2<\4\3\2\2\2=>\7q\2"+
		"\2>?\7t\2\2?\6\3\2\2\2@A\7p\2\2AB\7q\2\2BC\7v\2\2C\b\3\2\2\2DE\7k\2\2"+
		"EF\7h\2\2F\n\3\2\2\2GH\7*\2\2H\f\3\2\2\2IJ\7+\2\2J\16\3\2\2\2KL\7<\2\2"+
		"L\20\3\2\2\2MN\7g\2\2NO\7n\2\2OP\7k\2\2PQ\7h\2\2Q\22\3\2\2\2RS\7g\2\2"+
		"ST\7n\2\2TU\7u\2\2UV\7g\2\2V\24\3\2\2\2WX\7d\2\2XY\7t\2\2YZ\7g\2\2Z[\7"+
		"c\2\2[\\\7m\2\2\\\26\3\2\2\2]^\7y\2\2^_\7j\2\2_`\7k\2\2`a\7n\2\2ab\7g"+
		"\2\2b\30\3\2\2\2cd\7h\2\2de\7q\2\2ef\7t\2\2f\32\3\2\2\2gh\7k\2\2hi\7p"+
		"\2\2i\34\3\2\2\2jk\7t\2\2kl\7c\2\2lm\7p\2\2mn\7i\2\2no\7g\2\2op\7*\2\2"+
		"p\36\3\2\2\2qr\7.\2\2r \3\2\2\2sv\5)\25\2tv\7a\2\2us\3\2\2\2ut\3\2\2\2"+
		"v|\3\2\2\2w{\5)\25\2x{\7a\2\2y{\5\'\24\2zw\3\2\2\2zx\3\2\2\2zy\3\2\2\2"+
		"{~\3\2\2\2|z\3\2\2\2|}\3\2\2\2}\"\3\2\2\2~|\3\2\2\2\177\u0081\7/\2\2\u0080"+
		"\177\3\2\2\2\u0080\u0081\3\2\2\2\u0081\u0083\3\2\2\2\u0082\u0084\5\'\24"+
		"\2\u0083\u0082\3\2\2\2\u0084\u0085\3\2\2\2\u0085\u0083\3\2\2\2\u0085\u0086"+
		"\3\2\2\2\u0086$\3\2\2\2\u0087\u008b\7$\2\2\u0088\u008a\n\2\2\2\u0089\u0088"+
		"\3\2\2\2\u008a\u008d\3\2\2\2\u008b\u0089\3\2\2\2\u008b\u008c\3\2\2\2\u008c"+
		"\u008e\3\2\2\2\u008d\u008b\3\2\2\2\u008e\u008f\7$\2\2\u008f&\3\2\2\2\u0090"+
		"\u0091\t\3\2\2\u0091(\3\2\2\2\u0092\u0093\t\4\2\2\u0093*\3\2\2\2\u0094"+
		"\u009e\7?\2\2\u0095\u0096\7-\2\2\u0096\u009e\7?\2\2\u0097\u0098\7/\2\2"+
		"\u0098\u009e\7?\2\2\u0099\u009a\7,\2\2\u009a\u009e\7?\2\2\u009b\u009c"+
		"\7\61\2\2\u009c\u009e\7?\2\2\u009d\u0094\3\2\2\2\u009d\u0095\3\2\2\2\u009d"+
		"\u0097\3\2\2\2\u009d\u0099\3\2\2\2\u009d\u009b\3\2\2\2\u009e,\3\2\2\2"+
		"\u009f\u00a0\t\5\2\2\u00a0.\3\2\2\2\u00a1\u00a4\5#\22\2\u00a2\u00a4\5"+
		"!\21\2\u00a3\u00a1\3\2\2\2\u00a3\u00a2\3\2\2\2\u00a4\u00a6\3\2\2\2\u00a5"+
		"\u00a7\7\"\2\2\u00a6\u00a5\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a8\3\2"+
		"\2\2\u00a8\u00aa\5-\27\2\u00a9\u00ab\7\"\2\2\u00aa\u00a9\3\2\2\2\u00aa"+
		"\u00ab\3\2\2\2\u00ab\u00ae\3\2\2\2\u00ac\u00af\5#\22\2\u00ad\u00af\5!"+
		"\21\2\u00ae\u00ac\3\2\2\2\u00ae\u00ad\3\2\2\2\u00af\u00bd\3\2\2\2\u00b0"+
		"\u00b2\7\"\2\2\u00b1\u00b0\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b3\3\2"+
		"\2\2\u00b3\u00b5\5-\27\2\u00b4\u00b6\7\"\2\2\u00b5\u00b4\3\2\2\2\u00b5"+
		"\u00b6\3\2\2\2\u00b6\u00b9\3\2\2\2\u00b7\u00ba\5#\22\2\u00b8\u00ba\5!"+
		"\21\2\u00b9\u00b7\3\2\2\2\u00b9\u00b8\3\2\2\2\u00ba\u00bc\3\2\2\2\u00bb"+
		"\u00b1\3\2\2\2\u00bc\u00bf\3\2\2\2\u00bd\u00bb\3\2\2\2\u00bd\u00be\3\2"+
		"\2\2\u00be\60\3\2\2\2\u00bf\u00bd\3\2\2\2\u00c0\u00c4\7\f\2\2\u00c1\u00c3"+
		"\7\"\2\2\u00c2\u00c1\3\2\2\2\u00c3\u00c6\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c4"+
		"\u00c5\3\2\2\2\u00c5\u00c7\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c7\u00c8\b\31"+
		"\2\2\u00c8\62\3\2\2\2\u00c9\u00cb\t\6\2\2\u00ca\u00c9\3\2\2\2\u00cb\u00cc"+
		"\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce"+
		"\u00cf\b\32\2\2\u00cf\64\3\2\2\2\u00d0\u00db\7>\2\2\u00d1\u00d2\7>\2\2"+
		"\u00d2\u00db\7?\2\2\u00d3\u00db\7@\2\2\u00d4\u00d5\7@\2\2\u00d5\u00db"+
		"\7?\2\2\u00d6\u00d7\7?\2\2\u00d7\u00db\7?\2\2\u00d8\u00d9\7#\2\2\u00d9"+
		"\u00db\7?\2\2\u00da\u00d0\3\2\2\2\u00da\u00d1\3\2\2\2\u00da\u00d3\3\2"+
		"\2\2\u00da\u00d4\3\2\2\2\u00da\u00d6\3\2\2\2\u00da\u00d8\3\2\2\2\u00db"+
		"\66\3\2\2\2\u00dc\u00e0\7%\2\2\u00dd\u00df\n\7\2\2\u00de\u00dd\3\2\2\2"+
		"\u00df\u00e2\3\2\2\2\u00e0\u00de\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e18\3"+
		"\2\2\2\u00e2\u00e0\3\2\2\2\26\2uz|\u0080\u0085\u008b\u009d\u00a3\u00a6"+
		"\u00aa\u00ae\u00b1\u00b5\u00b9\u00bd\u00c4\u00cc\u00da\u00e0\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}