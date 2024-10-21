import ID
class Contexto:
    def __init__(self):
        self.tabla = {}
    
    # Añade un identificador al contexto
    # retorna True si lo logra
    # de lo contrario retorna False
    def addIdentificador(self,id :ID):
        if not id.nombre in self.tabla:
            self.tabla[id.nombre] = id
            return True
        else:
            return False