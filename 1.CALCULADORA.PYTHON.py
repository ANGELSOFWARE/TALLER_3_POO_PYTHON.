# -ESTA ES LA FUNCION PARA TOMARLE LOS DATOS AL CLIENTE...
def tomar_Numero1():
    NMERO1=int(input("Digite un numero"))
    return NMERO1

def tomar_Numero2():
    NMERO2=int(input("Digite el  numero"))
    return NMERO2

# -ESTA ES LA FUNCION PARA CALCULAR O PROCESAR DATOS...
def procesarDatos(opcion):
    match opcion:
            case "A":
                auxnum1= tomar_Numero1()
                auxnum2= tomar_Numero2()
                
                auxresultado=hacerSuma(auxnum1,auxnum2)
                imprimirResultado(auxresultado)
                
            case "B":
                auxnum1= tomar_Numero1()
                auxnum2= tomar_Numero2()
                
                auxresultado=hacerResta(auxnum1,auxnum2)
                imprimirResultado(auxresultado)
                
            case "C":
                auxnum1= tomar_Numero1()
                auxnum2= tomar_Numero2()
                
                auxresultado=hacermMultipli(auxnum1,auxnum2)
                imprimirResultado(auxresultado)
                
            case "D":
                auxnum1= tomar_Numero1()
                auxnum2= tomar_Numero2()
                
                auxresultado=hacerDivi(auxnum1,auxnum2)
                imprimirResultado(auxresultado)
        
            case "X":
                print("GRACIAS POR UTILIZAR NUESTRO PROGRAMA, FELIZ DIA...")
                
def imprimirResultado(auxresultado):
    print(f"El resultado es {auxresultado: f} ")

def hacerSuma(num1, num2):
    resultado= num1 + num2 
    return resultado
    
def hacerResta(num1, num2):
    resultado= num1 - num2 
    return resultado
    
def hacermMultipli(num1, num2):
    resultado= num1 * num2 
    return resultado
    
def hacerDivi(num1, num2):
    resultado= num1 / num2 
    return resultado


# -ESTA ES LA FUNCION PARA EL BUCLE DE BIENVENIDA - REALIZACION DEL PROGRAMA - SALIR...            
def mostrarMenu():
    print("BIENVENIDO AL PROGRAMA REY ")
    print("INGRESE 'A' PARA SUMAR")            
    print("INGRESE 'B' PARA RESTAR")
    print("INGRESE 'C' PARA MULTIPLICAR")
    print("INGRESE 'D' PARA DIVIDIR")
    print("INGRESE 'X' PARA SALIR...")
    opcion=input()
    return opcion
    
# -ESTA ES LA FUNCION PARA MOSTRAR EL RESULTADO AL CLIENTE...
while True:
    RESULTADO_OPCION=mostrarMenu()
    procesarDatos(RESULTADO_OPCION)
    if RESULTADO_OPCION=="X":
       break