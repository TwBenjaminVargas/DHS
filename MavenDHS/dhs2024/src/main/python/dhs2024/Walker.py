from compiladoresVisitor import compiladoresVisitor
from compiladoresParser import compiladoresParser
from IntermediateCode import IntermediateCode
from Temporales import Temporales
class Walker (compiladoresVisitor):
    
    def __init__(self):
        self.codigoIntermedio = IntermediateCode("src/main/python/dhs2024/out/cod.txt")
        self.temporales = Temporales()
        
    def visitPrograma(self,ctx : compiladoresParser.ProgramaContext):
        print("Inicia generacion de codigo intermedio...")
        return super().visitPrograma(ctx)
    
    def visitInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        print(f"Instruccion: {ctx.getText()}")
        return super().visitInstruccion(ctx)
    
    def visitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        return self.visitChildren(ctx)
    
    def visitTerm(self, ctx:compiladoresParser.TermContext):
        self.codigoIntermedio.addLine(f"{self.temporales.generateTemp()} = {ctx.getText()}")
        print(f"Me visito soy {ctx.getText()}")
        return None
    
    
    
    def visitE(self, ctx:compiladoresParser.EContext):
        if ctx.getChildCount() > 0:
            self.visitTerm(ctx.getChild(1))
            op =f"{self.temporales.getTop()} {ctx.getChild(0).getText()} {self.temporales.getPrevTop()}"
            self.codigoIntermedio.addLine(f"{self.temporales.generateTemp()} = {op}")
        return None
      