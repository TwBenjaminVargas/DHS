from Contexto import Contexto
class TablaSimbolos:
    
    def __init__(self):
        self.contextos = []
    
    # Añade un contexto a la pila de contextos 
    def addContexto(self):
        contexto = Contexto()
        self.contextos.append(contexto)
        return contexto
    
    # Elimina ultimo contexto añadido a la pila
    # y lo retorna
    def delContexto(self):
        return self.contextos.pop()
    
    # Agrega un identificador al ultimo contexto de la pila
    # retorna True si lo logra
    # de lo contrario retorna False    
    def addIdentificador(self,id):
        self.contextos[-1].addIdentificador(id)
    
    # Busca identificador en el contexto actual y retorna si lo encuentra      
    def buscarLocal(self,strid):
        if strid in self.contextos[-1].tabla:
            return self.contextos[-1].tabla[strid]
        else:
            return None
        
    def buscarGlobal(self, strid):
        for contexto in reversed(self.contextos):
            if strid in contexto.tabla:
                return contexto.tabla[strid]
        return None
    
        