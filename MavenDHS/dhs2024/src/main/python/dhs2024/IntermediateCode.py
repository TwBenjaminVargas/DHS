"""
    Clase encargada de la creacion y gestion de codigo intermedio
"""
class IntermediateCode():
    
    def __init__(self,route):
        self.file = open(route, 'w+')
        self.cod = ""
    
    def addLine(self,line:str):
        """
            Añade una linea al archivo
        """
        self.cod += line + "\n"
        self.file.write(line + "\n")
        
    def separateBlock(self):
        if not self.cod.endswith("\n\n") and not self.file.tell() == 0:
            self.cod +="\n"
            self.file.write("\n")
    
    def showCodeStatus(self):
        """
            Retorna el contenido actual del archivo
        """
        return self.cod
    
    def closeCode(self):
        """
            Cierra el archivo de codigo
        """
        self.file.close()
        
    def __del__(self):
        """
            Destructor de la clase
        """
        self.file.close()