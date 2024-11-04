from ID import ID

class Variable(ID):
    
    def __init__(self,tipoDato,nombre,inicializado = False,usado = False):
        self.tipoDato = tipoDato
        self.nombre = nombre
        self.inicializado = inicializado
        self.usado = usado
    def __str__(self):
            return"\n\tVariable:{}\n\tTipo:{}\n\tInicializado:{}\n\tUsado:{}".format(self.nombre,self.tipoDato,self.inicializado,self.usado)