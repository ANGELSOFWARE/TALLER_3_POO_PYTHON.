# -ESTA ES LA FUNCION PARA TOMARLE LOS DATOS AL CLIENTE...
def tomar_datos():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    operacion = input("Ingrese la operación (+, -, *, /): ").strip()
    return num1, num2, operacion

# -ESTA ES LA FUNCION PARA CALCULAR O PROCESAR DATOS...
def procesar_operacion(num1, num2, operacion):
    if operacion == "+":
        return num1 + num2, None
    elif operacion == "-":
        return num1 - num2, None
    elif operacion == "*":
        return num1 * num2, None
    elif operacion == "/":
        if num2 != 0:
            return num1 / num2, None
        else:
            return None
    else:
        return None

#  -ESTA ES LA FUNCION PARA MOSTRAR EL RESULTADO AL CLIENTE...
def imprimir_resultado(resultado, mensaje=None):
    if mensaje:
        print(mensaje)
    else:
        print(f"El resultado es: {resultado}")

# -ESTA ES LA FUNCION PARA EL BUCLE DE BIENVENIDA - REALIZACION DEL PROGRAMA - SALIR... 
def mostrar_menu():
    print("BIENBENIDO REY A NUESTRO PROGRAMA...")
    print("BIENVENIDO AL PROGRAMA DE CALCULADORA...")
    print("INGRESE '1' PARA RESOLVER LA CALCULADORA. ")
    print("INGRESE '2' PARA VOLVER HACER OTRO EJERCICIO. ")
    print("INGRESE '3' PARA SALIR. ")
    

def calculadora_simple():
    while True:
        mostrar_menu()
        opcion = input("INGRESE UNA OPCION: ").strip()

        if opcion == "1":
            num1, num2, operacion = tomar_datos()
            resultado, mensaje = procesar_operacion(num1, num2, operacion)
            imprimir_resultado(resultado, mensaje)

        elif opcion == "2":
            continue

        elif opcion == "3":
            print("GRACIAS POR UTILIZAR NUESTRO PROGRAMA, FELIZ DIA!")
            exit()

        else:
           print("OPCION, INVALIDA INGRESE CORRECTAMENTE, PORFAVOR!")

calculadora_simple()
