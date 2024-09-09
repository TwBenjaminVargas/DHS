#Mejoras en codigo y verificaciones
#Convierte string en flotante y lo agrega a la lista
def appendFloat(flstr, tjtlist):
    try:
        num = float(flstr)
    except ValueError:
        num = None
    tjtlist.append(num)
        
#Devuelve una lista con los datos de la linea
def processLine(linestr):
    data = [linestr[:8]]
    appendFloat(linestr[8:14],data)
    appendFloat(linestr[14:20],data)
    data.append(linestr[20:].strip())
    return data
try:
    file = open ("registro_temperatura365d_smn.txt", "r")
    registros = file.readlines()
except FileNotFoundError:
    print("Archivo no encontrado")
    exit()
file.close()

diccionario = dict()
for l in registros[3:-1]:
    data = processLine(l)
    if data[-1] in diccionario.keys(): # si la clave esta en el diccionario
        diccionario[data[-1]]["tmax"].append(data[1])
        diccionario[data[-1]]["tmin"].append(data[2])  
    else: #clave no esta en el diccionario
        temp = {"tmax":[data[1]],
                    "tmin":[data[2]]}
        item = {data[-1]: temp}
        diccionario.update(item)
    
try:
    print(diccionario["AEROPARQUE AERO"]["tmax"][0])
except KeyError:
    print("clave ingresada es invalida")