class Temporales:
    
    def __init__(self):
       self.index = 0
       self.tmp = list()
    
    def generateTemp(self):
        """
        Añade una variable temporal a la pila 
        """
        self.tmp.append(f"t{self.index}")
        self.index += 1
        return self.tmp[-1]
    
    def isEmpty(self):
        if not self.tmp:
            return True
    def getTop(self):
        return self.tmp[-1]
    
    def getPrevTop(self):
        return self.tmp[-2]