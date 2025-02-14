from antlr4 import ErrorNode, TerminalNode
from compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser
from TablaSimbolos import TablaSimbolos
from Variable import Variable
from Funcion import Funcion
from TipoDato import TipoDato

TAM = 80
class Escucha (compiladoresListener):
    
    def __init__(self, table:TablaSimbolos):
        
        self.numTokens = 0
        self.numNodos = 0
        self.tabla = table
        #pila de control de tipos
        self.compatibilityTypeList = list()
        
        #correspondencia en funciones
        self.currentParamLists = list()
        self.currentArgsLists = list()
        self.currentPrototipeLists = list()
        
        #stack para tipos usados
        self.vartypeStack = list()
        
        #flags
        self.inFuncion = False
        self.inParam = False
        self.inAsignacion = False
        self.itsReturns = False 
        self.inDeclaration = False
        self.errorcount = 0
        
    def isAnyError(self):
        if self.errorcount > 0:
            return True
        return False
    
    def printError(self, ctx, msj:str, tipo = "semantico"):
        print("- " + f"\033[31mError {tipo} en linea {ctx.start.line}: {msj}\033[0m")
        self.errorcount += 1
        
    def printAdvertencia(self, ctx, msj:str):
        print("- " + f"\033[33mAdvertencia en linea {ctx.start.line}: {msj}\033[0m")
        
    # Errores y advertencias
    
    def verificarTiposRetorno(self,tipoFuncion,ctx):
        """
            Verifica compatibilidad con los tipos retornados, en caso de incompatibilidad
            imprime error
        """
        if tipoFuncion == 'INT':
            if 'FLOAT' in self.compatibilityTypeList[-1]:
                self.printError(ctx,"Intento retonar FLOAT cuando se espera INT")
        if tipoFuncion == 'CHAR':
            if 'FLOAT' in self.compatibilityTypeList[-1]:
                self.printError(ctx,"Intento retornar FLOAT cuando se espera CHAR")
                
    def validarCompatibilidadTipos(self,list: list,ctx, tipodato = None):
        """
            Verifica la control list con el tipo esperado, si no son compatibles emite
            mensaje de error y retorna False
        """
        if tipodato:
            if tipodato == 'INT':
                if 'FLOAT' in list:
                    self.printError(ctx,"Intento asignar FLOAT a INT")
                    return False
            if tipodato == 'CHAR':
                if 'FLOAT' in list:
                    self.printError(ctx,"Intento asignar FLOAT a CHAR")
                    return False
        else:
            tipo = list[0]
            if len(list) > 1:
                if tipo == 'INT' or tipo == 'FLOAT':
                    if 'FLOAT' in list[1:] or 'INT' in list[1:]:
                        self.printError(ctx,"Intento comparar INT y FLOAT")
                        return False
                if tipo == 'CHAR':
                    if 'FLOAT' in list:
                        self.printError(ctx,"Intento comparar CHAR y FLOAT")
                        return False
                
        return True
                
    def verificarIDInicializado(self,idstr,ctx):
        """
            Verifica si un ID esta inicializado, y lo añade a la lista de control de tipos actual
        """
        myvar = self.tabla.buscarGlobal(idstr)
        if myvar:
            if not myvar.inicializado:
                self.printError(ctx,"Identificador \"{}\" no inicializado".format(idstr))
            myvar.usado = True
            self.compatibilityTypeList[-1].append(myvar.tipoDato)
            
        else:
            self.printError(ctx,"Identificador \"{}\" no definido".format(idstr))
            self.compatibilityTypeList[-1].append('UNDEF')
            return None
        
    def nombreIdentificadorRepetido(self,id,ctx):
        """
            Verifica si un identificador esta repetido en el contexto actual
        """
        if not self.tabla.buscarLocal(id.nombre):
            return False
        else:
            self.printError(ctx,f"Nombre de identificado repetido \"{id.nombre}\"")
            return True
      
    def enterBloque(self, ctx:compiladoresParser.BloqueContext):
        self.tabla.addContexto()
        if self.inFuncion:
            self.parametrosAContexto(ctx)

    def exitBloque(self, ctx:compiladoresParser.BloqueContext):
        self.verificarUsoIDs(ctx)
        self.tabla.delContexto()
        
    def parametrosAContexto(self,ctx):
        """
            Agrega parametros a el contexto actual en caso de estar dentro
            de una funcion
        """
        for param in self.currentParamLists:
            if not self.nombreIdentificadorRepetido(param,ctx):
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
    def verificarUsoIDs(self,ctx):
        """
            Busca los identificadores creados en el contexto actual
            y verifica que se haga uso de ellos, de lo contrario
            lanza una advertencia
        """        
        for idstr in self.tabla.contextos[-1].tabla:
            myvar = self.tabla.contextos[-1].tabla[idstr]
            if not myvar.usado:
                self.printAdvertencia(ctx,"Identificador \"{}\" no utilizado".format(myvar.nombre))
         
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("=" * TAM)
        print("INICIA COMPILACION".center(TAM))
        print("=" * TAM)
        
        # Añadimos contexto global
        self.tabla.addContexto()
        
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        self.verificarUsoIDs(ctx)
        
        for idstr in self.tabla.contextos[-1].tabla:
            id = self.tabla.contextos[-1].tabla[idstr]
            if not id.inicializado:
                if isinstance(id,Funcion):
                    self.printError(ctx,f"funcion {id.nombre} no declarada")
                else:
                    self.printAdvertencia(ctx,"Identificador \"{}\" no inicializado".format(id.nombre))
                
        
        #Borramos contexto global
        self.tabla.delContexto()
        print("=" * TAM)
        print("FIN COMPILACION".center(TAM))
        print("=" * TAM)
        print("")
        self.printHistoricoContextos()
        
        
    def exitInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        if ctx.exception:
            # lanzada cuando falta un punto y coma o falta el id o el tipo
            self.printError(ctx,"Posible falta de ';' o se utilizo un identificador o tipo invalido","sintactico")
    
            
    def exitT(self, ctx:compiladoresParser.TContext):
        if ctx.exception:
            # Obtener el conjunto de tokens esperados en la posición actual
            expected_tokens = ctx.exception.getExpectedTokens()
            
            tokenname = ctx.parser.symbolicNames[expected_tokens.intervals[0].start]
            if tokenname == 'PYC':
                self.printError(ctx,"Posible falta de ';'","sintactico")
            if tokenname == 'PC':
                self.printError(ctx,"Posible falta de ')'","sintactico")
        #division por cero
        if ctx.getChildCount() > 0:
            tkn = ctx.getChild(0).getSymbol()
            value = ctx.getChild(1).getText()
            if tkn.type == compiladoresParser.DIV and value == "0":
                self.printError(ctx, "Intento dividir por cero")
                
        

    def exitIif(self, ctx:compiladoresParser.IifContext):
        if ctx.exception:
            self.printError(ctx,"Posible falta de condicion, falta de llaves o parentesis","sintactico")
    def enterDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        self.inDeclaration = True
   
    def exitInit(self, ctx:compiladoresParser.InitContext):
        if ctx.exception:
                self.printError(ctx,"Posible falta de ';'","sintactico")
    
    def exitCondlist(self, ctx:compiladoresParser.CondlistContext):
        if ctx.exception:
                self.printError(ctx,"Posible falta de ';'","sintactico")
    
    def exitIwhile(self, ctx:compiladoresParser.IwhileContext):
        if ctx.exception:
                self.printError(ctx,"Posible cierre erroneo de parentesis","sintactico")       
    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):    
        
        # Añadimos la primera ID de la regla
        id = ctx.getToken(compiladoresParser.ID, 0)
        if id:
            myvar = Variable(self.vartypeStack[-1],ctx.getChild(1).getText())
            if not self.nombreIdentificadorRepetido(myvar,ctx):
                self.tabla.addIdentificador(myvar)
        
        self.inDeclaration = False
        
    def exitDec(self, ctx:compiladoresParser.DecContext):
        id = ctx.getToken(compiladoresParser.ID, 0)
        if id:
            myvar = Variable(self.vartypeStack[-1],id.getText())
            if not self.nombreIdentificadorRepetido(myvar,ctx):
                self.tabla.addIdentificador(myvar)
            
    def exitTipo(self, ctx:compiladoresParser.TipoContext):
        # Añadimos al stack de tipos usados
        self.vartypeStack.append(ctx.getChild(0).getText().upper())
    
    
    def enterAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        self.compatibilityTypeList .append([])
        self.inAsignacion = True
        
    def exitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        myvar = None
        if self.inDeclaration:
            myvar = Variable(self.vartypeStack[-1],ctx.getChild(0).getText())
            if not self.nombreIdentificadorRepetido(myvar,ctx):
                self.tabla.addIdentificador(myvar)
        else:
            myvar = self.obtenerIdentificadorDeclarado(ctx.getChild(0).getText(),ctx)
        
        # valida asignacion y establece inicializada
        if myvar:
            self.validarCompatibilidadTipos(self.compatibilityTypeList[-1],ctx, myvar.tipoDato)
            myvar.inicializado = True
        self.inAsignacion = False
        
        #limpiar lista de compatibilidad
        self.compatibilityTypeList.pop()
    
      
    def obtenerIdentificadorDeclarado(self,idstr,ctx):
        """
            Busca un identificador declarado, de no encotrarse imprime un error
        """
        myvar = self.tabla.buscarGlobal(idstr)
        if myvar:
            return myvar
        else:
            self.printError(ctx,f"Identificador \"{idstr}\" no declarado")
            return None
        
    def añadirTipoAListaControl(self,ctx:compiladoresParser.FactorContext):
        """
            Añade a la lista de control un tipo segun su token
        """
        if ctx.getToken(compiladoresParser.NUMERO, 0):
            self.compatibilityTypeList[-1].append("INT")
        if ctx.getToken(compiladoresParser.DECIMAL, 0):
            self.compatibilityTypeList[-1].append("FLOAT")
        if ctx.getToken(compiladoresParser.CARACTER, 0):
            self.compatibilityTypeList[-1].append("CHAR")
            
                   
    def exitFactor(self, ctx:compiladoresParser.FactorContext):
        if ctx.exception:
            self.printError(ctx,"Operacion incompleta o no reconocible", 1)
        self.añadirTipoAListaControl(ctx)
        id = ctx.getToken(compiladoresParser.ID, 0)
        if id:
            self.verificarIDInicializado(id.getText(),ctx)
        
            

    def enterIfuncion(self, ctx:compiladoresParser.IfuncionContext):
        self.inFuncion = True

    def exitIfuncion(self, ctx:compiladoresParser.IfuncionContext):
        tipoFuncion = ctx.getChild(0).getText().upper()
        idFuncion = ctx.getChild(1).getText()

        # Buscar si se declaro una funcion con ese nombre
        myprototipo = self.tabla.buscarGlobal(idFuncion)
        
        #Si existe el identificador
        if myprototipo:
            self.validarCorrespondeciaConPrototipo(myprototipo,tipoFuncion,ctx)
            myprototipo.inicializado = True
        else: #La creamos   
            myFuncion = Funcion(idFuncion,tipoFuncion,True,False,self.currentParamLists)
            self.tabla.addIdentificador(myFuncion)
            self.currentParamLists = []
            #verificar compatibilidad con los datos retornados
            if not self.itsReturns and tipoFuncion != 'VOID':
                self.printError(ctx,f"Se espera un valor de retorno {tipoFuncion} y no se proporciono ningun retorno")
                
        if self.itsReturns:
            self.verificarTiposRetorno(tipoFuncion ,ctx)
            # quitamos la lista de retorno
            self.compatibilityTypeList.pop()
            self.itsReturns = False
        
        self.inFuncion = False

    def validarCorrespondeciaConPrototipo(self, myprototipo : Funcion, tipostr,ctx):
        """
            verifica que una funcion cumple con su prototipo o si se repitio un identificador
        """
        #verificamos compatibilidad de tipos
        if tipostr == myprototipo.tipoDato:
            #verificamos que tenga la misma cantidad de parametros
            if len(myprototipo.args) == len(self.currentParamLists):
                for i,protoparam in enumerate(myprototipo.args):
                    if protoparam.tipoDato != self.currentParamLists[i].tipoDato:
                        self.printError(ctx,f"Los tipos de datos no coinciden con los del prototipo\nse esperaba {protoparam.tipoDato} y se dio {self.currentParamLists[i].tipoDato}")      
            else:
                self.printError(ctx,f"Cantidad de argumentos no coincide con el prototipo\n se esperaban {len(myprototipo.args)} y se dieron {len(self.currentParamLists)}")
        else:
            self.printError(ctx,f"Tipo de dato de retorno no coincide con el esperado : {protoparam.tipoDato}")
                  

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
        if not self.nombreIdentificadorRepetido(myFuncion,ctx):
            #confiamos en que el usuario la inicializara
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
        self.compatibilityTypeList.append([])
        
    def exitCond(self, ctx:compiladoresParser.CondContext):
        condlist = self.verificarTipoOpal(self.compatibilityTypeList.pop())
        #aca se deberia verificar si hay incompatibilodad de tipos
        #print(condlist)
        self.validarCompatibilidadTipos(condlist,ctx)
    
    # Enter a parse tree produced by compiladoresParser#ireturn.
    def enterIreturn(self, ctx:compiladoresParser.IreturnContext):
        self.compatibilityTypeList.append([])
        if not self.inFuncion :
            self.printError(ctx,"Utilizacion de un return sin funcion")
        self.itsReturns = True
    
    # Exit a parse tree produced by compiladoresParser#ireturn.
    # Se quita la lista de compatibilidad de retorno en el llamado a la funcion
    #def exitIreturn(self, ctx:compiladoresParser.IreturnContext):
        #self.compatibilityTypeList.pop()
        

    def exitIllamada(self, ctx:compiladoresParser.IllamadaContext):
        id = ctx.getChild(0)
        myfunc = self.tabla.buscarGlobal(id.getText())
        # buscar en la tabla el identificador en caso que no sea una asignacion
        if myfunc :
            # si encuetra el identificador pero es una variable
            if isinstance(myfunc, Variable):
                #OJO ACA
                self.printError(ctx,f"{myfunc.nombre} no es una funcion")
            else:
                #print(myfunc)
                if self.inAsignacion:
                    self.compatibilityTypeList[-1].append(myfunc.tipoDato) #añadimos a la lista de control de tipos

                myfunc.usado = True
                     
                # verificamos argumentos
                #invertimos la lista dado que es necesario para correspondencia
                self.currentArgsLists.reverse()
                
                if len(myfunc.args) != len(self.currentArgsLists):
                    self.printError(ctx,f"Cantidad de argumentos incompatibles en la llamada a {myfunc.nombre}")
                else:
                    for i , arg in enumerate(myfunc.args):
                        if not self.validarCompatibilidadTipos(self.currentArgsLists[i],ctx,arg.tipoDato):
                            self.printError(ctx,f"Tipo de argumento incompatible, se espera {arg.tipoDato} y se dio {self.currentArgsLists[i]}")
                self.currentArgsLists = []
                
        else:
            self.printError(ctx,f"funcion {id.getText()} no existente")

    
    def enterArgumento(self, ctx:compiladoresParser.ArgumentoContext):
        # añadimos una lista por cada argumento
        self.compatibilityTypeList.append([])
        
        
    # Exit a parse tree produced by compiladoresParser#argumento.
    # Por el momento solo acepta variables como argumentos
    def exitArgumento(self, ctx:compiladoresParser.ArgumentoContext):
        if ctx.getChildCount() > 0:
            # verifico el tipo del opal argumento y lo añado a la lista de argumentos
            self.currentArgsLists.append(self.verificarTipoOpal(self.compatibilityTypeList.pop()))
            # recordar que estan siendo acomodados de atras para adelante
        else:
            self.compatibilityTypeList.pop()
            
    def verificarTipoOpal(self, listaTipos):
        """Verifica en una lista de tipos cual es el tipo de dato predominante o si hay tipos combinados
        Retorna una lista con el tipo o los tipos del opal"""
        tlist = list()
        t = listaTipos[0]
        for tipo in listaTipos:
            if tipo != t:
                tlist.append(tipo)
        tlist.append(t)
        return tlist
    
    """
    TESTER CODE PARA DETECCION DE ERRORES SINTACTICOS
     
    def visitErrorNode(self, node):
        print(f"Error en el nodo: {node.getText()}")
        
    def exitEveryRule(self, ctx):
        #if ctx.exception:
          #  print(f"Error sintactico {ctx.exception.offendingToken}")
         if ctx.exception:
            print(type(ctx))
            # Obtener el conjunto de tokens esperados en la posición actual
            expected_tokens = ctx.exception.getExpectedTokens()
            
            # Mostrar los tokens esperados
            print("Tokens esperados en esta posición:")
            
            # Iterar a través de los intervalos y mostrar los tokens
            for interval in expected_tokens.intervals:
                for tokenindex in range(interval.start, interval.stop):
                    # Obtener el nombre del token por su tipo (token_type)
                    #token_name = ctx.parser.symbolicNames[token_type] if token_type < len(ctx.parser.symbolicNames) else f"Unknown({token_type})"
                    tokenname = ctx.parser.symbolicNames[tokenindex]
                    print(tokenname)
                    if tokenname == 'PYC':
                        print("Error se esperaba ';'")
            #self.stopsignal = True """