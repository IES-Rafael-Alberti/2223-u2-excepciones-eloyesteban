"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que 
ha cumplido (desde 1 hasta su edad). 
"""

def repeticion(edad):
    años_str = ""
    for i in range(1, edad + 1):
        años_str += str(i) + "\n"
    return años_str.strip()


if __name__ == "__main__":

    numCorrecto = False
    while not numCorrecto:
        try:
            edad = int(input("Introduce tu edad: "))
            numCorrecto = True
        except ValueError:
            print("Introduce numeros!!")



    años_cumplidos = repeticion(edad)



    print(años_cumplidos)