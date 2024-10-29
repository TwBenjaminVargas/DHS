# Generated from /home/antobadami/Documentos/proyectodhs/DHS/MavenDHS/dhs2024/src/main/python/dhs2024/compiladores.g4 by ANTLR 4.13.1
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
        4,1,33,249,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,76,8,1,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,3,2,89,8,2,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,
        5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,3,9,112,8,
        9,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,3,11,122,8,11,1,12,1,12,
        1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,136,8,13,
        1,14,1,14,1,14,1,15,1,15,1,15,3,15,144,8,15,1,16,1,16,1,16,1,17,
        1,17,1,17,3,17,152,8,17,1,18,1,18,1,18,1,19,1,19,1,19,3,19,160,8,
        19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,170,8,20,1,21,1,
        21,1,21,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,3,
        24,186,8,24,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,
        26,1,26,1,26,1,26,1,27,1,27,3,27,204,8,27,1,28,1,28,3,28,208,8,28,
        1,29,1,29,1,29,1,29,3,29,214,8,29,1,30,1,30,1,30,1,30,1,30,1,30,
        1,30,1,30,1,30,1,30,1,30,1,30,1,30,3,30,229,8,30,1,31,1,31,1,31,
        1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,33,1,33,1,33,
        3,33,247,8,33,1,33,0,0,34,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,0,5,1,0,
        28,31,1,0,19,22,1,0,7,8,1,0,9,11,1,0,12,13,241,0,68,1,0,0,0,2,75,
        1,0,0,0,4,88,1,0,0,0,6,90,1,0,0,0,8,93,1,0,0,0,10,95,1,0,0,0,12,
        99,1,0,0,0,14,101,1,0,0,0,16,103,1,0,0,0,18,111,1,0,0,0,20,113,1,
        0,0,0,22,121,1,0,0,0,24,123,1,0,0,0,26,135,1,0,0,0,28,137,1,0,0,
        0,30,143,1,0,0,0,32,145,1,0,0,0,34,151,1,0,0,0,36,153,1,0,0,0,38,
        159,1,0,0,0,40,169,1,0,0,0,42,171,1,0,0,0,44,174,1,0,0,0,46,177,
        1,0,0,0,48,185,1,0,0,0,50,187,1,0,0,0,52,191,1,0,0,0,54,203,1,0,
        0,0,56,207,1,0,0,0,58,213,1,0,0,0,60,228,1,0,0,0,62,230,1,0,0,0,
        64,233,1,0,0,0,66,246,1,0,0,0,68,69,3,2,1,0,69,70,5,0,0,1,70,1,1,
        0,0,0,71,72,3,4,2,0,72,73,3,2,1,0,73,76,1,0,0,0,74,76,1,0,0,0,75,
        71,1,0,0,0,75,74,1,0,0,0,76,3,1,0,0,0,77,78,3,6,3,0,78,79,5,5,0,
        0,79,89,1,0,0,0,80,89,3,46,23,0,81,89,3,50,25,0,82,89,3,52,26,0,
        83,89,3,60,30,0,84,85,3,10,5,0,85,86,5,5,0,0,86,89,1,0,0,0,87,89,
        3,64,32,0,88,77,1,0,0,0,88,80,1,0,0,0,88,81,1,0,0,0,88,82,1,0,0,
        0,88,83,1,0,0,0,88,84,1,0,0,0,88,87,1,0,0,0,89,5,1,0,0,0,90,91,3,
        8,4,0,91,92,5,33,0,0,92,7,1,0,0,0,93,94,7,0,0,0,94,9,1,0,0,0,95,
        96,5,33,0,0,96,97,5,18,0,0,97,98,3,12,6,0,98,11,1,0,0,0,99,100,3,
        14,7,0,100,13,1,0,0,0,101,102,3,16,8,0,102,15,1,0,0,0,103,104,3,
        20,10,0,104,105,3,18,9,0,105,17,1,0,0,0,106,107,5,15,0,0,107,108,
        3,16,8,0,108,109,3,18,9,0,109,112,1,0,0,0,110,112,1,0,0,0,111,106,
        1,0,0,0,111,110,1,0,0,0,112,19,1,0,0,0,113,114,3,24,12,0,114,115,
        3,22,11,0,115,21,1,0,0,0,116,117,5,14,0,0,117,118,3,20,10,0,118,
        119,3,22,11,0,119,122,1,0,0,0,120,122,1,0,0,0,121,116,1,0,0,0,121,
        120,1,0,0,0,122,23,1,0,0,0,123,124,3,28,14,0,124,125,3,26,13,0,125,
        25,1,0,0,0,126,127,5,17,0,0,127,128,3,24,12,0,128,129,3,26,13,0,
        129,136,1,0,0,0,130,131,5,16,0,0,131,132,3,24,12,0,132,133,3,26,
        13,0,133,136,1,0,0,0,134,136,1,0,0,0,135,126,1,0,0,0,135,130,1,0,
        0,0,135,134,1,0,0,0,136,27,1,0,0,0,137,138,3,32,16,0,138,139,3,30,
        15,0,139,29,1,0,0,0,140,141,7,1,0,0,141,144,3,28,14,0,142,144,1,
        0,0,0,143,140,1,0,0,0,143,142,1,0,0,0,144,31,1,0,0,0,145,146,3,36,
        18,0,146,147,3,34,17,0,147,33,1,0,0,0,148,149,7,2,0,0,149,152,3,
        32,16,0,150,152,1,0,0,0,151,148,1,0,0,0,151,150,1,0,0,0,152,35,1,
        0,0,0,153,154,3,40,20,0,154,155,3,38,19,0,155,37,1,0,0,0,156,157,
        7,3,0,0,157,160,3,40,20,0,158,160,1,0,0,0,159,156,1,0,0,0,159,158,
        1,0,0,0,160,39,1,0,0,0,161,170,5,24,0,0,162,170,5,33,0,0,163,164,
        5,1,0,0,164,165,3,14,7,0,165,166,5,2,0,0,166,170,1,0,0,0,167,170,
        3,42,21,0,168,170,3,44,22,0,169,161,1,0,0,0,169,162,1,0,0,0,169,
        163,1,0,0,0,169,167,1,0,0,0,169,168,1,0,0,0,170,41,1,0,0,0,171,172,
        5,33,0,0,172,173,7,4,0,0,173,43,1,0,0,0,174,175,7,4,0,0,175,176,
        5,33,0,0,176,45,1,0,0,0,177,178,5,23,0,0,178,179,5,1,0,0,179,180,
        3,48,24,0,180,181,5,2,0,0,181,182,3,4,2,0,182,47,1,0,0,0,183,186,
        3,12,6,0,184,186,3,40,20,0,185,183,1,0,0,0,185,184,1,0,0,0,186,49,
        1,0,0,0,187,188,5,3,0,0,188,189,3,2,1,0,189,190,5,4,0,0,190,51,1,
        0,0,0,191,192,5,25,0,0,192,193,5,1,0,0,193,194,3,54,27,0,194,195,
        5,5,0,0,195,196,3,56,28,0,196,197,5,5,0,0,197,198,3,58,29,0,198,
        199,5,2,0,0,199,200,3,4,2,0,200,53,1,0,0,0,201,204,3,10,5,0,202,
        204,1,0,0,0,203,201,1,0,0,0,203,202,1,0,0,0,204,55,1,0,0,0,205,208,
        3,48,24,0,206,208,1,0,0,0,207,205,1,0,0,0,207,206,1,0,0,0,208,57,
        1,0,0,0,209,214,1,0,0,0,210,214,3,10,5,0,211,214,3,42,21,0,212,214,
        3,44,22,0,213,209,1,0,0,0,213,210,1,0,0,0,213,211,1,0,0,0,213,212,
        1,0,0,0,214,59,1,0,0,0,215,216,5,26,0,0,216,217,5,1,0,0,217,218,
        3,48,24,0,218,219,5,2,0,0,219,220,3,4,2,0,220,229,1,0,0,0,221,222,
        5,26,0,0,222,223,5,1,0,0,223,224,3,48,24,0,224,225,5,2,0,0,225,226,
        3,4,2,0,226,227,3,62,31,0,227,229,1,0,0,0,228,215,1,0,0,0,228,221,
        1,0,0,0,229,61,1,0,0,0,230,231,5,27,0,0,231,232,3,4,2,0,232,63,1,
        0,0,0,233,234,3,8,4,0,234,235,5,33,0,0,235,236,5,1,0,0,236,237,3,
        66,33,0,237,238,5,2,0,0,238,239,3,4,2,0,239,65,1,0,0,0,240,241,3,
        6,3,0,241,242,5,6,0,0,242,243,3,66,33,0,243,247,1,0,0,0,244,247,
        3,6,3,0,245,247,1,0,0,0,246,240,1,0,0,0,246,244,1,0,0,0,246,245,
        1,0,0,0,247,67,1,0,0,0,15,75,88,111,121,135,143,151,159,169,185,
        203,207,213,228,246
    ]

