from compiladoresVisitor import compiladoresVisitor
from compiladoresParser import compiladoresParser
from IntermediateCode import IntermediateCode
from Temporales import Temporales
class Walker (compiladoresVisitor):
    
    def __init__(self):
        self.codigoIntermedio = IntermediateCode("src/main/python/dhs2024/out/cod.txt")
        self.temporales = Temporales()
        self.temporalesTerminales = list()
        self.isSimpleTerm = False
    def visitPrograma(self,ctx : compiladoresParser.ProgramaContext):
        print("Inicia generacion de codigo intermedio...")
        return super().visitPrograma(ctx)
    
    def visitInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        print(f"Instruccion: {ctx.getText()}")
        return super().visitInstruccion(ctx)
    
    def visitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        return self.visitChildren(ctx)
    
    def visitTerm(self, ctx:compiladoresParser.TermContext):
                
        if ctx.getChild(0).getChildCount() > 1:
            super().visitFactor(ctx.getChild(0))
            if ctx.getChild(1).getChildCount() > 0: # es parte de un termino complejo
                self.codigoIntermedio.addLine(f"{self.temporales.generateTemp()} = {self.temporalesTerminales[-1][-1]} {ctx.getChild(1).getChild(0).getText()} {ctx.getChild(1).getChild(1).getText()}")
                self.visitT(ctx.getChild(1).getChild(2))
                #VER SI GENERA ERROR EN 1*(1*2)*3*4
                self.temporalesTerminales[-1].append(self.temporales.getTop())
            else:
                self.isSimpleTerm = False
            return None
        
        if ctx.getChild(1).getChildCount() == 0:
            self.isSimpleTerm = True
        else:
            self.isSimpleTerm = False
        
        if self.isSimpleTerm and len(self.temporalesTerminales[-1]) == 0:
            self.codigoIntermedio.addLine(f"{self.temporales.generateTemp()} = {ctx.getText()}")
        elif not self.isSimpleTerm: #inicia  calculo de producto
            if "(" in ctx.getChild(1).getChild(1).getText():#se multiplica/divide por un producto
                self.codigoIntermedio.addLine(f"{self.temporales.generateTemp()} = {ctx.getChild(0).getText()}")
                self.temporalesTerminales[-1].append(self.temporales.getTop())
                self.visitExp(ctx.getChild(1).getChild(1).getChild(1)) # calculamos expresion dentro de parentesis
                op =f"{self.temporalesTerminales[-1][-2]} {ctx.getChild(1).getChild(0).getText()} {self.temporalesTerminales[-1][-1]}"
                #limpiamos pila
                self.temporalesTerminales[-1].pop()
                self.temporalesTerminales[-1].pop()
                #añadimos linea de codigo
                self.codigoIntermedio.addLine(f"{self.temporales.generateTemp()} = {op}")
            else:
                self.codigoIntermedio.addLine(f"{self.temporales.generateTemp()} = {ctx.getChild(0).getText()} {ctx.getChild(1).getChild(0).getText()} {ctx.getChild(1).getChild(1).getText()}")
            
            self.visitT(ctx.getChild(1).getChild(2))
        
        self.temporalesTerminales[-1].append(self.temporales.getTop())
        return None
    
    def visitExp(self, ctx:compiladoresParser.ExpContext):
        self.temporalesTerminales.append([])
        super().visitExp(ctx)
        # Respaldamos el ultimo valor y borramos la ultima pila
        print(self.temporalesTerminales)
        print(self.codigoIntermedio.showCodeStatus())
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

      