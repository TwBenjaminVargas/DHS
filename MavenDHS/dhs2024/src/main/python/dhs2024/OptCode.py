"""
 Clase dedicada a la optmimizacion de codigo intermedio
"""
from TablaSimbolos import TablaSimbolos
from Variable import Variable
import sys
class OptCode():
    
    def __init__(self, tablasim : TablaSimbolos):
        self.ventanas = []
        self.tabla = tablasim
        
    def optimizar(self,inroute,outroute):
        self.infile = open(inroute, "r")
        self.outfile = open("auxfile.txt","w+")
        self.eliminarAccionesRepetidas()
        self.infile.close()
        self.outfile.close()
        self.infile = open("auxfile.txt", "r")
        self.outfile = open(outroute,"w+")
        self.propagacionDeConstantes()
        self.infile.close()
        self.outfile.close()
        
    """
    Regsitra ventanas de oportunidad para aplicar optimizaciones
    """
    def findventanasOportunidad(self):
        self.ventanas = []
        
        cod = self.infile.readlines()
        self.infile.seek(0)
        saltar = 0
        index = 0
        for i,line in enumerate(cod,start=0):
            current = line.split()
            if len(current) > 0:
                if saltar > 0:
                    saltar -= 1
                else:
                    if i > 0 :
                        if i == len(cod) - 1:
                            self.closeVentana(i+1)
                        
                        if current[0] == "push":
                            if self.isllamadoAfuncion(i,cod):
                                saltar = 3
                                continue
                        if current[0] == "jmp":
                            self.enterVentana(i+1)
                            continue
                        if current[0] == "label" or current[0] == "ifnjmp":
                            self.enterVentana(i+1)
                            continue
                    else:
                        self.enterVentana(i+1)
        if len(self.ventanas) == 0:
            self.ventanas.append([1,1])
        elif len(self.ventanas[-1]) == 1:
            self.closeVentana(i+1) # 1 sola linea
    """verifica si se cumple la estructura de un llamado a la funcion
    """
    def isllamadoAfuncion(self,i,cod):
        if i + 3 < len(cod):
            current = cod[i].split()
            next = cod[i + 1].split()
            nnext = cod[i + 2].split()
            if next[0] == "jmp":
                if nnext and nnext[0] == "label" and nnext[1] == current[1]:
                    return True
        return False
    
    def closeVentana(self,lnum):
        self.ventanas[-1].append(lnum)
        
    def enterVentana(self,lnum):
        if len(self.ventanas) > 0:
            #cerrar el anterior
            self.ventanas[-1].append(lnum)
            if self.ventanas[-1][0] == self.ventanas[-1][1]:
                self.ventanas.pop() #en caso de colision descartamos
            self.ventanas.append([lnum + 1])
        #primera ventana
        else:
            self.ventanas.append([lnum])

    def propagacionDeConstantes(self):
        self.findventanasOportunidad()
        valores = dict()
        #blockedLabel = []
        cod = self.infile.readlines()
        for index,line in  enumerate(cod,start=1):
            linevector = line.split()
            if len(linevector) > 0:
                if linevector[0] == "ifnjmp":
                    #quitamos "," del ifnjmp
                    linevector[1] = linevector[1][:-1]
                sustituido = False
                for i in range(1,len(linevector)): #recorrer asignacion y cambiar valores
                    if linevector[i] in valores:
                        linevector[i] =valores[linevector[i]]
                        sustituido = True
                        
                        if self.isTerminal(linevector[0]):
                            myvar = self.tabla.buscarGlobalHistoric(linevector[0])
                            if isinstance(myvar,Variable) and myvar.tipoDato == "INT":
                                linevector[i] = str( int( float( linevector[i]  ) ) )

                if linevector[1] == "=" and not sustituido: #asignaciones
                    if len(linevector) == 3 and self.isNumericValue(linevector[-1]):
                            valores[linevector[0]] = linevector[2]
                            if not self.isTerminal(linevector):
                                continue
                    elif len(linevector) > 3 and self.isNumericValue(linevector[2]) and self.isNumericValue(linevector[4]):
                        # ------- Resolucion de operaciones matematicas -------
                        resul = 0
                        try:
                            resul = eval(" ".join(linevector[2:]))
                        except ZeroDivisionError:
                            print(f"\033[1;37;41mError durante optimizacion: Division por cero detectada\033[0m\n")
                            sys.exit()
                        if type(resul) == bool:
                            if resul:
                                resul = 1
                            else:
                                resul = 0
                        del linevector[2:]
                        linevector.append(str(resul))                         
    
                if linevector[0] == "ifnjmp":
                    #devolvemos el "," del ifnjmp
                    linevector[1] += ","
            
            self.outfile.write(" ".join(linevector) + "\n")
            self.controlPropagacion(index,valores)
    
            
            
    def controlPropagacion(self, currentline,valores : dict):
        for start,end in self.ventanas:
            if currentline < end:
                return
            if currentline == end:
                valores.clear()
                self.ventanas.pop(0)
                #print(f"Esto se deberia haber reiniciado {valores}")
                return
                
    def controlEliminacion(self, currentline, acciones : dict,sustitutos : dict):
        for start,end in self.ventanas:
            if currentline<end:
                return
            if currentline == end:
                acciones.clear()
                sustitutos.clear()
                self.ventanas.pop(0)
                #print(f"Esto se deberia haber reiniciado {acciones} {sustitutos}")
                return
            
    def isNumericValue(self,val: str):
        val = val.replace('.','',1) #eliminamos punto si es un decimal
        return val.isdigit()
        
    def eliminarAccionesRepetidas(self):
        self.findventanasOportunidad()
        acciones = dict()
        sustitutos = dict()
        cod = self.infile.readlines()
        for index,line in enumerate(cod,start=1):
            linevector = line.split()
            if len(linevector) > 0:
                if linevector[0] == "ifnjmp":
                    #quitamos "," del ifnjmp
                    linevector[1] = linevector[1][:-1]
                    
                sustituido = False
                for i in range(1,len(linevector)):
                    if linevector[i] in sustitutos:
                        linevector[i] = sustitutos[linevector[i]]
                        sustituido = True
                        
                if linevector[1] == "=": # asignacion
                    accion = " ".join(linevector[2:])
                    #print(f"{accion} linea {index}")
                    variable = linevector[0]
                    if self.isTerminal(linevector):
                        # en caso de actualizacion del valor de una variable debemos "limpiar diccionario de acciones 
                        # que la contenian asi evitamos que se sigan usando
                        #terminales.add(linevector[0])
                        self.limpiarDiccionario(acciones,variable)
                    elif not sustituido:    
                                if accion in acciones:
                                    sustitutos[variable] = acciones[accion]
                                    continue
                                else:
                                    acciones[accion] = variable

                if linevector[0] == "ifnjmp":
                    #devolvemos el "," del ifnjmp
                    linevector[1] += ","
                    
            self.outfile.write(" ".join(linevector) + "\n")
            self.controlEliminacion(index,acciones,sustitutos)
            
    
    def limpiarDiccionario(self, diccionario : dict, valor):
        diccionario_copy = diccionario.copy()
        for accion in diccionario_copy:
            if valor in accion:
                #print(f" salio {diccionario.pop(accion)} con la accion {accion}")
                diccionario.pop(accion)
    
    def isTerminal(self, line):
        """
            Determina si una linea es del tipo terminal por ejemplo a = t0
        """
        variable = line[0]
        if variable[0] == "t" and variable[1:].isdigit():
            return False
        return True
   
    def __del__(self):
        """
            Destructor de la clase
        """
        self.infile.close()
        self.outfile.close()