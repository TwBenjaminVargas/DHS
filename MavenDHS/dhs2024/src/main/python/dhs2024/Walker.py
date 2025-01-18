from compiladoresVisitor import compiladoresVisitor
from compiladoresParser import compiladoresParser
from IntermediateCode import IntermediateCode
from Temporales import Temporales
from Etiqueta import Etiqueta
from antlr4 import *
class Walker (compiladoresVisitor):
    
    def __init__(self):
        self.codigoIntermedio = IntermediateCode("src/main/python/dhs2024/out/cod.txt")
        self.temporales = Temporales()
        self.etiqueta = Etiqueta()
        self.etiquetaList = list()
        self.etiquetaFuncion = dict()
        self.temporalesTerminales = list()
        self.isSimpleTerm = False
        
    def visitPrograma(self,ctx : compiladoresParser.ProgramaContext):
        print("Inicia generacion de codigo intermedio...")
        return super().visitPrograma(ctx)
    
    def visitInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        #print(f"Instruccion: {ctx.getText()}")
        return super().visitInstruccion(ctx)
    
    def visitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        super().visitAsignacion(ctx)
        #print(self.temporalesTerminales)
        self.codigoIntermedio.addLine(f"{ctx.getChild(0).getText()} = {self.temporalesTerminales[-1][-1]}")
        # Limpiamos la pila de temporales terminales para la siguiente operacion
        self.temporalesTerminales = []
    
    """def visitTerm(self, ctx:compiladoresParser.TermContext):
        
        # primer termino llamada a funcion
        if ctx.getChild(0).getChild(0).getChildCount() == 4:
            self.visitIllamada(ctx.getChild(0).getChild(0))
            if ctx.getChild(1).getChildCount() > 0:
                self.visitT(ctx.getChild(1))
                self.temporalesTerminales[-1].append(self.temporales.getTop())
            self.isSimpleTerm = False
            return None
            
        # primer termino contiene parentesis           
        if ctx.getChild(0).getChildCount() > 1:
            super().visitFactor(ctx.getChild(0))
            self.isSimpleTerm = False
            # Si el termino en parentesis es la primera parte de un producto/division
            if ctx.getChild(1).getChildCount() > 0:
                # Limpiamos el temporal del termino con parentesis ya que no lo queremos guardar
                self.temporalesTerminales[-1].pop()
                self.visitT(ctx.getChild(1))
                self.temporalesTerminales[-1].append(self.temporales.getTop())
            return None
        
        # tratamiento de segundo termino
        if ctx.getChild(1).getChildCount() == 0:
            self.isSimpleTerm = True
        else:
            self.isSimpleTerm = False
        
        if self.isSimpleTerm and len(self.temporalesTerminales[-1]) == 0:
            self.codigoIntermedio.addLine(f"{self.temporales.generateTemp()} = {ctx.getText()}")
        # Inicia  calculo de producto
        elif not self.isSimpleTerm:
            if ctx.getChild(1).getChild(1).getChildCount() == 3:# segundo termino del producto/division es un parentesis
                self.codigoIntermedio.addLine(f"{self.temporales.generateTemp()} = {ctx.getChild(0).getText()}")
                self.visitT(ctx.getChild(1))
            elif isinstance(ctx.getChild(1).getChild(1).getChild(0),compiladoresParser.IllamadaContext): # segundo es una llamada
                self.codigoIntermedio.addLine(f"{self.temporales.generateTemp()} = {ctx.getChild(0).getText()}")
                self.visitT(ctx.getChild(1))
            else: #segundo termino es simple
                self.codigoIntermedio.addLine(f"{self.temporales.generateTemp()} = {ctx.getChild(0).getText()} {ctx.getChild(1).getChild(0).getText()} {ctx.getChild(1).getChild(1).getText()}")
                self.visitT(ctx.getChild(1).getChild(2))
        self.temporalesTerminales[-1].append(self.temporales.getTop())
        #print(f"Añadi el {self.temporalesTerminales[-1][-1]}")
        return None"""
    
    def visitExp(self, ctx:compiladoresParser.ExpContext):
        self.temporalesTerminales.append([])
        super().visitExp(ctx)
        # Respaldamos el ultimo valor y borramos la ultima lista en la pila
        if len(self.temporalesTerminales) > 1:
            self.temporalesTerminales[-2].append(self.temporalesTerminales[-1].pop())
            self.temporalesTerminales.pop()
        return None
    
    """def visitE(self, ctx:compiladoresParser.EContext):
        if ctx.getChildCount() > 0:
            self.visitTerm(ctx.getChild(1).getChild(0))
            op = ""
            if self.isSimpleTerm:
                op =f"{self.temporalesTerminales[-1][-1]} {ctx.getChild(0).getText()} {ctx.getChild(1).getChild(0).getText()}"
            else:
                op =f"{self.temporalesTerminales[-1][-2]} {ctx.getChild(0).getText()} {self.temporalesTerminales[-1][-1]}"
            
            self.codigoIntermedio.addLine(f"{self.temporales.generateTemp()} = {op}")
            self.temporalesTerminales[-1].append(self.temporales.getTop())
            self.visitE(ctx.getChild(1).getChild(1))
        return None"""
    
    
    """def visitT(self, ctx:compiladoresParser.TContext):
        if ctx.getChildCount() > 0:
            if ctx.getChild(1).getChildCount() > 1: # encontramos termino con parentesis en el camino
                # metemos el temporal anterior dentro de los terminales
                self.temporalesTerminales[-1].append(self.temporales.getTop())
                self.visitExp(ctx.getChild(1).getChild(1))
                self.codigoIntermedio.addLine(f"{self.temporales.generateTemp()} = {self.temporalesTerminales[-1].pop(-2)} {ctx.getChild(0).getText()} {self.temporalesTerminales[-1].pop()}")
                self.visitT(ctx.getChild(2))
            elif isinstance(ctx.getChild(1).getChild(0), compiladoresParser.IllamadaContext): #hay una llamada
                self.temporalesTerminales[-1].append(self.temporales.getTop())
                self.visitIllamada(ctx.getChild(1).getChild(0))
                self.codigoIntermedio.addLine(f"{self.temporales.generateTemp()} = {self.temporalesTerminales[-1].pop(-2)} {ctx.getChild(0).getText()} {self.temporalesTerminales[-1].pop()}")
                self.visitT(ctx.getChild(2))
            else:
                op = f"{self.temporales.getTop()} {ctx.getChild(0).getText()} {ctx.getChild(1).getText()}"
                self.codigoIntermedio.addLine(f"{self.temporales.generateTemp()} = {op}")
                self.visitT(ctx.getChild(2))
        return None"""
        
    def visitFactor(self, ctx:compiladoresParser.FactorContext):
        if ctx.getChildCount() > 1: #Parentesis
            self.visitExp(ctx.getChild(1))
                
        elif isinstance(ctx.getChild(0),TerminalNode):
            #if ctx.getChild(0).getSymbol().type == compiladoresParser.ID:
                #self.temporalesTerminales[-1].append(ctx.getChild(0).getText())
            self.temporalesTerminales[-1].append(ctx.getChild(0).getText())
        else:
            if isinstance(ctx.getChild(0),compiladoresParser.IllamadaContext): # llamada a funcion
                self.visitIllamada(ctx.getChild(0))
        return None
    
    def visitTerm(self, ctx:compiladoresParser.TermContext):
        if ctx.getChild(1).getChildCount() == 0 and isinstance(ctx.parentCtx,compiladoresParser.OpContext):
            self.visitFactor(ctx.getChild(0))
            return None
        else: # esta en una multiplicacion
            self.temporalesTerminales.append([])
            self.visitFactor(ctx.getChild(0))
            
            if isinstance(ctx.parentCtx, compiladoresParser.TContext): # si esta en el segundo termino de una suma
                return None
            self.visitT(ctx.getChild(1))
            # Respaldamos el ultimo valor y borramos la ultima lista en la pila
            self.temporalesTerminales[-2].append(self.temporalesTerminales[-1].pop())
            self.temporalesTerminales.pop()
        return None


    def visitT(self, ctx:compiladoresParser.TContext):
        if ctx.getChildCount() > 0:
            self.visitFactor(ctx.getChild(1))
            self.codigoIntermedio.addLine(f"{self.temporales.generateTemp()} = {self.temporalesTerminales[-1][-2]} {ctx.getChild(0).getText()} {self.temporalesTerminales[-1][-1]}")
            self.temporalesTerminales[-1].append(self.temporales.getTop())
            self.visitT(ctx.getChild(2))
        return None
    
    def visitOp(self, ctx:compiladoresParser.OpContext):
        # no esta en una Suma
        if ctx.getChild(1).getChildCount() == 0 and isinstance(ctx.parentCtx,compiladoresParser.CompContext):
            self.visitTerm(ctx.getChild(0))
            return None
        else: # esta en una suma
            self.temporalesTerminales.append([])
            self.visitTerm(ctx.getChild(0))
            
            if isinstance(ctx.parentCtx, compiladoresParser.EContext): # si esta en el segundo termino de una suma
                return None
            self.visitE(ctx.getChild(1))
            # Respaldamos el ultimo valor y borramos la ultima lista en la pila
            self.temporalesTerminales[-2].append(self.temporalesTerminales[-1].pop())
            self.temporalesTerminales.pop()
        return None


    def visitE(self, ctx:compiladoresParser.EContext):
        if ctx.getChildCount() > 0:
            self.visitTerm(ctx.getChild(1))
            self.codigoIntermedio.addLine(f"{self.temporales.generateTemp()} = {self.temporalesTerminales[-1][-2]} {ctx.getChild(0).getText()} {self.temporalesTerminales[-1][-1]}")
            self.temporalesTerminales[-1].append(self.temporales.getTop())
            self.visitE(ctx.getChild(2))
        return None
    
    def visitComp(self, ctx:compiladoresParser.CompContext):
        # no esta en una comparacion
        if ctx.getChild(1).getChildCount() == 0 and isinstance(ctx.parentCtx,compiladoresParser.InotContext):
            self.visitOp(ctx.getChild(0))
            return None
        else: # esta en una comparacion
            self.temporalesTerminales.append([])
            self.visitOp(ctx.getChild(0))
            
            if isinstance(ctx.parentCtx, compiladoresParser.CContext): # si esta en el segundo termino de una comparacion
                return None
            self.visitC(ctx.getChild(1))
            # Respaldamos el ultimo valor y borramos la ultima lista en la pila
            self.temporalesTerminales[-2].append(self.temporalesTerminales[-1].pop())
            self.temporalesTerminales.pop()
        return None
    
    def visitC(self, ctx:compiladoresParser.CContext):
        if ctx.getChildCount() > 0:
            self.visitOp(ctx.getChild(1))
            self.codigoIntermedio.addLine(f"{self.temporales.generateTemp()} = {self.temporalesTerminales[-1][-2]} {ctx.getChild(0).getText()} {self.temporalesTerminales[-1][-1]}")
            self.temporalesTerminales[-1].append(self.temporales.getTop())
            self.visitC(ctx.getChild(2))
        return None
    
    
    def visitInot(self, ctx:compiladoresParser.InotContext):
        # no esta en una comparacion
        if ctx.getChild(1).getChildCount() == 0 and isinstance(ctx.parentCtx,compiladoresParser.LandContext):
            self.visitComp(ctx.getChild(0))
            return None
        else: # esta en una comparacion
            self.temporalesTerminales.append([])
            self.visitComp(ctx.getChild(0))
            
            if isinstance(ctx.parentCtx, compiladoresParser.NContext): # si esta en el segundo termino de una comparacion
                return None
            self.visitN(ctx.getChild(1))
            # Respaldamos el ultimo valor y borramos la ultima lista en la pila
            self.temporalesTerminales[-2].append(self.temporalesTerminales[-1].pop())
            self.temporalesTerminales.pop()
        return None


    def visitN(self, ctx:compiladoresParser.NContext):
        if ctx.getChildCount() > 0:
            self.visitComp(ctx.getChild(1))
            self.codigoIntermedio.addLine(f"{self.temporales.generateTemp()} = {self.temporalesTerminales[-1][-2]} {ctx.getChild(0).getText()} {self.temporalesTerminales[-1][-1]}")
            self.temporalesTerminales[-1].append(self.temporales.getTop())
            self.visitN(ctx.getChild(2))
        return None
    
    def visitLand(self, ctx:compiladoresParser.LandContext):
        # no esta en una comparacion
        if ctx.getChild(1).getChildCount() == 0 and isinstance(ctx.parentCtx,compiladoresParser.LorContext):
            self.visitInot(ctx.getChild(0))
            return None
        else: # esta en una comparacion
            self.temporalesTerminales.append([])
            self.visitInot(ctx.getChild(0))
            
            if isinstance(ctx.parentCtx, compiladoresParser.LContext): # si esta en el segundo termino de una comparacion
                return None
            self.visitL(ctx.getChild(1))
            # Respaldamos el ultimo valor y borramos la ultima lista en la pila
            self.temporalesTerminales[-2].append(self.temporalesTerminales[-1].pop())
            self.temporalesTerminales.pop()
        return None
    
    def visitL(self, ctx:compiladoresParser.LContext):
        if ctx.getChildCount() > 0:
            self.visitInot(ctx.getChild(1))
            self.codigoIntermedio.addLine(f"{self.temporales.generateTemp()} = {self.temporalesTerminales[-1][-2]} {ctx.getChild(0).getText()} {self.temporalesTerminales[-1][-1]}")
            self.temporalesTerminales[-1].append(self.temporales.getTop())
            self.visitL(ctx.getChild(2))
        return None
    
    def visitLor(self, ctx:compiladoresParser.LorContext):
        # no esta en una comparacion
        if ctx.getChild(1).getChildCount() == 0 and isinstance(ctx.parentCtx,compiladoresParser.ExpContext):
            self.visitLand(ctx.getChild(0))
            return None
        else: # esta en una comparacion
            self.temporalesTerminales.append([])
            self.visitLand(ctx.getChild(0))
            
            if isinstance(ctx.parentCtx, compiladoresParser.AContext): # si esta en el segundo termino de una comparacion
                return None
            self.visitA(ctx.getChild(1))
            # Respaldamos el ultimo valor y borramos la ultima lista en la pila
            self.temporalesTerminales[-2].append(self.temporalesTerminales[-1].pop())
            self.temporalesTerminales.pop()
        return None


    # Visit a parse tree produced by compiladoresParser#a.
    def visitA(self, ctx:compiladoresParser.AContext):
        if ctx.getChildCount() > 0:
            self.visitLand(ctx.getChild(1))
            self.codigoIntermedio.addLine(f"{self.temporales.generateTemp()} = {self.temporalesTerminales[-1][-2]} {ctx.getChild(0).getText()} {self.temporalesTerminales[-1][-1]}")
            self.temporalesTerminales[-1].append(self.temporales.getTop())
            self.visitA(ctx.getChild(2))
        return None

    def visitIif(self, ctx:compiladoresParser.IifContext):
        ielse = False
        if ctx.getChildCount() == 6:
            ielse = True
        super().visitCond(ctx.getChild(2))
        self.codigoIntermedio.addLine(f"ifnjmp {self.temporalesTerminales[-1][-1]}, {self.etiqueta.generateLabel()}")
        self.etiquetaList.append(self.etiqueta.getLabel())
        super().visitInstruccion(ctx.getChild(4))
        # verificamos que tenga else
        if ielse:
            self.codigoIntermedio.addLine(f"jmp {self.etiqueta.generateLabel()}")
            self.etiquetaList.append(self.etiqueta.getLabel())
            # intercambiamos posiciones en la lista para cuando sean llamadas
            self.etiquetaList[-1],self.etiquetaList[-2] = self.etiquetaList[-2], self.etiquetaList[-1]
        self.codigoIntermedio.addLine(f"label {self.etiquetaList.pop()}")
        if ielse:
            self.visitIelse(ctx.getChild(5)) 
        return None
    
    def visitIelse(self, ctx:compiladoresParser.IelseContext):
        super().visitInstruccion(ctx.getChild(1))
        self.codigoIntermedio.addLine(f"label {self.etiquetaList.pop()}")
        return None
    
    def visitIfor(self, ctx:compiladoresParser.IforContext):
        # lista de iniciacion
        if ctx.getChild(2).getChildCount() > 0:
            super().visitInit(ctx.getChild(2))
        self.codigoIntermedio.addLine(f"label {self.etiqueta.generateLabel()}")
        self.etiquetaList.append(self.etiqueta.getLabel())
        # lista de condicion
        if ctx.getChild(4).getChildCount() > 0:
            super().visitCondlist(ctx.getChild(4))
            self.codigoIntermedio.addLine(f"ifnjmp {self.temporalesTerminales[-1][-1]}, {self.etiqueta.generateLabel()}")
            self.etiquetaList.append(self.etiqueta.getLabel())
            # invertimos posiciones
            self.etiquetaList[-1],self.etiquetaList[-2] = self.etiquetaList[-2], self.etiquetaList[-1]
        
        # cuerpo del for
        super().visitInstruccion(ctx.getChild(8))
        # lista de iteracion
        if ctx.getChild(6).getChildCount() > 0:
            super().visitIter(ctx.getChild(6))
        self.codigoIntermedio.addLine(f"jmp {self.etiquetaList.pop()}")
        if ctx.getChild(4).getChildCount() > 0:
            self.codigoIntermedio.addLine(f"label {self.etiquetaList.pop()}")
        return None
    
    def visitIwhile(self, ctx:compiladoresParser.IwhileContext):
        self.codigoIntermedio.addLine(f"label {self.etiqueta.generateLabel()}")
        self.etiquetaList.append(self.etiqueta.getLabel())
        super().visitCond(ctx.getChild(2))
        self.codigoIntermedio.addLine(f"ifnjmp {self.temporalesTerminales[-1][-1]}, {self.etiqueta.generateLabel()}")
        self.etiquetaList.append(self.etiqueta.getLabel())
        # invertimos posiciones
        self.etiquetaList[-1],self.etiquetaList[-2] = self.etiquetaList[-2], self.etiquetaList[-1]
        # cuerpo del while
        super().visitInstruccion(ctx.getChild(4))
        self.codigoIntermedio.addLine(f"jmp {self.etiquetaList.pop()}")
        self.codigoIntermedio.addLine(f"label {self.etiquetaList.pop()}")
        return None
    
    def visitIprototipo(self, ctx:compiladoresParser.IprototipoContext):
        self.etiquetaFuncion[ctx.getChild(1).getText()] = self.etiqueta.generateLabel() 
        return None
    
    def visitIfuncion(self, ctx:compiladoresParser.IfuncionContext):
        if ctx.getChild(1).getText() in self.etiquetaFuncion: #habia prototipo
            self.codigoIntermedio.addLine(f"label {self.etiquetaFuncion[ctx.getChild(1).getText()]}")
        else:
            self.codigoIntermedio.addLine(f"label {self.etiqueta.generateLabel()}")
            self.etiquetaFuncion[ctx.getChild(1).getText()] = self.etiqueta.getLabel()
        self.codigoIntermedio.addLine(f"pop {self.temporales.generateTemp()}")
        jmppos = self.temporales.getTop()
        self.visitParam(ctx.getChild(3))
        super().visitInstruccion(ctx.getChild(5))
        self.codigoIntermedio.addLine(f"jmp {jmppos}")
        return None
    
    def visitParam(self, ctx:compiladoresParser.ParamContext):
        if ctx.getChildCount() == 3:
            self.visitParam(ctx.getChild(2))
        if ctx.getChildCount() > 0:   
            self.visitP(ctx.getChild(0))       
        return None
    
    def visitP(self, ctx:compiladoresParser.PContext):
        self.codigoIntermedio.addLine(f"pop {ctx.getChild(1).getText()}")
        return None
    
    def visitIreturn(self, ctx:compiladoresParser.IreturnContext):
        super().visitOpal(ctx.getChild(1))
        self.codigoIntermedio.addLine(f"push {self.temporalesTerminales[-1][-1]}")
        return None
    
    def visitIllamada(self, ctx:compiladoresParser.IllamadaContext):
        #argumentos
        self.visitArgumento(ctx.getChild(2))
        self.codigoIntermedio.addLine(f"push {self.etiqueta.generateLabel()}")
        lblrtn = self.etiqueta.getLabel()
        self.codigoIntermedio.addLine(f"jmp {self.etiquetaFuncion[ctx.getChild(0).getText()]}")
        self.codigoIntermedio.addLine(f"label {lblrtn}")
        if isinstance (ctx.parentCtx,compiladoresParser.FactorContext):
            self.codigoIntermedio.addLine(f"pop {self.temporales.generateTemp()}")
            self.temporalesTerminales[-1].append(self.temporales.getTop())
        return None
    
    def visitArgumento(self, ctx:compiladoresParser.ArgumentoContext):
        # va a haber problemas cuando quieras mandar una valriable sola
        if ctx.getChildCount() > 0:
            self.temporalesTerminales.append([])
            super().visitOpal(ctx.getChild(0))
            self.codigoIntermedio.addLine(f"push {self.temporalesTerminales[-1][-1]}")
            self.temporalesTerminales.pop()
            # hay mas argumentos
            if ctx.getChildCount() > 1:
                self.visitArgumento(ctx.getChild(2))
        return None
    
    def finish(self):
        self.codigoIntermedio.closeCode()