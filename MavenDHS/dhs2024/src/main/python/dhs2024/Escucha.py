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
        #pila de control de tipos
        self.controlTypeLists = list()
        self.currentParamLists = list()
        self.inFuncion = False
        
    def exitContext(self):
        for idstr in self.tabla.contextos[-1].tabla:
            myvar = self.tabla.contextos[-1].tabla[idstr]
            if not myvar.usado:
                print("\nAdvertencia:\n\n\tVariable \"{}\" no utilizada".format(myvar.nombre))
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
        self.exitContext() 
        print("\nFinaliza analisis semantico")
        #print("Se encontraron:")
        #print("\tCantidad de nodos: " + str(self.numNodos))
        #print("\tTokens: " + str(self.numTokens))
        print("*" * 40)
        print("")
        

    
    # Enter a parse tree produced by compiladoresParser#declaracion.
    def enterDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        print("\n+Declaracion:\n")
        
        
        
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
        
        if self.inFuncion :
            self.currentParamLists.append(myvar)
        
                
    
    # Enter a parse tree produced by compiladoresParser#asignacion.
    def enterAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        print("\n+Asignacion")
        self.controlTypeLists.append(list()) #agregamos una lista de control 
    
    # Aqui se incluiran algunas reglas para validar una asignacion segun el tipo
    def validarAsignacion(self,tipodato):
        if tipodato == 'INT':
            if 'FLOAT' in self.controlTypeLists[-1]:
                print("\nError:\n\tIntento de asignacion de FLOAT a INT")
        if tipodato == 'CHAR':
            if 'FLOAT' in self.controlTypeLists[-1]:
                print("\nError:\n\tIntento de asignacion de FLOAT a CHAR")
      
    # Exit a parse tree produced by compiladoresParser#asignacion.
    def exitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        # buscar variable
        myvar = self.tabla.buscarGlobal(ctx.getChild(0).getText())
        # valida asignacion y establece inicializada
        if myvar:
            self.validarAsignacion(myvar.tipoDato)
            myvar.inicializado = True
            print("\n\tEstado Variable:\n")
            print(myvar)
        else:    
            print("\n-ERROR:\n\tidentificador no declarado")
            
            
        #eliminamos ultimo elemnto de pila de control
        print(f"\nTipos usados en esta asignacion: {self.controlTypeLists.pop()}")
        self.isInAsignacion = False
    
    #Verifica si un ID existe o esta inicializado y lo añade a la controlList
    def verificarID(self,id):
        myvar = self.tabla.buscarGlobal(id.getText())
        if myvar:
            if not myvar.inicializado:
                print("\nError:\n\tVariable \"{}\" no inicializada".format(id.getText()))
            myvar.usado = True
            self.controlTypeLists[-1].append(myvar.tipoDato)
        else:
            print("\nError:\n\tVariable \"{}\" no definida".format(id.getText()))
            
    # Añade un tipo de dato a la lista de control
    def addControlTypeListElement(self,ctx:compiladoresParser.FactorContext):
        if ctx.getToken(compiladoresParser.NUMERO, 0):
            self.controlTypeLists[-1].append("INT")
        if ctx.getToken(compiladoresParser.DECIMAL, 0):
            self.controlTypeLists[-1].append("FLOAT")
        if ctx.getToken(compiladoresParser.CARACTER, 0):
            self.controlTypeLists[-1].append("CHAR")
            
                   
    # Exit a parse tree produced by compiladoresParser#factor.
    def exitFactor(self, ctx:compiladoresParser.FactorContext):
        self.addControlTypeListElement(ctx)
        id = ctx.getToken(compiladoresParser.ID, 0)
        if id: # si encuentro un nodo ID
            self.verificarID(id)
        
    # Exit a parse tree produced by compiladoresParser#suf.
    def exitSuf(self, ctx:compiladoresParser.SufContext):
        id = ctx.getToken(compiladoresParser.ID, 0)
        if id: # si encuentro un nodo ID
            self.verificarID(id)
    
    # Exit a parse tree produced by compiladoresParser#pref.
    def exitPref(self, ctx:compiladoresParser.PrefContext):
        id = ctx.getToken(compiladoresParser.ID, 0)
        if id: # si encuentro un nodo ID
            self.verificarID(id)
        

        
 #  Enter a parse tree produced by compiladoresParser#iwhile.
    def enterIwhile(self, ctx:compiladoresParser.IwhileContext):
        # Iniciamos contexto while
        self.tabla.addContexto()
        print("\n" + "="*20 + " While " + "="*20)

    # Exit a parse tree produced by compiladoresParser#iwhile.
    def exitIwhile(self, ctx:compiladoresParser.IwhileContext):
        #print("\tCantidad de hijos: " + str(ctx.getChildCount()))
        #print("\tTokens: " +ctx.getText())
        self.exitContext()
        print("\n"+ "="*20 + " Fin While "+ "="*20)
    

    # Enter a parse tree produced by compiladoresParser#ifor.
    def enterIfor(self, ctx:compiladoresParser.IforContext):
        # Iniciamos contexto for
        self.tabla.addContexto()
        print("\n" + "="*20 + " For " + "="*20)
        

    # Exit a parse tree produced by compiladoresParser#ifor.
    def exitIfor(self, ctx:compiladoresParser.IforContext):
        #print("\tCantidad de hijos: " + str(ctx.getChildCount()))
        #print("\tTokens: " +ctx.getText())
        self.exitContext()
        print("\n"+ "="*20 + " Fin For "+ "="*20)
        

    # Enter a parse tree produced by compiladoresParser#iif.
    def enterIif(self, ctx:compiladoresParser.IifContext):
        # Iniciamos contexto if
        self.tabla.addContexto()
        print("\n" + "="*20 + " If " + "="*20)
        

    # Exit a parse tree produced by compiladoresParser#iif.
    def exitIif(self, ctx:compiladoresParser.IifContext):
        #print("\tCantidad de hijos: " + str(ctx.getChildCount()))
        #print("\tTokens: " +ctx.getText())
        
        #if solo elimina su contexto si else no lo elimino
        if ctx.getChildCount() == 5:
            self.exitContext()
            print("\n"+ "="*20 + " Fin If "+ "="*20)


    # Enter a parse tree produced by compiladoresParser#ielse.
    def enterIelse(self, ctx:compiladoresParser.IelseContext):
        #eliminamos contexto if
        self.exitContext()
        print("\n"+ "="*20 + " Fin If "+ "="*20)
        # Iniciamos contexto else
        self.tabla.addContexto()
        print("\n" + "="*20 + " Else " + "="*20)
        

    # Exit a parse tree produced by compiladoresParser#ielse.
    def exitIelse(self, ctx:compiladoresParser.IelseContext):
        #print("\tCantidad de hijos: " + str(ctx.getChildCount()))
        #print("\tTokens: " +ctx.getText())
        self.exitContext()
        print("\n"+ "="*20 + " Fin Else "+ "="*20)

    #Manejo de funciones

    # Enter a parse tree produced by compiladoresParser#ifuncion.
    def enterIfuncion(self, ctx:compiladoresParser.IfuncionContext):
        # Iniciamos contexto funcion
        self.tabla.addContexto()
        print("\n" + "="*20 + " Funcion " + "="*20)


    # Exit a parse tree produced by compiladoresParser#ifuncion.
    def exitIfuncion(self, ctx:compiladoresParser.IfuncionContext):
        #print("\tCantidad de hijos: " + str(ctx.getChildCount()))
        #print("\tTokens: " +ctx.getText())
        self.exitContext()
        tipoFuncion = ctx.getChild(0).getText()
        idFuncion = ctx.getChild(1).getText()
        myFuncion = Funcion(idFuncion,tipoFuncion,False,False,self.currentParamLists)
        self.currentParamLists = []
        # verificar existencia en contexto
        if not self.tabla.buscarLocal(myFuncion.nombre):
            self.tabla.addIdentificador(myFuncion)
            print("\nDatos de funcion:")
            print(myFuncion)
        else:
            print(f"-ERROR:\n\tIdentificado repetido {myFuncion.nombre}")
        
        print("\n"+ "="*20 + " Fin Funcion "+ "="*20)
        
    # Enter a parse tree produced by compiladoresParser#param.
    def enterParam(self, ctx:compiladoresParser.ParamContext):
        self.inFuncion = True

    # Exit a parse tree produced by compiladoresParser#param.
    def exitParam(self, ctx:compiladoresParser.ParamContext):
        self.inFuncion = False

     # Enter a parse tree produced by compiladoresParser#cond.
    def enterCond(self, ctx:compiladoresParser.CondContext):
        self.controlTypeLists.append(list())

    # Exit a parse tree produced by compiladoresParser#cond.
    def exitCond(self, ctx:compiladoresParser.CondContext):
        print(f"Tipos de datos usados en condicion : {self.controlTypeLists.pop()}")


    def visitTerminal(self, node: TerminalNode):
        #print("-----> Token: " + node.getText())
        self.numTokens +=1
    
    def visitErrorNode(self, node: ErrorNode):
        print("\nNODE ERROR")
    
    def enterEveryRule(self, ctx):
        self.numNodos += 1