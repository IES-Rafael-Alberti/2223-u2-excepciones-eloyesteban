"""
 Escribe un programa que capture la excepción división entre cero. Tendrá que mostar el 
 mensaje del error capturado. 
"""

def division(dividendo,divisor):
    resultado = dividendo/divisor
    return resultado

if __name__ == "__main__": 

    numCorrecto = False

    while not numCorrecto:
        try:
            dividendo = int(input("Introduce el dividendo: "))
            divisor = int(input("Introdcue el divisor: ")) 
            cociente = division(dividendo,divisor)
            numCorrecto = True
        except ZeroDivisionError:
            print("Por favor introduce una division posible!!")
        except ValueError:
            print("Introduce números!!")

    print(cociente)