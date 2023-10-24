"""
Actividad 2: Reescribe el programa conversor de temperaturas para que lea repetidamente la temperatura hasta 
que sea correcta, debe detectar los fallos usando try y except. 
"""

def conversion(fahr):

    if fahr < -459.67:
        raise ValueError("Temperatura Fahrenheit incorrecta: " + str(fahr))
    
    cel = (fahr - 32.0) * 5.0/9.0
    return cel


if __name__ == "__main__":

    numeroCorrecto = False
    fahr = None
    while not numeroCorrecto:
        try:
            fahr = float(input("Introduzca la temperatura en Fahrenheit: "))
            cel = conversion(fahr)
            numeroCorrecto = True
        except ValueError: 
            if fahr == None:
                print("Por favor introduce un número!!")
            else:
                print("La temperatura Fahrenheit no es correcta " + str(fahr))

    print(cel)

    