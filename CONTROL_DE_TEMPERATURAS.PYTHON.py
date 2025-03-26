import time
import random

# -ESTA ES LA FUNCION PARA TOMARLE LOS DATOS AL CLIENTE...
def tomar_datos():
    temperatura = random.uniform(0, 50)
    return temperatura

# -ESTA ES LA FUNCION PARA CALCULAR O PROCESAR DATOS...
def procesar_datos(temperatura):
    if temperatura < 10:
        return "Calefactor activado"
    elif 10 <= temperatura <= 25:
        return "Sistema inactivo"
    else:
        return "Ventilador activado"

#  -ESTA ES LA FUNCION PARA MOSTRAR EL RESULTADO AL CLIENTE...
def mostrar_resultado(estado, temperatura):
    print(f"Temperatura actual: {temperatura:.2f}°C - Estado: {estado}")

#FUNCION PRINCIPAL PARA EL CONTROL DE TEMPERATURAS...
def control_invernadero():
    while True:
        temperatura = tomar_datos() 
        estado = procesar_datos(temperatura)  
        mostrar_resultado(estado, temperatura) 
        time.sleep(5)  

# -ESTA ES LA FUNCION PARA EL BUCLE DE BIENVENIDA - REALIZACION DEL PROGRAMA - SALIR...  
def mostrar_menu():
    print("BIENBENIDO REY A NUESTRO PROGRAMA...")
    print("BIENVENIDO AL PROGRAMA DE CONTROL DE TEMPERATURAS..")
    print("INGRESE '1' PARA RESOLVER EL PROGRAMA.. ")
    print("INGRESE '2' PARA VOLVER HACER OTRO EJERCICIO. ")
    print("INGRESE '3' PARA SALIR. ")

def MENU():
    while True:
        mostrar_menu()  
        opcion = input("INGRESE UNA OPCION: (1-3): ")

        if opcion == '1':
            print("INICIANDO CONTROL DE TEMPERATURAS...")
            control_invernadero()
        elif opcion == '2':
            continue
        elif opcion == '3':
            print("GRACIAS POR UTILIZAR NUESTRO PROGRAMA, FELIZ DIA!")
            break
        else:
            print("OPCION, INVALIDA INGRESE CORRECTAMENTE, PORFAVOR!")
MENU()
