// DELETE THIS CONTENT IF YOU PUT COMBINED GRAMMAR IN Parser TAB
lexer grammar DANKLexer;

EQ : '=' ;
LT: '<';
GT: '>';
LTE: '<=';
GTE: '>=';
NEQ: '~';


COMMA : ',' ;
SEMI : ';' ;
LPAREN : '(' ;
RPAREN : ')' ;

PLUS : '+';
MINUS: '-';
MULT: '*';
DIV: '/';

PRINT_BEGIN: '<present>';
PRINT_END: '</present>';
LOOP_BEGIN: '<cycle>';
LOOP_END: '</cycle>';
BREAKPOINT: '<leave>';
CONDITIONAL_BEGIN: '<branch condition="' -> pushMode(CONDITIONAL_MODE);
CONDITIONAL_END: '</branch>';

PARAMS_BEGIN: '<params>';
PARAMS_END:'</params>';




FUNCTION_BEGIN: '<delegate name="' -> pushMode(DELEGATE_MODE);
FUNCTION_END:'</delegate>';




    
SIGN: PLUS | MINUS;
NUMBER: [1-9][0-9]* '.' [0-9]* 
    | [0-9]* '.' [0-9]* 
    | [1-9][0-9]*
    | [0];


STRING : '"' ( '\\' '"' | ~["\\] )*? '"' ;

ID: [a-zA-Z_][a-zA-Z_0-9]* ;




WS: [ \t\n\r\f]+ -> skip ;
COMMENT: '<comment>' .*? '</comment>' ->skip;


mode CONDITIONAL_MODE;


COND_ID     : [a-zA-Z_][a-zA-Z_0-9]* ;
COND_NUMBER : [1-9][0-9]* '.' [0-9]* 
    | [0-9]* '.' [0-9]* 
    | [1-9][0-9]*
    | [0];
COND_GT     : '>';
COND_LT     : '<';
COND_GTE    : '>=';
COND_LTE    : '<=';
COND_EQ     : '=';
COND_NEQ    : '~';
COND_PLUS   : '+';
COND_MINUS  : '-';

END_QUOTE_GT_COND: '">' -> popMode;
COND_WS : [ \t\r\n]+ -> skip ;

mode DELEGATE_MODE;
FUNCTION_NAME: ID;
END_QUOTE_GT : '">' -> popMode;