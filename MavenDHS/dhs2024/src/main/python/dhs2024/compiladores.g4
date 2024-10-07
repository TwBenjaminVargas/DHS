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
INC:'++';
DEC: '--';

//Operadores logicos
AND: '&&';
OR: '||';
IGUAL: '==';

ASIG : '=';

WHILE :'while';
NUMERO : DIGITO+ ;
INT:'int';
FOR: 'for';
IF: 'if';

//saltarse todo tipo de espacio
WS : [ \t\n\r] -> skip;

//varables
ID : (LETRA | '_')(LETRA | DIGITO | '_')* ;

/*OTRO : . ;



//control tokens
s : ID     {print("ID ->" + $ID.text + "<--") }         s
  | NUMERO {print("NUMERO ->" + $NUMERO.text + "<--") } s
  | OTRO   {print("Otro ->" + $OTRO.text + "<--") }     s
  | EOF
  ;
  */

//si : s EOF; que comience en un nodo, que sea solo la razi del arbol
//s: PA s PC s  s permite la anidacion, se cierra un parentesis y se puede abrirotro parentesis. Verifica balance de parentesis


//programa
programa : instrucciones EOF ; //secuencia de instrucciones hasta el final del archivo

instrucciones : instruccion instrucciones //es una instruccion con mas instrucciones 
                |
                ;
instruccion: declaracion PYC
            | iwhile
            | bloque
            | ifor
            | iif
            | asignacion PYC
            ;

declaracion: INT ID;

asignacion: ID ASIG opal;

//operaciones aritmeticas y logicas
opal: exp
    | logic
    ; //completar considerar orden de prioridades

// se realizan las siguiente reglas para cumplir con el orden de prioridades
logic : log  l;
l : OR  log  l
  |
  ;

log: exp lo;
lo: AND exp lo
  |
  ;


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

iwhile : WHILE PA ID PC instruccion ;

bloque : LLA instrucciones LLC; 


// estructura for
ifor  : FOR PA  init  PYC cond PYC iter PC  instruccion;

init  : asignacion
      |
      ;
cond : logic
     |
     ;
iter  : ID INC
      | ID DEC
      | asignacion
      |
      ;

iif:  PA cond PC instruccion;
//preguntas:
//- Se puede declarar en el for?
//mejoras:
//-Incrementos añadidos a las operaciones aritmeticas
//menor o igual en logicas