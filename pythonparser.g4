grammar pythonparser;

start: 
    (definitions)* EOF;

definitions: 
    variable | ifblocks | whileloop | comment | forloop | function;

variable:  
    VAR ASSIGN_OP (VAR | STRING | NUMBER | ARITH_FUNC) NEWLINE?;

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

ASSIGN_OP: 
	('=' | '+=' | '-=' | '*=' | '/=');

ARITH_OP: 
	('+' | '-' | '*' | '/' | '%');

// at minimum, an arithmetic function must be complete, e.g. x + y / 1 + 1 
// you can always add more aritmetic operators onto the minimum
ARITH_FUNC: 
	(NUMBER | VAR) ' '? ARITH_OP ' '? (NUMBER| VAR) (' '? ARITH_OP ' '? (NUMBER | VAR))*;

// a new line always has \n 
NEWLINE: 
	('\n' ' '*) -> skip;

WHITE_SPACE: 
	[ \r\n\t]+ -> skip;

conditional: 
    VAR
    | NUMBER
    | STRING
    | ARITH_FUNC
    | conditional ('and' | 'or' | 'not') conditional
    | conditional COND_OP conditional
    | conditional ARITH_OP conditional;

COND_OP: 
    ('<' | '<=' | '>' | '>=' | '==' | '!=');

ifblocks: 
    ('if' '('? conditional ')'? ':' block)
    ('elif' '('? conditional ')'? ':' block)*
    ('else' ':' block)?;

block: 
    (((definitions)+ 'break'? | 'break') NEWLINE?);

whileloop: 
    ('while' conditional ':' block);

comment : 
    COMMENT;

COMMENT: 
    '#' ~('\n' | '\r')*;

// range parameters are start and stop
forloop: 
    ('for' VAR 'in' (VAR | 'range(' (NUMBER | ((VAR | NUMBER | ARITH_FUNC) ',' (VAR | NUMBER | ARITH_FUNC)))) '):'  block);

function: 
    ('def' VAR '(' ((VAR | NUMBER)','?)* '):' block);