#Creadores: Gustavo López Alvarado y Mel Acuña
#Día de creación: 26/4/26
#Última modificación: 5/5/26
#Versión de Python: 3.14

#Funcion Aux de la opción 1 del menú:
def cargarTokensAux(nombre, separador):
    '''
    Funcionamiento:
    -Entrada:
        Se valida que el nombre del archivo no esté vacío y que el separador no esté vacío.
    -Salida:
        Se muestre el mensaje correspondiente si alguna de las validaciones falla o se retorna True si todas las validaciones son correctas.
    '''
    if nombre.strip()=="": #Valida si el nombre del archivo está vacío o solo tiene espacios
        return "El nombre del archivo no puede estar vacío"
    elif separador.strip()=="": #Valida si el separador está vacío o solo tiene espacios
        return "El separador no puede estar vacío"
    return True

#Funcion Aux de la opción 1 y 3 del menú:
def buscarPosicionToken(pPalabra,pTokens):
    '''
    Funcionamiento:
    -Entrada:
        Se agarra una palabra y la lista de tokens para buscar si esa palabra ya existe
        dentro de la lista.
    -Salida:
        Se retorna la posición donde se encuentra la palabra si existe.
        Si no existe, se retorna -1.
    '''
    i=0
    while i<len(pTokens):
        if pTokens[i][0].lower()==pPalabra.lower(): #Compara la palabra original del token con la palabra buscada
#El i es para agarrar las diferentes tuplas dentro de la lista y el 0 es para agarrar la palabra que se busca dentro de esa tupla
            return i #Retorna la posición donde encontró la palabra
        i+=1
    return -1 #Retorna -1 si no encontró la palabra

#Funcion Aux de la opción 2 del menú:
def mostrarTokensAux(pTokens):
    '''
    Funcionamiento:
    -Entrada:
        Se ingresa los tokens 
    -Salida:
        Si la lista de tokens es diferente de 0 se devuelve True
        Si la lista de tokens es igual a 0 se devuelve el mensaje
    '''
    if len(pTokens)==0: #Si al leer la lista es igual a 0 se muestra el mensaje
        return("No hay tokens cargados")
    return True #Si al leer la lista es diferente a 0 se devuelve True

#Funcion Aux de la opción 3 del menú:
def agregarModificarTokensAux(pToken,pSeparador):
    if pSeparador not in pToken: #Valida si el separador no está dentro del token
            return "El separador no coincide con alguno de los tokens"
    elif pSeparador=="":
        return "El separador no puede estar vacío"
    return True

#Funcion Aux de la opción 3 del menú:
def confirmarOpcion3(pOpcion):
    if pOpcion=='1':
        return True
    elif pOpcion=='0':
        print("Opción cancelada")
        return False
    else:
        print("Opción no valida")
        return False
    
#Funcion Aux de la opción 4 del menú:
def guardarTokensAux(pTokens, nombre, separador):
    '''
    Funcionamiento:
    -Entrada:
        Se valida que la lista de tokens no esté vacía, que el nombre del archivo no esté vacío y que el separador no esté vacío.
    -Salida:
        Se muestre el mensaje correspondiente si alguna de las validaciones falla o se retorna True si todas las validaciones son correctas.
    '''
    if len(pTokens)==0: #Valida si la lista de tokens está vacía
        return "No hay tokens para guardar"
    elif nombre.strip()=="": #Valida si el nombre del archivo está vacío o solo tiene espacios
        return "El nombre del archivo no puede estar vacío"
    elif separador.strip()=="": #Valida si el separador está vacío o solo tiene espacios
        return "El separador no puede estar vacío"
    i=0
    while i<len(pTokens):
        if separador in pTokens[i][0] or separador in pTokens[i][1]: #Valida si el separador está dentro de alguno de los tokens
            return "El separador no puede estar dentro de los tokens"
        i+=1
    return True

#Funcion Aux de la opción 5 del menú:
def separarLineaAux(pLinea):
    """
     Entrada:
    - Una línea que contiene un token en formato "original->nuevo".  
    Salida:
    - Lista con dos elementos: [original, nuevo] 
    """
    resultado=[]
    palabra=""
    i=0
    while i<len(pLinea):
        letra=pLinea[i]
        if letra.isalnum():
            palabra+=letra
        else:
            if palabra!="":
                resultado.append(palabra)
                palabra=""
            resultado.append(letra)
        i+=1
    if palabra!="":
        resultado.append(palabra)
    return resultado

#Funcion Aux de la opción 5 del menú:
def traducirLineaAux(linea, pTokens):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe una línea de texto (string) y la lista de tokens con formato
        (original, nuevo, contador).
    -Salida:
        Se retorna una nueva línea traducida donde las palabras que coinciden
        con los tokens son reemplazadas por su equivalente, y además se actualiza
        el contador de cada token utilizado.
   '''
    lista = separarLineaAux(linea)
    nuevaLista = []
    i = 0
    while i < len(lista):
        elemento = lista[i]
        pos = buscarPosicionToken(elemento, pTokens)
        if pos != -1:
            original, nuevo, contador = pTokens[pos]
            nuevaLista.append(nuevo)
            pTokens[pos] = (original, nuevo, contador + 1)
        else:
            nuevaLista.append(elemento)
        i += 1
    nuevaLinea = ""
    i = 0
    while i < len(nuevaLista):
        nuevaLinea += nuevaLista[i]
        i += 1
    return nuevaLinea

def CSVAux(pTokens):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la lista de tokens con formato (original, nuevo, contador).
    -Salida:
        Se retorna True o False dependiendo de si la lista de tokens es vacía o no.
    '''
    if len(pTokens)=='':
        return "No hay tokens para guardar"
    return True