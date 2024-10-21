# Generated from /home/ben/Documentos/DHS/MavenDHS/dhs2024/src/main/python/dhs2024/compiladores.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete listener for a parse tree produced by compiladoresParser.
class compiladoresListener(ParseTreeListener):

    # Enter a parse tree produced by compiladoresParser#programa.
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        pass

    # Exit a parse tree produced by compiladoresParser#programa.
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        pass


    # Enter a parse tree produced by compiladoresParser#instrucciones.
    def enterInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        pass

    # Exit a parse tree produced by compiladoresParser#instrucciones.
    def exitInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        pass


    # Enter a parse tree produced by compiladoresParser#instruccion.
    def enterInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#instruccion.
    def exitInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#declaracion.
    def enterDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#declaracion.
    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#asignacion.
    def enterAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#asignacion.
    def exitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#opal.
    def enterOpal(self, ctx:compiladoresParser.OpalContext):
        pass

    # Exit a parse tree produced by compiladoresParser#opal.
    def exitOpal(self, ctx:compiladoresParser.OpalContext):
        pass


    # Enter a parse tree produced by compiladoresParser#expr.
    def enterExpr(self, ctx:compiladoresParser.ExprContext):
        pass

    # Exit a parse tree produced by compiladoresParser#expr.
    def exitExpr(self, ctx:compiladoresParser.ExprContext):
        pass


    # Enter a parse tree produced by compiladoresParser#logic.
    def enterLogic(self, ctx:compiladoresParser.LogicContext):
        pass

    # Exit a parse tree produced by compiladoresParser#logic.
    def exitLogic(self, ctx:compiladoresParser.LogicContext):
        pass


    # Enter a parse tree produced by compiladoresParser#l.
    def enterL(self, ctx:compiladoresParser.LContext):
        pass

    # Exit a parse tree produced by compiladoresParser#l.
    def exitL(self, ctx:compiladoresParser.LContext):
        pass


    # Enter a parse tree produced by compiladoresParser#relation.
    def enterRelation(self, ctx:compiladoresParser.RelationContext):
        pass

    # Exit a parse tree produced by compiladoresParser#relation.
    def exitRelation(self, ctx:compiladoresParser.RelationContext):
        pass


    # Enter a parse tree produced by compiladoresParser#r.
    def enterR(self, ctx:compiladoresParser.RContext):
        pass

    # Exit a parse tree produced by compiladoresParser#r.
    def exitR(self, ctx:compiladoresParser.RContext):
        pass


    # Enter a parse tree produced by compiladoresParser#log.
    def enterLog(self, ctx:compiladoresParser.LogContext):
        pass

    # Exit a parse tree produced by compiladoresParser#log.
    def exitLog(self, ctx:compiladoresParser.LogContext):
        pass


    # Enter a parse tree produced by compiladoresParser#lo.
    def enterLo(self, ctx:compiladoresParser.LoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#lo.
    def exitLo(self, ctx:compiladoresParser.LoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#exp.
    def enterExp(self, ctx:compiladoresParser.ExpContext):
        pass

    # Exit a parse tree produced by compiladoresParser#exp.
    def exitExp(self, ctx:compiladoresParser.ExpContext):
        pass


    # Enter a parse tree produced by compiladoresParser#e.
    def enterE(self, ctx:compiladoresParser.EContext):
        pass

    # Exit a parse tree produced by compiladoresParser#e.
    def exitE(self, ctx:compiladoresParser.EContext):
        pass


    # Enter a parse tree produced by compiladoresParser#term.
    def enterTerm(self, ctx:compiladoresParser.TermContext):
        pass

    # Exit a parse tree produced by compiladoresParser#term.
    def exitTerm(self, ctx:compiladoresParser.TermContext):
        pass


    # Enter a parse tree produced by compiladoresParser#t.
    def enterT(self, ctx:compiladoresParser.TContext):
        pass

    # Exit a parse tree produced by compiladoresParser#t.
    def exitT(self, ctx:compiladoresParser.TContext):
        pass


    # Enter a parse tree produced by compiladoresParser#factor.
    def enterFactor(self, ctx:compiladoresParser.FactorContext):
        pass

    # Exit a parse tree produced by compiladoresParser#factor.
    def exitFactor(self, ctx:compiladoresParser.FactorContext):
        pass


    # Enter a parse tree produced by compiladoresParser#iwhile.
    def enterIwhile(self, ctx:compiladoresParser.IwhileContext):
        pass

    # Exit a parse tree produced by compiladoresParser#iwhile.
    def exitIwhile(self, ctx:compiladoresParser.IwhileContext):
        pass


    # Enter a parse tree produced by compiladoresParser#bloque.
    def enterBloque(self, ctx:compiladoresParser.BloqueContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloque.
    def exitBloque(self, ctx:compiladoresParser.BloqueContext):
        pass


    # Enter a parse tree produced by compiladoresParser#ifor.
    def enterIfor(self, ctx:compiladoresParser.IforContext):
        pass

    # Exit a parse tree produced by compiladoresParser#ifor.
    def exitIfor(self, ctx:compiladoresParser.IforContext):
        pass


    # Enter a parse tree produced by compiladoresParser#init.
    def enterInit(self, ctx:compiladoresParser.InitContext):
        pass

    # Exit a parse tree produced by compiladoresParser#init.
    def exitInit(self, ctx:compiladoresParser.InitContext):
        pass


    # Enter a parse tree produced by compiladoresParser#cond.
    def enterCond(self, ctx:compiladoresParser.CondContext):
        pass

    # Exit a parse tree produced by compiladoresParser#cond.
    def exitCond(self, ctx:compiladoresParser.CondContext):
        pass


    # Enter a parse tree produced by compiladoresParser#iter.
    def enterIter(self, ctx:compiladoresParser.IterContext):
        pass

    # Exit a parse tree produced by compiladoresParser#iter.
    def exitIter(self, ctx:compiladoresParser.IterContext):
        pass


    # Enter a parse tree produced by compiladoresParser#iif.
    def enterIif(self, ctx:compiladoresParser.IifContext):
        pass

    # Exit a parse tree produced by compiladoresParser#iif.
    def exitIif(self, ctx:compiladoresParser.IifContext):
        pass


    # Enter a parse tree produced by compiladoresParser#ielse.
    def enterIelse(self, ctx:compiladoresParser.IelseContext):
        pass

    # Exit a parse tree produced by compiladoresParser#ielse.
    def exitIelse(self, ctx:compiladoresParser.IelseContext):
        pass



del compiladoresParser