// Generated from /Users/darianhu/Desktop/PythonParse/CMP_SC_4450_Parser_Project/.history/pythonparser_20221116230245.g4 by ANTLR 4.9.2
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
		VAR=1, NUMBER=2, STRING=3, DIGIT=4, LETTER=5, ASSIGNMENT_OPERATORS=6, 
		ARITHMETIC_OPERATORS=7, ARITHMETIC_FUNCTIONS=8, NEWLINE=9, WHITE_SPACE=10;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"VAR", "NUMBER", "STRING", "DIGIT", "LETTER", "ASSIGNMENT_OPERATORS", 
			"ARITHMETIC_OPERATORS", "ARITHMETIC_FUNCTIONS", "NEWLINE", "WHITE_SPACE"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "VAR", "NUMBER", "STRING", "DIGIT", "LETTER", "ASSIGNMENT_OPERATORS", 
			"ARITHMETIC_OPERATORS", "ARITHMETIC_FUNCTIONS", "NEWLINE", "WHITE_SPACE"
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
	public String getGrammarFileName() { return "pythonparser_20221116230245.g4"; }

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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\ft\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\3\2\3\2\5\2\32\n\2\3\2\3\2\3\2\7\2\37\n\2\f\2\16\2\"\13\2\3\3\5\3"+
		"%\n\3\3\3\6\3(\n\3\r\3\16\3)\3\4\3\4\7\4.\n\4\f\4\16\4\61\13\4\3\4\3\4"+
		"\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7B\n\7\3\b\3\b"+
		"\3\t\3\t\5\tH\n\t\3\t\5\tK\n\t\3\t\3\t\5\tO\n\t\3\t\3\t\5\tS\n\t\3\t\5"+
		"\tV\n\t\3\t\3\t\5\tZ\n\t\3\t\3\t\5\t^\n\t\7\t`\n\t\f\t\16\tc\13\t\3\n"+
		"\3\n\7\ng\n\n\f\n\16\nj\13\n\3\n\3\n\3\13\6\13o\n\13\r\13\16\13p\3\13"+
		"\3\13\2\2\f\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\3\2\7\3\2\f"+
		"\f\3\2\62;\4\2C\\c|\6\2\'\',-//\61\61\5\2\13\f\17\17\"\"\2\u0088\2\3\3"+
		"\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2"+
		"\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\3\31\3\2\2\2\5$\3\2"+
		"\2\2\7+\3\2\2\2\t\64\3\2\2\2\13\66\3\2\2\2\rA\3\2\2\2\17C\3\2\2\2\21G"+
		"\3\2\2\2\23d\3\2\2\2\25n\3\2\2\2\27\32\5\13\6\2\30\32\7a\2\2\31\27\3\2"+
		"\2\2\31\30\3\2\2\2\32 \3\2\2\2\33\37\5\13\6\2\34\37\7a\2\2\35\37\5\t\5"+
		"\2\36\33\3\2\2\2\36\34\3\2\2\2\36\35\3\2\2\2\37\"\3\2\2\2 \36\3\2\2\2"+
		" !\3\2\2\2!\4\3\2\2\2\" \3\2\2\2#%\7/\2\2$#\3\2\2\2$%\3\2\2\2%\'\3\2\2"+
		"\2&(\5\t\5\2\'&\3\2\2\2()\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*\6\3\2\2\2+/\7"+
		"$\2\2,.\n\2\2\2-,\3\2\2\2.\61\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60\62\3\2"+
		"\2\2\61/\3\2\2\2\62\63\7$\2\2\63\b\3\2\2\2\64\65\t\3\2\2\65\n\3\2\2\2"+
		"\66\67\t\4\2\2\67\f\3\2\2\28B\7?\2\29:\7-\2\2:B\7?\2\2;<\7/\2\2<B\7?\2"+
		"\2=>\7,\2\2>B\7?\2\2?@\7\61\2\2@B\7?\2\2A8\3\2\2\2A9\3\2\2\2A;\3\2\2\2"+
		"A=\3\2\2\2A?\3\2\2\2B\16\3\2\2\2CD\t\5\2\2D\20\3\2\2\2EH\5\5\3\2FH\5\3"+
		"\2\2GE\3\2\2\2GF\3\2\2\2HJ\3\2\2\2IK\7\"\2\2JI\3\2\2\2JK\3\2\2\2KL\3\2"+
		"\2\2LN\5\17\b\2MO\7\"\2\2NM\3\2\2\2NO\3\2\2\2OR\3\2\2\2PS\5\5\3\2QS\5"+
		"\3\2\2RP\3\2\2\2RQ\3\2\2\2Sa\3\2\2\2TV\7\"\2\2UT\3\2\2\2UV\3\2\2\2VW\3"+
		"\2\2\2WY\5\17\b\2XZ\7\"\2\2YX\3\2\2\2YZ\3\2\2\2Z]\3\2\2\2[^\5\5\3\2\\"+
		"^\5\3\2\2][\3\2\2\2]\\\3\2\2\2^`\3\2\2\2_U\3\2\2\2`c\3\2\2\2a_\3\2\2\2"+
		"ab\3\2\2\2b\22\3\2\2\2ca\3\2\2\2dh\7\f\2\2eg\7\"\2\2fe\3\2\2\2gj\3\2\2"+
		"\2hf\3\2\2\2hi\3\2\2\2ik\3\2\2\2jh\3\2\2\2kl\b\n\2\2l\24\3\2\2\2mo\t\6"+
		"\2\2nm\3\2\2\2op\3\2\2\2pn\3\2\2\2pq\3\2\2\2qr\3\2\2\2rs\b\13\2\2s\26"+
		"\3\2\2\2\24\2\31\36 $)/AGJNRUY]ahp\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}