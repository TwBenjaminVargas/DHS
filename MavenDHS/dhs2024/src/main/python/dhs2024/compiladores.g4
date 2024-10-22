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
WHILE :'while';
NUMERO : DIGITO+ ;
INT:'int';
FOR: 'for';
IF: 'if';
ELSE: 'else';

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

opal : exp ; //completar

//exp : lor a ;
exp : lor ;

lor: land a ;
a : OR lor a
  |
  ;

land : inot l ;
l : AND land l
  |
  ;

inot : comp n ;
n : NOT inot n
  | IGUAL inot n
  |
  ;

comp : op c ;
/*c : MAYOR comp c
  | MENOR comp c
  | MAI comp c
  | MEI comp c
  |
  ;*/
c : (MAYOR | MENOR | MAI | MEI) comp  // Comparadores
  |                                   // Regla vacía permitiendo finalizar sin comparador
  ;

op : term e ;
/*e : SUMA op e
  | RESTA op e
//  | op e
  |
  ; */
e : (SUMA | RESTA) op 
  |                  // Regla vacía permitiendo finalizar sin SUMA o RESTA
  ;

term : factor t ;
/*t : MULT factor t 
  | DIV factor t
  | MOD factor t
  |
  ;*/
t : (MULT | DIV | MOD) factor 
  |                       // Regla vacía permitiendo finalizar sin operador
  ;


factor : NUMERO 
       | ID
       | PA exp PC
       | suf
       | pref
       ;


suf : ID (INC | DEC);

pref : (INC | DEC)  ID;



iwhile : WHILE PA ID PC instruccion ;

bloque : LLA instrucciones LLC; 


// estructura for
ifor  : FOR PA  init  PYC cond PYC iter PC  instruccion;

init  : asignacion
      |
      ;
cond : opal
     |
     ;
iter  : 
      | asignacion
      | suf
      | pref
      ;

iif : IF PA cond PC instruccion
    | IF PA cond PC instruccion ielse;

ielse : ELSE instruccion;
//preguntas:
//- Se puede declarar en el for?
//  -NO ES NECESARIO
//mejoras:
//-Incrementos añadidos a las operaciones aritmeticas
//menor o igual en logicas