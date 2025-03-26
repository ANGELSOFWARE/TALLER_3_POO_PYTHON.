# -ESTA ES LA FUNCION PARA TOMARLE LOS DATOS AL CLIENTE...
def tomar_datos():
    print("EL JUEGO FIZZBUZZ COMENZO:")
    return None

# -ESTA ES LA FUNCION PARA CALCULAR O PROCESAR DATOS...
def procesar_fizzbuzz():
    resultados = []
    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            resultados.append("FizzBuzz")
        elif numero % 3 == 0:
            resultados.append("Fizz")
        elif numero % 5 == 0:
            resultados.append("Buzz")
        else:
            resultados.append(str(numero))
    return resultados

# -ESTA ES LA FUNCION PARA MOSTRAR EL RESULTADO AL CLIENTE...
def imprimir_resultados(resultados):
    for resultado in resultados:
        print(resultado)

# -ESTA ES LA FUNCION PARA EL BUCLE DE BIENVENIDA - REALIZACION DEL PROGRAMA - SALIR... 
def mostrar_menu():
    print("BIENBENIDO REY A NUESTRO PROGRAMA...")
    print("BIENVENIDO AL PROGRAMA DE JUEGO FIZZBUZZ...")
    print("INGRESE '1' PARA EMPESAR JUEGO. ")
    print("INGRESE '2' PARA VOLVER HACER OTRO EJERCICIO. ")
    print("INGRESE '3' PARA SALIR. ")

# -FUNCION PRINCIPAL PARA EL JUEGO FIZZBUZZ...
def juego_fizzbuzz():
    while True:
        mostrar_menu()
        opcion = input("INGRESE UNA OPCION: ")

        if opcion == "1":
            tomar_datos()
            resultados = procesar_fizzbuzz()
            imprimir_resultados(resultados)

        elif opcion == "2":
            continue

        elif opcion == "3":
            print("GRACIAS POR UTILIZAR NUESTRO PROGRAMA, FELIZ DIA!")
            break

        else:
            print("OPCION, INVALIDA INGRESE CORRECTAMENTE, PORFAVOR!")

juego_fizzbuzz()
