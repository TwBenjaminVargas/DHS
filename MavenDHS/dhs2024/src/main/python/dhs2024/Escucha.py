from antlr4 import ErrorNode, TerminalNode
from compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser
from TablaSimbolos import TablaSimbolos
from Variable import Variable
from Funcion import Funcion
from TipoDato import TipoDato

TAM = 80
class Escucha (compiladoresListener):
    
    def __init__(self):
        self.numTokens = 0
        self.numNodos = 0
        self.tabla = TablaSimbolos()
        
        self.lastTypeUsed = None
        
        #pila de control de tipos
        self.controlTypeLists = list()
        self.currentParamLists = list()
        self.currentDeclarationList = list()
        
        #flags
        self.inFuncion = False
        self.inParam = False
        self.inAsignacion = False
        self.itsReturns = False 
        self.inDeclaration = False

    def exitContext(self):
        """
            Busca las variables creadas en el contexto actual
            y verifica que se haga uso de ellas, de lo contrario
            lanza una advertencia
        """        
        # optimizar
        for idstr in self.tabla.contextos[-1].tabla:
            myvar = self.tabla.contextos[-1].tabla[idstr]
            if not myvar.usado:
                print("")
                print("-"*TAM)
                print("ADVERTENCIA:".center(TAM))
                print("Identificador \"{}\" no utilizado".format(myvar.nombre).center(80))
                print("-"*TAM)
                
        self.tabla.delContexto()
         
    # Enter a parse tree produced by compiladoresParser#programa.
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("=" * TAM)
        print("INICIA COMPILACION".center(TAM))
        print("=" * TAM)
        # Añadimos contexto global
        self.tabla.addContexto()
        
    # Exit a parse tree produced by compiladoresParser#programa.
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        self.exitContext() 
        print("=" * TAM)
        print("FIN COMPILACION".center(TAM))
        print("=" * TAM)
        print("")
        
        print("TABLA CONTEXTOS:")
        for i, contexto in enumerate(self.tabla.contextosHistoric):
            print("."*TAM)
            print(f"CONTEXTO {i}:" + contexto.__str__())
        print("."*TAM)
        print("")


    
    # Enter a parse tree produced by compiladoresParser#declaracion.
    def enterDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        #print("\n+Declaracion:\n")
        self.inDeclaration = True
        
        
        
    # Exit a parse tree produced by compiladoresParser#declaracion.
    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):    
        
        # instanciamos objeto variable
        
        #obtenemos el tipo de dato
        vartype = ctx.getChild(0).getChild(0).getText().upper()
        self.lastTypeUsed = vartype
        #añadimos la primera ID a la lista de declaraciones solo si es un id
        id = ctx.getToken(compiladoresParser.ID, 0)
        if id:
            self.currentDeclarationList.append(Variable(0,ctx.getChild(1).getText()))
        for myvar in self.currentDeclarationList:
            myvar.tipoDato = vartype   
            # verificar existencia en contexto
            if not self.tabla.buscarLocal(myvar.nombre):
                self.tabla.addIdentificador(myvar)
                #print(myvar)
            else:
                print("")
                print("-"*TAM)
                print("ERROR SEMANTICO:".center(TAM))
                print(f"Nombre de identificado repetido \"{myvar.nombre}\"".center(TAM))
                print("-"*TAM)
                
            # REVISAR 
            if self.inParam :
                myvar.inicializado = True #suponemos inicializado un parametro
                self.currentParamLists.append(myvar)
        
        self.inDeclaration = False
        self.lastTypeUsed = None
        self.currentDeclarationList = [] 
    
    # Exit a parse tree produced by compiladoresParser#dec.
    def exitDec(self, ctx:compiladoresParser.DecContext):
        id = ctx.getToken(compiladoresParser.ID, 0)
        if id:
            self.currentDeclarationList.append(Variable(0,id.getText()))
    
    # Enter a parse tree produced by compiladoresParser#asignacion.
    def enterAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        #print("\n+Asignacion")
        self.controlTypeLists.append(list()) #agregamos una lista de control
        self.inAsignacion = True
    
    # Aqui se incluiran algunas reglas para validar una asignacion segun el tipo
    def validarAsignacion(self,tipodato):
        if self.itsReturns :
            if tipodato == 'INT':
                if 'FLOAT' in self.controlTypeLists[-1]:
                    print("")
                    print("-"*TAM)
                    print("ERROR SEMANTICO:".center(TAM))
                    print("Intento retonar FLOAT cuando se espera INT".center(TAM))
                    print("-"*TAM)
            if tipodato == 'CHAR':
                if 'FLOAT' in self.controlTypeLists[-1]:
                    print("")
                    print("-"*TAM)
                    print("ERROR SEMANTICO:".center(TAM))
                    print("Intento retornar FLOAT cuando se espera CHAR".center(TAM))
                    print("-"*TAM)
        else:    
            if tipodato == 'INT':
                if 'FLOAT' in self.controlTypeLists[-1]:
                    print("")
                    print("-"*TAM)
                    print("ERROR SEMANTICO:".center(TAM))
                    print("Intento asignar FLOAT a INT".center(TAM))
                    print("-"*TAM)
            if tipodato == 'CHAR':
                if 'FLOAT' in self.controlTypeLists[-1]:
                    print("")
                    print("-"*TAM)
                    print("ERROR SEMANTICO:".center(TAM))
                    print("Intento asignar FLOAT a CHAR".center(TAM))
                    print("-"*TAM)
      
    # Exit a parse tree produced by compiladoresParser#asignacion.
    def exitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        myvar = None
        if self.inDeclaration:
            self.currentDeclarationList.append(Variable(self.lastTypeUsed,ctx.getChild(0).getText()))
            myvar = self.currentDeclarationList[-1]
        else:
            # buscar variable
            myvar = self.tabla.buscarGlobal(ctx.getChild(0).getText())
        # valida asignacion y establece inicializada
        if myvar:
            self.validarAsignacion(myvar.tipoDato)
            myvar.inicializado = True
            #print("\n\tEstado Variable:\n")
            #print(myvar)
        else:    
            print("")
            print("-"*TAM)
            print("ERROR SEMANTICO:".center(TAM))
            print(f"Identificador \"{ctx.getChild(0).getText()}\" no declarado".center(TAM))
            print("-"*TAM)
            
        self.inAsignacion = False
        #eliminamos ultimo elemnto de pila de control
        #print(f"\nTipos usados en esta asignacion: {self.controlTypeLists.pop()}\n")
    
    #Verifica si un ID existe o esta inicializado y lo añade a la controlList
    def verificarID(self,id):
        myvar = self.tabla.buscarGlobal(id.getText())
        if myvar:
            if not myvar.inicializado:
                print("")
                print("-"*TAM)
                print("ERROR SEMANTICO:".center(TAM))
                print("Identificador \"{}\" no inicializado".format(id.getText()).center(TAM))
                print("-"*TAM)
            myvar.usado = True
            self.controlTypeLists[-1].append(myvar.tipoDato)
            
        else:
            print("")
            print("-"*TAM)
            print("ERROR SEMANTICO:".center(TAM))
            print("Identificador \"{}\" no definido".format(id.getText()).center(TAM))
            print("-"*TAM)
            return None
        
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
        #print("\n" + "="*20 + " While " + "="*20)

    # Exit a parse tree produced by compiladoresParser#iwhile.
    def exitIwhile(self, ctx:compiladoresParser.IwhileContext):
        self.exitContext()
        #print("\n"+ "="*20 + " Fin While "+ "="*20)
    

    # Enter a parse tree produced by compiladoresParser#ifor.
    def enterIfor(self, ctx:compiladoresParser.IforContext):
        # Iniciamos contexto for
        self.tabla.addContexto()
        #print("\n" + "="*20 + " For " + "="*20)
        

    # Exit a parse tree produced by compiladoresParser#ifor.
    def exitIfor(self, ctx:compiladoresParser.IforContext):
        self.exitContext()
        #print("\n"+ "="*20 + " Fin For "+ "="*20)
        

    # Enter a parse tree produced by compiladoresParser#iif.
    def enterIif(self, ctx:compiladoresParser.IifContext):
        # Iniciamos contexto if
        self.tabla.addContexto()
        #print("\n" + "="*20 + " If " + "="*20)
        

    # Exit a parse tree produced by compiladoresParser#iif.
    def exitIif(self, ctx:compiladoresParser.IifContext):
        
        #if solo elimina su contexto si else no lo elimino
        if ctx.getChildCount() == 5:
            self.exitContext()
            #print("\n"+ "="*20 + " Fin If "+ "="*20)


    # Enter a parse tree produced by compiladoresParser#ielse.
    def enterIelse(self, ctx:compiladoresParser.IelseContext):
        #eliminamos contexto if
        self.exitContext()
        #print("\n"+ "="*20 + " Fin If "+ "="*20)
        # Iniciamos contexto else
        self.tabla.addContexto()
        #print("\n" + "="*20 + " Else " + "="*20)
        

    # Exit a parse tree produced by compiladoresParser#ielse.
    def exitIelse(self, ctx:compiladoresParser.IelseContext):
        self.exitContext()
        #print("\n"+ "="*20 + " Fin Else "+ "="*20)


    #Manejo de funciones

    # Enter a parse tree produced by compiladoresParser#ifuncion.
    def enterIfuncion(self, ctx:compiladoresParser.IfuncionContext):
        # Iniciamos contexto funcion
        self.tabla.addContexto()
        self.inFuncion = True
        #print("\n" + "="*20 + " Funcion " + "="*20)

    # Exit a parse tree produced by compiladoresParser#ifuncion.
    def exitIfuncion(self, ctx:compiladoresParser.IfuncionContext):
        
        self.exitContext()
        tipoFuncion = ctx.getChild(0).getText().upper()
        idFuncion = ctx.getChild(1).getText()
        myFuncion = Funcion(idFuncion,tipoFuncion,True,False,self.currentParamLists)
        
        self.currentParamLists = []
        # verificar existencia en contexto
        if not self.tabla.buscarLocal(myFuncion.nombre):
            self.tabla.addIdentificador(myFuncion)
            #print("\nDatos de funcion:")
            #print(myFuncion)
        else:
            print("")
            print("-"*TAM)
            print("ERROR SEMANTICO:".center(TAM))
            print(f"Identificado repetido {myFuncion.nombre}".center(TAM))
            print("-"*TAM)
        
        #verificar compatibilidad con los datos retornados
        if not self.itsReturns and tipoFuncion != 'VOID':
            print("")
            print("-"*TAM)
            print("ERROR SEMANTICO:".center(TAM))
            print(f"Se espera un valor de retorno {tipoFuncion} y no se proporciono ningun retorno".center(TAM))
            print("-"*TAM)
            
        if self.itsReturns:
            self.validarAsignacion(tipoFuncion)
            #print(f"\nTipos de datos usados en return : {self.controlTypeLists.pop()}")
            self.itsReturns = False
        
        self.inFuncion = False
        #print("\n"+ "="*20 + " Fin Funcion "+ "="*20)
        
    # Enter a parse tree produced by compiladoresParser#param.
    def enterParam(self, ctx:compiladoresParser.ParamContext):
        self.inParam = True

    # Exit a parse tree produced by compiladoresParser#param.
    def exitParam(self, ctx:compiladoresParser.ParamContext):
        self.inParam = False
 
 # Exit a parse tree produced by compiladoresParser#p.
    def exitP(self, ctx:compiladoresParser.PContext):
        varname = ctx.getChild(1).getText()
        vartype = ctx.getChild(0).getText().upper()
        myvar = Variable (vartype,varname,True,False)
        self.currentParamLists.append(myvar)
        # verificar existencia en contexto
        if not self.tabla.buscarLocal(myvar.nombre):
            self.tabla.addIdentificador(myvar)
        else:
            print("")
            print("-"*TAM)
            print("ERROR SEMANTICO:".center(TAM))
            print(f"Nombre de identificado repetido \"{myvar.nombre}\"".center(TAM))
            print("-"*TAM)
        

        
    # Enter a parse tree produced by compiladoresParser#cond.
    def enterCond(self, ctx:compiladoresParser.CondContext):
        self.controlTypeLists.append(list())

    # Exit a parse tree produced by compiladoresParser#cond.
    def exitCond(self, ctx:compiladoresParser.CondContext):
        #print(f"Tipos de datos usados en condicion : {self.controlTypeLists.pop()}")
        pass
    
    # Enter a parse tree produced by compiladoresParser#ireturn.
    def enterIreturn(self, ctx:compiladoresParser.IreturnContext):
        self.controlTypeLists.append(list())
        if not self.inFuncion :
            print("")
            print("-"*TAM)
            print("ERROR SEMANTICO:".center(TAM))
            print("Utilizacion de un return sin funcion".center(TAM))
            print("-"*TAM)
        self.itsReturns = True

    # Enter a parse tree produced by compiladoresParser#illamada.
    def enterIllamada(self, ctx:compiladoresParser.IllamadaContext):
        #print("\n+Llamada a funcion:\n")
        pass

    # Exit a parse tree produced by compiladoresParser#illamada.
    def exitIllamada(self, ctx:compiladoresParser.IllamadaContext):
        id = ctx.getChild(0)
        myfunc = self.tabla.buscarGlobal(id.getText())
        # buscar en la tabla el identificador en caso que no sea una asignacion
        if myfunc :
            #print(myfunc)
            if self.inAsignacion:
                ## --------------> OPTIMIZAR
                self.controlTypeLists[-1].append(myfunc.tipoDato) #lo añadimos a la lista de control de tipos
            
            myfunc.usado = True        
            # verificamos argumentos
            if len(myfunc.args) != len(self.currentParamLists):
                print("")
                print("-"*TAM)
                print("ERROR SEMANTICO:".center(TAM))
                print("Cantidad de argumentos incompatibles".center(TAM))
                print("-"*TAM)
            else:
                for i , arg in enumerate(myfunc.args):
                    if arg.tipoDato != self.currentParamLists[i].tipoDato:
                        print("")
                        print("-"*TAM)
                        print("ERROR SEMANTICO:".center(TAM))
                        print(f"Tipo de argumento incompatible, se espera {arg.tipoDato} y se dio {self.currentParamLists[i].tipoDato}".center(TAM))
                        print("-"*TAM)
            self.currentParamLists = []
        else: 
            print("")
            print("-"*TAM)
            print("ERROR SEMANTICO:".center(TAM))
            print(f"funcion {id.getText()} no declarada".center(TAM))
            print("-"*TAM)
        
        
        
    # Exit a parse tree produced by compiladoresParser#argumento.
    # Por el momento solo acepta variables como argumentos
    def exitArgumento(self, ctx:compiladoresParser.ArgumentoContext):
         id = ctx.getToken(compiladoresParser.ID, 0)
         if id:
            arg = self.tabla.buscarGlobal(id.getText())
            if arg:
                self.currentParamLists.append(arg)
                arg.usado = True
            else:
                print("")
                print("-"*TAM)
                print("ERROR SEMANTICO:".center(TAM))
                print(f"Identificador {id.getText()} no declarado".center(TAM))
                print("-"*TAM)
            


    def visitTerminal(self, node: TerminalNode):
        #print("-----> Token: " + node.getText())
        self.numTokens +=1
    
    def visitErrorNode(self, node: ErrorNode):
        print("-"*TAM)
        print(f"ERROR SINTACTICO: Linea <{node.getSymbol().line}>".center(TAM))
        print("-"*TAM)
    
    def enterEveryRule(self, ctx):
        self.numNodos += 1