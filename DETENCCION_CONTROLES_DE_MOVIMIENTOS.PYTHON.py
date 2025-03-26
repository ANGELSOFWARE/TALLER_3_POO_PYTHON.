import random
import time

# -ESTA ES LA FUNCION PARA TOMARLE LOS DATOS AL CLIENTE...
def tomar_datos():
    sensores = [random.choice([True, False]) for _ in range(3)]
    
    es_de_noche = random.choice([True, False])
    return sensores, es_de_noche

# -ESTA ES LA FUNCION PARA CALCULAR O PROCESAR DATOS...
def procesar_datos(sensores, es_de_noche):
    if es_de_noche and sum(sensores) >= 2:
        return True  
    else:
        return False  

#  -ESTA ES LA FUNCION PARA MOSTRAR EL RESULTADO AL CLIENTE...
def mostrar_resultado(alarma_activada, sensores, es_de_noche):
    print(f"Sensores: {sensores}")
    print(f"Es de noche: {es_de_noche}")
    if alarma_activada:
        print("¡Alarma activada! Intruso detectado.")
    else:
        print("Sistema seguro. Alarma desactivada.")

# -ESTA ES LA FUNCION PARA EL BUCLE DE BIENVENIDA - REALIZACION DEL PROGRAMA - SALIR...  
def mostrar_menu():
    print("BIENBENIDO REY A NUESTRO PROGRAMA...")
    print("BIENVENIDO AL PROGRAMA DE DETECCION DE CONTROLES DE MOVIMIENTOS..")
    print("INGRESE '1' PARA RESOLVER EL PROGRAMA.. ")
    print("INGRESE '2' PARA VOLVER HACER OTRO EJERCICIO ")
    print("INGRESE '3' PARA SALIR. ")

# -ESTA ES LA FUNCION DEL MENU DE SEGURIDAD...
def mostrar_menu_seguridad():
    print("MENU DE SEGURIDAD..")
    print("INGRESE 1 PARA ACTIVAR LA ALARMA")
    print("INGRESE 2 PARA DESACTIVAR ALARMA")
    print("INGRESE 3 PARA REGRESAR AL MENU PRINCIPAL")

def MENU():
    while True:
        print("BIENVENIDO AL SISTEMA DE SEGURIDAD..")
        mostrar_menu()
        opcion = input("INGRESE UNA OPCION: (1-3): ")

        if opcion == '1':
            alarma_activada = False
            while True:
                mostrar_menu_seguridad()
                opcion_seguridad = input("INGRESE UNA OPCION: (1-3): ")

                if opcion_seguridad == '1':
                    alarma_activada = True
                    print("ALARMA ACTIVADA, SISTEMA VIGILANDO...")
                    while alarma_activada:
                        sensores, es_de_noche = tomar_datos()  
                        alarma_activada = procesar_datos(sensores, es_de_noche) 
                        mostrar_resultado(alarma_activada, sensores, es_de_noche)  
                        time.sleep(3)

                elif opcion_seguridad == '2':
                    alarma_activada = False
                    print("ALARMA DESACTIVADA, SISTEMA NO VIGILANDO..")
                    
                elif opcion_seguridad == '3':
                    break
                else:
                    print("OPCION INVALIDA, INGRESAR DATOS VALIDOS PORFAVOR!!")
        
        elif opcion == '2':
            print("ELEGIR OTRO EJERCICIO PARA REALIZAR..")
        
        elif opcion == '3':
            print("GRACIAS POR UTILIZAR NUESTRO PROGRAMA, FELIZ DIA!")
            break
        
        else:
            print("OPCION, INVALIDA INGRESE CORRECTAMENTE, PORFAVOR!")
MENU()
