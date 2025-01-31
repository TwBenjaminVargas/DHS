from antlr4.error.ErrorListener import ErrorListener
import sys

class ErrorEscucha (ErrorListener):

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        
        err = "- " + f"\033[31mError de sintaxis en línea {line}, columna {column} \033[0m"
        
        if "missing" in msg:
            err += f"\033[31m: Se esperaba '{msg[msg.find("'") + 1]}'\033[0m"
        if "extraneous" in msg:
            err += f"\033[31m: Simbolo extraño'{msg[msg.find("'") + 1]}'\033[0m"
        if "no viable alternative at input" in msg:
            pos = msg.find("'") + 1
            err += f"\033[31m: Compilador no reconoce '{msg[pos:msg.find("'",pos)]}'\033[0m"
        
        print(err)
        sys.exit()