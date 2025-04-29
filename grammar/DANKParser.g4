parser grammar DANKParser;
options { tokenVocab=DANKLexer; }

program: statement* EOF;

statement: print
    | fun_def
    | fun_call
    | loop
    | var_def
    | conditional
    | breakpoint
    ;

print: PRINT_BEGIN expression? PRINT_END;

factor
    : '(' expression ')'
    | (PLUS | MINUS | COND_PLUS | COND_MINUS)? operand
    ;

term
    : factor ((MULT | DIV) factor)*
    ;

expression
    : term ((PLUS | MINUS) term)*
    ;


loop: LOOP_BEGIN statement* LOOP_END;
var_def: ID EQ expression;

operand: STRING | ID | NUMBER | COND_ID | COND_NUMBER;

logical_expression: factor (COND_EQ | COND_LT | COND_GT | COND_LTE | COND_GTE | COND_NEQ) factor;

conditional: CONDITIONAL_BEGIN logical_expression END_QUOTE_GT_COND statement* CONDITIONAL_END;
breakpoint: BREAKPOINT;



params: params_2 ',' factor | factor;
params_2: params_2 ',' factor | factor;


fun_def: FUNCTION_BEGIN FUNCTION_NAME END_QUOTE_GT PARAMS_BEGIN ids? PARAMS_END statement* FUNCTION_END;
ids: ids_2 ',' ID | ID;
ids_2: ids_2 ',' ID | ID;
fun_call: ID '(' params? ')';