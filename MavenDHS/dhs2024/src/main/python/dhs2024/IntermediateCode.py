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
    
    def showCodeStatus(self):
        """
            Retorna el contenido actual del archivo
        """
        return self.cod
        
    def __del__(self):
        """
            Destructor de la clase
        """
        self.file.close()