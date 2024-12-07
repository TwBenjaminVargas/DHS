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
            
        #pila de control de tipos
        self.compatibilityTypeList = list()
        self.currentParamLists = list()
        self.currentArgsLists = list()
        self.currentDeclarationList = list()
        self.currentPrototipeLists = list()
        #stack para tipos usados
        self.vartypeStack = list()
        
        #flags
        self.inFuncion = False
        self.inParam = False
        self.inAsignacion = False
        self.itsReturns = False 
        self.inDeclaration = False
        
    # Errores y advertencias
    def verificarTiposRetorno(self,tipoFuncion):
        """
            Verifica compatibilidad con los tipos retornados, en caso de incompatibilidad
            imprime error
        """
        if tipoFuncion == 'INT':
            if 'FLOAT' in self.compatibilityTypeList:
                print("")
                print("-"*TAM)
                print("ERROR SEMANTICO:".center(TAM))
                print("Intento retonar FLOAT cuando se espera INT".center(TAM))
                print("-"*TAM)
        if tipoFuncion == 'CHAR':
            if 'FLOAT' in self.compatibilityTypeList:
                print("")
                print("-"*TAM)
                print("ERROR SEMANTICO:".center(TAM))
                print("Intento retornar FLOAT cuando se espera CHAR".center(TAM))
                print("-"*TAM)
                
    def validarCompatibilidadTipos(self,tipodato):
        """
            Verifica la control list con el tipo esperado, si no son compatibles emite
            mensaje de error
        """
        if tipodato == 'INT':
            if 'FLOAT' in self.compatibilityTypeList:
                print("")
                print("-"*TAM)
                print("ERROR SEMANTICO:".center(TAM))
                print("Intento asignar FLOAT a INT".center(TAM))
                print("-"*TAM)
        if tipodato == 'CHAR':
            if 'FLOAT' in self.compatibilityTypeList:
                print("")
                print("-"*TAM)
                print("ERROR SEMANTICO:".center(TAM))
                print("Intento asignar FLOAT a CHAR".center(TAM))
                print("-"*TAM)
                
    def verificarIDInicializado(self,idstr):
        """
            Verifica si un ID esta inicializado, y lo añade a la lista de control de tipos actual
        """
        myvar = self.tabla.buscarGlobal(idstr)
        if myvar:
            if not myvar.inicializado:
                print("")
                print("-"*TAM)
                print("ERROR SEMANTICO:".center(TAM))
                print("Identificador \"{}\" no inicializado".format(idstr).center(TAM))
                print("-"*TAM)
            myvar.usado = True
            self.compatibilityTypeList.append(myvar.tipoDato)
            
        else:
            print("")
            print("-"*TAM)
            print("ERROR SEMANTICO:".center(TAM))
            print("Identificador \"{}\" no definido".format(idstr).center(TAM))
            print("-"*TAM)
            return None
        
    def nombreIdentificadorRepetido(self,id):
        """
            Verifica si un identificador esta repetido en el contexto actual
        """
        if not self.tabla.buscarLocal(id.nombre):
            return False
        else:
            print("")
            print("-"*TAM)
            print("ERROR SEMANTICO:".center(TAM))
            print(f"Nombre de identificado repetido \"{id.nombre}\"".center(TAM))
            print("-"*TAM)
            return True
      
    def enterBloque(self, ctx:compiladoresParser.BloqueContext):
        self.tabla.addContexto()
        if self.inFuncion:
            self.parametrosAContexto()

    def exitBloque(self, ctx:compiladoresParser.BloqueContext):
        self.verificarUsoIDs()
        self.tabla.delContexto()
        
    def parametrosAContexto(self):
        """
            Agrega parametros a el contexto actual en caso de estar dentro
            de una funcion
        """
        for param in self.currentParamLists:
            if not self.nombreIdentificadorRepetido(param):
                self.tabla.addIdentificador(param)
                
    def printHistoricoContextos(self):
        """
            Imprime el historico de los contextos utilizados
        """
        print("TABLA CONTEXTOS:")
        for i, contexto in enumerate(self.tabla.contextosHistoric):
            print("."*TAM)
            print(f"CONTEXTO {i}:" + contexto.__str__())
        print("."*TAM)
        print("")
        

    #OPT
    def verificarUsoIDs(self):
        """
            Busca los identificadores creados en el contexto actual
            y verifica que se haga uso de ellos, de lo contrario
            lanza una advertencia
        """        
        for idstr in self.tabla.contextos[-1].tabla:
            myvar = self.tabla.contextos[-1].tabla[idstr]
            if not myvar.usado:
                print("")
                print("-"*TAM)
                print("ADVERTENCIA:".center(TAM))
                print("Identificador \"{}\" no utilizado".format(myvar.nombre).center(80))
                print("-"*TAM)
         
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("=" * TAM)
        print("INICIA COMPILACION".center(TAM))
        print("=" * TAM)
        
        # Añadimos contexto global
        self.tabla.addContexto()
        
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        self.verificarUsoIDs()
        
        #Borramos contexto global
        self.tabla.delContexto()
        print("=" * TAM)
        print("FIN COMPILACION".center(TAM))
        print("=" * TAM)
        print("")
        
        self.printHistoricoContextos()


    def enterDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        self.inDeclaration = True
   
        
    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):    
        
        # Añadimos la primera ID de la regla
        id = ctx.getToken(compiladoresParser.ID, 0)
        if id:
            myvar = Variable(self.vartypeStack[-1],ctx.getChild(1).getText())
            if not self.nombreIdentificadorRepetido(myvar):
                self.tabla.addIdentificador(myvar)
        
        self.inDeclaration = False
        self.currentDeclarationList = []
        
    def exitDec(self, ctx:compiladoresParser.DecContext):
        id = ctx.getToken(compiladoresParser.ID, 0)
        if id:
            myvar = Variable(self.vartypeStack[-1],id.getText())
            if not self.nombreIdentificadorRepetido(myvar):
                self.tabla.addIdentificador(myvar)
            
    def exitTipo(self, ctx:compiladoresParser.TipoContext):
        # Añadimos al stack de tipos usados
        self.vartypeStack.append(ctx.getChild(0).getText().upper())
    
    
    def enterAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        self.compatibilityTypeList = []
        self.inAsignacion = True
        
    def exitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        myvar = None
        if self.inDeclaration:
            myvar = Variable(self.vartypeStack[-1],ctx.getChild(0).getText())
            if not self.nombreIdentificadorRepetido(myvar):
                self.tabla.addIdentificador(myvar)
        else:
            myvar = self.obtenerIdentificadorDeclarado(ctx.getChild(0).getText())
        
        # valida asignacion y establece inicializada
        if myvar:
            self.validarCompatibilidadTipos(myvar.tipoDato)
            myvar.inicializado = True
        self.inAsignacion = False
    
      
    def obtenerIdentificadorDeclarado(self,idstr):
        """
            Busca un identificador declarado, de no encotrarse imprime un error
        """
        myvar = self.tabla.buscarGlobal(idstr)
        if myvar:
            return myvar
        else:
            print("")
            print("-"*TAM)
            print("ERROR SEMANTICO:".center(TAM))
            print(f"Identificador \"{idstr}\" no declarado".center(TAM))
            print("-"*TAM)
            return None
    def añadirTipoAListaControl(self,ctx:compiladoresParser.FactorContext):
        """
            Añade a la lista de control un tipo segun su token
        """
        if ctx.getToken(compiladoresParser.NUMERO, 0):
            self.compatibilityTypeList.append("INT")
        if ctx.getToken(compiladoresParser.DECIMAL, 0):
            self.compatibilityTypeList.append("FLOAT")
        if ctx.getToken(compiladoresParser.CARACTER, 0):
            self.compatibilityTypeList.append("CHAR")
            
                   
    def exitFactor(self, ctx:compiladoresParser.FactorContext):
        self.añadirTipoAListaControl(ctx)
        id = ctx.getToken(compiladoresParser.ID, 0)
        if id:
            self.verificarIDInicializado(id.getText())
        
    def exitSuf(self, ctx:compiladoresParser.SufContext):
        id = ctx.getToken(compiladoresParser.ID, 0)
        if id: # si encuentro un nodo ID
            self.verificarIDInicializado(id.getText())
    
    
    def exitPref(self, ctx:compiladoresParser.PrefContext):
        id = ctx.getToken(compiladoresParser.ID, 0)
        if id: # si encuentro un nodo ID
            self.verificarIDInicializado(id.getText())
            

    def enterIfuncion(self, ctx:compiladoresParser.IfuncionContext):
        self.inFuncion = True

    def exitIfuncion(self, ctx:compiladoresParser.IfuncionContext):
        tipoFuncion = ctx.getChild(0).getText().upper()
        idFuncion = ctx.getChild(1).getText()

        # Buscar si se declaro una funcion con ese nombre
        myprototipo = self.tabla.buscarGlobal(idFuncion)
        
        #Si existe el identificador
        if myprototipo:
            self.validarCorrespondeciaConPrototipo(myprototipo,tipoFuncion)
            myprototipo.inicializado = True
        else: #La creamos   
            myFuncion = Funcion(idFuncion,tipoFuncion,True,False,self.currentParamLists)
            self.tabla.addIdentificador(myFuncion)
            self.currentParamLists = []
            #verificar compatibilidad con los datos retornados
            if not self.itsReturns and tipoFuncion != 'VOID':
                print("")
                print("-"*TAM)
                print("ERROR SEMANTICO:".center(TAM))
                print(f"Se espera un valor de retorno {tipoFuncion} y no se proporciono ningun retorno".center(TAM))
                print("-"*TAM)
                
        if self.itsReturns:
            self.verificarTiposRetorno(tipoFuncion)
            self.itsReturns = False
        
        self.inFuncion = False

    def validarCorrespondeciaConPrototipo(self, myprototipo : Funcion, tipostr):
        """
            verifica que una funcion cumple con su prototipo o si se repitio un identificador
        """
        #verificamos compatibilidad de tipos
        if tipostr == myprototipo.tipoDato:
            #verificamos que tenga la misma cantidad de parametros
            if len(myprototipo.args) == len(self.currentParamLists):
                for i,protoparam in enumerate(myprototipo.args):
                    if protoparam.tipoDato != self.currentParamLists[i].tipoDato:
                        print("")
                        print("-"*TAM)
                        print("ERROR SEMANTICO:".center(TAM))
                        print(f"Los tipos de datos no coinciden con los del prototipo\nse esperaba {protoparam.tipoDato} y se dio {self.currentParamLists[i].tipoDato}".center(TAM))
                        print("-"*TAM)      
            else:
                print("")
                print("-"*TAM)
                print("ERROR SEMANTICO:".center(TAM))
                print(f"Cantidad de argumentos no coincide con el prototipo\n se esperaban {len(myprototipo.args)} y se dieron {len(self.currentParamLists)}".center(TAM))
                print("-"*TAM)        
        else:
            print("")
            print("-"*TAM)
            print("ERROR SEMANTICO:".center(TAM))
            print(f"Tipo de dato de retorno no coincide con el esperado : {protoparam.tipoDato}".center(TAM))
            print("-"*TAM)
                  

    # Enter a parse tree produced by compiladoresParser#param.
    def enterParam(self, ctx:compiladoresParser.ParamContext):
        self.inParam = True

    # Exit a parse tree produced by compiladoresParser#param.
    def exitParam(self, ctx:compiladoresParser.ParamContext):
        self.inParam = False
 
    # Enter a parse tree produced by compiladoresParser#iprototipo.
    def enterIprototipo(self, ctx:compiladoresParser.IprototipoContext):
        self.currentPrototipeLists = []

    def exitIprototipo(self, ctx:compiladoresParser.IprototipoContext):
        tipoFuncion = ctx.getChild(0).getText().upper()
        idFuncion = ctx.getChild(1).getText()
        myFuncion = Funcion(idFuncion,tipoFuncion,False,False,self.currentPrototipeLists)
        if not self.nombreIdentificadorRepetido(myFuncion):
            self.tabla.addIdentificador(myFuncion)

    def exitProtoparam(self, ctx:compiladoresParser.ProtoparamContext):
        vartype = self.vartypeStack[-1]
        myvar = Variable (vartype,"unnamed",True,False)
        self.currentPrototipeLists.append(myvar)

 # Exit a parse tree produced by compiladoresParser#p.
    def exitP(self, ctx:compiladoresParser.PContext):
        varname = ctx.getChild(1).getText()
        vartype = self.vartypeStack[-1]
        myvar = Variable (vartype,varname,True,False)
        self.currentParamLists.append(myvar)        


    # Enter a parse tree produced by compiladoresParser#cond.
    def enterCond(self, ctx:compiladoresParser.CondContext):
        self.compatibilityTypeList = []

    
    # Enter a parse tree produced by compiladoresParser#ireturn.
    def enterIreturn(self, ctx:compiladoresParser.IreturnContext):
        self.compatibilityTypeList = []
        if not self.inFuncion :
            print("")
            print("-"*TAM)
            print("ERROR SEMANTICO:".center(TAM))
            print("Utilizacion de un return sin funcion".center(TAM))
            print("-"*TAM)
        self.itsReturns = True


    def exitIllamada(self, ctx:compiladoresParser.IllamadaContext):
        id = ctx.getChild(0)
        myfunc = self.tabla.buscarGlobal(id.getText())
        # buscar en la tabla el identificador en caso que no sea una asignacion
        if myfunc :
            if myfunc.inicializado:
                #print(myfunc)
                if self.inAsignacion:
                    self.compatibilityTypeList.append(myfunc.tipoDato) #añadimos a la lista de control de tipos

                myfunc.usado = True        
                # verificamos argumentos
                if len(myfunc.args) != len(self.currentArgsLists):
                    print("")
                    print("-"*TAM)
                    print("ERROR SEMANTICO:".center(TAM))
                    print(f"Cantidad de argumentos incompatibles en la llamada a {myfunc.nombre}".center(TAM))
                    print("-"*TAM)
                else:
                    for i , arg in enumerate(myfunc.args):
                        if arg.tipoDato != self.currentArgsLists[i].tipoDato:
                            print("")
                            print("-"*TAM)
                            print("ERROR SEMANTICO:".center(TAM))
                            print(f"Tipo de argumento incompatible, se espera {arg.tipoDato} y se dio {self.currentParamLists[i].tipoDato}".center(TAM))
                            print("-"*TAM)
                self.currentArgsLists = []
            else:
                print("")
                print("-"*TAM)
                print("ERROR SEMANTICO:".center(TAM))
                print(f"funcion {id.getText()} no inicializada".center(TAM))
                print("-"*TAM) 
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
            arg = self.obtenerIdentificadorDeclarado(id.getText())
            if arg:
                self.currentArgsLists.append(arg)
                arg.usado = True
            


    def visitTerminal(self, node: TerminalNode):
        #print("-----> Token: " + node.getText())
        self.numTokens +=1
    
    def visitErrorNode(self, node: ErrorNode):
        print("-"*TAM)
        print(f"ERROR SINTACTICO: Linea <{node.getSymbol().line}>".center(TAM))
        print("-"*TAM)
    
    def enterEveryRule(self, ctx):
        self.numNodos += 1