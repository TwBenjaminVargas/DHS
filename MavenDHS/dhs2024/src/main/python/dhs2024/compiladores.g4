grammar compiladores;

fragment LETRA : [A-Za-z] ;
fragment DIGITO : [0-9] ;

//INST : (LETRA | DIGITO | [- ,;{}()+=>] )+ '\n'; es una letra, un digito .. no quiero que exceda el guion 
PA: '(';
PC: ')';
LLA: '{';
LLC: '}';
PYC: ';';
C: ',';
PTO : '.';
COMILLA : '\'';
//Operadores matematicos
SUMA: '+';
RESTA: '-';
MULT: '*';
DIV: '/';
MOD: '%';
INC:'++';
DEC: '--';

//Operadores logicos
AND: '&&';
OR: '||';
IGUAL: '==';
NOT: '!=';
ASIG : '=';
MENOR : '<';
MAYOR : '>';
MEI : '<=';
MAI : '>=';
NUMERO : DIGITO+ ;
DECIMAL : NUMERO PTO NUMERO ;
CARACTER : COMILLA (LETRA|DIGITO|) COMILLA ;
WHILE :'while';
FOR: 'for';
IF: 'if';
ELSE: 'else';
RETURN : 'return';

//tipo de dato
INT:'int';
FLOAT: 'float';
CHAR: 'char';
VOID: 'void';

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
            | ifuncion
            | ireturn
            | illamada PYC
            | iprototipo
            ;


//declaracion: ;
declaracion : tipo ID dec
            | tipo asignacion dec
            ;

dec : C ID dec
    | C asignacion dec
    |
    ;

tipo  : (INT | VOID | FLOAT | CHAR);

// corregir para permitir la combinacion de los mismos
asignacion: ID ASIG opal
          ;

opal : exp ; 

exp : lor ;

lor: land a ;
a : OR land a
  |
  ;

land : inot l ;
l : AND inot l
  |
  ;

inot : comp n ;
n : NOT comp n
  | IGUAL comp n
  |
  ;

comp : op c ;
c : MAYOR op c
  | MENOR op c
  | MAI op c
  | MEI op c
  |
  ;

op : term e ;

e : SUMA term e
  | RESTA term e
  |
  ; 

term : factor t ;
t : MULT factor t 
  | DIV factor t
  | MOD factor t
  |
  ;


factor : NUMERO 
       | ID
       | DECIMAL
       | CARACTER
       | PA exp PC
       | illamada
       ;


iwhile  :  WHILE PA cond PC instruccion ;

cond  : opal;

bloque  :  LLA instrucciones LLC; 


// estructura for
ifor  : FOR PA  init  PYC condlist PYC iter PC  instruccion;

init  : asignacion
      |
      ;

condlist  : cond
          |
          ;
iter  : asignacion
      |
      ;

iif : IF PA cond PC instruccion
    | IF PA cond PC instruccion ielse;

ielse : ELSE instruccion;

iprototipo : tipo ID PA protoparam PC PYC ;

protoparam : tipo C protoparam
      | tipo
      |
      ;

ifuncion  : tipo ID PA param PC instruccion;

param : p C param
      | p
      |
      ;

p : tipo ID;

ireturn : RETURN opal PYC;

illamada : ID PA argumento PC;

argumento : opal C argumento
          | opal
          |
          ;

