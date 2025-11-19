grammar matriz;

programa    : sentencia* EOF ;

sentencia   : assignar ';'
            | imprimir ';'
            ;

assignar    : ID '=' expr ;
imprimir    : 'print' ID ;

expr        : punto ( '*' punto )* ;

punto       : matriz
            | ID
            | '(' expr ')'
            ;

matriz      : '[' filas ']' ;
filas       : fila (',' fila)* ;
fila        : '[' numeros ']' ;
numeros     : NUMERO (',' NUMERO)* ;

ID          : [a-zA-Z_][a-zA-Z_0-9]* ;
NUMERO      : '-'? [0-9]+ ('.' [0-9]+)? ;
WS          : [ \t\r\n]+ -> skip ;

