# -ESTA ES LA FUNCION PARA TOMARLE LOS DATOS AL CLIENTE...
def tomar_datos(asientos_disponibles):
    print(f"Asientos disponibles: {asientos_disponibles}")
    asiento = int(input("Ingrese el número de asiento que desea reservar (1-10): "))
    return asiento

# -ESTA ES LA FUNCION PARA CALCULAR O PROCESAR DATOS...
def procesar_reserva(asiento, asientos_reservados):
    if asiento in asientos_reservados:
        return False, "El asiento ya está reservado."
    elif 1 <= asiento <= 10:
        asientos_reservados.add(asiento)
        return True, "Reserva exitosa."
    else:
        return False, "Número de asiento inválido."
    
# -ESTA ES LA FUNCION PARA MOSTRAR EL RESULTADO AL CLIENTE...
def imprimir_resultado(exito, mensaje):
    if exito:
        print(f"¡Éxito! {mensaje}")
    else:
        print(f"Error: {mensaje}")

# -ESTA ES LA FUNCION PARA EL BUCLE DE BIENVENIDA - REALIZACION DEL PROGRAMA - SALIR...  
def mostrar_menu():
    print("BIENBENIDO REY A NUESTRO PROGRAMA...")
    print("BIENVENIDO AL PROGRAMA DE RESERVAS DE ASIENTOS..")
    print("INGRESE '1' PARA RESERVAR EL ASIENTO. ")
    print("INGRESE '2' PARA VOLVER HACER OTRO EJERCICIO DE ASIENTOS. ")
    print("INGRESE '3' PARA SALIR. ")

# -FUNCION PRINCIPAL PARA EL SISTEMA DE RESERVAS...
def sistema_reservas():
    asientos_reservados = set()
    capacidad = 10

    while True:
        mostrar_menu()
        opcion = input("INGRESE UNA OPCION: ")

        if opcion == "1":
            asiento = tomar_datos(capacidad - len(asientos_reservados))
            exito, mensaje = procesar_reserva(asiento, asientos_reservados)
            imprimir_resultado(exito, mensaje)

            if len(asientos_reservados) == capacidad:
                print("TODOS LOS ASIENTOS ESTAN RESERVADOS...")
                break

        elif opcion == "2":
            continue

        elif opcion == "3":
            print("GRACIAS POR UTILIZAR NUESTRO PROGRAMA, FELIZ DIA!")
            exit()

        else:
            print("OPCION, INVALIDA INGRESE CORRECTAMENTE, PORFAVOR!")

sistema_reservas()
