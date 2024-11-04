# Generated from /home/ben/Documentos/DHS/MavenDHS/dhs2024/src/main/python/dhs2024/compiladores.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,38,281,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,
        1,82,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,3,2,99,8,2,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,3,5,112,
        8,5,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,3,9,126,8,9,
        1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,3,11,136,8,11,1,12,1,12,
        1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,150,8,13,
        1,14,1,14,1,14,1,15,1,15,1,15,3,15,158,8,15,1,16,1,16,1,16,1,17,
        1,17,1,17,3,17,166,8,17,1,18,1,18,1,18,1,19,1,19,1,19,3,19,174,8,
        19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,186,8,
        20,1,21,1,21,1,21,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,
        24,1,24,3,24,202,8,24,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,
        26,1,26,1,26,1,26,1,26,1,26,1,27,1,27,3,27,220,8,27,1,28,1,28,3,
        28,224,8,28,1,29,1,29,1,29,1,29,3,29,230,8,29,1,30,1,30,1,30,1,30,
        1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,3,30,245,8,30,1,31,
        1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,33,
        1,33,1,33,3,33,263,8,33,1,34,1,34,1,34,1,34,1,35,1,35,1,35,1,35,
        1,35,1,36,1,36,1,36,1,36,1,36,3,36,279,8,36,1,36,0,0,37,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,
        52,54,56,58,60,62,64,66,68,70,72,0,5,1,0,33,36,1,0,21,24,1,0,9,10,
        1,0,11,13,1,0,14,15,277,0,74,1,0,0,0,2,81,1,0,0,0,4,98,1,0,0,0,6,
        100,1,0,0,0,8,103,1,0,0,0,10,111,1,0,0,0,12,113,1,0,0,0,14,115,1,
        0,0,0,16,117,1,0,0,0,18,125,1,0,0,0,20,127,1,0,0,0,22,135,1,0,0,
        0,24,137,1,0,0,0,26,149,1,0,0,0,28,151,1,0,0,0,30,157,1,0,0,0,32,
        159,1,0,0,0,34,165,1,0,0,0,36,167,1,0,0,0,38,173,1,0,0,0,40,185,
        1,0,0,0,42,187,1,0,0,0,44,190,1,0,0,0,46,193,1,0,0,0,48,201,1,0,
        0,0,50,203,1,0,0,0,52,207,1,0,0,0,54,219,1,0,0,0,56,223,1,0,0,0,
        58,229,1,0,0,0,60,244,1,0,0,0,62,246,1,0,0,0,64,249,1,0,0,0,66,262,
        1,0,0,0,68,264,1,0,0,0,70,268,1,0,0,0,72,278,1,0,0,0,74,75,3,2,1,
        0,75,76,5,0,0,1,76,1,1,0,0,0,77,78,3,4,2,0,78,79,3,2,1,0,79,82,1,
        0,0,0,80,82,1,0,0,0,81,77,1,0,0,0,81,80,1,0,0,0,82,3,1,0,0,0,83,
        84,3,6,3,0,84,85,5,5,0,0,85,99,1,0,0,0,86,99,3,46,23,0,87,99,3,50,
        25,0,88,99,3,52,26,0,89,99,3,60,30,0,90,91,3,10,5,0,91,92,5,5,0,
        0,92,99,1,0,0,0,93,99,3,64,32,0,94,99,3,68,34,0,95,96,3,70,35,0,
        96,97,5,5,0,0,97,99,1,0,0,0,98,83,1,0,0,0,98,86,1,0,0,0,98,87,1,
        0,0,0,98,88,1,0,0,0,98,89,1,0,0,0,98,90,1,0,0,0,98,93,1,0,0,0,98,
        94,1,0,0,0,98,95,1,0,0,0,99,5,1,0,0,0,100,101,3,8,4,0,101,102,5,
        38,0,0,102,7,1,0,0,0,103,104,7,0,0,0,104,9,1,0,0,0,105,106,5,38,
        0,0,106,107,5,20,0,0,107,112,3,12,6,0,108,109,5,38,0,0,109,110,5,
        20,0,0,110,112,3,70,35,0,111,105,1,0,0,0,111,108,1,0,0,0,112,11,
        1,0,0,0,113,114,3,14,7,0,114,13,1,0,0,0,115,116,3,16,8,0,116,15,
        1,0,0,0,117,118,3,20,10,0,118,119,3,18,9,0,119,17,1,0,0,0,120,121,
        5,17,0,0,121,122,3,16,8,0,122,123,3,18,9,0,123,126,1,0,0,0,124,126,
        1,0,0,0,125,120,1,0,0,0,125,124,1,0,0,0,126,19,1,0,0,0,127,128,3,
        24,12,0,128,129,3,22,11,0,129,21,1,0,0,0,130,131,5,16,0,0,131,132,
        3,20,10,0,132,133,3,22,11,0,133,136,1,0,0,0,134,136,1,0,0,0,135,
        130,1,0,0,0,135,134,1,0,0,0,136,23,1,0,0,0,137,138,3,28,14,0,138,
        139,3,26,13,0,139,25,1,0,0,0,140,141,5,19,0,0,141,142,3,24,12,0,
        142,143,3,26,13,0,143,150,1,0,0,0,144,145,5,18,0,0,145,146,3,24,
        12,0,146,147,3,26,13,0,147,150,1,0,0,0,148,150,1,0,0,0,149,140,1,
        0,0,0,149,144,1,0,0,0,149,148,1,0,0,0,150,27,1,0,0,0,151,152,3,32,
        16,0,152,153,3,30,15,0,153,29,1,0,0,0,154,155,7,1,0,0,155,158,3,
        28,14,0,156,158,1,0,0,0,157,154,1,0,0,0,157,156,1,0,0,0,158,31,1,
        0,0,0,159,160,3,36,18,0,160,161,3,34,17,0,161,33,1,0,0,0,162,163,
        7,2,0,0,163,166,3,32,16,0,164,166,1,0,0,0,165,162,1,0,0,0,165,164,
        1,0,0,0,166,35,1,0,0,0,167,168,3,40,20,0,168,169,3,38,19,0,169,37,
        1,0,0,0,170,171,7,3,0,0,171,174,3,40,20,0,172,174,1,0,0,0,173,170,
        1,0,0,0,173,172,1,0,0,0,174,39,1,0,0,0,175,186,5,25,0,0,176,186,
        5,38,0,0,177,186,5,26,0,0,178,186,5,27,0,0,179,180,5,1,0,0,180,181,
        3,14,7,0,181,182,5,2,0,0,182,186,1,0,0,0,183,186,3,42,21,0,184,186,
        3,44,22,0,185,175,1,0,0,0,185,176,1,0,0,0,185,177,1,0,0,0,185,178,
        1,0,0,0,185,179,1,0,0,0,185,183,1,0,0,0,185,184,1,0,0,0,186,41,1,
        0,0,0,187,188,5,38,0,0,188,189,7,4,0,0,189,43,1,0,0,0,190,191,7,
        4,0,0,191,192,5,38,0,0,192,45,1,0,0,0,193,194,5,28,0,0,194,195,5,
        1,0,0,195,196,3,48,24,0,196,197,5,2,0,0,197,198,3,4,2,0,198,47,1,
        0,0,0,199,202,3,12,6,0,200,202,3,40,20,0,201,199,1,0,0,0,201,200,
        1,0,0,0,202,49,1,0,0,0,203,204,5,3,0,0,204,205,3,2,1,0,205,206,5,
        4,0,0,206,51,1,0,0,0,207,208,5,29,0,0,208,209,5,1,0,0,209,210,3,
        54,27,0,210,211,5,5,0,0,211,212,3,56,28,0,212,213,5,5,0,0,213,214,
        3,58,29,0,214,215,5,2,0,0,215,216,3,4,2,0,216,53,1,0,0,0,217,220,
        3,10,5,0,218,220,1,0,0,0,219,217,1,0,0,0,219,218,1,0,0,0,220,55,
        1,0,0,0,221,224,3,48,24,0,222,224,1,0,0,0,223,221,1,0,0,0,223,222,
        1,0,0,0,224,57,1,0,0,0,225,230,1,0,0,0,226,230,3,10,5,0,227,230,
        3,42,21,0,228,230,3,44,22,0,229,225,1,0,0,0,229,226,1,0,0,0,229,
        227,1,0,0,0,229,228,1,0,0,0,230,59,1,0,0,0,231,232,5,30,0,0,232,
        233,5,1,0,0,233,234,3,48,24,0,234,235,5,2,0,0,235,236,3,4,2,0,236,
        245,1,0,0,0,237,238,5,30,0,0,238,239,5,1,0,0,239,240,3,48,24,0,240,
        241,5,2,0,0,241,242,3,4,2,0,242,243,3,62,31,0,243,245,1,0,0,0,244,
        231,1,0,0,0,244,237,1,0,0,0,245,61,1,0,0,0,246,247,5,31,0,0,247,
        248,3,4,2,0,248,63,1,0,0,0,249,250,3,8,4,0,250,251,5,38,0,0,251,
        252,5,1,0,0,252,253,3,66,33,0,253,254,5,2,0,0,254,255,3,4,2,0,255,
        65,1,0,0,0,256,257,3,6,3,0,257,258,5,6,0,0,258,259,3,66,33,0,259,
        263,1,0,0,0,260,263,3,6,3,0,261,263,1,0,0,0,262,256,1,0,0,0,262,
        260,1,0,0,0,262,261,1,0,0,0,263,67,1,0,0,0,264,265,5,32,0,0,265,
        266,3,12,6,0,266,267,5,5,0,0,267,69,1,0,0,0,268,269,5,38,0,0,269,
        270,5,1,0,0,270,271,3,72,36,0,271,272,5,2,0,0,272,71,1,0,0,0,273,
        274,5,38,0,0,274,275,5,6,0,0,275,279,3,72,36,0,276,279,5,38,0,0,
        277,279,1,0,0,0,278,273,1,0,0,0,278,276,1,0,0,0,278,277,1,0,0,0,
        279,73,1,0,0,0,17,81,98,111,125,135,149,157,165,173,185,201,219,
        223,229,244,262,278
    ]

