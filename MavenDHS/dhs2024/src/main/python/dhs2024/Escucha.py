from antlr4 import ErrorNode, TerminalNode
from compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser
from TablaSimbolos import TablaSimbolos
from Variable import Variable
from Funcion import Funcion
from TipoDato import TipoDato

class Escucha (compiladoresListener):
    
    def __init__(self):
        self.numTokens = 0
        self.numNodos = 0
        self.tabla = TablaSimbolos()
        
        
    # Enter a parse tree produced by compiladoresParser#programa.
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("Comienza la compilacion")
        
        # Añadimos contexto global
        self.tabla.addContexto()
        
    # Exit a parse tree produced by compiladoresParser#programa.
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("Finaliza la compilacion")
        print("Se encontraron:")
        print("\tCantidad de nodos: " + str(self.numNodos))
        print("\tTokens: " + str(self.numTokens))
        
        # Borrar contexto global
        self.tabla.delContexto()
        

    
    # Enter a parse tree produced by compiladoresParser#declaracion.
    def enterDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        print(" ###Declaracion")
        
        
        
    # Exit a parse tree produced by compiladoresParser#declaracion.
    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        #me muevo y le pido el texto a la hoja
        #hijo [0 en adelante], elijo el 1
        #print("\tNombre de la variable: " + ctx.getChild(1).getText())
        
        vartype = ctx.getChild(0).getText().upper()
        name = ctx.getChild(1).getText()
        
        # Creacion de variable
        variable = Variable(name,vartype,False,False)
        if not self.tabla.buscarGlobal(variable.nombre):
            self.tabla.addIdentificador(variable)
            print(f"  variable añadida{variable}")
        else:
            print("\tERROR SEMANTICO ---> identificador repetido")
        
    # Enter a parse tree produced by compiladoresParser#asignacion.
    def enterAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        print("\tAsignacion")  

    # Exit a parse tree produced by compiladoresParser#asignacion.
    def exitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        if not self.tabla.buscarGlobal(ctx.getChild(0).getText()):
            print("\tERROR SEMANTICO ---> identificador no declarado")
    

        
 #  Enter a parse tree produced by compiladoresParser#iwhile.
    def enterIwhile(self, ctx:compiladoresParser.IwhileContext):
        print("While")
        
        # Iniciamos contexto while
        self.tabla.addContexto()

    # Exit a parse tree produced by compiladoresParser#iwhile.
    def exitIwhile(self, ctx:compiladoresParser.IwhileContext):
        print("Fin While")
        print("\tCantidad de hijos: " + str(ctx.getChildCount()))
        print("\tTokens: " +ctx.getText())
        
        # Borramos contexto while
        self.tabla.delContexto()
        
    def visitTerminal(self, node: TerminalNode):
        #print("-----> Token: " + node.getText())
        self.numTokens +=1
    
    def visitErrorNode(self, node: ErrorNode):
        print("----------> ERROR")
    
    def enterEveryRule(self, ctx):
        self.numNodos += 1