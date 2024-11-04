import ID
class Contexto:
    def __init__(self):
        self.tabla = {}
    
    # Añade un identificador al contexto
    # retorna True si lo logra
    # de lo contrario retorna False
    def addIdentificador(self,id :ID):
        self.tabla[id.nombre] = id
    
    def __str__(self):
        str = ""
        for strid in self.tabla:
            str=str + "\n" + self.tabla[strid].__str__()
        return str