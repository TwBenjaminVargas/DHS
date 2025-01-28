"""
 Clase dedicada a la optmimizacion de codigo intermedio
"""
class OptCode():
       
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
        
    def propagacionDeConstantes(self):
        valores = dict()
        for line in self.infile:
            linevector = line.split()
            
            if linevector[0] == "ifnjmp":
                #quitamos "," del ifnjmp
                linevector[1] = linevector[1][:-1]
                
            sustituido = False
            for i in range(1,len(linevector)): #recorrer asignacion y cambiar valores
                if linevector[i] in valores:
                    linevector[i] =valores[linevector[i]]
                    sustituido = True
            
            if linevector[1] == "=" and not sustituido: #asignaciones
                if len(linevector) == 3 and self.isNumericValue(linevector[-1]):
                        valores[linevector[0]] = linevector[2]
                        if not self.isTerminal(linevector):
                            continue
                elif len(linevector) > 3 and self.isNumericValue(linevector[2]) and self.isNumericValue(linevector[4]):
                    resul = eval(" ".join(linevector[2:]))
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
            
    def isNumericValue(self,val: str):
        val = val.replace('.','',1) #eliminamos punto si es un decimal
        return val.isdigit()
        
    def eliminarAccionesRepetidas(self):
        acciones = dict()
        sustitutos = dict()
        
        for line in self.infile:
            linevector = line.split()
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
        if len(variable) == 2 and ( variable[0] == "t" and variable[1:].isdigit()):
            return False
        return True
   
    def __del__(self):
        """
            Destructor de la clase
        """
        self.infile.close()
        self.outfile.close()