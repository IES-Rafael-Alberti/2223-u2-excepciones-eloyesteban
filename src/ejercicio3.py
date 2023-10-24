""" 
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
la cuenta atrás desde ese número hasta cero separados por comas. Deberá solicitar el número 
hasta introducir uno correcto. 
"""

def cuenta_atras(numero):
    numero_str = ""
    for i in range(numero, -1, -1):
        numero_str += str(i) + ", "
    return numero_str[:-2]

if __name__=="__main__":


    #Entrada

    numCorrecto = False
    while not numCorrecto:
        try:
            numero = int(input("Introduce un número entero positivo: "))
            while numero <= 0:
                numero = int(input("Introduce un número entero positivo: "))
            numCorrecto = True
        except ValueError:
            print("Introduce numeros!!")

    #Procesar

    resultado = cuenta_atras(numero)

    #Salida

    print(resultado)