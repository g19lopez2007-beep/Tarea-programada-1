from funcionesAux import mostrarTokensAux

def mostrarTokens(pTokens):
    '''
    Funcionamiento:
    -Entrada:
        Se agarra la lita de tokens para mostrar los resultados ya guardados
    -Salida:
        Se muestra la lista de tokens
    '''
    resultado=mostrarTokensAux(pTokens)
    if resultado!=True: #Mientras que el resultado sea diferente de True se imprime el mensaje
        print(resultado)
    else:
        print("Tokens cargados:")
        i=0
        while i<len(pTokens): 
#Se agarra el primer elemento de la lista y luego se muesta el primer elemento de la tupla y se separa con el simbolo de "->" para poner el segundo elemento de la tupla
            print(pTokens[i][0], "->", pTokens[i][1])
            i+=1