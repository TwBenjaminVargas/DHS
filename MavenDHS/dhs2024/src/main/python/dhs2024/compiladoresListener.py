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


    # Enter a parse tree produced by compiladoresParser#tipo.
    def enterTipo(self, ctx:compiladoresParser.TipoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#tipo.
    def exitTipo(self, ctx:compiladoresParser.TipoContext):
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


    # Enter a parse tree produced by compiladoresParser#exp.
    def enterExp(self, ctx:compiladoresParser.ExpContext):
        pass

    # Exit a parse tree produced by compiladoresParser#exp.
    def exitExp(self, ctx:compiladoresParser.ExpContext):
        pass


    # Enter a parse tree produced by compiladoresParser#lor.
    def enterLor(self, ctx:compiladoresParser.LorContext):
        pass

    # Exit a parse tree produced by compiladoresParser#lor.
    def exitLor(self, ctx:compiladoresParser.LorContext):
        pass


    # Enter a parse tree produced by compiladoresParser#a.
    def enterA(self, ctx:compiladoresParser.AContext):
        pass

    # Exit a parse tree produced by compiladoresParser#a.
    def exitA(self, ctx:compiladoresParser.AContext):
        pass


    # Enter a parse tree produced by compiladoresParser#land.
    def enterLand(self, ctx:compiladoresParser.LandContext):
        pass

    # Exit a parse tree produced by compiladoresParser#land.
    def exitLand(self, ctx:compiladoresParser.LandContext):
        pass


    # Enter a parse tree produced by compiladoresParser#l.
    def enterL(self, ctx:compiladoresParser.LContext):
        pass

    # Exit a parse tree produced by compiladoresParser#l.
    def exitL(self, ctx:compiladoresParser.LContext):
        pass


    # Enter a parse tree produced by compiladoresParser#inot.
    def enterInot(self, ctx:compiladoresParser.InotContext):
        pass

    # Exit a parse tree produced by compiladoresParser#inot.
    def exitInot(self, ctx:compiladoresParser.InotContext):
        pass


    # Enter a parse tree produced by compiladoresParser#n.
    def enterN(self, ctx:compiladoresParser.NContext):
        pass

    # Exit a parse tree produced by compiladoresParser#n.
    def exitN(self, ctx:compiladoresParser.NContext):
        pass


    # Enter a parse tree produced by compiladoresParser#comp.
    def enterComp(self, ctx:compiladoresParser.CompContext):
        pass

    # Exit a parse tree produced by compiladoresParser#comp.
    def exitComp(self, ctx:compiladoresParser.CompContext):
        pass


    # Enter a parse tree produced by compiladoresParser#c.
    def enterC(self, ctx:compiladoresParser.CContext):
        pass

    # Exit a parse tree produced by compiladoresParser#c.
    def exitC(self, ctx:compiladoresParser.CContext):
        pass


    # Enter a parse tree produced by compiladoresParser#op.
    def enterOp(self, ctx:compiladoresParser.OpContext):
        pass

    # Exit a parse tree produced by compiladoresParser#op.
    def exitOp(self, ctx:compiladoresParser.OpContext):
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


    # Enter a parse tree produced by compiladoresParser#suf.
    def enterSuf(self, ctx:compiladoresParser.SufContext):
        pass

    # Exit a parse tree produced by compiladoresParser#suf.
    def exitSuf(self, ctx:compiladoresParser.SufContext):
        pass


    # Enter a parse tree produced by compiladoresParser#pref.
    def enterPref(self, ctx:compiladoresParser.PrefContext):
        pass

    # Exit a parse tree produced by compiladoresParser#pref.
    def exitPref(self, ctx:compiladoresParser.PrefContext):
        pass


    # Enter a parse tree produced by compiladoresParser#iwhile.
    def enterIwhile(self, ctx:compiladoresParser.IwhileContext):
        pass

    # Exit a parse tree produced by compiladoresParser#iwhile.
    def exitIwhile(self, ctx:compiladoresParser.IwhileContext):
        pass


    # Enter a parse tree produced by compiladoresParser#cond.
    def enterCond(self, ctx:compiladoresParser.CondContext):
        pass

    # Exit a parse tree produced by compiladoresParser#cond.
    def exitCond(self, ctx:compiladoresParser.CondContext):
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


    # Enter a parse tree produced by compiladoresParser#condlist.
    def enterCondlist(self, ctx:compiladoresParser.CondlistContext):
        pass

    # Exit a parse tree produced by compiladoresParser#condlist.
    def exitCondlist(self, ctx:compiladoresParser.CondlistContext):
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


    # Enter a parse tree produced by compiladoresParser#ifuncion.
    def enterIfuncion(self, ctx:compiladoresParser.IfuncionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#ifuncion.
    def exitIfuncion(self, ctx:compiladoresParser.IfuncionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#param.
    def enterParam(self, ctx:compiladoresParser.ParamContext):
        pass

    # Exit a parse tree produced by compiladoresParser#param.
    def exitParam(self, ctx:compiladoresParser.ParamContext):
        pass


    # Enter a parse tree produced by compiladoresParser#ireturn.
    def enterIreturn(self, ctx:compiladoresParser.IreturnContext):
        pass

    # Exit a parse tree produced by compiladoresParser#ireturn.
    def exitIreturn(self, ctx:compiladoresParser.IreturnContext):
        pass


    # Enter a parse tree produced by compiladoresParser#illamada.
    def enterIllamada(self, ctx:compiladoresParser.IllamadaContext):
        pass

    # Exit a parse tree produced by compiladoresParser#illamada.
    def exitIllamada(self, ctx:compiladoresParser.IllamadaContext):
        pass


    # Enter a parse tree produced by compiladoresParser#argumento.
    def enterArgumento(self, ctx:compiladoresParser.ArgumentoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#argumento.
    def exitArgumento(self, ctx:compiladoresParser.ArgumentoContext):
        pass



del compiladoresParser