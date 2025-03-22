# -ESTA ES LA FUNCION PARA TOMARLE LOS DATOS AL CLIENTE...
def tomar_datos():
    print("INGRESE LA OPCION DE CONVERCION:")
    print("INGRESE '1' PARA CONVERTIR DE CELSIUS A FAHRENHEIT: ")
    print("INGRESE '2' PARA CONVERTIR DE FAHRENHEIT A CELSIUS: ")
    opcion = input("SELECCIONE '1' o '2': ")
    
    temperatura=float(input("Ingrese la temperatura: "))
    return opcion, temperatura

# -ESTA ES LA FUNCION PARA CALCULAR O PROCESAR DATOS...
def convertir_temperatura(opcion, temperatura):
    if opcion == '1':
        fahrenheit = (temperatura * 9/5) + 32
        return fahrenheit
    
    elif opcion == '2':
        celsius = (temperatura - 32) * 5/9
        return celsius
    else:
        print("OPERACION, INVALIDA...")

# -ESTA ES LA FUNCION PARA MOSTRAR EL RESULTADO AL CLIENTE...
def muestro_resultado(opcion, resultado):
        if opcion == '1':
            print(f"LA TEMPERATURA CONVERTIDA ES: {resultado}° FAHRENHEIT...")
        elif opcion == '2':
            print(f"LA TEMPERATURA CONVERTIDA ES: {resultado}° CELSIUS...")

# -ESTA ES LA FUNCION PARA EL BUCLE DE BIENVENIDA - REALIZACION DEL PROGRAMA - SALIR...
def menu():
    print("BIENVENIDO AL PROGRAMA REY.")
    print("INGRESE '1' PARA CONVERTIR CELSIUS A FAHRENHEIT...")
    print("INGRESE '2' PARA CONVERTIR FAHRENHEIT A CELSIUS...")
    print("INGRESE '3' PARA VOLVER HACER OTRO EJERCICIO...")
    print("INGRESE '4'PARA SALIR...")
    
def OPCION():
    while True:
        menu()  
        opcion=input("Seleccione una opción: ")

        if opcion == '1' or opcion == '2': 
            opcion_conversion, temperatura = tomar_datos()  
            resultado = convertir_temperatura(opcion_conversion, temperatura)  
            muestro_resultado(opcion_conversion, resultado)  

        elif opcion == '3':
            continue
        
        elif opcion == '4':  
            print("¡GRACIAS PARA UTILIZAR NUESTRO PROGRAMA, FELIZ DIA...")
            break  
        else:
            print("OPCION INVALIDA, PORRFAVOR INGRESAR DATOS VALIDOS, INGRESADOS EN EL SISTEMA. GRACIASS...")
OPCION()
