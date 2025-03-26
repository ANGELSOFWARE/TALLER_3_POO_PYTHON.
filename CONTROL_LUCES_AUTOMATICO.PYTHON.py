import random
import time

# -ESTA ES LA FUNCION PARA TOMARLE LOS DATOS AL CLIENTE...
def tomar_datos():
    es_de_noche = random.choice([True, False])
    
    hay_movimiento = random.choice([True, False])
    return es_de_noche, hay_movimiento

# -ESTA ES LA FUNCION PARA CALCULAR O PROCESAR DATOS...
def procesar_datos(es_de_noche, hay_movimiento):
    if es_de_noche and hay_movimiento:
        return "Luces encendidas"
    else:
        return "Luces apagadas"

#  -ESTA ES LA FUNCION PARA MOSTRAR EL RESULTADO AL CLIENTE...
def mostrar_resultado(estado_luces, es_de_noche, hay_movimiento):
    print(f"\nEs de noche: {es_de_noche}")
    print(f"Movimiento detectado: {hay_movimiento}")
    print(f"Estado de las luces: {estado_luces}")

# -ESTA ES LA FUNCION PARA EL BUCLE DE BIENVENIDA - REALIZACION DEL PROGRAMA - SALIR...  
def mostrar_menu():
    print("BIENBENIDO REY A NUESTRO PROGRAMA...")
    print("BIENVENIDO AL PROGRAMA DE CONTROL DE LUCES AUTOMATICO..")
    print("INGRESE '1' PARA RESOLVER EL PROGRAMA.. ")
    print("INGRESE '2' PARA VOLVER HACER OTRO EJERCICIO ")
    print("INGRESE '3' PARA SALIR. ")

# -ESTA ES LA FUNCION PRINCIPAL DE CONTROL DE LUCES...
def control_luces():
    while True:
        es_de_noche, hay_movimiento = tomar_datos()
        estado_luces = procesar_datos(es_de_noche, hay_movimiento) 
        mostrar_resultado(estado_luces, es_de_noche, hay_movimiento) 
        time.sleep(10) 

def MENU():
    while True:
        print("BIENVENIDO AL SISTEMA DE LUCES AUTOMATICAS...")
        mostrar_menu()
        opcion = input("INGRESE UNA OPCION: (1-3): ")

        if opcion == '1':
            print("INICIANDO EL CONTROL DE LUCES AUTOMATICAS..")
            control_luces() 

        elif opcion == '2':
            print("ELEGIR OTRO EJERCICIO PARA REALIZAR..")

        elif opcion == '3':
            print("GRACIAS POR UTILIZAR NUESTRO PROGRAMA, FELIZ DIA!")
            break

        else:
            print("OPCION, INVALIDA INGRESE CORRECTAMENTE, PORFAVOR!")
MENU()
