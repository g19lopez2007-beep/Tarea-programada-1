#Creadores: Gustavo López Alvarado y Mel Acuña
#Día de creación: 26/4/26
#Última modificación: 08/05/26
#Versión de Python: 3.14

from funciones import *
from funcionesAux import confirmarOpcion3



def menu():
    '''
    Funcionamiento:
    -Entrada:
        El usuario escoge la opción que necesite
    -Salida:
        Se muestra el resultado de la opción que el usuario eligió
    '''
    tokens=[] #Aquí se guarda la lista de tokens
    while True:
        print("\n===== TRADUCTOR DE TOKENS =====")
        print("1. Cargar tokens")
        print("2. Mostrar tokens")
        print("3. Agregar/modificar token")
        print("4. Guardar tokens")
        print("5. Traducir código")
        print("6. Generar reporte CSV")
        print("7. Generar reporte HTML")
        print("8. Submenú de bitácora")
        print("9. Salir")
        opcion=input("Seleccione una opción: ")
        if opcion=="1":
            nombre=input("Por favor ingrese el nombre del archivo para cargar los tokens: ")
            separador=input("Por favor ingrese el separador usado para cargar los tokens: ")
            tokens=cargarTokens(tokens, nombre, separador)
        elif opcion=="2":
            mostrarTokens(tokens)
        elif opcion=="3":
            cadena=input("Digite los tokens: ")
            separador=input("Digite el separador usado: ")
            validar=input("Desea continuar? 1=Si, 0=No: ")
            if confirmarOpcion3(validar)==True:
                tokens=agregarModificarTokens(tokens,cadena,separador)
        elif opcion=="4":
            nombre=input("Por favor ingrese el nombre del archivo para guardar los tokens: ")
            separador=input("Por favor ingrese el separador usado para guardar los tokens: ")
            guardarTokens(tokens, nombre, separador)
        elif opcion=="5":
            print("Aquí debe llamar la función traducirCodigo()")
        elif opcion=="6":
            guardarCSV(tokens)
        elif opcion=="7":
            generarHTML(tokens)
        elif opcion=="8":
            submenuBitacora()
        elif opcion=="9":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida")
menu()

def submenuBitacora():
    '''
    Funcionamiento:
    -Entrada:
        El usuario selecciona una opción del submenú.
    -Salida:
        Se ejecutan las funciones de búsqueda de bitácora.
    '''

    opcion = ""

    while opcion != "0":

        print("\n===== BITÁCORA =====")
        print("1. Acciones por día escogido")
        print("2. Acciones por palabra clave")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            bitacoraPorDia()

        elif opcion == "2":
            bitacoraPorPalabra()

        elif opcion == "0":
            print("Saliendo de bitácora")
            break

        else:
            print("Opción inválida")