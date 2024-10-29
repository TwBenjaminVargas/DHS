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
        
    def exitContext(self):
        for idstr in self.tabla.contextos[-1].tabla:
           myvar = self.tabla.contextos[-1].tabla[idstr]
           if not myvar.usado:
               print("\nAdvertencia:\n\tVariable \"{}\" no utilizada".format(myvar.nombre))
        self.tabla.delContexto()
         
    # Enter a parse tree produced by compiladoresParser#programa.
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("")
        print("*" * 40)
        print("Comienza analisis semantico:")
        # Añadimos contexto global
        self.tabla.addContexto()
        
    # Exit a parse tree produced by compiladoresParser#programa.
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("\nFinaliza analisis semantico")
        #print("Se encontraron:")
        #print("\tCantidad de nodos: " + str(self.numNodos))
        #print("\tTokens: " + str(self.numTokens))
        print("*" * 40)
        print("")
        
        self.exitContext() 

    
    # Enter a parse tree produced by compiladoresParser#declaracion.
    def enterDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        print("\n+Declaracion:")
        
        
        
    # Exit a parse tree produced by compiladoresParser#declaracion.
    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        #me muevo y le pido el texto a la hoja
        #hijo [0 en adelante], elijo el 1
        #print("\tNombre de la variable: " + ctx.getChild(1).getText())
        
        # instanciamos objeto variable
        vartype = ctx.getChild(0).getChild(0).getText().upper()
        varname = ctx.getChild(1).getText()
        
        myvar = Variable(vartype,varname)
        
        # verificar existencia en contexto
        if not self.tabla.buscarLocal(myvar.nombre):
            self.tabla.addIdentificador(myvar)
            print(myvar)
        else:
            print(f"-ERROR:\n\tIdentificado repetido {myvar.nombre}")
            

    # Enter a parse tree produced by compiladoresParser#asignacion.
    def enterAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        print("\n+Asignacion")

    # Exit a parse tree produced by compiladoresParser#asignacion.
    def exitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        
        # buscar variable y la establece inicializada
        myvar = self.tabla.buscarGlobal(ctx.getChild(0).getText())
        if myvar:
            myvar.inicializado = True
            print(myvar)
        else:    
            print("\n-ERROR:\n\tidentificador no declarado")
    

    def verificarID(self,id):
        if id: # si encuentro un nodo ID
            myvar = self.tabla.buscarGlobal(id.getText())
            if myvar:
                if myvar.inicializado:
                    myvar.usado = True
                    print(f"Uso:\n{myvar}")
                else:
                    print("\nError:\n\tVariable \"{}\" no inicializada".format(id.getText()))
            else:
                print("\nError:\n\tVariable \"{}\" no definida".format(id.getText()))
    
    # Exit a parse tree produced by compiladoresParser#factor.
    def exitFactor(self, ctx:compiladoresParser.FactorContext):
        id = ctx.getToken(compiladoresParser.ID, 0)
        self.verificarID(id)
        
    # Exit a parse tree produced by compiladoresParser#suf.
    def exitSuf(self, ctx:compiladoresParser.SufContext):
        id = ctx.getToken(compiladoresParser.ID, 0)
        self.verificarID(id)
    
    # Exit a parse tree produced by compiladoresParser#pref.
    def exitPref(self, ctx:compiladoresParser.PrefContext):
        id = ctx.getToken(compiladoresParser.ID, 0)
        self.verificarID(id)
        
     
        
            
                
        

        
 #  Enter a parse tree produced by compiladoresParser#iwhile.
    def enterIwhile(self, ctx:compiladoresParser.IwhileContext):
        print("\n" + "="*20 + " While " + "="*20)
        
        # Iniciamos contexto while
        self.tabla.addContexto()

    # Exit a parse tree produced by compiladoresParser#iwhile.
    def exitIwhile(self, ctx:compiladoresParser.IwhileContext):
        print("\n"+ "="*20 + " Fin While "+ "="*20)
        #print("\tCantidad de hijos: " + str(ctx.getChildCount()))
        #print("\tTokens: " +ctx.getText())
        
        self.exitContext()
    
    
    def visitTerminal(self, node: TerminalNode):
        #print("-----> Token: " + node.getText())
        self.numTokens +=1
    
    def visitErrorNode(self, node: ErrorNode):
        print("\nNODE ERROR")
    
    def enterEveryRule(self, ctx):
        self.numNodos += 1