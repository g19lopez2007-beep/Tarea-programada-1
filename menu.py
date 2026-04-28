#Creadores: Gustavo López Alvarado y Mel Acuña
#Día de creación: 26/4/26
#Última modificación: 26/4/26
#Versión de Python: 3.14

from funciones import *
from funcionesAux import confirmarOpcion3

def submenuBitacora():
    '''
    Funcionamiento:
    -Entrada:
        El usuario ingresa un número
        1 = sirve para elegir la opción de buscar por acciones por día escogido
        2 = sirve para elegir la opción de buscar por acciones por palabra clave
        3 = para salir del submenú
    -Salida:
        Se muestra el resultado de la opción que se eligiera
    '''
    while True:
        print("\n===== BITÁCORA =====")
        print("1. Acciones por día escogido")
        print("2. Acciones por palabra clave")
        print("3. Salir del submenú")
        opcion=input("Digite una opción: ")
        if opcion=="1": #Si la opción es 1 se muestra el resultado de buscarBitacoraPorDia
            print("Aquí debe llamar buscarBitacoraPorDia()")
        elif opcion=="2": #Si la opción es 2 se muestra el resultado de buscarBitacoraPorPalabra
            print("Aquí debe llamar buscarBitacoraPorPalabra()")
        elif opcion=="3": #Si la opción es 3 se sale del menú
            break
        else:
            print("Opción inválida")

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
            print("Aquí debe llamar la función cargarTokens()")
        elif opcion=="2":
            mostrarTokens(tokens)
        elif opcion=="3":
            cadena=input("Digite los tokens: ")
            separador=input("Digite el separador usado: ")
            validar=input('Desea continuar? 1=Si, 0=No: ')
            if confirmarOpcion3(validar)==True:
                tokens=agregarModificarTokens(tokens,cadena,separador)
        elif opcion=="4":
            print("Aquí debe llamar la función guardarTokens()")
        elif opcion=="5":
            print("Aquí debe llamar la función traducirCodigo()")
        elif opcion=="6":
            print("Aquí debe llamar la función generarCSV()")
        elif opcion=="7":
            print("Aquí debe llamar la función generarHTML()")
        elif opcion=="8":
            submenuBitacora()
        elif opcion=="9":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida")
menu()