class compiladoresParser ( Parser ):

    grammarFileName = "compiladores.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "';'", "','", 
                     "'.'", "'''", "'+'", "'-'", "'*'", "'/'", "'%'", "'++'", 
                     "'--'", "'&&'", "'||'", "'=='", "'!='", "'='", "'<'", 
                     "'>'", "'<='", "'>='", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'while'", "'for'", "'if'", "'else'", "'return'", "'int'", 
                     "'float'", "'char'", "'void'" ]

    symbolicNames = [ "<INVALID>", "PA", "PC", "LLA", "LLC", "PYC", "C", 
                      "PTO", "COMILLA", "SUMA", "RESTA", "MULT", "DIV", 
                      "MOD", "INC", "DEC", "AND", "OR", "IGUAL", "NOT", 
                      "ASIG", "MENOR", "MAYOR", "MEI", "MAI", "NUMERO", 
                      "DECIMAL", "CARACTER", "WHILE", "FOR", "IF", "ELSE", 
                      "RETURN", "INT", "FLOAT", "CHAR", "VOID", "WS", "ID" ]

    RULE_programa = 0
    RULE_instrucciones = 1
    RULE_instruccion = 2
    RULE_declaracion = 3
    RULE_tipo = 4
    RULE_asignacion = 5
    RULE_opal = 6
    RULE_exp = 7
    RULE_lor = 8
    RULE_a = 9
    RULE_land = 10
    RULE_l = 11
    RULE_inot = 12
    RULE_n = 13
    RULE_comp = 14
    RULE_c = 15
    RULE_op = 16
    RULE_e = 17
    RULE_term = 18
    RULE_t = 19
    RULE_factor = 20
    RULE_suf = 21
    RULE_pref = 22
    RULE_iwhile = 23
    RULE_cond = 24
    RULE_bloque = 25
    RULE_ifor = 26
    RULE_init = 27
    RULE_condlist = 28
    RULE_iter = 29
    RULE_iif = 30
    RULE_ielse = 31
    RULE_ifuncion = 32
    RULE_param = 33
    RULE_ireturn = 34
    RULE_illamada = 35
    RULE_argumento = 36

    ruleNames =  [ "programa", "instrucciones", "instruccion", "declaracion", 
                   "tipo", "asignacion", "opal", "exp", "lor", "a", "land", 
                   "l", "inot", "n", "comp", "c", "op", "e", "term", "t", 
                   "factor", "suf", "pref", "iwhile", "cond", "bloque", 
                   "ifor", "init", "condlist", "iter", "iif", "ielse", "ifuncion", 
                   "param", "ireturn", "illamada", "argumento" ]

    EOF = Token.EOF
    PA=1
    PC=2
    LLA=3
    LLC=4
    PYC=5
    C=6
    PTO=7
    COMILLA=8
    SUMA=9
    RESTA=10
    MULT=11
    DIV=12
    MOD=13
    INC=14
    DEC=15
    AND=16
    OR=17
    IGUAL=18
    NOT=19
    ASIG=20
    MENOR=21
    MAYOR=22
    MEI=23
    MAI=24
    NUMERO=25
    DECIMAL=26
    CARACTER=27
    WHILE=28
    FOR=29
    IF=30
    ELSE=31
    RETURN=32
    INT=33
    FLOAT=34
    CHAR=35
    VOID=36
    WS=37
    ID=38

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instrucciones(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionesContext,0)


        def EOF(self):
            return self.getToken(compiladoresParser.EOF, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = compiladoresParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.instrucciones()
            self.state = 75
            self.match(compiladoresParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


        def instrucciones(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionesContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_instrucciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrucciones" ):
                listener.enterInstrucciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrucciones" ):
                listener.exitInstrucciones(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrucciones" ):
                return visitor.visitInstrucciones(self)
            else:
                return visitor.visitChildren(self)




    def instrucciones(self):

        localctx = compiladoresParser.InstruccionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instrucciones)
        try:
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 28, 29, 30, 32, 33, 34, 35, 36, 38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.instruccion()
                self.state = 78
                self.instrucciones()
                pass
            elif token in [-1, 4]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion(self):
            return self.getTypedRuleContext(compiladoresParser.DeclaracionContext,0)


        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

        def iwhile(self):
            return self.getTypedRuleContext(compiladoresParser.IwhileContext,0)


        def bloque(self):
            return self.getTypedRuleContext(compiladoresParser.BloqueContext,0)


        def ifor(self):
            return self.getTypedRuleContext(compiladoresParser.IforContext,0)


        def iif(self):
            return self.getTypedRuleContext(compiladoresParser.IifContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(compiladoresParser.AsignacionContext,0)


        def ifuncion(self):
            return self.getTypedRuleContext(compiladoresParser.IfuncionContext,0)


        def ireturn(self):
            return self.getTypedRuleContext(compiladoresParser.IreturnContext,0)


        def illamada(self):
            return self.getTypedRuleContext(compiladoresParser.IllamadaContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_instruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion" ):
                listener.enterInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion" ):
                listener.exitInstruccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccion" ):
                return visitor.visitInstruccion(self)
            else:
                return visitor.visitChildren(self)




    def instruccion(self):

        localctx = compiladoresParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_instruccion)
        try:
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.declaracion()
                self.state = 84
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.iwhile()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 87
                self.bloque()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 88
                self.ifor()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 89
                self.iif()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 90
                self.asignacion()
                self.state = 91
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 93
                self.ifuncion()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 94
                self.ireturn()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 95
                self.illamada()
                self.state = 96
                self.match(compiladoresParser.PYC)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(compiladoresParser.TipoContext,0)


        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_declaracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)




    def declaracion(self):

        localctx = compiladoresParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.tipo()
            self.state = 101
            self.match(compiladoresParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(compiladoresParser.INT, 0)

        def VOID(self):
            return self.getToken(compiladoresParser.VOID, 0)

        def FLOAT(self):
            return self.getToken(compiladoresParser.FLOAT, 0)

        def CHAR(self):
            return self.getToken(compiladoresParser.CHAR, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo" ):
                return visitor.visitTipo(self)
            else:
                return visitor.visitChildren(self)




    def tipo(self):

        localctx = compiladoresParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 128849018880) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def ASIG(self):
            return self.getToken(compiladoresParser.ASIG, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def illamada(self):
            return self.getTypedRuleContext(compiladoresParser.IllamadaContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = compiladoresParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_asignacion)
        try:
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.match(compiladoresParser.ID)
                self.state = 106
                self.match(compiladoresParser.ASIG)
                self.state = 107
                self.opal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.match(compiladoresParser.ID)
                self.state = 109
                self.match(compiladoresParser.ASIG)
                self.state = 110
                self.illamada()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(compiladoresParser.ExpContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_opal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpal" ):
                listener.enterOpal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpal" ):
                listener.exitOpal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpal" ):
                return visitor.visitOpal(self)
            else:
                return visitor.visitChildren(self)




    def opal(self):

        localctx = compiladoresParser.OpalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_opal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lor(self):
            return self.getTypedRuleContext(compiladoresParser.LorContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = compiladoresParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.lor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def land(self):
            return self.getTypedRuleContext(compiladoresParser.LandContext,0)


        def a(self):
            return self.getTypedRuleContext(compiladoresParser.AContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_lor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLor" ):
                listener.enterLor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLor" ):
                listener.exitLor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLor" ):
                return visitor.visitLor(self)
            else:
                return visitor.visitChildren(self)




    def lor(self):

        localctx = compiladoresParser.LorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_lor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.land()
            self.state = 118
            self.a()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OR(self):
            return self.getToken(compiladoresParser.OR, 0)

        def lor(self):
            return self.getTypedRuleContext(compiladoresParser.LorContext,0)


        def a(self):
            return self.getTypedRuleContext(compiladoresParser.AContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_a

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterA" ):
                listener.enterA(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitA" ):
                listener.exitA(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitA" ):
                return visitor.visitA(self)
            else:
                return visitor.visitChildren(self)




    def a(self):

        localctx = compiladoresParser.AContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_a)
        try:
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.match(compiladoresParser.OR)
                self.state = 121
                self.lor()
                self.state = 122
                self.a()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def inot(self):
            return self.getTypedRuleContext(compiladoresParser.InotContext,0)


        def l(self):
            return self.getTypedRuleContext(compiladoresParser.LContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_land

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLand" ):
                listener.enterLand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLand" ):
                listener.exitLand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLand" ):
                return visitor.visitLand(self)
            else:
                return visitor.visitChildren(self)




    def land(self):

        localctx = compiladoresParser.LandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_land)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.inot()
            self.state = 128
            self.l()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(compiladoresParser.AND, 0)

        def land(self):
            return self.getTypedRuleContext(compiladoresParser.LandContext,0)


        def l(self):
            return self.getTypedRuleContext(compiladoresParser.LContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_l

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterL" ):
                listener.enterL(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitL" ):
                listener.exitL(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitL" ):
                return visitor.visitL(self)
            else:
                return visitor.visitChildren(self)




    def l(self):

        localctx = compiladoresParser.LContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_l)
        try:
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.match(compiladoresParser.AND)
                self.state = 131
                self.land()
                self.state = 132
                self.l()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InotContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comp(self):
            return self.getTypedRuleContext(compiladoresParser.CompContext,0)


        def n(self):
            return self.getTypedRuleContext(compiladoresParser.NContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_inot

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInot" ):
                listener.enterInot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInot" ):
                listener.exitInot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInot" ):
                return visitor.visitInot(self)
            else:
                return visitor.visitChildren(self)




    def inot(self):

        localctx = compiladoresParser.InotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_inot)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.comp()
            self.state = 138
            self.n()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(compiladoresParser.NOT, 0)

        def inot(self):
            return self.getTypedRuleContext(compiladoresParser.InotContext,0)


        def n(self):
            return self.getTypedRuleContext(compiladoresParser.NContext,0)


        def IGUAL(self):
            return self.getToken(compiladoresParser.IGUAL, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_n

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterN" ):
                listener.enterN(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitN" ):
                listener.exitN(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitN" ):
                return visitor.visitN(self)
            else:
                return visitor.visitChildren(self)




    def n(self):

        localctx = compiladoresParser.NContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_n)
        try:
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.match(compiladoresParser.NOT)
                self.state = 141
                self.inot()
                self.state = 142
                self.n()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.match(compiladoresParser.IGUAL)
                self.state = 145
                self.inot()
                self.state = 146
                self.n()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op(self):
            return self.getTypedRuleContext(compiladoresParser.OpContext,0)


        def c(self):
            return self.getTypedRuleContext(compiladoresParser.CContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_comp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComp" ):
                listener.enterComp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComp" ):
                listener.exitComp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComp" ):
                return visitor.visitComp(self)
            else:
                return visitor.visitChildren(self)




    def comp(self):

        localctx = compiladoresParser.CompContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_comp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.op()
            self.state = 152
            self.c()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comp(self):
            return self.getTypedRuleContext(compiladoresParser.CompContext,0)


        def MAYOR(self):
            return self.getToken(compiladoresParser.MAYOR, 0)

        def MENOR(self):
            return self.getToken(compiladoresParser.MENOR, 0)

        def MAI(self):
            return self.getToken(compiladoresParser.MAI, 0)

        def MEI(self):
            return self.getToken(compiladoresParser.MEI, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_c

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterC" ):
                listener.enterC(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitC" ):
                listener.exitC(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitC" ):
                return visitor.visitC(self)
            else:
                return visitor.visitChildren(self)




    def c(self):

        localctx = compiladoresParser.CContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_c)
        self._la = 0 # Token type
        try:
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21, 22, 23, 24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 31457280) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 155
                self.comp()
                pass
            elif token in [2, 5, 16, 17, 18, 19]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(compiladoresParser.TermContext,0)


        def e(self):
            return self.getTypedRuleContext(compiladoresParser.EContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp" ):
                listener.enterOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp" ):
                listener.exitOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp" ):
                return visitor.visitOp(self)
            else:
                return visitor.visitChildren(self)




    def op(self):

        localctx = compiladoresParser.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.term()
            self.state = 160
            self.e()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op(self):
            return self.getTypedRuleContext(compiladoresParser.OpContext,0)


        def SUMA(self):
            return self.getToken(compiladoresParser.SUMA, 0)

        def RESTA(self):
            return self.getToken(compiladoresParser.RESTA, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_e

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterE" ):
                listener.enterE(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitE" ):
                listener.exitE(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitE" ):
                return visitor.visitE(self)
            else:
                return visitor.visitChildren(self)




    def e(self):

        localctx = compiladoresParser.EContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_e)
        self._la = 0 # Token type
        try:
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                _la = self._input.LA(1)
                if not(_la==9 or _la==10):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 163
                self.op()
                pass
            elif token in [2, 5, 16, 17, 18, 19, 21, 22, 23, 24]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(compiladoresParser.FactorContext,0)


        def t(self):
            return self.getTypedRuleContext(compiladoresParser.TContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = compiladoresParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.factor()
            self.state = 168
            self.t()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(compiladoresParser.FactorContext,0)


        def MULT(self):
            return self.getToken(compiladoresParser.MULT, 0)

        def DIV(self):
            return self.getToken(compiladoresParser.DIV, 0)

        def MOD(self):
            return self.getToken(compiladoresParser.MOD, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT" ):
                listener.enterT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT" ):
                listener.exitT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT" ):
                return visitor.visitT(self)
            else:
                return visitor.visitChildren(self)




    def t(self):

        localctx = compiladoresParser.TContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_t)
        self._la = 0 # Token type
        try:
            self.state = 173
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14336) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 171
                self.factor()
                pass
            elif token in [2, 5, 9, 10, 16, 17, 18, 19, 21, 22, 23, 24]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self):
            return self.getToken(compiladoresParser.NUMERO, 0)

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def DECIMAL(self):
            return self.getToken(compiladoresParser.DECIMAL, 0)

        def CARACTER(self):
            return self.getToken(compiladoresParser.CARACTER, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def exp(self):
            return self.getTypedRuleContext(compiladoresParser.ExpContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def suf(self):
            return self.getTypedRuleContext(compiladoresParser.SufContext,0)


        def pref(self):
            return self.getTypedRuleContext(compiladoresParser.PrefContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = compiladoresParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_factor)
        try:
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.match(compiladoresParser.NUMERO)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.match(compiladoresParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 177
                self.match(compiladoresParser.DECIMAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 178
                self.match(compiladoresParser.CARACTER)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 179
                self.match(compiladoresParser.PA)
                self.state = 180
                self.exp()
                self.state = 181
                self.match(compiladoresParser.PC)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 183
                self.suf()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 184
                self.pref()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SufContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def INC(self):
            return self.getToken(compiladoresParser.INC, 0)

        def DEC(self):
            return self.getToken(compiladoresParser.DEC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_suf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuf" ):
                listener.enterSuf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuf" ):
                listener.exitSuf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuf" ):
                return visitor.visitSuf(self)
            else:
                return visitor.visitChildren(self)




    def suf(self):

        localctx = compiladoresParser.SufContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_suf)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(compiladoresParser.ID)
            self.state = 188
            _la = self._input.LA(1)
            if not(_la==14 or _la==15):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def INC(self):
            return self.getToken(compiladoresParser.INC, 0)

        def DEC(self):
            return self.getToken(compiladoresParser.DEC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_pref

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPref" ):
                listener.enterPref(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPref" ):
                listener.exitPref(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPref" ):
                return visitor.visitPref(self)
            else:
                return visitor.visitChildren(self)




    def pref(self):

        localctx = compiladoresParser.PrefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_pref)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            _la = self._input.LA(1)
            if not(_la==14 or _la==15):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 191
            self.match(compiladoresParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IwhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(compiladoresParser.WHILE, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def cond(self):
            return self.getTypedRuleContext(compiladoresParser.CondContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_iwhile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIwhile" ):
                listener.enterIwhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIwhile" ):
                listener.exitIwhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIwhile" ):
                return visitor.visitIwhile(self)
            else:
                return visitor.visitChildren(self)




    def iwhile(self):

        localctx = compiladoresParser.IwhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_iwhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(compiladoresParser.WHILE)
            self.state = 194
            self.match(compiladoresParser.PA)
            self.state = 195
            self.cond()
            self.state = 196
            self.match(compiladoresParser.PC)
            self.state = 197
            self.instruccion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def factor(self):
            return self.getTypedRuleContext(compiladoresParser.FactorContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_cond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond" ):
                listener.enterCond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond" ):
                listener.exitCond(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCond" ):
                return visitor.visitCond(self)
            else:
                return visitor.visitChildren(self)




    def cond(self):

        localctx = compiladoresParser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_cond)
        try:
            self.state = 201
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self.opal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 200
                self.factor()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLA(self):
            return self.getToken(compiladoresParser.LLA, 0)

        def instrucciones(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionesContext,0)


        def LLC(self):
            return self.getToken(compiladoresParser.LLC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = compiladoresParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_bloque)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(compiladoresParser.LLA)
            self.state = 204
            self.instrucciones()
            self.state = 205
            self.match(compiladoresParser.LLC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IforContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(compiladoresParser.FOR, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def init(self):
            return self.getTypedRuleContext(compiladoresParser.InitContext,0)


        def PYC(self, i:int=None):
            if i is None:
                return self.getTokens(compiladoresParser.PYC)
            else:
                return self.getToken(compiladoresParser.PYC, i)

        def condlist(self):
            return self.getTypedRuleContext(compiladoresParser.CondlistContext,0)


        def iter_(self):
            return self.getTypedRuleContext(compiladoresParser.IterContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_ifor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfor" ):
                listener.enterIfor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfor" ):
                listener.exitIfor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfor" ):
                return visitor.visitIfor(self)
            else:
                return visitor.visitChildren(self)




    def ifor(self):

        localctx = compiladoresParser.IforContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_ifor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(compiladoresParser.FOR)
            self.state = 208
            self.match(compiladoresParser.PA)
            self.state = 209
            self.init()
            self.state = 210
            self.match(compiladoresParser.PYC)
            self.state = 211
            self.condlist()
            self.state = 212
            self.match(compiladoresParser.PYC)
            self.state = 213
            self.iter_()
            self.state = 214
            self.match(compiladoresParser.PC)
            self.state = 215
            self.instruccion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self):
            return self.getTypedRuleContext(compiladoresParser.AsignacionContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_init

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInit" ):
                listener.enterInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInit" ):
                listener.exitInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit" ):
                return visitor.visitInit(self)
            else:
                return visitor.visitChildren(self)




    def init(self):

        localctx = compiladoresParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_init)
        try:
            self.state = 219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.asignacion()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cond(self):
            return self.getTypedRuleContext(compiladoresParser.CondContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_condlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondlist" ):
                listener.enterCondlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondlist" ):
                listener.exitCondlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondlist" ):
                return visitor.visitCondlist(self)
            else:
                return visitor.visitChildren(self)




    def condlist(self):

        localctx = compiladoresParser.CondlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_condlist)
        try:
            self.state = 223
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 14, 15, 25, 26, 27, 38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.cond()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self):
            return self.getTypedRuleContext(compiladoresParser.AsignacionContext,0)


        def suf(self):
            return self.getTypedRuleContext(compiladoresParser.SufContext,0)


        def pref(self):
            return self.getTypedRuleContext(compiladoresParser.PrefContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_iter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIter" ):
                listener.enterIter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIter" ):
                listener.exitIter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIter" ):
                return visitor.visitIter(self)
            else:
                return visitor.visitChildren(self)




    def iter_(self):

        localctx = compiladoresParser.IterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_iter)
        try:
            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.asignacion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 227
                self.suf()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 228
                self.pref()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(compiladoresParser.IF, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def cond(self):
            return self.getTypedRuleContext(compiladoresParser.CondContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


        def ielse(self):
            return self.getTypedRuleContext(compiladoresParser.IelseContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_iif

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIif" ):
                listener.enterIif(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIif" ):
                listener.exitIif(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIif" ):
                return visitor.visitIif(self)
            else:
                return visitor.visitChildren(self)




    def iif(self):

        localctx = compiladoresParser.IifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_iif)
        try:
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.match(compiladoresParser.IF)
                self.state = 232
                self.match(compiladoresParser.PA)
                self.state = 233
                self.cond()
                self.state = 234
                self.match(compiladoresParser.PC)
                self.state = 235
                self.instruccion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.match(compiladoresParser.IF)
                self.state = 238
                self.match(compiladoresParser.PA)
                self.state = 239
                self.cond()
                self.state = 240
                self.match(compiladoresParser.PC)
                self.state = 241
                self.instruccion()
                self.state = 242
                self.ielse()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IelseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(compiladoresParser.ELSE, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_ielse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIelse" ):
                listener.enterIelse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIelse" ):
                listener.exitIelse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIelse" ):
                return visitor.visitIelse(self)
            else:
                return visitor.visitChildren(self)




    def ielse(self):

        localctx = compiladoresParser.IelseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_ielse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(compiladoresParser.ELSE)
            self.state = 247
            self.instruccion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(compiladoresParser.TipoContext,0)


        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def param(self):
            return self.getTypedRuleContext(compiladoresParser.ParamContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_ifuncion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfuncion" ):
                listener.enterIfuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfuncion" ):
                listener.exitIfuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfuncion" ):
                return visitor.visitIfuncion(self)
            else:
                return visitor.visitChildren(self)




    def ifuncion(self):

        localctx = compiladoresParser.IfuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_ifuncion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.tipo()
            self.state = 250
            self.match(compiladoresParser.ID)
            self.state = 251
            self.match(compiladoresParser.PA)
            self.state = 252
            self.param()
            self.state = 253
            self.match(compiladoresParser.PC)
            self.state = 254
            self.instruccion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion(self):
            return self.getTypedRuleContext(compiladoresParser.DeclaracionContext,0)


        def C(self):
            return self.getToken(compiladoresParser.C, 0)

        def param(self):
            return self.getTypedRuleContext(compiladoresParser.ParamContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = compiladoresParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_param)
        try:
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.declaracion()
                self.state = 257
                self.match(compiladoresParser.C)
                self.state = 258
                self.param()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 260
                self.declaracion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IreturnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(compiladoresParser.RETURN, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_ireturn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIreturn" ):
                listener.enterIreturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIreturn" ):
                listener.exitIreturn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIreturn" ):
                return visitor.visitIreturn(self)
            else:
                return visitor.visitChildren(self)




    def ireturn(self):

        localctx = compiladoresParser.IreturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_ireturn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(compiladoresParser.RETURN)
            self.state = 265
            self.opal()
            self.state = 266
            self.match(compiladoresParser.PYC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IllamadaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def argumento(self):
            return self.getTypedRuleContext(compiladoresParser.ArgumentoContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_illamada

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIllamada" ):
                listener.enterIllamada(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIllamada" ):
                listener.exitIllamada(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIllamada" ):
                return visitor.visitIllamada(self)
            else:
                return visitor.visitChildren(self)




    def illamada(self):

        localctx = compiladoresParser.IllamadaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_illamada)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(compiladoresParser.ID)
            self.state = 269
            self.match(compiladoresParser.PA)
            self.state = 270
            self.argumento()
            self.state = 271
            self.match(compiladoresParser.PC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def C(self):
            return self.getToken(compiladoresParser.C, 0)

        def argumento(self):
            return self.getTypedRuleContext(compiladoresParser.ArgumentoContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_argumento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumento" ):
                listener.enterArgumento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumento" ):
                listener.exitArgumento(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumento" ):
                return visitor.visitArgumento(self)
            else:
                return visitor.visitChildren(self)




    def argumento(self):

        localctx = compiladoresParser.ArgumentoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_argumento)
        try:
            self.state = 278
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.match(compiladoresParser.ID)
                self.state = 274
                self.match(compiladoresParser.C)
                self.state = 275
                self.argumento()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.match(compiladoresParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





