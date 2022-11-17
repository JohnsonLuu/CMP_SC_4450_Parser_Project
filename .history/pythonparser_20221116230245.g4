grammar pythonparser;

start: (variable)* EOF;

variable:  
    VAR ASSIGNMENT_OPERATORS (VAR | STRING | NUMBER | ARITHMETIC_FUNCTIONS) NEWLINE?;

VAR: 
    (LETTER | '_') (LETTER | '_' | DIGIT)*;
// a number can contain a negative (match zero or one instance)
NUMBER: 
    (('-'? DIGIT+));
// string is between two " " a string cannot contain a new line or line break in between the quotes
STRING: 
    (('"' ~('\n')* '"'));
DIGIT: 
    ([0-9]);
LETTER:
    [a-zA-Z];

ASSIGNMENT_OPERATORS: 
	('=' | '+=' | '-=' | '*=' | '/=');

ARITHMETIC_OPERATORS: 
	('+' | '-' | '*' | '/' | '%');

// at minimum, an arithmetic function must be complete, e.g. x + y / 1 + 1 
// you can always add more aritmetic operators onto the minimum
ARITHMETIC_FUNCTIONS: 
	(NUMBER | VAR) ' '? ARITHMETIC_OPERATORS ' '? (NUMBER| VAR) (' '? ARITHMETIC_OPERATORS ' '? (NUMBER | VAR))*;

// a new line always has \n 
NEWLINE: 
	('\n' ' '*) -> skip;

WHITE_SPACE: 
	[ \r\n\t]+ -> skip;