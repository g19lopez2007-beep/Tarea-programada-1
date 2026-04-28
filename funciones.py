from funcionesAux import mostrarTokensAux, buscarPosicionToken, agregarModificarTokensAux

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

def agregarModificarTokens(pTokens,pPartes,pSeparador):
    '''
    Funcionamiento:
    -Entrada:
        Se agarra la lista de tokens, una cadena con los tokens que el usuario quiere
        agregar o modificar y el separador usado para dividir la palabra original
        del reemplazo.
    -Salida:
        Se muestra si el token fue agregado, actualizado o si ocurrió algún error.
        Además, se retorna la lista de tokens actualizada.
    '''
    partes=pPartes.split(" ")  #Separa la cadena ingresada con espacio
    i=0 #Contador para recorrer cada token separado
    while i<len(partes):
        token=partes[i].strip() #Guarda un token individual y elimina espacios al inicio y al final
        validacion=agregarModificarTokensAux(token,pSeparador) #Guarda el resultado del Aux
        if validacion!=True: 
            print(validacion)
            return pTokens #Retorna la lista sin cambios para evitar perder los tokens
        elif pSeparador in token:
            datos=token.split(pSeparador) #Separa el token en palabra original y reemplazo
            if len(datos)==2: #Valida que existan exactamente dos partes
                original=datos[0].strip()  #Guarda la palabra original sin espacios extra
                nuevo=datos[1].strip() #Guarda el nuevo reemplazo sin espacios extra
                posicion=buscarPosicionToken(original,pTokens) #Busca si la palabra original ya existe
                if posicion!=-1: #Si la posición es diferente de -1, significa que el token ya existe
                        pTokens[posicion]=(original,nuevo)
                        print("Token actualizado:",original)
                else:
                    pTokens.append((original,nuevo))  #Agrega el token nuevo como una tupla
                    print("Token agregado:",original)
        i+=1 #Avanza al siguiente token ingresado
    return pTokens #Retorna la lista con los cambios realizados