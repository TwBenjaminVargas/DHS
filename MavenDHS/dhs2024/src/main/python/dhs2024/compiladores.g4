grammar compiladores;

fragment LETRA : [A-Za-z] ;
fragment DIGITO : [0-9] ;

//INST : (LETRA | DIGITO | [- ,;{}()+=>] )+ '\n'; es una letra, un digito .. no quiero que exceda el guion 
PA: '(';
PC: ')';
LLA: '{';
LLC: '}';
PYC: ';';
//Operadores matematicos
SUMA: '+';
RESTA: '-';
MUL: '*';
DIV: '/';
MOD: '%';

ASIG : '=';
IGUAL: '==';

WHILE :'while';
NUMERO : DIGITO+ ;
INT:'int';
FOR: 'for';

WS : [ \t\n\r] -> skip;
ID : (LETRA | '_')(LETRA | DIGITO | '_')* ;

/*OTRO : . ;


s : ID     {print("ID ->" + $ID.text + "<--") }         s
  | NUMERO {print("NUMERO ->" + $NUMERO.text + "<--") } s
  | OTRO   {print("Otro ->" + $OTRO.text + "<--") }     s
  | EOF
  ;
  */

//si : s EOF; que comience en un nodo, que sea solo la razi del arbol
//s: PA s PC s  s permite la anidacion, se cierra un parentesis y se puede abrirotro parentesis. Verifica balance de parentesis
  //|
//;

programa : instrucciones EOF ; //secuencia de instrucciones hasta el final del archivo

instrucciones : instruccion instrucciones //es una instruccion con mas instrucciones 
                |
                ;
instruccion: declaracion
            | iwhile
            | bloque
            ;

declaracion: INT ID PYC ;

asignacion: ID ASIG opal PYC;

//operaciones aritmeticas y logicas
opal: exp; //completar considerar orden de prioridades
//expresion es la parte arimetica de las operaciones aritmeticas y logicas
exp: term e;
e : SUMA  term e
  | RESTA term e
  |
  ;
term  : factor  t;
t : MUL factor  t
  | DIV factor  t
  | MOD factor  t
  | 
  ;

factor  : NUMERO
        | ID
        | PA exp PC
        ;

iwhile : WHILE PA ID PC instruccion ;//llave representa una instruccion compuesta, despues del while viene siempre una instruccion

bloque : LLA instrucciones LLC; 

// Instruccion for
// ifor : FOR PA PYC PYC PC instruccion;
// init : ;
// cond : ;
// iter : ;
