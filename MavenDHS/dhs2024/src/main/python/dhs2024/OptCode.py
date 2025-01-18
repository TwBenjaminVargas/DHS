"""
 Clase dedicada a la optmimizacion de codigo intermedio
"""
class OptCode():
    
    def __init__(self,inroute, outroute):
        self.infile = open(inroute, "r")
        self.outfile = open(outroute,"w+")
        
    def optimizar(self):
        self.eliminarAccionesRepetidas()
            
    def eliminarAccionesRepetidas(self):
        acciones = dict()
        sustitutos = dict()
        sustituido  = False
        # lectura del archivo
        for line in self.infile:
            linelist = line.split()
            #FILTROS
            # descartamos asignaciones (mejorar filtros)
            if len(linelist) > 3:
                #obtener accion
                accion = " ".join(linelist[2:])
                sustituido = False
                
                #verificamos si hay valores sustituibles
                for val in [linelist[2],linelist[-1]]:
                    # si hay sustituir
                    if val in sustitutos:
                        val = sustitutos[val]
                        sustituido = True
                
                if sustituido:
                    # escribe linea a la que se le aplica sustitucion
                    self.outfile.write(" ".join(linelist))
                    print("Sustucion en: " + " ".join(linelist))
                    
                else:
                    #si la accion ya esta registrada 
                    if accion in acciones:
                        #añadir a sustitutos y descartar linea
                        sustitutos[linelist[0]] = acciones[accion]
                    else:
                    # asociar acciones a valor
                        acciones[accion] = linelist[0]
            else:
                self.outfile.write(line)
        print(acciones)
        print(sustitutos)
        return None 
    
    def __del__(self):
        """
            Destructor de la clase
        """
        self.infile.close()
        self.outfile.close()