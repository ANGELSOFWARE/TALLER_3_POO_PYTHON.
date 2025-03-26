import random
import time

# -ESTA ES LA FUNCION PARA TOMARLE LOS DATOS AL CLIENTE...
def tomar_datos():
    temperatura = random.uniform(20, 35)
    
    humedad = random.uniform(40, 80) 
    return temperatura, humedad

# -ESTA ES LA FUNCION PARA CALCULAR O PROCESAR DATOS...
def procesar_datos(temperatura, humedad):
    if (temperatura > 28 and humedad > 60) or temperatura > 30:
        return "Aire acondicionado encendido"
    else:
        return "Aire acondicionado apagado"

#  -ESTA ES LA FUNCION PARA MOSTRAR EL RESULTADO AL CLIENTE...
def mostrar_resultado(estado_ac, temperatura, humedad):
    print(f"Temperatura: {temperatura:.2f}°C")
    print(f"Humedad: {humedad:.2f}%")
    print(f"Estado del aire acondicionado: {estado_ac}")

# -ESTA ES LA FUNCION PARA EL BUCLE DE BIENVENIDA - REALIZACION DEL PROGRAMA - SALIR...  
def mostrar_menu():
    print("BIENBENIDO REY A NUESTRO PROGRAMA...")
    print("BIENVENIDO AL PROGRAMA DE CONTROL DE AIRE ACONDICIONADO..")
    print("INGRESE '1' PARA RESOLVER EL PROGRAMA.. ")
    print("INGRESE '2' PARA VOLVER HACER OTRO EJERCICIO ")
    print("INGRESE '3' PARA SALIR. ")

# -ESTA ES LA FUNCION PRINCIPAL DEL CONTROL DEL AIRE ACONDICIONADO...
def control_aire_acondicionado():
    while True:
        temperatura, humedad = tomar_datos()  
        estado_ac = procesar_datos(temperatura, humedad) 
        mostrar_resultado(estado_ac, temperatura, humedad)  
        time.sleep(10)

def MENU():
    while True:
        print("BIENVENIDO AL SISTEMA DE CONTROL DE AIRE ACONDICIONADO...")
        mostrar_menu()
        opcion = input("INGRESE UNA OPCION: (1-3): ")

        if opcion == '1':
            print("INICIANDO CONTROL DEL AIRE ACONDICIONADO..")
            control_aire_acondicionado()

        elif opcion == '2':
            print("ELEGIR OTRO EJERCICIO PARA REALIZAR..")

        elif opcion == '3':
            print("GRACIAS POR UTILIZAR NUESTRO PROGRAMA, FELIZ DIA!")
            break

        else:
            print("OPCION, INVALIDA INGRESE CORRECTAMENTE, PORFAVOR!")
MENU()
