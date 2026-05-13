#Creadores: Gustavo López Alvarado y Mel Acuña
#Día de creación: 26/4/26
#Última modificación: 12/5/26
#Versión de Python: 3.14

from funcionesAux import *
import csv

#Funcion de la opción 1:
def cargarTokens(pTokens, nombre, separador):
    '''
    Funcionamiento:
    -Entrada:
        Se agarra la lista de tokens para cargar los tokens desde un archivo de texto
    -Salida:
        Se muestra un mensaje indicando que los tokens fueron cargados exitosamente
    '''
    if cargarTokensAux(nombre, separador)!=True:
        print(cargarTokensAux(nombre, separador))
        return pTokens #Retorna la lista sin cambios para evitar perder los tokens
    try:
        archivo=open(nombre, "r") #Abre el archivo en modo lectura
    except FileNotFoundError:
        print("Archivo no encontrado")
        return pTokens #Retorna la lista sin cambios para evitar perder los tokens
    nuevaLista=[] #Crea una nueva lista para almacenar los tokens cargados
    for linea in archivo: #Recorre cada línea del archivo
        linea=linea.strip() #Elimina espacios al inicio y al final de la línea
        if separador in linea:
            partes=linea.split(separador) #Separa la línea en palabra original y reemplazo
            if len(partes)==2: #Valida que existan exactamente dos partes
                original=partes[0].strip().lower() #Guarda la palabra original sin espacios extra
                nuevo=partes[1].strip().lower() #Guarda el nuevo reemplazo sin espacios extra
                posicion=buscarPosicionToken(original,pTokens) #Busca si la palabra original ya existe
                if posicion!=-1: #Si la posición es diferente de -1, significa que el token ya existe
                    _, _, contador = pTokens[posicion] #Lo que hace es una funcion que hace que no se tomen los otros 2 elementos de la tupla y solo se use el contador
                    pTokens[posicion]=(original,nuevo,contador+1) #Actualiza el token existente con el nuevo reemplazo y aumenta el contador
                    print("Token actualizado:",original)
                else:
                    pTokens.append((original,nuevo,1)) #Agrega el token nuevo como una tupla
                    print("Token agregado:",original)
    archivo.close() #Cierra el archivo después de leerlo
    return pTokens #Retorna los tokens cargados

#Funcion de la opción 2:
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
        print("\nTokens cargados:")
        i=0
        while i<len(pTokens): 
#Se agarra el primer elemento de la lista y luego se muesta el primer elemento de la tupla y se separa con el simbolo de "->" para poner el segundo elemento de la tupla
            print(pTokens[i][0],"=",pTokens[i][1])
            i+=1

#Funcion de la opción 3:
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
                        _, _, contador = pTokens[posicion] #Lo que hace es una funcion que hace que no se tomen los otros 2 elementos de la tupla y solo se use el contador
                        pTokens[posicion]=(original,nuevo,contador+1) #Actualiza el token existente con el nuevo reemplazo y aumenta el contador
                        print("Token actualizado:",original)
                else:
                    pTokens.append((original,nuevo,1)) #Agrega el token nuevo como una tupla
                    print("Token agregado:",original)
        i+=1 #Avanza al siguiente token ingresado
    return pTokens #Retorna la lista con los cambios realizados

#Funcion de la opción 4:
def guardarTokens(pTokens, nombre, separador):
    '''
    Funcionamiento:
    -Entrada:
        Se agarra la lista de tokens para guardarlos en un archivo de texto
    -Salida:
        Se muestra un mensaje indicando que los tokens fueron guardados exitosamente
        o si ocurrió algún error.
    '''
    if guardarTokensAux(pTokens, nombre, separador)!=True:
        print(guardarTokensAux(pTokens, nombre, separador))
        return pTokens #Retorna la lista sin cambios para evitar perder los tokens
    with open(nombre, "w") as archivo: #Abre el archivo en modo escritura
            for token in pTokens: #Recorre cada token en la lista
                linea=token[0] + separador + token[1] + "\n" #Crea una línea con el formato "original->nuevo"
                archivo.write(linea) #Escribe la línea en el archivo
    print("Tokens guardados")

