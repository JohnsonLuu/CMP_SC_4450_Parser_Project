grammar pythonparser;

start: (variable)* EOF;

// variable assignment/definition TODO
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

//ASSIGNMENT_OPERATORS: 
 
//ARITHMETIC_OPERATORS: 

//ARITHMETIC_FUNCTIONS: 
   
//NEWLINE: 

//WHITE_SPACE: 
