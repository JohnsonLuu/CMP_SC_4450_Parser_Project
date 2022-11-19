// Generated from c:\Users\johns\Downloads\git\CMP_SC_4450_Parser_Project\pythonparser.g4 by ANTLR 4.9.2
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
		VAR=10, NUMBER=11, STRING=12, DIGIT=13, LETTER=14, ASSIGNMENT_OPERATORS=15, 
		ARITHMETIC_OPERATORS=16, ARITHMETIC_FUNCTIONS=17, NEWLINE=18, WHITE_SPACE=19, 
		CONDITIONAL_OPERATORS=20;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"VAR", "NUMBER", "STRING", "DIGIT", "LETTER", "ASSIGNMENT_OPERATORS", 
			"ARITHMETIC_OPERATORS", "ARITHMETIC_FUNCTIONS", "NEWLINE", "WHITE_SPACE", 
			"CONDITIONAL_OPERATORS"
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\26\u00b2\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3"+
		"\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n"+
		"\3\n\3\n\3\n\3\n\3\13\3\13\5\13L\n\13\3\13\3\13\3\13\7\13Q\n\13\f\13\16"+
		"\13T\13\13\3\f\5\fW\n\f\3\f\6\fZ\n\f\r\f\16\f[\3\r\3\r\7\r`\n\r\f\r\16"+
		"\rc\13\r\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20"+
		"\3\20\3\20\5\20t\n\20\3\21\3\21\3\22\3\22\5\22z\n\22\3\22\5\22}\n\22\3"+
		"\22\3\22\5\22\u0081\n\22\3\22\3\22\5\22\u0085\n\22\3\22\5\22\u0088\n\22"+
		"\3\22\3\22\5\22\u008c\n\22\3\22\3\22\5\22\u0090\n\22\7\22\u0092\n\22\f"+
		"\22\16\22\u0095\13\22\3\23\3\23\7\23\u0099\n\23\f\23\16\23\u009c\13\23"+
		"\3\23\3\23\3\24\6\24\u00a1\n\24\r\24\16\24\u00a2\3\24\3\24\3\25\3\25\3"+
		"\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u00b1\n\25\2\2\26\3\3\5\4"+
		"\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22"+
		"#\23%\24\'\25)\26\3\2\7\3\2\f\f\3\2\62;\4\2C\\c|\6\2\'\',-//\61\61\5\2"+
		"\13\f\17\17\"\"\2\u00cb\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2"+
		"\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25"+
		"\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2"+
		"\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\3+\3\2\2"+
		"\2\5/\3\2\2\2\7\62\3\2\2\2\t\66\3\2\2\2\139\3\2\2\2\r;\3\2\2\2\17=\3\2"+
		"\2\2\21?\3\2\2\2\23D\3\2\2\2\25K\3\2\2\2\27V\3\2\2\2\31]\3\2\2\2\33f\3"+
		"\2\2\2\35h\3\2\2\2\37s\3\2\2\2!u\3\2\2\2#y\3\2\2\2%\u0096\3\2\2\2\'\u00a0"+
		"\3\2\2\2)\u00b0\3\2\2\2+,\7c\2\2,-\7p\2\2-.\7f\2\2.\4\3\2\2\2/\60\7q\2"+
		"\2\60\61\7t\2\2\61\6\3\2\2\2\62\63\7p\2\2\63\64\7q\2\2\64\65\7v\2\2\65"+
		"\b\3\2\2\2\66\67\7k\2\2\678\7h\2\28\n\3\2\2\29:\7*\2\2:\f\3\2\2\2;<\7"+
		"+\2\2<\16\3\2\2\2=>\7<\2\2>\20\3\2\2\2?@\7g\2\2@A\7n\2\2AB\7k\2\2BC\7"+
		"h\2\2C\22\3\2\2\2DE\7g\2\2EF\7n\2\2FG\7u\2\2GH\7g\2\2H\24\3\2\2\2IL\5"+
		"\35\17\2JL\7a\2\2KI\3\2\2\2KJ\3\2\2\2LR\3\2\2\2MQ\5\35\17\2NQ\7a\2\2O"+
		"Q\5\33\16\2PM\3\2\2\2PN\3\2\2\2PO\3\2\2\2QT\3\2\2\2RP\3\2\2\2RS\3\2\2"+
		"\2S\26\3\2\2\2TR\3\2\2\2UW\7/\2\2VU\3\2\2\2VW\3\2\2\2WY\3\2\2\2XZ\5\33"+
		"\16\2YX\3\2\2\2Z[\3\2\2\2[Y\3\2\2\2[\\\3\2\2\2\\\30\3\2\2\2]a\7$\2\2^"+
		"`\n\2\2\2_^\3\2\2\2`c\3\2\2\2a_\3\2\2\2ab\3\2\2\2bd\3\2\2\2ca\3\2\2\2"+
		"de\7$\2\2e\32\3\2\2\2fg\t\3\2\2g\34\3\2\2\2hi\t\4\2\2i\36\3\2\2\2jt\7"+
		"?\2\2kl\7-\2\2lt\7?\2\2mn\7/\2\2nt\7?\2\2op\7,\2\2pt\7?\2\2qr\7\61\2\2"+
		"rt\7?\2\2sj\3\2\2\2sk\3\2\2\2sm\3\2\2\2so\3\2\2\2sq\3\2\2\2t \3\2\2\2"+
		"uv\t\5\2\2v\"\3\2\2\2wz\5\27\f\2xz\5\25\13\2yw\3\2\2\2yx\3\2\2\2z|\3\2"+
		"\2\2{}\7\"\2\2|{\3\2\2\2|}\3\2\2\2}~\3\2\2\2~\u0080\5!\21\2\177\u0081"+
		"\7\"\2\2\u0080\177\3\2\2\2\u0080\u0081\3\2\2\2\u0081\u0084\3\2\2\2\u0082"+
		"\u0085\5\27\f\2\u0083\u0085\5\25\13\2\u0084\u0082\3\2\2\2\u0084\u0083"+
		"\3\2\2\2\u0085\u0093\3\2\2\2\u0086\u0088\7\"\2\2\u0087\u0086\3\2\2\2\u0087"+
		"\u0088\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008b\5!\21\2\u008a\u008c\7\""+
		"\2\2\u008b\u008a\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008f\3\2\2\2\u008d"+
		"\u0090\5\27\f\2\u008e\u0090\5\25\13\2\u008f\u008d\3\2\2\2\u008f\u008e"+
		"\3\2\2\2\u0090\u0092\3\2\2\2\u0091\u0087\3\2\2\2\u0092\u0095\3\2\2\2\u0093"+
		"\u0091\3\2\2\2\u0093\u0094\3\2\2\2\u0094$\3\2\2\2\u0095\u0093\3\2\2\2"+
		"\u0096\u009a\7\f\2\2\u0097\u0099\7\"\2\2\u0098\u0097\3\2\2\2\u0099\u009c"+
		"\3\2\2\2\u009a\u0098\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u009d\3\2\2\2\u009c"+
		"\u009a\3\2\2\2\u009d\u009e\b\23\2\2\u009e&\3\2\2\2\u009f\u00a1\t\6\2\2"+
		"\u00a0\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a3"+
		"\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a5\b\24\2\2\u00a5(\3\2\2\2\u00a6"+
		"\u00b1\7>\2\2\u00a7\u00a8\7>\2\2\u00a8\u00b1\7?\2\2\u00a9\u00b1\7@\2\2"+
		"\u00aa\u00ab\7@\2\2\u00ab\u00b1\7?\2\2\u00ac\u00ad\7?\2\2\u00ad\u00b1"+
		"\7?\2\2\u00ae\u00af\7#\2\2\u00af\u00b1\7?\2\2\u00b0\u00a6\3\2\2\2\u00b0"+
		"\u00a7\3\2\2\2\u00b0\u00a9\3\2\2\2\u00b0\u00aa\3\2\2\2\u00b0\u00ac\3\2"+
		"\2\2\u00b0\u00ae\3\2\2\2\u00b1*\3\2\2\2\25\2KPRV[asy|\u0080\u0084\u0087"+
		"\u008b\u008f\u0093\u009a\u00a2\u00b0\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}