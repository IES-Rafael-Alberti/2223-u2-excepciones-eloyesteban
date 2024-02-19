"""
Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará 
el mensaje "La entrada no es correcta" y lanzará la excepción capturada. 
"""



def obtener_numero_entero(entrada):
    try:
        numero = int(entrada)
        return numero
    except ValueError:
        raise ValueError("La entrada no es correcta")

if __name__ == "__main__":
    entrada = input("Introduce un número entero: ")
    try:
        num = obtener_numero_entero(entrada)
        print("Has introducido el número " + str(num))
    except ValueError as e:
        print(e)