# Funcionalida 5: Traducir código
def traducirArchivo(nombreEntrada, nombreSalida, pTokens):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe el nombre del archivo de entrada, el nombre del archivo de salida
        y la lista de tokens con formato (original, nuevo, contador).
    -Salida:
        Se genera un nuevo archivo con el contenido traducido utilizando los tokens,
        procesando el archivo línea por línea.
    '''
    validacion=tokensAux(pTokens)
    if validacion!=True:
        print(validacion)
    try:
        entrada = open(nombreEntrada, "r")
        salida = open(nombreSalida, "w")
    except FileNotFoundError:
        print("Error al abrir los archivos")
        return
    linea = entrada.readline()
    while linea != "":
        nuevaLinea = traducirLineaAux(linea, pTokens)
        salida.write(nuevaLinea)
        linea = entrada.readline()
    entrada.close()
    salida.close()
    print("Archivo traducido correctamente")

#Funcion de la opción 6:
def guardarCSV(pTokens):
    '''
    Funcionamiwento:
    -Entrada:
        Se agarra la lista de tokens para guardarlos en un archivo CSV
    -Salida:
        En base a la lista de tokens se crea el CSV donde se agrega la ultima versión de cada token, y el contador de cuántas veces se ha actualizado cada token.
    '''
    validacion=tokensAux(pTokens)
    if validacion!=True:
        print(validacion)
        return pTokens #Retorna la lista sin cambios para evitar perder los tokens
    with open("tokens.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["La distribución es: Original, Token, Contador"])  #Escribe la cabecera del CSV
        for original, nuevo, contador in pTokens: #Crea el como se tiene que ver
            fila = f"{original}={nuevo}({contador})"
            writer.writerow([fila])
    print("El archivo CSV fue generado correctamente")

#Funcion de la opción 7:
def generarHTML(pTokens):
    '''
    Funcionamiento:
    -Entrada:
        Lista de tokens (original, nuevo, contador)
    -Salida:
        Se genera un archivo HTML con una tabla que muestra los tokens
    '''
    validacion=tokensAux(pTokens)
    if validacion!=True:
        print(validacion)
        return pTokens
    try:
        with open("reporte.html", "w", encoding="utf-8") as file:
            file.write("<html>\n")
            file.write("<head>\n")
            file.write("<title>Reporte de Tokens</title>\n")
            file.write("</head>\n")
            file.write("<body>\n")
            file.write("<h1>Reporte de Tokens</h1>\n")
            file.write("<table border='1'>\n")
            file.write("<tr><th>Original</th><th>Token</th><th>Contador</th></tr>\n")
            for original, nuevo, contador in pTokens:
                file.write("<tr>")
                file.write(f"<td>{original}</td>")
                file.write(f"<td>{nuevo}</td>")
                file.write(f"<td>{contador}</td>")
                file.write("</tr>\n")
            file.write("</table>\n")
            file.write("</body>\n")
            file.write("</html>\n")
        print("Archivo HTML generado correctamente")
    except:
        print("Error al generar el HTML")

#Funciones de la opcion 8

def guardarBitacora(mensaje):
    '''
    Funcionamiento:
    -Entrada: 
        Se recibe un mensaje con la acción realizada.
    -Salida: 
        Se guarda el mensaje en el archivo bitácora.
    '''
    archivo = open("bitacora.txt", "a")
    archivo.write(mensaje + "\n")
    archivo.close()
    print("Mensaje guardado en la bitácora")

def bitacoraPorDia():
    '''
    Funcionamiento:
    -Entrada: 
        Se recibe una fecha ingresada por el usuario.
    -Salida: 
        Se muestran las acciones registradas en esa fecha.
    '''
    fechaBuscada = input("Ingrese la fecha (YYYY-MM-DD): ")
    try:
        archivo = open("bitacora.txt", "r", encoding="utf-8")
        encontrado = False
        for linea in archivo:
            if fechaBuscada in linea:
                print(linea.strip())
                encontrado = True
        if encontrado == False:
            print("No hay acciones registradas para esa fecha")
        archivo.close()
    except:
        print("Error al leer la bitácora")

def bitacoraPorPalabra():
    '''
    Funcionamiento:
    -Entrada:
        Se recibe una palabra clave ingresada por el usuario.
    -Salida:
        Se muestran las acciones que contienen esa palabra.
    '''
    palabra = input("Ingrese palabra clave: ").lower()
    try:
        archivo = open("bitacora.txt", "r", encoding="utf-8")
        encontrado = False
        for linea in archivo:
            if palabra in linea.lower():
                print(linea.strip())
                encontrado = True
        if encontrado == False:
            print("No se encontraron coincidencias")

        archivo.close()
    except:
        print("Error al leer la bitácora")