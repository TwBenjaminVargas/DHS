from antlr4.error.ErrorListener import ErrorListener
import sys

class ErrorEscucha (ErrorListener):
    def __init__(self):
        super(ErrorEscucha , self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Error de sintaxis en línea {line}, columna {column}")
        sys.exit()
