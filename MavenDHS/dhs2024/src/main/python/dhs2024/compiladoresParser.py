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
        4,1,23,178,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,52,8,1,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,64,8,2,1,3,1,3,1,3,1,4,1,4,1,4,
        1,4,1,5,1,5,3,5,75,8,5,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,3,7,85,8,
        7,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,3,9,95,8,9,1,10,1,10,1,10,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,109,8,11,1,12,1,12,
        1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,3,13,127,8,13,1,14,1,14,1,14,1,14,1,14,1,14,3,14,135,8,14,1,
        15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,
        17,1,17,1,17,1,17,1,17,1,17,1,17,1,18,1,18,3,18,159,8,18,1,19,1,
        19,3,19,163,8,19,1,20,1,20,1,20,1,20,1,20,1,20,3,20,171,8,20,1,21,
        1,21,1,21,1,21,1,21,1,21,0,0,22,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,34,36,38,40,42,0,0,176,0,44,1,0,0,0,2,51,1,0,0,0,4,63,
        1,0,0,0,6,65,1,0,0,0,8,68,1,0,0,0,10,74,1,0,0,0,12,76,1,0,0,0,14,
        84,1,0,0,0,16,86,1,0,0,0,18,94,1,0,0,0,20,96,1,0,0,0,22,108,1,0,
        0,0,24,110,1,0,0,0,26,126,1,0,0,0,28,134,1,0,0,0,30,136,1,0,0,0,
        32,142,1,0,0,0,34,146,1,0,0,0,36,158,1,0,0,0,38,162,1,0,0,0,40,170,
        1,0,0,0,42,172,1,0,0,0,44,45,3,2,1,0,45,46,5,0,0,1,46,1,1,0,0,0,
        47,48,3,4,2,0,48,49,3,2,1,0,49,52,1,0,0,0,50,52,1,0,0,0,51,47,1,
        0,0,0,51,50,1,0,0,0,52,3,1,0,0,0,53,54,3,6,3,0,54,55,5,5,0,0,55,
        64,1,0,0,0,56,64,3,30,15,0,57,64,3,32,16,0,58,64,3,34,17,0,59,64,
        3,42,21,0,60,61,3,8,4,0,61,62,5,5,0,0,62,64,1,0,0,0,63,53,1,0,0,
        0,63,56,1,0,0,0,63,57,1,0,0,0,63,58,1,0,0,0,63,59,1,0,0,0,63,60,
        1,0,0,0,64,5,1,0,0,0,65,66,5,19,0,0,66,67,5,23,0,0,67,7,1,0,0,0,
        68,69,5,23,0,0,69,70,5,16,0,0,70,71,3,10,5,0,71,9,1,0,0,0,72,75,
        3,20,10,0,73,75,3,12,6,0,74,72,1,0,0,0,74,73,1,0,0,0,75,11,1,0,0,
        0,76,77,3,16,8,0,77,78,3,14,7,0,78,13,1,0,0,0,79,80,5,14,0,0,80,
        81,3,16,8,0,81,82,3,14,7,0,82,85,1,0,0,0,83,85,1,0,0,0,84,79,1,0,
        0,0,84,83,1,0,0,0,85,15,1,0,0,0,86,87,3,20,10,0,87,88,3,18,9,0,88,
        17,1,0,0,0,89,90,5,13,0,0,90,91,3,20,10,0,91,92,3,18,9,0,92,95,1,
        0,0,0,93,95,1,0,0,0,94,89,1,0,0,0,94,93,1,0,0,0,95,19,1,0,0,0,96,
        97,3,24,12,0,97,98,3,22,11,0,98,21,1,0,0,0,99,100,5,6,0,0,100,101,
        3,24,12,0,101,102,3,22,11,0,102,109,1,0,0,0,103,104,5,7,0,0,104,
        105,3,24,12,0,105,106,3,22,11,0,106,109,1,0,0,0,107,109,1,0,0,0,
        108,99,1,0,0,0,108,103,1,0,0,0,108,107,1,0,0,0,109,23,1,0,0,0,110,
        111,3,28,14,0,111,112,3,26,13,0,112,25,1,0,0,0,113,114,5,8,0,0,114,
        115,3,28,14,0,115,116,3,26,13,0,116,127,1,0,0,0,117,118,5,9,0,0,
        118,119,3,28,14,0,119,120,3,26,13,0,120,127,1,0,0,0,121,122,5,10,
        0,0,122,123,3,28,14,0,123,124,3,26,13,0,124,127,1,0,0,0,125,127,
        1,0,0,0,126,113,1,0,0,0,126,117,1,0,0,0,126,121,1,0,0,0,126,125,
        1,0,0,0,127,27,1,0,0,0,128,135,5,18,0,0,129,135,5,23,0,0,130,131,
        5,1,0,0,131,132,3,20,10,0,132,133,5,2,0,0,133,135,1,0,0,0,134,128,
        1,0,0,0,134,129,1,0,0,0,134,130,1,0,0,0,135,29,1,0,0,0,136,137,5,
        17,0,0,137,138,5,1,0,0,138,139,5,23,0,0,139,140,5,2,0,0,140,141,
        3,4,2,0,141,31,1,0,0,0,142,143,5,3,0,0,143,144,3,2,1,0,144,145,5,
        4,0,0,145,33,1,0,0,0,146,147,5,20,0,0,147,148,5,1,0,0,148,149,3,
        36,18,0,149,150,5,5,0,0,150,151,3,38,19,0,151,152,5,5,0,0,152,153,
        3,40,20,0,153,154,5,2,0,0,154,155,3,4,2,0,155,35,1,0,0,0,156,159,
        3,8,4,0,157,159,1,0,0,0,158,156,1,0,0,0,158,157,1,0,0,0,159,37,1,
        0,0,0,160,163,3,12,6,0,161,163,1,0,0,0,162,160,1,0,0,0,162,161,1,
        0,0,0,163,39,1,0,0,0,164,165,5,23,0,0,165,171,5,11,0,0,166,167,5,
        23,0,0,167,171,5,12,0,0,168,171,3,8,4,0,169,171,1,0,0,0,170,164,
        1,0,0,0,170,166,1,0,0,0,170,168,1,0,0,0,170,169,1,0,0,0,171,41,1,
        0,0,0,172,173,5,1,0,0,173,174,3,38,19,0,174,175,5,2,0,0,175,176,
        3,4,2,0,176,43,1,0,0,0,11,51,63,74,84,94,108,126,134,158,162,170
    ]

