grammar pythonparser;

start: (variable)* EOF;

// variable assignment/definition TODO
variable:  
    VAR ASSIGNMENT_OPERATORS (VAR | STRING | NUMBER | ARITHMETIC_FUNCTIONS) NEWLINE?;

//VAR: 

//NUMBER: 

//STRING: 

//DIGIT: 

//LETTER:

//ASSIGNMENT_OPERATORS: 
 
//ARITHMETIC_OPERATORS: 

//ARITHMETIC_FUNCTIONS: 
   
//NEWLINE: 

//WHITE_SPACE: 