class compiladoresParser ( Parser ):

    grammarFileName = "compiladores.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "';'", "','", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'++'", "'--'", 
                     "'&&'", "'||'", "'=='", "'!='", "'='", "'<'", "'>'", 
                     "'<='", "'>='", "'while'", "<INVALID>", "'for'", "'if'", 
                     "'else'", "'int'", "'float'", "'char'", "'void'" ]

    symbolicNames = [ "<INVALID>", "PA", "PC", "LLA", "LLC", "PYC", "C", 
                      "SUMA", "RESTA", "MULT", "DIV", "MOD", "INC", "DEC", 
                      "AND", "OR", "IGUAL", "NOT", "ASIG", "MENOR", "MAYOR", 
                      "MEI", "MAI", "WHILE", "NUMERO", "FOR", "IF", "ELSE", 
                      "INT", "FLOAT", "CHAR", "VOID", "WS", "ID" ]

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

    ruleNames =  [ "programa", "instrucciones", "instruccion", "declaracion", 
                   "tipo", "asignacion", "opal", "exp", "lor", "a", "land", 
                   "l", "inot", "n", "comp", "c", "op", "e", "term", "t", 
                   "factor", "suf", "pref", "iwhile", "cond", "bloque", 
                   "ifor", "init", "condlist", "iter", "iif", "ielse", "ifuncion", 
                   "param" ]

    EOF = Token.EOF
    PA=1
    PC=2
    LLA=3
    LLC=4
    PYC=5
    C=6
    SUMA=7
    RESTA=8
    MULT=9
    DIV=10
    MOD=11
    INC=12
    DEC=13
    AND=14
    OR=15
    IGUAL=16
    NOT=17
    ASIG=18
    MENOR=19
    MAYOR=20
    MEI=21
    MAI=22
    WHILE=23
    NUMERO=24
    FOR=25
    IF=26
    ELSE=27
    INT=28
    FLOAT=29
    CHAR=30
    VOID=31
    WS=32
    ID=33

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
            self.state = 68
            self.instrucciones()
            self.state = 69
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
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 23, 25, 26, 28, 29, 30, 31, 33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.instruccion()
                self.state = 72
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
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.declaracion()
                self.state = 78
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.iwhile()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 81
                self.bloque()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 82
                self.ifor()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 83
                self.iif()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 84
                self.asignacion()
                self.state = 85
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 87
                self.ifuncion()
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
            self.state = 90
            self.tipo()
            self.state = 91
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
            self.state = 93
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4026531840) != 0)):
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
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(compiladoresParser.ID)
            self.state = 96
            self.match(compiladoresParser.ASIG)
            self.state = 97
            self.opal()
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
            self.state = 99
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
            self.state = 101
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
            self.state = 103
            self.land()
            self.state = 104
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
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                self.match(compiladoresParser.OR)
                self.state = 107
                self.lor()
                self.state = 108
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
            self.state = 113
            self.inot()
            self.state = 114
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
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.match(compiladoresParser.AND)
                self.state = 117
                self.land()
                self.state = 118
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
            self.state = 123
            self.comp()
            self.state = 124
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
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.match(compiladoresParser.NOT)
                self.state = 127
                self.inot()
                self.state = 128
                self.n()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.match(compiladoresParser.IGUAL)
                self.state = 131
                self.inot()
                self.state = 132
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
            self.state = 137
            self.op()
            self.state = 138
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
            self.state = 143
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 20, 21, 22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7864320) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 141
                self.comp()
                pass
            elif token in [2, 5, 14, 15, 16, 17]:
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
            self.state = 145
            self.term()
            self.state = 146
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
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                _la = self._input.LA(1)
                if not(_la==7 or _la==8):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 149
                self.op()
                pass
            elif token in [2, 5, 14, 15, 16, 17, 19, 20, 21, 22]:
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
            self.state = 153
            self.factor()
            self.state = 154
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
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10, 11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3584) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 157
                self.factor()
                pass
            elif token in [2, 5, 7, 8, 14, 15, 16, 17, 19, 20, 21, 22]:
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
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.match(compiladoresParser.NUMERO)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.match(compiladoresParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 163
                self.match(compiladoresParser.PA)
                self.state = 164
                self.exp()
                self.state = 165
                self.match(compiladoresParser.PC)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 167
                self.suf()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 168
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
            self.state = 171
            self.match(compiladoresParser.ID)
            self.state = 172
            _la = self._input.LA(1)
            if not(_la==12 or _la==13):
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
            self.state = 174
            _la = self._input.LA(1)
            if not(_la==12 or _la==13):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 175
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
            self.state = 177
            self.match(compiladoresParser.WHILE)
            self.state = 178
            self.match(compiladoresParser.PA)
            self.state = 179
            self.cond()
            self.state = 180
            self.match(compiladoresParser.PC)
            self.state = 181
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
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.opal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
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
            self.state = 187
            self.match(compiladoresParser.LLA)
            self.state = 188
            self.instrucciones()
            self.state = 189
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
            self.state = 191
            self.match(compiladoresParser.FOR)
            self.state = 192
            self.match(compiladoresParser.PA)
            self.state = 193
            self.init()
            self.state = 194
            self.match(compiladoresParser.PYC)
            self.state = 195
            self.condlist()
            self.state = 196
            self.match(compiladoresParser.PYC)
            self.state = 197
            self.iter_()
            self.state = 198
            self.match(compiladoresParser.PC)
            self.state = 199
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
            self.state = 203
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
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
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 12, 13, 24, 33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
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
            self.state = 213
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                self.asignacion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 211
                self.suf()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 212
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
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.match(compiladoresParser.IF)
                self.state = 216
                self.match(compiladoresParser.PA)
                self.state = 217
                self.cond()
                self.state = 218
                self.match(compiladoresParser.PC)
                self.state = 219
                self.instruccion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.match(compiladoresParser.IF)
                self.state = 222
                self.match(compiladoresParser.PA)
                self.state = 223
                self.cond()
                self.state = 224
                self.match(compiladoresParser.PC)
                self.state = 225
                self.instruccion()
                self.state = 226
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
            self.state = 230
            self.match(compiladoresParser.ELSE)
            self.state = 231
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
            self.state = 233
            self.tipo()
            self.state = 234
            self.match(compiladoresParser.ID)
            self.state = 235
            self.match(compiladoresParser.PA)
            self.state = 236
            self.param()
            self.state = 237
            self.match(compiladoresParser.PC)
            self.state = 238
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
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.declaracion()
                self.state = 241
                self.match(compiladoresParser.C)
                self.state = 242
                self.param()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
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





