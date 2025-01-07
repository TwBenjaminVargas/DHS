class Etiqueta:
    
    def __init__(self):
       self.index = 0
       self.lbl = list()
       self.history = list()
    
    def generateLabel(self):
        self.lbl.append(f"l{self.index}")
        self.history.append(self.lbl[-1])
        self.index += 1
        return self.lbl[-1]
    
    def getLabel(self):
        if self.lbl:
            return self.lbl.pop()
        return None