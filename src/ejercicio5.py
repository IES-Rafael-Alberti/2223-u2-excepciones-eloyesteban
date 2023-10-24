"""
Escribir que solicite una contraseña, y si no coincide con la que se tiene, lance la excepción NameError 
con el mensaje, "Incorrect Password!!"  
"""

def verificar_contraseña(contraseña_ingresada, contraseña_correcta="contraseña"):
    es_correcta = False
    if contraseña_ingresada == contraseña_correcta:
        es_correcta = True
    else:
        raise NameError("Contraseña Incorrecta!!")
    return es_correcta

if __name__ == "__main__":
    contraseña_ingresada = input("Introduce la contraseña: ")
    try:
        if verificar_contraseña(contraseña_ingresada):
            print("¡Contraseña Correcta!")
    except NameError as e:
        print(e)
