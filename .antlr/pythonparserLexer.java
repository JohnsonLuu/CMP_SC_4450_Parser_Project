// Generated from /Users/darianhu/Desktop/PythonParse/CMP_SC_4450_Parser_Project/pythonparser.g4 by ANTLR 4.9.2
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
		T__0=1, T__1=2, T__2=3, VAR=4, NUMBER=5, STRING=6, DIGIT=7, LETTER=8, 
		ASSIGNMENT_OPERATORS=9, ARITHMETIC_OPERATORS=10, ARITHMETIC_FUNCTIONS=11, 
		NEWLINE=12, WHITE_SPACE=13, CONDITIONAL_OPERATORS=14;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "VAR", "NUMBER", "STRING", "DIGIT", "LETTER", 
			"ASSIGNMENT_OPERATORS", "ARITHMETIC_OPERATORS", "ARITHMETIC_FUNCTIONS", 
			"NEWLINE", "WHITE_SPACE", "CONDITIONAL_OPERATORS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'and'", "'or'", "'not'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, "VAR", "NUMBER", "STRING", "DIGIT", "LETTER", 
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20\u0093\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\3\2\3\2\3\2\3\2\3\3\3\3\3"+
		"\3\3\4\3\4\3\4\3\4\3\5\3\5\5\5-\n\5\3\5\3\5\3\5\7\5\62\n\5\f\5\16\5\65"+
		"\13\5\3\6\5\68\n\6\3\6\6\6;\n\6\r\6\16\6<\3\7\3\7\7\7A\n\7\f\7\16\7D\13"+
		"\7\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\nU\n"+
		"\n\3\13\3\13\3\f\3\f\5\f[\n\f\3\f\5\f^\n\f\3\f\3\f\5\fb\n\f\3\f\3\f\5"+
		"\ff\n\f\3\f\5\fi\n\f\3\f\3\f\5\fm\n\f\3\f\3\f\5\fq\n\f\7\fs\n\f\f\f\16"+
		"\fv\13\f\3\r\3\r\7\rz\n\r\f\r\16\r}\13\r\3\r\3\r\3\16\6\16\u0082\n\16"+
		"\r\16\16\16\u0083\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3"+
		"\17\3\17\5\17\u0092\n\17\2\2\20\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23"+
		"\13\25\f\27\r\31\16\33\17\35\20\3\2\7\3\2\f\f\3\2\62;\4\2C\\c|\6\2\'\'"+
		",-//\61\61\5\2\13\f\17\17\"\"\2\u00ac\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2"+
		"\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2"+
		"\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3"+
		"\2\2\2\3\37\3\2\2\2\5#\3\2\2\2\7&\3\2\2\2\t,\3\2\2\2\13\67\3\2\2\2\r>"+
		"\3\2\2\2\17G\3\2\2\2\21I\3\2\2\2\23T\3\2\2\2\25V\3\2\2\2\27Z\3\2\2\2\31"+
		"w\3\2\2\2\33\u0081\3\2\2\2\35\u0091\3\2\2\2\37 \7c\2\2 !\7p\2\2!\"\7f"+
		"\2\2\"\4\3\2\2\2#$\7q\2\2$%\7t\2\2%\6\3\2\2\2&\'\7p\2\2\'(\7q\2\2()\7"+
		"v\2\2)\b\3\2\2\2*-\5\21\t\2+-\7a\2\2,*\3\2\2\2,+\3\2\2\2-\63\3\2\2\2."+
		"\62\5\21\t\2/\62\7a\2\2\60\62\5\17\b\2\61.\3\2\2\2\61/\3\2\2\2\61\60\3"+
		"\2\2\2\62\65\3\2\2\2\63\61\3\2\2\2\63\64\3\2\2\2\64\n\3\2\2\2\65\63\3"+
		"\2\2\2\668\7/\2\2\67\66\3\2\2\2\678\3\2\2\28:\3\2\2\29;\5\17\b\2:9\3\2"+
		"\2\2;<\3\2\2\2<:\3\2\2\2<=\3\2\2\2=\f\3\2\2\2>B\7$\2\2?A\n\2\2\2@?\3\2"+
		"\2\2AD\3\2\2\2B@\3\2\2\2BC\3\2\2\2CE\3\2\2\2DB\3\2\2\2EF\7$\2\2F\16\3"+
		"\2\2\2GH\t\3\2\2H\20\3\2\2\2IJ\t\4\2\2J\22\3\2\2\2KU\7?\2\2LM\7-\2\2M"+
		"U\7?\2\2NO\7/\2\2OU\7?\2\2PQ\7,\2\2QU\7?\2\2RS\7\61\2\2SU\7?\2\2TK\3\2"+
		"\2\2TL\3\2\2\2TN\3\2\2\2TP\3\2\2\2TR\3\2\2\2U\24\3\2\2\2VW\t\5\2\2W\26"+
		"\3\2\2\2X[\5\13\6\2Y[\5\t\5\2ZX\3\2\2\2ZY\3\2\2\2[]\3\2\2\2\\^\7\"\2\2"+
		"]\\\3\2\2\2]^\3\2\2\2^_\3\2\2\2_a\5\25\13\2`b\7\"\2\2a`\3\2\2\2ab\3\2"+
		"\2\2be\3\2\2\2cf\5\13\6\2df\5\t\5\2ec\3\2\2\2ed\3\2\2\2ft\3\2\2\2gi\7"+
		"\"\2\2hg\3\2\2\2hi\3\2\2\2ij\3\2\2\2jl\5\25\13\2km\7\"\2\2lk\3\2\2\2l"+
		"m\3\2\2\2mp\3\2\2\2nq\5\13\6\2oq\5\t\5\2pn\3\2\2\2po\3\2\2\2qs\3\2\2\2"+
		"rh\3\2\2\2sv\3\2\2\2tr\3\2\2\2tu\3\2\2\2u\30\3\2\2\2vt\3\2\2\2w{\7\f\2"+
		"\2xz\7\"\2\2yx\3\2\2\2z}\3\2\2\2{y\3\2\2\2{|\3\2\2\2|~\3\2\2\2}{\3\2\2"+
		"\2~\177\b\r\2\2\177\32\3\2\2\2\u0080\u0082\t\6\2\2\u0081\u0080\3\2\2\2"+
		"\u0082\u0083\3\2\2\2\u0083\u0081\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0085"+
		"\3\2\2\2\u0085\u0086\b\16\2\2\u0086\34\3\2\2\2\u0087\u0092\7>\2\2\u0088"+
		"\u0089\7>\2\2\u0089\u0092\7?\2\2\u008a\u0092\7@\2\2\u008b\u008c\7@\2\2"+
		"\u008c\u0092\7?\2\2\u008d\u008e\7?\2\2\u008e\u0092\7?\2\2\u008f\u0090"+
		"\7#\2\2\u0090\u0092\7?\2\2\u0091\u0087\3\2\2\2\u0091\u0088\3\2\2\2\u0091"+
		"\u008a\3\2\2\2\u0091\u008b\3\2\2\2\u0091\u008d\3\2\2\2\u0091\u008f\3\2"+
		"\2\2\u0092\36\3\2\2\2\25\2,\61\63\67<BTZ]aehlpt{\u0083\u0091\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}