class compiladoresParser ( Parser ):

    grammarFileName = "compiladores.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "';'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'++'", "'--'", "'&&'", 
                     "'||'", "'=='", "'='", "'while'", "<INVALID>", "'int'", 
                     "'for'", "'if'" ]

    symbolicNames = [ "<INVALID>", "PA", "PC", "LLA", "LLC", "PYC", "SUMA", 
                      "RESTA", "MUL", "DIV", "MOD", "INC", "DEC", "AND", 
                      "OR", "IGUAL", "ASIG", "WHILE", "NUMERO", "INT", "FOR", 
                      "IF", "WS", "ID" ]

    RULE_programa = 0
    RULE_instrucciones = 1
    RULE_instruccion = 2
    RULE_declaracion = 3
    RULE_asignacion = 4
    RULE_opal = 5
    RULE_logic = 6
    RULE_l = 7
    RULE_log = 8
    RULE_lo = 9
    RULE_exp = 10
    RULE_e = 11
    RULE_term = 12
    RULE_t = 13
    RULE_factor = 14
    RULE_iwhile = 15
    RULE_bloque = 16
    RULE_ifor = 17
    RULE_init = 18
    RULE_cond = 19
    RULE_iter = 20
    RULE_iif = 21

    ruleNames =  [ "programa", "instrucciones", "instruccion", "declaracion", 
                   "asignacion", "opal", "logic", "l", "log", "lo", "exp", 
                   "e", "term", "t", "factor", "iwhile", "bloque", "ifor", 
                   "init", "cond", "iter", "iif" ]

    EOF = Token.EOF
    PA=1
    PC=2
    LLA=3
    LLC=4
    PYC=5
    SUMA=6
    RESTA=7
    MUL=8
    DIV=9
    MOD=10
    INC=11
    DEC=12
    AND=13
    OR=14
    IGUAL=15
    ASIG=16
    WHILE=17
    NUMERO=18
    INT=19
    FOR=20
    IF=21
    WS=22
    ID=23

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
            self.state = 44
            self.instrucciones()
            self.state = 45
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
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 17, 19, 20, 23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.instruccion()
                self.state = 48
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
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.declaracion()
                self.state = 54
                self.match(compiladoresParser.PYC)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.iwhile()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 57
                self.bloque()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 4)
                self.state = 58
                self.ifor()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 5)
                self.state = 59
                self.iif()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 6)
                self.state = 60
                self.asignacion()
                self.state = 61
                self.match(compiladoresParser.PYC)
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


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(compiladoresParser.INT, 0)

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
            self.state = 65
            self.match(compiladoresParser.INT)
            self.state = 66
            self.match(compiladoresParser.ID)
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
        self.enterRule(localctx, 8, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(compiladoresParser.ID)
            self.state = 69
            self.match(compiladoresParser.ASIG)
            self.state = 70
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


        def logic(self):
            return self.getTypedRuleContext(compiladoresParser.LogicContext,0)


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
        self.enterRule(localctx, 10, self.RULE_opal)
        try:
            self.state = 74
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.logic()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def log(self):
            return self.getTypedRuleContext(compiladoresParser.LogContext,0)


        def l(self):
            return self.getTypedRuleContext(compiladoresParser.LContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_logic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogic" ):
                listener.enterLogic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogic" ):
                listener.exitLogic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogic" ):
                return visitor.visitLogic(self)
            else:
                return visitor.visitChildren(self)




    def logic(self):

        localctx = compiladoresParser.LogicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_logic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.log()
            self.state = 77
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

        def OR(self):
            return self.getToken(compiladoresParser.OR, 0)

        def log(self):
            return self.getTypedRuleContext(compiladoresParser.LogContext,0)


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
        self.enterRule(localctx, 14, self.RULE_l)
        try:
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.match(compiladoresParser.OR)
                self.state = 80
                self.log()
                self.state = 81
                self.l()
                pass
            elif token in [2, 5]:
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


    class LogContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(compiladoresParser.ExpContext,0)


        def lo(self):
            return self.getTypedRuleContext(compiladoresParser.LoContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_log

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLog" ):
                listener.enterLog(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLog" ):
                listener.exitLog(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLog" ):
                return visitor.visitLog(self)
            else:
                return visitor.visitChildren(self)




    def log(self):

        localctx = compiladoresParser.LogContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_log)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.exp()
            self.state = 87
            self.lo()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(compiladoresParser.AND, 0)

        def exp(self):
            return self.getTypedRuleContext(compiladoresParser.ExpContext,0)


        def lo(self):
            return self.getTypedRuleContext(compiladoresParser.LoContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_lo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLo" ):
                listener.enterLo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLo" ):
                listener.exitLo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLo" ):
                return visitor.visitLo(self)
            else:
                return visitor.visitChildren(self)




    def lo(self):

        localctx = compiladoresParser.LoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_lo)
        try:
            self.state = 94
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.match(compiladoresParser.AND)
                self.state = 90
                self.exp()
                self.state = 91
                self.lo()
                pass
            elif token in [2, 5, 14]:
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


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(compiladoresParser.TermContext,0)


        def e(self):
            return self.getTypedRuleContext(compiladoresParser.EContext,0)


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
        self.enterRule(localctx, 20, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.term()
            self.state = 97
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

        def SUMA(self):
            return self.getToken(compiladoresParser.SUMA, 0)

        def term(self):
            return self.getTypedRuleContext(compiladoresParser.TermContext,0)


        def e(self):
            return self.getTypedRuleContext(compiladoresParser.EContext,0)


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
        self.enterRule(localctx, 22, self.RULE_e)
        try:
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.match(compiladoresParser.SUMA)
                self.state = 100
                self.term()
                self.state = 101
                self.e()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.match(compiladoresParser.RESTA)
                self.state = 104
                self.term()
                self.state = 105
                self.e()
                pass
            elif token in [2, 5, 13, 14]:
                self.enterOuterAlt(localctx, 3)

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
        self.enterRule(localctx, 24, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.factor()
            self.state = 111
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

        def MUL(self):
            return self.getToken(compiladoresParser.MUL, 0)

        def factor(self):
            return self.getTypedRuleContext(compiladoresParser.FactorContext,0)


        def t(self):
            return self.getTypedRuleContext(compiladoresParser.TContext,0)


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
        self.enterRule(localctx, 26, self.RULE_t)
        try:
            self.state = 126
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.match(compiladoresParser.MUL)
                self.state = 114
                self.factor()
                self.state = 115
                self.t()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.match(compiladoresParser.DIV)
                self.state = 118
                self.factor()
                self.state = 119
                self.t()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 121
                self.match(compiladoresParser.MOD)
                self.state = 122
                self.factor()
                self.state = 123
                self.t()
                pass
            elif token in [2, 5, 6, 7, 13, 14]:
                self.enterOuterAlt(localctx, 4)

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
        self.enterRule(localctx, 28, self.RULE_factor)
        try:
            self.state = 134
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.match(compiladoresParser.NUMERO)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.match(compiladoresParser.ID)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 130
                self.match(compiladoresParser.PA)
                self.state = 131
                self.exp()
                self.state = 132
                self.match(compiladoresParser.PC)
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


    class IwhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(compiladoresParser.WHILE, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

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
        self.enterRule(localctx, 30, self.RULE_iwhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(compiladoresParser.WHILE)
            self.state = 137
            self.match(compiladoresParser.PA)
            self.state = 138
            self.match(compiladoresParser.ID)
            self.state = 139
            self.match(compiladoresParser.PC)
            self.state = 140
            self.instruccion()
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
        self.enterRule(localctx, 32, self.RULE_bloque)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(compiladoresParser.LLA)
            self.state = 143
            self.instrucciones()
            self.state = 144
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

        def cond(self):
            return self.getTypedRuleContext(compiladoresParser.CondContext,0)


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
        self.enterRule(localctx, 34, self.RULE_ifor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(compiladoresParser.FOR)
            self.state = 147
            self.match(compiladoresParser.PA)
            self.state = 148
            self.init()
            self.state = 149
            self.match(compiladoresParser.PYC)
            self.state = 150
            self.cond()
            self.state = 151
            self.match(compiladoresParser.PYC)
            self.state = 152
            self.iter_()
            self.state = 153
            self.match(compiladoresParser.PC)
            self.state = 154
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
        self.enterRule(localctx, 36, self.RULE_init)
        try:
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
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


    class CondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logic(self):
            return self.getTypedRuleContext(compiladoresParser.LogicContext,0)


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
        self.enterRule(localctx, 38, self.RULE_cond)
        try:
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 18, 23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.logic()
                pass
            elif token in [2, 5]:
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

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def INC(self):
            return self.getToken(compiladoresParser.INC, 0)

        def DEC(self):
            return self.getToken(compiladoresParser.DEC, 0)

        def asignacion(self):
            return self.getTypedRuleContext(compiladoresParser.AsignacionContext,0)


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
        self.enterRule(localctx, 40, self.RULE_iter)
        try:
            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.match(compiladoresParser.ID)
                self.state = 165
                self.match(compiladoresParser.INC)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.match(compiladoresParser.ID)
                self.state = 167
                self.match(compiladoresParser.DEC)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 168
                self.asignacion()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)

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

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def cond(self):
            return self.getTypedRuleContext(compiladoresParser.CondContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


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
        self.enterRule(localctx, 42, self.RULE_iif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(compiladoresParser.PA)
            self.state = 173
            self.cond()
            self.state = 174
            self.match(compiladoresParser.PC)
            self.state = 175
            self.instruccion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





