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