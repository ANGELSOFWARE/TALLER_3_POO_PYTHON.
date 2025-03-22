# -ESTA ES LA FUNCION PARA TOMARLE LOS DATOS AL CLIENTE...
def tomar_datos():
    NMERO1 = int(input("DIGITE UN NUMERO:  "))
    return NMERO1

# -ESTA ES LA FUNCION PARA CALCULAR O PROCESAR DATOS...
def es_par(numero):
    if numero % 2 == 0:
        return True  
    else:
        return False 

# -ESTA ES LA FUNCION PARA MOSTRAR EL RESULTADO AL CLIENTE...
def muestro_el_resultado(es_par):
    if es_par:
        print("EL NUMERO INGRESADO ES PAR.")
    else:
        print("EL NUMERO INGRESADO ES IMPAR.")

# -ESTA ES LA FUNCION PARA EL BUCLE DE BIENVENIDA - REALIZACION DEL PROGRAMA - SALIR...
def menu():
    print("BIENVENIDO REY AL PROGRAMA...")
    print("INGRESE '1' PARA VERIFICAR SI ES 'PAR' O 'IMPAR'.  ")
    print("INGRESE '2' PARA SALIR. ")


def OPCION():
    while True:
        menu()  
        opcion = input("Seleccione una opción: ")

        if opcion == '1':  
            numero = tomar_datos()  
            resultado = es_par(numero)  
            muestro_el_resultado(resultado)  
        elif opcion == '2':  
            print("GRACIAS POR UTILIZAR NUESTRO PROGRAMA, FELIZ DIA...")
            break  
        else:
            print("ERROR, INVALIDA POR FAVOR INGRESE OPCION VALIDA SOLICITADA EN EL SISTEMA... ")
OPCION()