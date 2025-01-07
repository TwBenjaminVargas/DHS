from compiladoresVisitor import compiladoresVisitor
from compiladoresParser import compiladoresParser
from IntermediateCode import IntermediateCode
from Temporales import Temporales
from Etiqueta import Etiqueta
class Walker (compiladoresVisitor):
    
    def __init__(self):
        self.codigoIntermedio = IntermediateCode("src/main/python/dhs2024/out/cod.txt")
        self.temporales = Temporales()
        self.etiqueta = Etiqueta()
        self.etiquetaList = list()
        self.temporalesTerminales = list()
        self.isSimpleTerm = False
        self.isInComparacion = False
        
    def visitPrograma(self,ctx : compiladoresParser.ProgramaContext):
        print("Inicia generacion de codigo intermedio...")
        return super().visitPrograma(ctx)
    
    def visitInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        print(f"Instruccion: {ctx.getText()}")
        return super().visitInstruccion(ctx)
    
    def visitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        super().visitAsignacion(ctx)
        print(self.temporalesTerminales)
        self.codigoIntermedio.addLine(f"{ctx.getChild(0).getText()} = {self.temporalesTerminales[-1][-1]}")
        # Limpiamos la pila de temporales terminales para la siguiente operacion
        self.temporalesTerminales = []
    
    def visitTerm(self, ctx:compiladoresParser.TermContext):
                
        if ctx.getChild(0).getChildCount() > 1:
            super().visitFactor(ctx.getChild(0))
            # Si el termino en parentesis es la primera parte de un producto/division
            if ctx.getChild(1).getChildCount() > 0: 
                self.codigoIntermedio.addLine(f"{self.temporales.generateTemp()} = {self.temporalesTerminales[-1][-1]} {ctx.getChild(1).getChild(0).getText()} {ctx.getChild(1).getChild(1).getText()}")
                # Limpiamos el temporal del termino con parentesis ya que no lo queremos guardar
                self.temporalesTerminales[-1].pop()
                self.visitT(ctx.getChild(1).getChild(2))
                # Guardamos el temporal con el resultado del producto
                self.temporalesTerminales[-1].append(self.temporales.getTop())
            else:
                self.isSimpleTerm = False
            return None
        
        if ctx.getChild(1).getChildCount() == 0:
            self.isSimpleTerm = True
        else:
            self.isSimpleTerm = False
        
        if self.isSimpleTerm and (len(self.temporalesTerminales[-1]) == 0 or self.isInComparacion):
            self.codigoIntermedio.addLine(f"{self.temporales.generateTemp()} = {ctx.getText()}")
        # Inicia  calculo de producto
        elif not self.isSimpleTerm: 
            # POSIBLE MEJORA DE CONDICION
            if "(" in ctx.getChild(1).getChild(1).getText():#se multiplica/divide por un termino en parentesis
                self.codigoIntermedio.addLine(f"{self.temporales.generateTemp()} = {ctx.getChild(0).getText()}")
                self.temporalesTerminales[-1].append(self.temporales.getTop())
                self.visitExp(ctx.getChild(1).getChild(1).getChild(1)) # calculamos expresion dentro de parentesis
                op =f"{self.temporalesTerminales[-1][-2]} {ctx.getChild(1).getChild(0).getText()} {self.temporalesTerminales[-1][-1]}"
                # Limpiamos pila de valores que ya no necesitamos
                self.temporalesTerminales[-1].pop()
                self.temporalesTerminales[-1].pop()
                # Añadimos linea de codigo intermedio
                self.codigoIntermedio.addLine(f"{self.temporales.generateTemp()} = {op}")
            else:
                self.codigoIntermedio.addLine(f"{self.temporales.generateTemp()} = {ctx.getChild(0).getText()} {ctx.getChild(1).getChild(0).getText()} {ctx.getChild(1).getChild(1).getText()}")
            
            self.visitT(ctx.getChild(1).getChild(2))
        
        self.temporalesTerminales[-1].append(self.temporales.getTop())
        print(f"Añadi el {self.temporalesTerminales[-1][-1]}")
        return None
    
    def visitExp(self, ctx:compiladoresParser.ExpContext):
        self.temporalesTerminales.append([])
        super().visitExp(ctx)
        #print(self.temporalesTerminales)
        #print(self.codigoIntermedio.showCodeStatus())
        # Respaldamos el ultimo valor y borramos la ultima lista en la pila
        if len(self.temporalesTerminales) > 1:
            self.temporalesTerminales[-2].append(self.temporalesTerminales[-1].pop())
            self.temporalesTerminales.pop()
        return None
    
    def visitE(self, ctx:compiladoresParser.EContext):
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
        return None
    
    
    def visitT(self, ctx:compiladoresParser.TContext):
        if ctx.getChildCount() > 0:
                op = f"{self.temporales.getTop()} {ctx.getChild(0).getText()} {ctx.getChild(1).getText()}"
                self.codigoIntermedio.addLine(f"{self.temporales.generateTemp()} = {op}")
                self.visitT(ctx.getChild(2))
        return None
    
    def visitComp(self, ctx:compiladoresParser.CompContext):
        """
         Al visitarse una comparacion se establece una bandera isInComparacion y se calcula
         el primer termino de la misma, luego se trabaja con el nodo C
        """
        super().visitOp(ctx.getChild(0))
        if ctx.getChild(1).getChildCount() > 0:
            self.isInComparacion = True
            self.visitC(ctx.getChild(1))
        else:
            self.isInComparacion = False
        return None
    
    def visitC(self, ctx:compiladoresParser.CContext):
        """
        Se visista la comparacio de manera recursiva, con la finalidad de calcular el segundo
        termino de la misma.
        Luego se procede a aplicar la comparacion de los dos terminos, esto con la finalidad de comparar terminos complejos
        """
        self.visitComp(ctx.getChild(1))
        self.codigoIntermedio.addLine(f"{self.temporales.generateTemp()} = {self.temporalesTerminales[-1][-2]} {ctx.getChild(0).getText()} {self.temporalesTerminales[-1][-1]}")
        self.temporalesTerminales[-1].append(self.temporales.getTop())
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
        super().visitInit(ctx.getChild(2))
        self.codigoIntermedio.addLine(f"label {self.etiqueta.generateLabel()}")
        self.etiquetaList.append(self.etiqueta.getLabel())
        # lista de condicion
        super().visitCondlist(ctx.getChild(4))
        self.codigoIntermedio.addLine(f"ifnjmp {self.temporalesTerminales[-1][-1]}, {self.etiqueta.generateLabel()}")
        self.etiquetaList.append(self.etiqueta.getLabel())
        # invertimos posiciones
        self.etiquetaList[-1],self.etiquetaList[-2] = self.etiquetaList[-2], self.etiquetaList[-1]
        
        # cuerpo del for
        super().visitInstruccion(ctx.getChild(8))
        # lista de iteracion
        super().visitIter(ctx.getChild(6))
        self.codigoIntermedio.addLine(f"jmp {self.etiquetaList.pop()}")
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