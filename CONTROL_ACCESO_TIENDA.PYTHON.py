import random
import time
from datetime import datetime

# -ESTA ES LA FUNCION PARA TOMARLE LOS DATOS AL CLIENTE...
def tomar_datos():
    tiene_membresia = random.choice([True, False])
    
    es_empleado = random.choice([True, False])
    hora_actual = datetime.now().hour  
    
    horario_atencion = 9 <= hora_actual < 18
    return tiene_membresia, es_empleado, horario_atencion

# -ESTA ES LA FUNCION PARA CALCULAR O PROCESAR DATOS...
def procesar_datos(tiene_membresia, es_empleado, horario_atencion):
    if (tiene_membresia and horario_atencion) or es_empleado:
        return "Acceso permitido"
    else:
        return "Acceso denegado"

#  -ESTA ES LA FUNCION PARA MOSTRAR EL RESULTADO AL CLIENTE...
def mostrar_resultado(estado_acceso, tiene_membresia, es_empleado, horario_atencion):
    print(f"Membresía válida: {tiene_membresia}")
    print(f"Empleado: {es_empleado}")
    print(f"Horario de atención (9:00 - 18:00): {horario_atencion}")
    print(f"Estado del acceso: {estado_acceso}")


# -ESTA ES LA FUNCION PARA EL BUCLE DE BIENVENIDA - REALIZACION DEL PROGRAMA - SALIR...  
def mostrar_menu():
    print("BIENBENIDO REY A NUESTRO PROGRAMA...")
    print("BIENVENIDO AL PROGRAMA DE CONTROL DE ACCESO A LA TIENDA..")
    print("INGRESE '1' PARA RESOLVER EL PROGRAMA.. ")
    print("INGRESE '2' PARA VOLVER HACER OTRO EJERCICIO ")
    print("INGRESE '3' PARA SALIR. ")

# -ESTA ES LA FUNCION PRINCIPAL PARA EL CONTROL DE ACESSO A LA TIENDA... 
def control_acceso():
    while True:
        tiene_membresia, es_empleado, horario_atencion = tomar_datos()  
        estado_acceso = procesar_datos(tiene_membresia, es_empleado, horario_atencion)  
        mostrar_resultado(estado_acceso, tiene_membresia, es_empleado, horario_atencion)  
        time.sleep(5)

def MENU():
    while True:
        print("BIENVENIDO AL SISTEMA DE CONTROL DE ACCESO A TIENDA...")
        mostrar_menu()
        opcion = input("INGRESE UNA OPCION: (1-3): ")

        if opcion == '1':
            print("INICIANDO CONTROL DE ACCESO A TIENDA..")
            control_acceso()  

        elif opcion == '2':
            print("ELEGIR OTRO EJERCICIO PARA REALIZAR..")
            
        elif opcion == '3':
            print("GRACIAS POR UTILIZAR NUESTRO PROGRAMA, FELIZ DIA!")
            break

        else:
            print("OPCION, INVALIDA INGRESE CORRECTAMENTE, PORFAVOR!")
MENU()
