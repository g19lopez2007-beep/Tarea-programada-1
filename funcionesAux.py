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
        if pTokens[i][0]==pPalabra: #Compara la palabra original del token con la palabra buscada
#El i es para agarrar las diferentes tuplas dentro de la lista y el 0 es para agarrar la palabra que se busca dentro de esa tupla
            return i #Retorna la posición donde encontró la palabra
        i+=1
    return -1 #Retorna -1 si no encontró la palabra

def agregarModificarTokensAux(pToken,pSeparador):
    if pSeparador not in pToken: #Valida si el separador no está dentro del token
            return "El separador no coindice con alguno de los tokens"
    elif pSeparador=="":
        return "El separador no puede estar vacío"
    return True